# Research Proposal

## Research Question

*To what extent is a gradient memory layout to blur the difference between cache and RAM useful in optimizing the access times of speed sensitive resources in CPUs?*

## Summary

The aim of this research is to analyze the effectiveness that dynamic memory placement algorithms can have on application performance as opposed to regular cache-RAM separated architectures.
By developing an architecture that allows the closer segments of RAM to act as a faster cache without bounding the cache statically, this research also aims to benefit from the middle areas where performance can be increased.
Similarly, by repurposing the RAM as a sort of cache without the drawbacks that come from the relatively distant placement of RAM from the CPU in traditional architectures, the size of the cache can also be easily upgraded through simple RAM upgrades.

The ultimate goal of this research is to rethink the traditional computer architecture from what it is today to create new avenues for program execution on CPUs without outdated technologies such as virtual memory management for processes.
By redesigning the arrangement of parts in the architecture, it also forces us to rethink core concepts such as how to handle cacheing data to begin with and deal with storing virtual memory mappings in cache.
Ideally, this research will ultimately revolutionize the world of computer architecture by limiting the drawbacks of cache-misses and potentially greatly increasing optimization of pointer based containers such as linked lists. 
Since cache and main memory use SRAM and DRAM respectively, this research's goal will simply to search for improvements in DRAM performance since SRAM is almost a requirement for the cpu and always close to the processor anyway.

## Methodology

1. Verilog using Verilator
   1. Create a basic traditional architecture to test against
   2. Create a basic architecture as proof of concept of gradient cacheing data
   3. Create a basic set of instructions for later testing
2. Research how handle virtual memory mappings and processes (optional)
3. Research how virtual memory mappings are cached in traditional CPUs
   1. Use similar optimization techniques to determine which memory should be stored closer to the CPU
   2. Edit these traditional algorithms to potentially work on a gradient of addresses, essentially scoring memory on its calling importance
   3. Implement versions of these cacheing algorithms:
      1. Copying existing data from outside cache to cache for faster read
      2. Storing data as normal to begin with but manage memory that is expected to be used often near cache
      3. Any other implementations that may add to the efficiency
4. Research Collaboration and Ideation
   1. Collaborate with team members to analyze existing research papers
   2. Encourage members to potentially publish research
5. Implementation and Evaluation
   1. Implement the architecture in a real world scenario
   2. Evaluate its effectiveness and create changes to processor ideology accordingly

## Resources Needed

- Lab Computer: Verilator tends to require a lot of RAM (up to 100GB) for any reasonable simulating of larger processors, so especially at the memory mapping stage this will be required
- Nvidia GPU or Similar: Verilator has GPU plugins to significantly increase simulating performance so that complex programs can be loaded onto the CPU. Running these purely on the CPU is not feasible due to the complexity of the program.

## Annotated Bibliography

1. Paper Title: "The Virtual Block Interface: A Flexible Alternative to the Conventional Virtual Memory Framework"
- Source: arxiv
- Description:
  - This paper proposes a revolutionary method to update the outdated virtual memory management from the 1970s. This paper specifically uses a more efficient cache lookup system that prevents excess system calls to the RAM, and a more efficient block system to assign virtual memory to between processes to limit the need to map memory directly from process to memory, but rather from block to memory (reducing overhead).
- Evaluation: This is mainly useful for this research because it goes into heavy detail about the traditional and new virtual memory management systems which is useful since this is a major performance bottleneck that needs to be considered before any performance claims can be made by this research's ideal processor.

2. Paper Title: "A Secure Processor Architecture for Encrypted Computation on Untrusted Programs"
- Source: MIT
- Description:
  - This paper goes through a secure processor implementation that will handle untrusted programs with minimal security risks beyond side channel attacks that look at power consumption and such. Specifically this source focuses on obfuscation as its main source of security, while not a perfect security solution, still works to dissuade attackers.
- Evaluation: This source is still heavily useful since it goes through a full processor architecture which is useful for creating one in this research project.