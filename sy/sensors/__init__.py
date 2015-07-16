from sy.tests import dummy
from sy.sensors import usage

TYPES = {
    'dummy': dummy.DummySensor,
    'dummy_redis': dummy.DummyRedisSensor,
    'dummy_rmq': dummy.DummyRMQSensor,
    'cpu_perc': usage.CPUPercSensor,
    'mem_perc': usage.MemoryPercSensor,
    'cpu_mem_perc': usage.CPUMemoryPercSensor,
}
