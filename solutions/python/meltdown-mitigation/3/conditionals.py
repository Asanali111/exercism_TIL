
# Functions to prevent a nuclear meltdown.
NORMAL_TEMPERTURE_OF_REACTOR = 800 #kelvin
BASELINE_NEUTRON_NUMBER_P = 500
PRODUCT_TEMP_AND_NEUTRONS = 500000

def is_criticality_balanced(temperature, neutrons_emitted):

    if temperature >= NORMAL_TEMPERTURE_OF_REACTOR or                              neutrons_emitted<=BASELINE_NEUTRON_NUMBER_P:
        return False
    if temperature * neutrons_emitted >= PRODUCT_TEMP_AND_NEUTRONS:
        return False
    return True
        
        

def reactor_efficiency(voltage, current, theoretical_max_power):
    """function that analyzes the reactor efficiency by color codes
  """
    
    efficiency = (voltage * current) / theoretical_max_power * 100
    if efficiency >= 80:
        return "green" 
    if 80>efficiency>=60:
        return "orange"
    if 60>efficiency>=30:
        return  "red"
    return "black"
        
def fail_safe(temperature, neutrons_produced_per_second, threshold):
    
    power = temperature *neutrons_produced_per_second
    if power>threshold*1.1:
        return "DANGER"
    if threshold*0.9<=power<=threshold*1.1:
        return "NORMAL"
    return "LOW"

    
