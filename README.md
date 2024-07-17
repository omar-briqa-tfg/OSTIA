<h1 align="center"> Open Science Toolkit Information Access </h1>

![CI](https://github.com/omar-briqa-tfg/OSTIA/actions/workflows/main.yaml/badge.svg)
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![MIT License][license-shield]][license-url]

## Thesis

Final Degree Project [ca]: https://upcommons.upc.edu/handle/2117/411792

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

In the current context of data science, every record of an event is crucial. Investigating this information can yield valuable information. We have been granted access to the logs of the UPCommons server, which is the portal for the global access to the UPC knowledge.

Logs are the access logs, which contain the fingerprints of each user on the platform. This access is recorded for each exam, document, video or other resource that is consulted. Our objective is to gather all of this data and transform it into valuable information.

There are three steps involved in this process. Firstly, comprehend the semantics and syntax of the registers. What type of information will we process, where it is located, what information it includes, and how we will analyze it. All this, taking into account the size of the task, includes all access records from 2006 to 2023, which represents 1.922.392.760 input records.

Secondly, once the semantics of the logs have been clarified, a storage solution is needed to perform an analysis of previously studied information. We have to filter and decide what we will store, in what format it will be stored, and most importantly, where we will store it.

We have finally created an open source tool that can analyze and store all access logs. We can define a use case to analyze a specific characteristic. By using the Grafana observability tool, results can be shown visually.

For instance, we can examine which resource is most frequently consulted and represent its progression. If malicious requests have infected the server, we can use this tool to analyze the symptoms. Also, relate the resource to its metadata: authors, license, language, and other relevant information.

The value we propose is a tool that can be used for various purposes, and it provides a starting point for future research.

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
