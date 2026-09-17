"""Functions to prevent a nuclear meltdown."""
NORMAL_TEMPERTURE_OF_REACTOR = 800 #kelvin
BASELINE_NEUTRON_NUMBER_P = 500
PRODUCT_TEMP_AND_NEUTRONS = 500000

def is_criticality_balanced(temperature, neutrons_emitted):

    if temperature >= NORMAL_TEMPERTURE_OF_REACTOR or neutrons_emitted<=BASELINE_NEUTRON_NUMBER_P:
        return False
    elif temperature * neutrons_emitted >= PRODUCT_TEMP_AND_NEUTRONS:
        return False
    else:
        return True
        


def reactor_efficiency(voltage, current, theoretical_max_power):
  

    efficiency = voltage*current*100/theoretical_max_power
    if efficiency >= 80:
        return("green")
    elif 80>efficiency>=60:
        return("orange")
    elif 60>efficiency>=30:
        return("red")
    else:
        return("black")
        
def fail_safe(temperature, neutrons_produced_per_second, threshold):
    
    power = temperature *neutrons_produced_per_second
    if power>threshold*1.1:
        return("DANGER")
    elif threshold*0.9<=power<=threshold*1.1:
        return("NORMAL")
    else:
        return("LOW")

    
