class Function:


    def __init__(self,  hydrogen_number: int or float, coordination_coefficient: int or float,
                 ionization_constant_Ka1: int or float, ionization_constant_Ka2: int or float,
                 ionization_constant_Ka3: int or float, ionization_constant_Ka4: int or float,
                 conditional_stability_constant: int or float, ligand_concentration: int or float,
                 system_pH_value: int or float):
        self.a = hydrogen_number
        self.b = coordination_coefficient
        self.k_a1 = ionization_constant_Ka1
        self.k_a2 = ionization_constant_Ka2
        self.k_a3 = ionization_constant_Ka3
        self.k_a4 = ionization_constant_Ka4
        self.K = conditional_stability_constant
        self.y = ligand_concentration
        self.x = system_pH_value
        self.k_sp = 10 ** (-8.5)

    def fx(self):
        return (10 ** (-16.63) * 10 ** (-4.8)) / (10 ** (-2 * self.x) + 10 ** (-10.25) * 10 ** (-self.x) + 10 ** (-16.63))

    def gx(self):
        return 0.5 * 10 ** (self.x - 14)

    def hx0(self):
        return 1

    def hx1(self):
        return self.hx1() + ((10 ** (-self.x)) / self.k_a1)

    def hx2(self):
        return self.hx1() + self.hx2() + ((10 ** (-2 * self.x)) / (self.k_a1 * self.k_a2))

    def hx3(self):
        return self.hx1() + self.hx2() + self.hx3() + (10 ** (-3 * self.x)) / (self.k_a1 * self.k_a2 * self.k_a3)

    def hx4(self):
        return self.hx1() + self.hx2() + self.hx3() + (10 ** (-4 * self.x)) / (self.k_a1 * self.k_a2 * self.k_a3 * self.k_a4)

    def hx(self):
        if self.a == 0:
            return 1
        elif self.a == 1:
            return 1 + ((10 ** (-self.x)) / self.k_a1)
        elif self.a == 2:
            return 1 + ((10 ** (-self.x)) / self.k_a1) + ((10 ** (-2 * self.x)) / (self.k_a1 * self.k_a2))
        elif self.a == 3:
            return (1 + ((10 ** (-self.x)) / self.k_a1) + ((10 ** (-2 * self.x)) / (self.k_a1 * self.k_a2)) +
                    (10 ** (-3 * self.x)) / (self.k_a1 * self.k_a2 * self.k_a3))
        elif self.a == 4:
            return ((1 + ((10 ** (-self.x)) / self.k_a1) + ((10 ** (-2 * self.x)) / (self.k_a1 * self.k_a2)) +
                    (10 ** (-3 * self.x)) / (self.k_a1 * self.k_a2 * self.k_a3)) +
                    (10 ** (-4 * self.x)) / (self.k_a1 * self.k_a2 * self.k_a3 * self.k_a4))

    def z(self):
        # result = None
        if self.b == 0.5:
            z_result = (((-1 / 2) * (self.fx() + (self.k_sp / self.gx())) + ((1 / 4) * (self.fx() + (self.k_sp / self.gx()))
                                                                        ** 2 + 2 * self.k_sp * (self.K / self.hx()) *
                                                                        (self.fx() + (self.k_sp / self.gx())) * self.y)
                    ** 0.5) / (2 * self.k_sp * (self.K / self.hx()))) - ((-1 / 2 + (1 / 4 + 2 * self.K / self.hx() *
                                                                                    self.gx() * self.y) ** 0.5) /
                                                                         (2 * self.gx() * self.K / self.hx()))
        elif self.b == 1:
            z_result = ((self.y * (self.fx() + self.k_sp / self.gx())) / (self.k_sp * self.K / self.hx() + (self.fx() +
                                                                                                         self.k_sp / self.gx()))
                      - self.y / ((self.K / self.hx()) * self.gx() + 1))
        elif self.b == 2:
            z_result = ((self.y * (self.fx() + (self.k_sp / self.gx())) ** 2) / (10 ** (-17) * self.K / self.hx() +
                                                                              (self.fx() + self.k_sp / self.gx()) ** 2)
                      - self.y / (self.K / self.hx() * (self.gx()) ** 2 + 1))

        result = z_result / self.gx()
        if result > 0.05:
            return result
        else:
            return invalidoutput(result)

    def check_input(self):
        pass

class InputDataError(Exception):
    def __init__(self, parameter, input_data):
        self.param = parameter
        self.input = input_data
        self.message = (f"{str(self.param)}'s input is {str(self.input)} and it's out of range. The range of {str(self.param)}"
                        f" is ")
        super().__init__(self.message)

def invalidoutput(result):
    return f"The calculated result of the equation is {str(result)}, which is smaller than 0.05. Output is invalid."

class InvalidOutput(Exception):
    def __init__(self, result):
        self.res = result
        self.message = f"The calculated result of the equation is {str(result)}, which is smaller than 0.05. Output is invalid."
        super().__init__(self.message)
