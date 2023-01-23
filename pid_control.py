class PID:

    def __init__(self):
        self.Kp = 30.0  # Ganho Proporcional
        self.Ki = 0.2  # Ganho Integral
        self.Kd = 400.0  # Ganho Derivativo
        self.T = 1.0  # Período de Amostragem (ms)
        self.erro_total = 0.0
        self.erro_anterior = 0.0
        self.sinal_de_controle_MAX = 100.0
        self.sinal_de_controle_MIN = -100.0
        self.sinal_de_controle = 0.0

    def output(self, referencia, saida_medida):
        erro = referencia - saida_medida
        self.erro_total += erro  # Acumula o erro (Termo Integral)

        if self.erro_total >= self.sinal_de_controle_MAX:
            self.erro_total = self.sinal_de_controle_MAX
        elif self.erro_total <= self.sinal_de_controle_MIN:
            self.erro_total = self.sinal_de_controle_MIN

        delta_error = erro - self.erro_anterior  # Diferença entre os erros (Termo Derivativo)
        self.sinal_de_controle = self.Kp * erro + (self.Ki * self.T) * self.erro_total + (
                self.Kd / self.T) * delta_error  # PID calcula sinal de controle

        if self.sinal_de_controle >= self.sinal_de_controle_MAX:
            self.sinal_de_controle = self.sinal_de_controle_MAX
        elif self.sinal_de_controle <= self.sinal_de_controle_MIN:
            self.sinal_de_controle = self.sinal_de_controle_MIN

        self.erro_anterior = erro

        return self.sinal_de_controle
