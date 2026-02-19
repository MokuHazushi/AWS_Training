Below are questions to consider before thinking of services. They serve to identify the application's profile (those are oriented for micro-service applications):

# Compute and memory requirements
- How much CPU and memory are required for your tasks to be stable and serve an acceptable amount of requests deemed by load testing? 
- Do you have graphics processing unit (GPU) requirements?
- Do you have unique scaling scenarios that you would want to manually control?
- Is your application more read or write intensive?

# Storage requirements
- Is your application stateful or stateless? Do you need to store state or session data on the server (stateful) or do you not have any state to store (stateless)?
- Do you have any persistent data?
- What type of data do you have to store?
- What type of storage do you need?
- How fast do you need to access the data? What is your required throughput?
- Do you have streaming data?

# Network requirements
- How do your containers communicate?
- Do you need service-to-service communication?
- Do your containers need outbound or inbound access to the internet?
- Do you have a workload with consistent demand? Or do your traffic levels change very quickly?
- Do you need to control communications between tasks and services at a granular level for tasks located on the same host?
- Do you need multiple tasks on the instance?
- Do you have an existing virtual private cloud (VPC) with a small Classless Inter-Domain Routing (CIDR) range?

# Security requirements
- What sort of security requirements do you have?
- Who can have access to your containers?
- What access do your containers need?
- Does your data need to be encrypted in transit, or at rest? 
- Do you have credentials you need to store?
- Do you have any regulatory concerns?

# Observability requirements
- Are your applications going to be massively distributed?
- Do you need to alert on a metric you defined earlier?
- Do you need to monitor application programming interface (API) calls?
- Do you have any regulations around tracking?
- Do you have any legal concerns or regulations?
- Do you need your logs in a particular format (for example: for analytics or batch processing)?

# Cost, performance, and resilience
- What are the highest priorities for your application? Is it most important that you keep cost down, that you minimize downtime, or that you maximize the performance of your application?
- Think of these three categories as interrelated levers: when you make an adjustment to one, you usually impact the other two.