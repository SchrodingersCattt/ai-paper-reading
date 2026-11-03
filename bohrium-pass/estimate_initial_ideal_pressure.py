"""按未反应初始组成估算理想气体压力；论文并未报告该压力数值。"""
import sys
from decimal import Decimal as D

sys.stdout.reconfigure(encoding='utf-8')

# 论文第 2 页的初始体系；摩尔质量和气体常数为本计算采用的常数。
n_ch4, n_o2 = D('100'), D('200')
m_ch4, m_o2 = D('16.042'), D('31.998')  # g/mol
rho, temperature = D('0.25'), D('3000')  # g/cm³, K
gas_constant = D('82.057')  # cm³·atm/(mol·K)

mean_mass = (n_ch4 * m_ch4 + n_o2 * m_o2) / (n_ch4 + n_o2)
pressure = rho * gas_constant * temperature / mean_mass

print('初始组成：100 CH4、200 O2；密度 0.25 g/cm³；温度 3000 K。')
print('假设尚未反应，并按理想气体处理；P = ρRT/M。')
print(f'平均摩尔质量 M = {mean_mass:.10f} g/mol')
print(f'理想气体估算压力 P = {pressure:.8f} atm（约 2.31 × 10³ atm）')
print('这是所列假设下的估算，不是论文报告的轨迹实际压力。')
