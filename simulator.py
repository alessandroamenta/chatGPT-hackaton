import requests

class SolarPanel:
    # the losses need a better empirical estimation but this number has been found accurate accourding to sunrun calculations
    def __init__(self, system_capacity, module_type=0, losses=30.08, array_type=1, tilt=30, azimuth=180, address='',panel_wattage= 395,
     api_key='bItQKyAUZD2234KAutGtaurBrxF2P0o38h2gppte'):
        self.api_url = 'https://developer.nrel.gov/api/pvwatts/v6.json'
        self.system_capacity = system_capacity
        self.module_type = module_type
        self.losses = losses
        self.array_type = array_type
        self.tilt = tilt
        self.azimuth = azimuth
        self.address = address
        self.api_key = api_key
        # the panel wattage depends on the brand you can check here if it is update https://pvfree.azurewebsites.net/cec_modules/
        self.panel_wattage = panel_wattage
    
    # calculate the energy production per kWh per year based on the system size
    def power_kwh_needed(self):
        # Build the API request URL
        params = {
            'api_key': self.api_key,
            'system_capacity': self.system_capacity,
            'module_type': self.module_type,
            'losses': self.losses,
            'array_type': self.array_type,
            'tilt': self.tilt,
            'azimuth': self.azimuth,
            'address': self.address
        }

        # Send the API request
        response = requests.get(self.api_url, params=params)

        # Parse the API response
        if response.status_code == 200:
            data = response.json()
            if data['errors']:
                return 'Error: {}'.format(data['errors'])
            else:
                # Return the estimated energy production
                return data['outputs']['ac_annual']
        else:
            return 'Error: {}'.format(response.text)
    
    def number_of_panels(self):
        panel_wattage = self.panel_wattage
        Number_of_panels = (system_capacity * 1000)/panel_wattage
        return Number_of_panels

    
    def price_lease(power_kwh_needed):
       # Implement the logic for calculating the lease price
        power_kwh_needed = solar_panel.power_kwh_needed()
        cost_per_kwh = 0.16
        interest_rate_escalation = 3.5
        cost_per_year = power_kwh_needed * cost_per_kwh
        cost_per_month_1 = cost_per_year / 12
        result = [cost_per_month_1]
        # Initialize the result list with the lease price for the first year
    
        for i in range(1, 26):
            cost_per_month = ((interest_rate_escalation / 100 + 1) * result[-1])
            result.append(cost_per_month)
        for i, price in enumerate(result, start=1):
            print('Average Lease Price for Year {}: {}'.format(i, price))
        
        
    
    def power_kwh_needed_financing(self):
        cost_per_kwh = 0.10
        life_time_cost = cost_per_kwh*power_kwh_needed*25
        return life_time_cost
    
    def power_kwh_needed_cash(self):
        cost_per_kwh = 0.10
        cost_per_year = power_kwh_needed * cost_per_kwh
        total_cost = cost_per_year * 25
        return total_cost


if __name__ == '__main__':
    # Get the input values from the user
    system_capacity = float(input('Enter the system capacity (kW): '))
    address = input('Enter the address of the location: ')

    # Create an instance of the SolarPanel class
    solar_panel = SolarPanel(
        system_capacity=system_capacity,
        address=address
    )

    # Calculate the price purchase and lease
    power_kwh_needed = solar_panel.power_kwh_needed()
    price_lease = solar_panel.price_lease()
    total_cost = solar_panel.power_kwh_needed_cash()
    number_of_panels = solar_panel.number_of_panels()

    # Print the results
    print('Estimated Average Ownership Price {} $'.format(total_cost))
    print('Estimated Annual Energy Production: {} kWh'.format(power_kwh_needed))
    print('Estimated Number of Panels: {} and Panel Wattage: {} W'.format(number_of_panels, solar_panel.panel_wattage))


    
# to have a more complete bot we could retrive data for the price of the average utility 

#bill based on the utility name or location and calculate the difference in savings between 

#how much they pay and how much they would pay going solar