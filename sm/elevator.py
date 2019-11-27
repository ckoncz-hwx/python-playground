import os
from sismic.io import import_from_yaml
from sismic.interpreter import Interpreter

def print_info(step):
    print("\nInfo:")
    for attribute in ['event', 'transitions', 'entered_states', 'exited_states', 'sent_events']:
        print('  {}: {}'.format(attribute, getattr(step, attribute)))

def print_events(interpreter):
    print("\nEvents:")
    for _, event in interpreter._external_queue:
       print("  event = %s"%event.name)


# Load statechart from yaml file
print('__file__', __file__)
elevator = import_from_yaml(filepath=os.path.dirname(__file__)+'/elevator.yaml')

# Create an interpreter for this statechart
interpreter = Interpreter(elevator)

print('Before:', interpreter.configuration)

step = interpreter.execute_once()

print('After:', interpreter.configuration)

print_info(step)

interpreter.queue('click', 'clack', 'clock')
print('filled queue')

print_events(interpreter)

while True:
    step = interpreter.execute_once()
    if step:
        print_info(step)
        print_events(interpreter)
    else:
        break
