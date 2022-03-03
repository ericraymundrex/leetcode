### Build and Deploy 💻  👉 ☁️:

**Problems 1:**
- When we develop an application in any programming language, the deployment becomes difficult as we use different compilers.

- Lets take the example for Amazon, while testing the Amazon the developer need to pay the money here we use a sandbox account. This should not be shiped to the actual environment. 

- So, we need package manager, build manager , environment manager.

- So, the USER -> DEVELOPS -> TEST -> APPROVE -> PRODUCTION -> NEW VERSIONS -> DEVELOP

- :point_up: This is called as **Pipe lines**

**Solutions :**
- Here, we used a methodlogy called as continous development and integration.

- To make this methodlogy happen we use different software called as Jenkins, Docker, Terraform, Selinium [E2E Test Tools].

- This operation is called as **Devops**

- The Devops evolve around -> TestOps, DevSecOps.

|Software   | Concept   | Containerization Solution Provider |
|-----------|-----------|------------------------------------|
|Docker     | Container | AWS Container, kubernates, GCP     |
|jenkins    |           |                                    |
|Kubernaties|           |                                    |

**Problem 2:**
- When the code moves from the DEVELOPER to TESTER then configuration of the system should be same.

**Solutions 1:**

- We create a container this have all the system configurations (like version of databasse or a version of softwares) 

- This can be done by the **Virtual Machine**.

- In windows, we use **Hypervisor**. Examples: vm ware, and virtual box. This is a hyper visor inbuilt called as Hyper-V. Hypervisor is a virualisation engine.

| App1   | App2    |
|--------|---------|
|Bin/Libs|Bins/Libs|
|Guest OS|Guest OS |
|    Hypervisor   ||
|     Host OS     ||

- In the End it is the Virtual Machine, It uses the RAM, CPU Core.
- This also requires Hardware like memory, CPU core for the Host OS also.

- **The problem with hypervisor is the hypervisor have the entire operating system in Guest OS along with its kernel, its hardware abstraction layer, its lib, and network card.**
- **These are required by the OS, but not by the application.**

- **This might be avilable in the host OS itself. But for the sake of CI/CD we have to use 2 different OS.**

- _Here the problem is waste of Hardware, and dependent libraries._
```
Application <-> Hyper visor -> [Host OS : Only the Hardware and processing hypervisor]
```
**Solution 2:**

- Use Containers.
- In containerization, only the lib is installed in the docker engine, but this will not take hardware and dependent lib.

```
Applications <-> Doker Engine <-> Host OS
```

| App1   | App2    |
|--------|---------|
|Bin/Libs|Bins/Libs|
|Guest OS|Guest OS |
|    Docker Engine||
|     Host OS     ||


### Installation:

- In a standard way we can use the docker engine for Windows and MacOS.
- So, we have to install Docker desktop (Run time environment) as a daemon service, this runs Docker engine and utilies.

- In mac os,
```
doker verion
```
in terminal, this will show need to run daemon service.

<img src="./src/img1.png"/>

- But we dont need Desktop for Linux. 

### Docker hub and installing the images: 

- Login to the service.
- Here we can install the image of the service.

- For example if we want to install the node.js
```
sudo docker run node
```
:point_up: **This will check the internally the node.js is installed if so it will take the local image only** else it will go to the docker hub and intall node.js.

