"""
- Need to calculate the maximum bandwidth > Current usage > the new application usage

Plan
    - Add all the constants given
    - Create a variable that is going to convert the mbps to bps 
    - Calculate
        - The network capacity in bps (max * conversion_variable) 
        - The current usage in bps (Users * (A+B))
        - The current availability in bps (network capacity - current usage)
        - The new applications requirements in bps = New application requirements
        - The bandwidth available if the new application is installed (in Mbps) -> (network capacity - current usage + New application requirements) / mbps_to_bps
    - Show outputs 
    - 



- 1 Mbps = 1000000 bps

- Maximum network bandwidth = 1000 mbps
- Current users = 200
- Current application A requirements = 200000 bps
- Current application B requirements = 100000 bps
- New application requirements = 350000 bps
"""

mbps_to_bps = 1000000  #bps

max_network_bandwidth_bps = 1000 * mbps_to_bps #bps

number_current_users = 200

current_app_bandwidth_requirements_A = 200000 #bps
current_app_bandwidth_requirements_B = 100000 #bps


# The network capacity in bps
network_capacity_bps = max_network_bandwidth_bps

# The current usage in bps
current_usage_bps = (number_current_users * (current_app_bandwidth_requirements_A + current_app_bandwidth_requirements_B))

# The current availability in bps
current_availability_bps = (max_network_bandwidth_bps - current_usage_bps)

# The new applications requirements in bps
new_application_requirement = 350000 #bps

#The bandwidth available if the new application is installed (in Mbps)
bandwidth_available_if_new_app_installed_mbps = (((max_network_bandwidth_bps - current_usage_bps) + new_application_requirement) / mbps_to_bps)


print(f"Network capacity: {network_capacity_bps} bps" )
print(f"Current usage: {current_usage_bps} bps" )
print(f"Current availability: {current_availability_bps} bps" )
print(f"New Application requirements: {new_application_requirement} bps" )

print(f"Bandwidth available with new application: {bandwidth_available_if_new_app_installed_mbps} Mbps" )
