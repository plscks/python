# Testing interfacing with iptables
# script grabbed from https://github.com/ldx/python-iptables documentation
# edited by plscks
import iptc

chain = iptc.Chain(iptc.Table(iptc.Table.FILTER), "INPUT")
rule = iptc.Rule()
#rule.in_interface = "eth+"
rule.src = '173.239.230.33'
target = iptc.Target(rule, 'DROP')
rule.target = target
chain.insert_rule(rule)
