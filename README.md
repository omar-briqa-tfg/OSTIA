<h1 align="center"> Open Science Toolkit Information Access </h1>

![CI](https://github.com/omar-briqa-tfg/OSTIA/actions/workflows/main.yaml/badge.svg)
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![MIT License][license-shield]][license-url]

## Thesis

Final Degree Project [ca] report will be available [here](https://github.com/omar-briqa-tfg/OSTIA) soon ...

## Project Structure

<pre>
.
├── LICENCE
├── Pipfile
├── Makefile
├── README.md
├── requirements.txt
├── pre-commit-config.yaml
└── .github/
│   └── workflows
│       └── main.yaml
└── config
│   ├── influxdb/
│   ├── mongodb/
│   ├── telegraf/
│   └── docker-compose.yaml
└── docs/
│   ├── source/
│   ├── Makefile
│   ├── README.md
│   └── ...
└── scripts/
│   └── unzip.sh
└── src/
│   ├── logs
│   ├── metadata
│   ├── queries
|   └── dashboards
└── test/
    ├── logs
    └── metadata

</pre>

## Built With


[![Git][git]][git-url]
[![GitHub][github]][github-url]
[![GitHub Actions][github-actions]][github-actions-url]
[![Python][python]][python-url]
[![Docker][docker]][docker-url]
[![InfluxDB][influxdb]][influxdb-url]
[![MongoDB][mongodb]][mongodb-url]
[![Bash][bash]][bash-url]
[![Grafana][grafana]][grafana-url]

## About The Project

In the current context of data science, everything related to data is highly valuable. Going over this information, analyzing, decomposing, and extracting everything can provide valuable insights. In our case, we have been given access to the logs of the UPCommons server, the principal repository of digital content resources for UPC.

The logs are the access register, the footprint of every user of the platform. Every exam, documentation, papers, videos, etc accessed is being registered. Our objective is to gather all these details, and somehow convert it into valuable information.

There are three main steps in the process. First of all, understanding the semantics and syntax of the log files. What type of information are we going to deal with, where it is located, which information it includes, and how are we going to analyze it? Taking into account the task's scope, access logs from 2006 to 2023, specifically, 1.922.392.760 log entries.

Secondly, once we cleared and clarified, a storage solution is needed to perform analysis over the previously analyzed information. We should filter and decide what we are going to store, in which format it will be stored, and the most important, where. Because we need the expertise, we have to leverage every I/O, read/write operation to an external system, and customization is not within our scope.

Finally, we end up with the final stage. We have been able to build a tool that can analyze and store all the access logs. We can define a use case in order to analyze a certain feature, or even just out of curiosity. Using an observability tool called Grafana, the values can be visually represented. The value that we propose is a tool that can be used for different purposes, and a starting point for following investigations.

For example, we can check which resource is the most accessed within a period of time and represent its evolution. If malicious petitions have infected the server, use this tool to analyze the symptoms and create useful metrics and SLOs. Even more, relate the resource to its metadata, and include the most popular authors, as well as the evolution of language use among new published papers, and much more.

The code was developed in accordance with the best practices of software engineering and the software development cycle. The Open Science Toolkit Information Access repository, located at https://github.com/omar-briqa-tfg/OSTIA, is available to the public and is licensed under an MIT license.

## License

Distributed under the MIT License. See `LICENSE` for more information.


## Contact

[![LinkedIn][linkedin-shield]][linkedin-url]
[![e-mail][email-shield]][email-url] <br>
<b>Omar Briqa</b>

[contributors-url]: https://github.com/omar-briqa-tfg/OSTIA/graphs/contributors
[contributors-shield]: https://img.shields.io/github/contributors/omar-briqa-tfg/OSTIA.svg?style=flat
[forks-url]: https://github.com/omar-briqa-tfg/OSTIA/network/members
[forks-shield]: https://img.shields.io/github/forks/omar-briqa-tfg/OSTIA.svg?style=flat
[stars-url]: https://github.com/omar-briqa-tfg/OSTIA/stargazers
[stars-shield]: https://img.shields.io/github/stars/omar-briqa-tfg/OSTIA.svg?style=flat
[license-url]: https://github.com/omar-briqa-tfg/OSTIA/blob/master/LICENSE
[license-shield]: https://img.shields.io/github/license/omar-briqa-tfg/OSTIA.svg?style=flat
[linkedin-url]: https://www.linkedin.com/in/omar-briqa/
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=flat&logo=linkedin&colorB=555
[email-url]: mailto:omarbriqa@gmail.com
[email-shield]:https://img.shields.io/badge/contact-email-blue
[influxdb]: https://img.shields.io/badge/InfluxDB-22ADF6?style=flat&logo=InfluxDB&logoColor=white
[influxdb-url]: https://www.influxdata.com/
[python]: https://img.shields.io/badge/Python-FFD43B?style=flat&logo=python&logoColor=blue
[python-url]: https://www.python.org/
[mongodb]: https://img.shields.io/badge/MongoDB-4EA94B?style=flat&logo=mongodb&logoColor=white
[mongodb-url]: https://www.mongodb.com/
[docker]: https://img.shields.io/badge/Docker-2CA5E0?style=flat&logo=docker&logoColor=white
[docker-url]: https://www.docker.com/
[bash]: https://img.shields.io/badge/Shell_Script-121011?style=flat&logo=gnu-bash&logoColor=white
[bash-url]: https://www.linuxfoundation.org/
[git]: https://img.shields.io/badge/GIT-E44C30?style=flat&logo=git&logoColor=white
[git-url]: https://www.git-scm.com/
[github]: https://img.shields.io/badge/GitHub-100000?style=flat&logo=github&logoColor=white
[github-url]: https://github.com/
[github-actions]: https://img.shields.io/badge/Github%20Actions-282a2e?style=flat&logo=githubactions&logoColor=367cfe
[github-actions-url]: https://github.com/features/actions
[grafana]: https://img.shields.io/badge/Grafana-F2F4F9?style=flat&logo=grafana&logoColor=orange&labelColor=F2F4F9
[grafana-url]: https://grafana.com/
