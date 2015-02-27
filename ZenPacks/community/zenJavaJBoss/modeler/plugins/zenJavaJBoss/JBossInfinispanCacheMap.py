from Products.DataCollector.plugins.CollectorPlugin import CollectorPlugin
from Products.DataCollector.plugins.DataMaps import ObjectMap
from Products.ZenUtils.Utils import prepId
from ZenPacks.community.zenJavaJBoss.Definition import *
from ZenPacks.community.zenJavaApp.lib.JavaAppScan import *
from ZenPacks.community.zenJavaApp.lib.CommonMBeanMap import *

class JBossInfinispanCacheMap(CommonMBeanMap):
    """Map JMX Client output table to model."""
    
    constr = Construct(JBossInfinispanCacheDefinition)
    relname = constr.relname
    modname = constr.zenpackComponentModule
    baseid = constr.baseid
    
    searchMBean = 'jboss.infinispan:type=Cache,name=*,manager=*,component=Statistics'


