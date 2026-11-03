"""估算 Zeng 2020 生产模拟初始组成的理想气体压力。

只使用 Python 标准库。不联网，不读取凭证，不调用玻尔。

数据
    分子数、密度、温度来自 Zeng et al., Nature Communications 11, 5713 (2020)
    PDF 第 2 页：初始体系 100 CH4 + 200 O2，密度 0.25 g/cm³，温度 3000 K。
    该页写 relatively high density (and thus high pressure)，没有给出 atm 压力。
    摩尔质量和气体常数是本估算采用的常数，不是论文报告的测量值：
    CH4 = 16.042 g/mol，O2 = 31.998 g/mol，R = 82.057 cm³·atm/(mol·K)。

假设
    初始的 100 个 CH4 与 200 个 O2 尚未反应，混合物按理想气体处理。

公式
    M = (n_CH4 * M_CH4 + n_O2 * M_O2) / (n_CH4 + n_O2)
    P = rho * R * T / M
    M 的单位是 g/mol，P 的单位是 atm。
"""

import sys
from decimal import Decimal

sys.stdout.reconfigure(encoding="utf-8")

N_CH4 = Decimal(100)
N_O2 = Decimal(200)
M_CH4 = Decimal("16.042")  # g/mol
M_O2 = Decimal("31.998")  # g/mol
RHO = Decimal("0.25")  # g/cm³
T = Decimal(3000)  # K
R = Decimal("82.057")  # cm³·atm/(mol·K)

_SUP = str.maketrans("0123456789-", "⁰¹²³⁴⁵⁶⁷⁸⁹⁻")


def sci_3(value):
    mantissa, exp = f"{value:.2e}".split("e")
    return f"{mantissa} × 10{str(int(exp)).translate(_SUP)}"


def main():
    n_total = N_CH4 + N_O2
    weighted = N_CH4 * M_CH4 + N_O2 * M_O2
    molar_mass = weighted / n_total
    pressure = RHO * R * T / molar_mass

    print("输入")
    print(f"  n(CH4) = {N_CH4} ，无量纲分子数")
    print(f"  n(O2) = {N_O2} ，无量纲分子数")
    print(f"  M(CH4) = {M_CH4} g/mol")
    print(f"  M(O2) = {M_O2} g/mol")
    print(f"  rho = {RHO} g/cm³")
    print(f"  T = {T} K")
    print(f"  R = {R} cm³·atm/(mol·K)")
    print("数据")
    print("  分子数、密度和温度：Zeng et al., Nat. Commun. 11, 5713 (2020)，PDF 第 2 页。")
    print("  该页写出相对高的密度，因而高压力，没有报告 atm 压力。")
    print("  CH4、O2 的摩尔质量和 R 是本估算选用的常数。")
    print("假设")
    print("  初始组成尚未反应，并按理想气体处理。")
    print("公式")
    print("  M = (n(CH4)*M(CH4) + n(O2)*M(O2)) / (n(CH4) + n(O2))")
    print("  P = rho * R * T / M")
    print("结果")
    print(f"  加权和 = {weighted} g/mol")
    print(f"  分子数合计 = {n_total}")
    print(f"  平均摩尔质量 M = {molar_mass:.10f} g/mol")
    print(f"  M 记到 0.01 g/mol = {molar_mass.quantize(Decimal('0.01'))} g/mol")
    print(f"  理想气体估算压力 P = {pressure:.8f} atm")
    print(f"  P 按三位有效数字 = {sci_3(pressure)} atm")
    print("  这是所列假设下的估算，不是论文报告的轨迹实际压力。")


if __name__ == "__main__":
    main()
