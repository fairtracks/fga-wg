---
search:
  boost: 2.0
---# Enum: AccessMethods 




_Access methods (i.e. communication protocols), following the vocabulary defined in the GA4GH DRS specification (https://ga4gh.github.io/data-repository-service-schemas/preview/release/drs-1.4.0/docs/#tag/AccessMethodModel/operation/getAccessMethod)._



<div data-search-exclude markdown="1">

URI: [https://w3id.org/fga-wg/schema/top_level/AccessMethods](https://w3id.org/fga-wg/schema/top_level/AccessMethods)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| s3 | None | Amazon S3 and other S3-compatible bucket |
| gs | None | Google Cloud Storage (and compatible) bucket |
| ftp | None | File Transfer Protocol |
| gsiftp | None | GridFTP protocol (an extension of the File Transfer Protocol (FTP) for grid c... |
| globus | None | Data transfer via the Globus research cyberinfrastructure (https://www |
| htsget | None | GA4GH HTSget standard for retrieving subsections of genomic data (https://www |
| https | None | Hypertext Transfer Protocol Secure, the standard encrypted protocol used on t... |
| file | None | For local files accessible via a file URI (e |




## Slots

| Name | Description |
| ---  | --- |
| [access_method](access_method.md) | Access method used to access the File object (orig: DrsObject) |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/fga-wg/schema/top_level






## LinkML Source

<details>
```yaml
name: AccessMethods
description: Access methods (i.e. communication protocols), following the vocabulary
  defined in the GA4GH DRS specification (https://ga4gh.github.io/data-repository-service-schemas/preview/release/drs-1.4.0/docs/#tag/AccessMethodModel/operation/getAccessMethod).
from_schema: https://w3id.org/fga-wg/schema/top_level
rank: 1000
permissible_values:
  s3:
    text: s3
    description: Amazon S3 and other S3-compatible bucket.
  gs:
    text: gs
    description: Google Cloud Storage (and compatible) bucket.
  ftp:
    text: ftp
    description: File Transfer Protocol.
  gsiftp:
    text: gsiftp
    description: GridFTP protocol (an extension of the File Transfer Protocol (FTP)
      for grid computing).
  globus:
    text: globus
    description: Data transfer via the Globus research cyberinfrastructure (https://www.globus.org/.)
  htsget:
    text: htsget
    description: GA4GH HTSget standard for retrieving subsections of genomic data
      (https://www.ga4gh.org/product/htsget/).
  https:
    text: https
    description: Hypertext Transfer Protocol Secure, the standard encrypted protocol
      used on the web.
  file:
    text: file
    description: For local files accessible via a file URI (e.g., file://path/to/file).

```
</details>

</div>