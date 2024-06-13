# Open Science Toolkit Information Access

## Introduction

Check thesis report ->  [PDF](https://github.com/OBriqa/TFG)

## Project Structure

<pre>
.
├── Makefile
├── README.md
├── LICENCE
└── build/
│   └── debug/
│   └── release/
│       ├── app.exe
│       └── view.exe
└── <b>doc</b>umentation/
│   ├── documentation.md
│   ├── user-manual.md
│   └── INSTALL.md
└── lib/
│   ├── dependencies/
│   └── externals/
└── <b>res</b>ources/
│   ├── images/
│   └── icons/
└── scripts/
│   ├── generate-docs.sh
│   ├── run-tests.sh
│   └── code-formatting.sh
└── src/
    ├── log-analyser
    │   ├── integration/
    │   ├── main/
    │   └── test/
    └── log-viewer
        ├── integration/
        ├── main/
        └── test/

</pre>

## Summary

In the current context of data science, everything related to data is highly valuable. Going over this information, analyzing, decomposing, and extracting everything can provide valuable insights. In our case, we have been given access to the logs of the UPCommons server, the principal repository of digital content resources for UPC.

The logs are the access register, the footprint of every user of the platform. Every exam, documentation, papers, videos, etc accessed is being registered. Our objective is to gather all these details, and somehow convert it into valuable information.

There are three main steps in the process. First of all, understanding the semantics and syntax of the log files. What type of information are we going to deal with, where it is located, which information it includes, and how are we going to analyze it? Taking into account the task's scope, access logs from 2006 to 2023, specifically, 1.922.392.760 log entries.

Secondly, once we cleared and clarified, a storage solution is needed to perform analysis over the previously analyzed information. We should filter and decide what we are going to store, in which format it will be stored, and the most important, where. Because we need the expertise, we have to leverage every I/O, read/write operation to an external system, and customization is not within our scope.

Finally, we end up with the final stage. We have been able to build a tool that can analyze and store all the access logs. We can define a use case in order to analyze a certain feature, or even just out of curiosity. Using an observability tool called Grafana, the values can be visually represented. The value that we propose is a tool that can be used for different purposes, and a starting point for following investigations.

For example, we can check which resource is the most accessed within a period of time and represent its evolution. If malicious petitions have infected the server, use this tool to analyze the symptoms and create useful metrics and SLOs. Even more, relate the resource to its metadata, and include the most popular authors, as well as the evolution of language use among new published papers, and much more.

The code was developed in accordance with the best practices of software engineering and the software development cycle. The Open Science Toolkit Information Access repository, located at https://github.com/omar-briqa-tfg/OSTIA, is available to the public and is licensed under an MIT license.
