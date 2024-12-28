# SimpleMPLSNetwork
This small-scale ISP network connects the customer's sites with MPLS and L3 VPNs.<br/>
The aim is to design, configure and manage an MPLS-based network, automate tasks using Python and utilize Linux for network management and troubleshooting.

## Project Steps

### 1. Networking Setup
#### MPLS Configuration:
* Enable MPLS on core routers.
* Configure LDP (Label Distribution Protocol) to distribute labels.
#### L3 VPN Configuration:
* Create VRFs (Virtual Routing and Forwarding instances) for each customer on PE routers.
* Use MP-BGP (Multiprotocol BGP) to advertise customer routes between PE routers.
#### Verification:
Ensure communication between CE1 and CE2 for the same customer using ```ping```.

---
### 2. Linux Integration
#### Tasks:
* Set up SSH on all routers to allow remote management.
* Use Linux tools for troubleshooting:
  * ```ping``` for connectivity checks.
  * ```traceroute``` for routing path verification.
  * ```tcpdump``` for traffic analysis.
* Document all configurations and outputs.

---
### 3. Python Automation
#### Automation Scripts:
* Use ```netmiko``` to automate configuration tasks such as pushing configurations to routers.
* Write scripts to fetch data from devices, such as:
  * Routing table snapshots.
  * Interface status reports.
* Optionally, interact with device APIs to perform CRUD operations.

---
### 4. Documentation
#### Deliverables:
* Save and document:
  * **Topology File:** GNS3 or Packet Tracer project file.
  * **Router Configurations:** Exported configurations for all devices.
  * **Python Scripts:** Include automation scripts for specific tasks.
  * **README.md:**
    * Include a summary of the topology and its purpose.
    * Provide configuration and usage instructions for Python scripts.
    * List observations and troubleshooting steps.

---
### 5. Verification
#### Confirm the following:
* MPLS is fully operational with label distribution functioning.
* CE devices for the same customer can successfully communicate through the L3 VPN.
* Python scripts simplify repetitive tasks and gather necessary data.
* SSH management works seamlessly via the Linux VM.

---
### 6. Expected Outcome
* Hands-on experience with MPLS and L3 VPN configuration.
* Integration of Linux for network management.
* Practical understanding of Python automation in networking tasks.
