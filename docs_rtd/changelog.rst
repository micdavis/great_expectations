.. _changelog:

#########
Changelog
#########

0.16.12
-----------------
* [FEATURE] Plumbing of validation_result_url from cloud response ([#7809](https://github.com/great-expectations/great_expectations/pull/7809))
* [FEATURE] Splitters work with Spark Fluent Datasources ([#7832](https://github.com/great-expectations/great_expectations/pull/7832))
* [FEATURE] Update `get_context` to scaffold project structure for file-backed usecases ([#7693](https://github.com/great-expectations/great_expectations/pull/7693))
* [BUGFIX] Azure Package Presence/Absence Tests Strengthening ([#7818](https://github.com/great-expectations/great_expectations/pull/7818))
* [BUGFIX] Handle "persist" directive in "SparkDFExecutionEngine" properly. ([#7830](https://github.com/great-expectations/great_expectations/pull/7830))
* [BUGFIX] Adding support for Fluent Batch Requests to context.get_validator ([#7808](https://github.com/great-expectations/great_expectations/pull/7808))
* [BUGFIX] FDS - Deletes not immediately reflected in `great_expectations.yml` ([#7843](https://github.com/great-expectations/great_expectations/pull/7843))
* [BUGFIX] `batching_regex` tags are now correctly rendered in docs ([#7845](https://github.com/great-expectations/great_expectations/pull/7845))
* [BUGFIX] Fix link checker and add to mypy type checking ([#7857](https://github.com/great-expectations/great_expectations/pull/7857))
* [BUGFIX] expect_day_count_to_be_close_to_equivalent_week_day_mean ([#7782](https://github.com/great-expectations/great_expectations/pull/7782)) (thanks @HadasManor)
* [BUGFIX] Docs-Tests: `Connection.connect()` was causing Snowflake and BigQuery Tests to Fail ([#7863](https://github.com/great-expectations/great_expectations/pull/7863))
* [DOCS] Prerequisites Cleanup ([#7811](https://github.com/great-expectations/great_expectations/pull/7811))
* [DOCS] Update docs for how_to_initialize_a_filesystem_data_context_in_python ([#7831](https://github.com/great-expectations/great_expectations/pull/7831))
* [DOCS] Updating Checkpoint terms page ([#7722](https://github.com/great-expectations/great_expectations/pull/7722))
* [DOCS] Update how to create a checkpoint with Test YAML config ([#7835](https://github.com/great-expectations/great_expectations/pull/7835))
* [DOCS] Removing datasource centric test_yaml_config doc ([#7836](https://github.com/great-expectations/great_expectations/pull/7836))
* [DOCS] Creating a Checkpoint from an In-Memory Dataframe ([#7701](https://github.com/great-expectations/great_expectations/pull/7701))
* [DOCS] Review and Revise Great Expectations Quickstart ([#7727](https://github.com/great-expectations/great_expectations/pull/7727))
* [MAINTENANCE] FDS - Datasources can rebuild their own asset data_connectors ([#7826](https://github.com/great-expectations/great_expectations/pull/7826))
* [MAINTENANCE] Enable Spark-S3 Integration tests on Azure CI/CD ([#7819](https://github.com/great-expectations/great_expectations/pull/7819))
* [MAINTENANCE] Clean up: Remove duplicated fixture and utilize deeper filtering mechanism for configuration assertions. ([#7825](https://github.com/great-expectations/great_expectations/pull/7825))
* [MAINTENANCE] Enable S3/Spark Connecting To Your Data tests ([#7828](https://github.com/great-expectations/great_expectations/pull/7828))
* [MAINTENANCE] New PR template ([#7710](https://github.com/great-expectations/great_expectations/pull/7710))
* [MAINTENANCE] ruff `.0.262 -> .0.265` ([#7829](https://github.com/great-expectations/great_expectations/pull/7829))
* [MAINTENANCE] Boto import pattern established ([#7796](https://github.com/great-expectations/great_expectations/pull/7796))
* [MAINTENANCE] Prevent TCH001 warnings for pydantic model annotations ([#7846](https://github.com/great-expectations/great_expectations/pull/7846))
* [MAINTENANCE] Pin altair ([#7849](https://github.com/great-expectations/great_expectations/pull/7849))
* [MAINTENANCE] Adding docs link checker to invoke ([#7841](https://github.com/great-expectations/great_expectations/pull/7841))
* [MAINTENANCE] Clean up version checker message formatting ([#7838](https://github.com/great-expectations/great_expectations/pull/7838))
* [MAINTENANCE] Bump nbconvert version ([#7847](https://github.com/great-expectations/great_expectations/pull/7847))
* [MAINTENANCE] Return empty set instead of None ([#7797](https://github.com/great-expectations/great_expectations/pull/7797))
* [MAINTENANCE] Improve misconfigured sampler error message ([#7858](https://github.com/great-expectations/great_expectations/pull/7858))
* [MAINTENANCE] Fixing path formatting for DataConnector of Fluent SparkAzureBlobStorageDatasource and correction of the `SQLAlchemy` compatibility usage in `TableHead` metric ([#7860](https://github.com/great-expectations/great_expectations/pull/7860))
* [MAINTENANCE] S3 Spark Integration Guide - Rendering Fix ([#7864](https://github.com/great-expectations/great_expectations/pull/7864))

0.16.11
-----------------
* [FEATURE] Add tests for `Checkpoint` utilizing SQLAlchemy style Fluent Datasources. ([#7759](https://github.com/great-expectations/great_expectations/pull/7759))
* [FEATURE] Spark parquet reader support for fluent datasources ([#7754](https://github.com/great-expectations/great_expectations/pull/7754))
* [FEATURE] Add tests for `SimpleCheckpoint` utilizing Fluent Datasources with Pandas, Spark, and SQLAlchemy test cases. ([#7778](https://github.com/great-expectations/great_expectations/pull/7778))
* [FEATURE] Spark read directory of files as a single batch for CSV ([#7777](https://github.com/great-expectations/great_expectations/pull/7777))
* [FEATURE] Enable passing "spark_config" through to "SparkDFExecutionEngine" constructor as arguments to "add_spark*()" Fluent Datasources methods. ([#7810](https://github.com/great-expectations/great_expectations/pull/7810))
* [BUGFIX] Patch faulty version checker logic ([#7783](https://github.com/great-expectations/great_expectations/pull/7783))
* [BUGFIX] Fix FDS Sqlite config round tripping ([#7791](https://github.com/great-expectations/great_expectations/pull/7791))
* [BUGFIX] Correct import errors in Azure Blob Storage tests and make Azure Glob Storage and Google Cloud Storage tests more elegant. ([#7795](https://github.com/great-expectations/great_expectations/pull/7795))
* [BUGFIX] Add `pytest` decorator to fixture ([#7803](https://github.com/great-expectations/great_expectations/pull/7803))
* [BUGFIX] fix class name ([#7734](https://github.com/great-expectations/great_expectations/pull/7734)) (thanks @tb102122)
* [BUGFIX] Repair handling of regular expressions partitioning for cloud file storage environments utilizing prefix directive. ([#7798](https://github.com/great-expectations/great_expectations/pull/7798))
* [BUGFIX] AWS Docs reference clash ([#7817](https://github.com/great-expectations/great_expectations/pull/7817))
* [BUGFIX] Cloud - Fix FDS Asset has no attribute `_data_connector` ([#7813](https://github.com/great-expectations/great_expectations/pull/7813))
* [BUGFIX] Upper bound `pyathena` due to breaking API in V3 ([#7821](https://github.com/great-expectations/great_expectations/pull/7821))
* [DOCS] FDS Deployment Pattern - Google Cloud:  BigQuery and GCS ([#7741](https://github.com/great-expectations/great_expectations/pull/7741))
* [DOCS] Remove temporary pin for ipython ([#7784](https://github.com/great-expectations/great_expectations/pull/7784))
* [DOCS] Add CLI Admonition ([#7765](https://github.com/great-expectations/great_expectations/pull/7765))
* [DOCS] Link Update ([#7788](https://github.com/great-expectations/great_expectations/pull/7788))
* [DOCS] Remove Redundant Introduction Headings ([#7747](https://github.com/great-expectations/great_expectations/pull/7747))
* [DOCS] Remove Prerequisites from Admonitions ([#7786](https://github.com/great-expectations/great_expectations/pull/7786))
* [DOCS] Link Updates ([#7781](https://github.com/great-expectations/great_expectations/pull/7781))
* [DOCS] FDS Deployment Pattern - AWS: Spark and S3 ([#7775](https://github.com/great-expectations/great_expectations/pull/7775))
* [MAINTENANCE] Add check to `CloudDataContext` to ensure using latest PyPI version ([#7753](https://github.com/great-expectations/great_expectations/pull/7753))
* [MAINTENANCE] Cache the latest great_expectations version ([#7785](https://github.com/great-expectations/great_expectations/pull/7785))
* [MAINTENANCE] Enable `flake8-bugbear` rules ([#7776](https://github.com/great-expectations/great_expectations/pull/7776))
* [MAINTENANCE] Cleanup of Fluent `BatchRequest` type and immutability constraints ([#7769](https://github.com/great-expectations/great_expectations/pull/7769))
* [MAINTENANCE] CLI warnings for `suite new` command ([#7787](https://github.com/great-expectations/great_expectations/pull/7787))
* [MAINTENANCE] Update pip instal extras and use AWS_ env vars ([#7793](https://github.com/great-expectations/great_expectations/pull/7793))
* [MAINTENANCE] Test DirectoryCSVAsset with both str and pathlib.Path ([#7801](https://github.com/great-expectations/great_expectations/pull/7801))
* [MAINTENANCE] Lint `test/data_context` ([#7767](https://github.com/great-expectations/great_expectations/pull/7767))
* [MAINTENANCE] FDS Documentation Update - S3 Pandas reference fixes ([#7789](https://github.com/great-expectations/great_expectations/pull/7789))
* [MAINTENANCE] Update all pytest calls in CI to show reason skipped ([#7806](https://github.com/great-expectations/great_expectations/pull/7806))
* [MAINTENANCE] Dont run runme_script_runner_tests stage on forks ([#7807](https://github.com/great-expectations/great_expectations/pull/7807))
* [MAINTENANCE] Lint `tests/checkpoint` & `tests/execution_engine` ([#7804](https://github.com/great-expectations/great_expectations/pull/7804))
* [MAINTENANCE] docs-integration re-start ([#7735](https://github.com/great-expectations/great_expectations/pull/7735))
* [MAINTENANCE] Remove runme fixtures/stages and enable docs-integration to run automatically ([#7812](https://github.com/great-expectations/great_expectations/pull/7812))
* [MAINTENANCE] Fix linting error. ([#7820](https://github.com/great-expectations/great_expectations/pull/7820))
* [MAINTENANCE] Fix pin count. ([#7823](https://github.com/great-expectations/great_expectations/pull/7823))

0.16.10
-----------------
* [FEATURE] Add tests for `Checkpoint` utilizing Pandas and Spark style Fluent Datasources. ([#7740](https://github.com/great-expectations/great_expectations/pull/7740))
* [FEATURE] Fluent `BatchRequest` slicing ([#7706](https://github.com/great-expectations/great_expectations/pull/7706))
* [BUGFIX] Patch Expectation registry issue introduced in 0.16.9 ([#7771](https://github.com/great-expectations/great_expectations/pull/7771))
* [DOCS] Remove, relocate, consolidate, and edit Contributing content ([#7669](https://github.com/great-expectations/great_expectations/pull/7669))
* [DOCS] Temporarily pin ipython for python 3.8 before building api docs ([#7764](https://github.com/great-expectations/great_expectations/pull/7764))
* [DOCS] Update Links in Configure Topics ([#7760](https://github.com/great-expectations/great_expectations/pull/7760))
* [DOCS] Link Updates ([#7768](https://github.com/great-expectations/great_expectations/pull/7768))
* [MAINTENANCE] FDS Deployment Guide - Pandas S3 fix reference ([#7755](https://github.com/great-expectations/great_expectations/pull/7755))
* [MAINTENANCE] IPython Python 3.8 upper bound ([#7763](https://github.com/great-expectations/great_expectations/pull/7763))
* [MAINTENANCE] breakup mypy ci steps ([#7761](https://github.com/great-expectations/great_expectations/pull/7761))
* [MAINTENANCE] fix async type-check step ([#7772](https://github.com/great-expectations/great_expectations/pull/7772))
* [MAINTENANCE] Bump Python version in `static_type_check` stage of async CI ([#7773](https://github.com/great-expectations/great_expectations/pull/7773))

0.16.9
-----------------
* [FEATURE] Implementing Fluent Datasources Support for Checkpoint ([#7697](https://github.com/great-expectations/great_expectations/pull/7697))
* [FEATURE] FDS persist `DataAsset` to YAML file immediately on creation ([#7705](https://github.com/great-expectations/great_expectations/pull/7705))
* [FEATURE] Cloud support FDS deletes ([#7682](https://github.com/great-expectations/great_expectations/pull/7682))
* [FEATURE] Persist Cloud DataAssets on creation ([#7748](https://github.com/great-expectations/great_expectations/pull/7748))
* [FEATURE] Add tests for `Checkpoint` utilizing Pandas and Spark style Fluent Datasources. ([#7740](https://github.com/great-expectations/great_expectations/pull/7740))
* [BUGFIX] Render Correct Fonts in Data Assistant Plot graphs ([#7676](https://github.com/great-expectations/great_expectations/pull/7676))
* [BUGFIX] fix rendering data asset name in microsoft teams notification ([#7675](https://github.com/great-expectations/great_expectations/pull/7675))
* [BUGFIX] Register core Expectations JIT in Validator workflows ([#7683](https://github.com/great-expectations/great_expectations/pull/7683))
* [BUGFIX] Data Context Datasource CRUD support for Fluent Datasources ([#7660](https://github.com/great-expectations/great_expectations/pull/7660))
* [BUGFIX] Replace renamed fixture ([#7711](https://github.com/great-expectations/great_expectations/pull/7711))
* [BUGFIX] Add missing pyspark reference ([#7684](https://github.com/great-expectations/great_expectations/pull/7684)) (thanks @willfeltman)
* [DOCS] Add fluent datasources and yaml configuration warning message ([#7673](https://github.com/great-expectations/great_expectations/pull/7673))
* [DOCS] D/ /fluent connect to data overview ([#7671](https://github.com/great-expectations/great_expectations/pull/7671))
* [DOCS] Update fluent In Progress Cautionary Note ([#7681](https://github.com/great-expectations/great_expectations/pull/7681))
* [DOCS] Remove version reference ([#7644](https://github.com/great-expectations/great_expectations/pull/7644))
* [DOCS] Removing in-progress from docs confirmed as up-to-date ([#7686](https://github.com/great-expectations/great_expectations/pull/7686))
* [DOCS] Updated Datasource terms page ([#7692](https://github.com/great-expectations/great_expectations/pull/7692))
* [DOCS] Removing json schema profiler documentation ([#7694](https://github.com/great-expectations/great_expectations/pull/7694))
* [DOCS] Removing CLI-based suite edit workflow ([#7689](https://github.com/great-expectations/great_expectations/pull/7689))
* [DOCS] Updated onboarding data assistant docs test script to Fluent-style ([#7695](https://github.com/great-expectations/great_expectations/pull/7695))
* [DOCS] Update for fluent datasources: Expectations that span multiple batches evaluation params ([#7668](https://github.com/great-expectations/great_expectations/pull/7668))
* [DOCS] Add fluent docs and test create and edit expectations with profiler ([#7696](https://github.com/great-expectations/great_expectations/pull/7696))
* [DOCS] Quick docstring update for list_datasources ([#7699](https://github.com/great-expectations/great_expectations/pull/7699))
* [DOCS] Retiring the CLI ([#7700](https://github.com/great-expectations/great_expectations/pull/7700))
* [DOCS] Updating the Rule-Based Profiler doc to Fluent ([#7698](https://github.com/great-expectations/great_expectations/pull/7698))
* [DOCS] Update Batch Request glossary entry. ([#7716](https://github.com/great-expectations/great_expectations/pull/7716))
* [DOCS] Removed guide for no YML, redirect to EphemeralDataContext ([#7702](https://github.com/great-expectations/great_expectations/pull/7702))
* [DOCS] Update for fluent datasources: Dynamically load evaluation params from a database ([#7717](https://github.com/great-expectations/great_expectations/pull/7717))
* [DOCS] Update batch glossary docs. ([#7726](https://github.com/great-expectations/great_expectations/pull/7726))
* [DOCS] Update for fluent datasources: Create a new Checkpoint ([#7729](https://github.com/great-expectations/great_expectations/pull/7729))
* [DOCS] Temporarily revert `update_expectation_suite` call in GX Cloud quickstart ([#7736](https://github.com/great-expectations/great_expectations/pull/7736))
* [DOCS] Light update to How to add validations data or suites to a Checkpoint ([#7703](https://github.com/great-expectations/great_expectations/pull/7703))
* [DOCS] Updating cross-table comparison guide with Fluent Datasources ([#7691](https://github.com/great-expectations/great_expectations/pull/7691))
* [DOCS] Better output from `invoke public-api` report ([#7730](https://github.com/great-expectations/great_expectations/pull/7730))
* [DOCS] Removed unneeded calls to update datasource in docs. ([#7739](https://github.com/great-expectations/great_expectations/pull/7739))
* [DOCS] FDS Deployment Pattern - AWS S3 Pandas ([#7718](https://github.com/great-expectations/great_expectations/pull/7718))
* [DOCS] Update pypyi page urls ([#7752](https://github.com/great-expectations/great_expectations/pull/7752))
* [MAINTENANCE] Correcting minor typographical errors and type hints issues in Checkpoint and Test Checkpoint Modules ([#7665](https://github.com/great-expectations/great_expectations/pull/7665))
* [MAINTENANCE] Only attempt docs-integration pipeline when manually triggered ([#7674](https://github.com/great-expectations/great_expectations/pull/7674))
* [MAINTENANCE] Clean up Checkpoint test method names and usage of batch_request_dict fixture ([#7670](https://github.com/great-expectations/great_expectations/pull/7670))
* [MAINTENANCE] Correct typo in Checkpoint test method fixture ([#7677](https://github.com/great-expectations/great_expectations/pull/7677))
* [MAINTENANCE] Enable remaining `CloudDataContext` `ExpectationSuite` CRUD ([#7646](https://github.com/great-expectations/great_expectations/pull/7646))
* [MAINTENANCE] list_datasources should return FDS configs as well ([#7667](https://github.com/great-expectations/great_expectations/pull/7667))
* [MAINTENANCE] Exit with error when attempting to delete a fluent style datasource using the CLI ([#7687](https://github.com/great-expectations/great_expectations/pull/7687))
* [MAINTENANCE] Add warning to `datasource list` command if fluent datasources are detected ([#7690](https://github.com/great-expectations/great_expectations/pull/7690))
* [MAINTENANCE] ruff update `0.0.262` ([#7707](https://github.com/great-expectations/great_expectations/pull/7707))
* [MAINTENANCE] Adding black to invoke lint ([#7715](https://github.com/great-expectations/great_expectations/pull/7715))
* [MAINTENANCE] Use same version of mypy in contrib tool ([#7724](https://github.com/great-expectations/great_expectations/pull/7724))
* [MAINTENANCE] Update a Fluent Datasource related fixture name to better reflect its capabilities ([#7725](https://github.com/great-expectations/great_expectations/pull/7725))
* [MAINTENANCE] Add CLI warnings when adding a checkpoint with fluent datasources ([#7685](https://github.com/great-expectations/great_expectations/pull/7685))
* [MAINTENANCE] Iterate over the regex_pattern characters too in ([#7720](https://github.com/great-expectations/great_expectations/pull/7720))
* [MAINTENANCE] Minor stylistic cleanup ([#7732](https://github.com/great-expectations/great_expectations/pull/7732))
* [MAINTENANCE] fix get available data assets names for fds ([#7723](https://github.com/great-expectations/great_expectations/pull/7723))
* [MAINTENANCE] add warning messages when using CLI to edit an expectaiton suite if fluent datasources are present ([#7714](https://github.com/great-expectations/great_expectations/pull/7714))
* [MAINTENANCE] add warning to `datasource new` CLI command ([#7709](https://github.com/great-expectations/great_expectations/pull/7709))
* [MAINTENANCE] Add split/join logic to build_gallery process ([#7572](https://github.com/great-expectations/great_expectations/pull/7572))
* [MAINTENANCE] Use invoke public-api in main CI pipeline ([#7746](https://github.com/great-expectations/great_expectations/pull/7746))
* [MAINTENANCE] Add remaining `public_api` decorators for core fluent datasources ([#7749](https://github.com/great-expectations/great_expectations/pull/7749))
* [MAINTENANCE] FDS update schemas - fixes CI ([#7751](https://github.com/great-expectations/great_expectations/pull/7751))
* [MAINTENANCE] FDS Deployment Guide - Pandas S3 fix reference ([#7755](https://github.com/great-expectations/great_expectations/pull/7755))

0.16.8
-----------------
* [FEATURE] add Fluent Datasources to `CloudDataContext` ([#7570](https://github.com/great-expectations/great_expectations/pull/7570))
* [BUGFIX] fix marshmallow schema for SQLAlchemy `connect_args` passthrough ([#7614](https://github.com/great-expectations/great_expectations/pull/7614))
* [BUGFIX] MapCondition Memory Inefficiencies in Spark ([#7626](https://github.com/great-expectations/great_expectations/pull/7626))
* [BUGFIX] Fix capitalone_dataprofiler_expectations imports ([#7658](https://github.com/great-expectations/great_expectations/pull/7658))
* [BUGFIX] CloudDataContext creates `great_expectations.yml` when adding a Fluent datasource ([#7657](https://github.com/great-expectations/great_expectations/pull/7657))
* [BUGFIX] Correct GX configuration structure that incorporates both V3 and Fluent Datasources ([#7661](https://github.com/great-expectations/great_expectations/pull/7661))
* [BUGFIX] Patch broken `include_rendered_content` test in advance of `0.16.8` release ([#7663](https://github.com/great-expectations/great_expectations/pull/7663))
* [DOCS] Corrects Step Numbering in How to instantiate a specific Filesystem Data Context ([#7612](https://github.com/great-expectations/great_expectations/pull/7612))
* [DOCS] Corrects Heading Issue in How to host and share Data Docs on Azure Blob Storage ([#7620](https://github.com/great-expectations/great_expectations/pull/7620))
* [DOCS] Update overview.md ([#7627](https://github.com/great-expectations/great_expectations/pull/7627))
* [DOCS] Updates the "Interactive Mode" guide for creating Expectations ([#7624](https://github.com/great-expectations/great_expectations/pull/7624))
* [DOCS] Updates the language in the banner linking the legacy site to the current docs. ([#7636](https://github.com/great-expectations/great_expectations/pull/7636))
* [DOCS] Improve expect_column_values_to_be_of_type docstring ([#7632](https://github.com/great-expectations/great_expectations/pull/7632))
* [DOCS] Corrects a typo found in the navigation section of the legacy docs ([#7643](https://github.com/great-expectations/great_expectations/pull/7643))
* [DOCS] Add lakeFS to list of data version control tools ([#7642](https://github.com/great-expectations/great_expectations/pull/7642)) (thanks @rmoff)
* [DOCS] Standardize language around GX Cloud access tokens ([#7621](https://github.com/great-expectations/great_expectations/pull/7621))
* [DOCS] Added IAM user and IAM assume role doc ([#7634](https://github.com/great-expectations/great_expectations/pull/7634)) (thanks @Reactor11)
* [DOCS] update to location of cloud callout in the OSS Quickstart ([#7616](https://github.com/great-expectations/great_expectations/pull/7616))
* [MAINTENANCE] Update `teams.yml` ([#7623](https://github.com/great-expectations/great_expectations/pull/7623))
* [MAINTENANCE] Utilize `NotImported` for SQLAlchemy, Google Cloud Services, Azure Blob Storage, and Spark import usage ([#7617](https://github.com/great-expectations/great_expectations/pull/7617))
* [MAINTENANCE] Remove stray cloud test marker. ([#7639](https://github.com/great-expectations/great_expectations/pull/7639))
* [MAINTENANCE] Upgrade mypy to 1.2.0 ([#7645](https://github.com/great-expectations/great_expectations/pull/7645))
* [MAINTENANCE] Static type checking with python 3.8 ([#7637](https://github.com/great-expectations/great_expectations/pull/7637))
* [MAINTENANCE] Static type checking with python 3.8 followup ([#7647](https://github.com/great-expectations/great_expectations/pull/7647))
* [MAINTENANCE] The 'sklearn' PyPI package is deprecated, use 'scikit-learn' ([#7651](https://github.com/great-expectations/great_expectations/pull/7651))
* [MAINTENANCE] numpy.typing only available after v1.20 ([#7654](https://github.com/great-expectations/great_expectations/pull/7654))
* [MAINTENANCE] Update NotImported mechanism to use scoped compatibility modules ([#7635](https://github.com/great-expectations/great_expectations/pull/7635))
* [MAINTENANCE] Uncap `altair` version, and bump minimum version to `4.2.1`. Also uncap `urllib3` version, and bump minimum version to `1.26` ([#7650](https://github.com/great-expectations/great_expectations/pull/7650))

0.16.7
-----------------
* [FEATURE] Added AssumeRole Feature ([#7547](https://github.com/great-expectations/great_expectations/pull/7547)) (thanks @Reactor11)
* [BUGFIX] Fix Fluent Spark `DataConnectors` on config load ([#7560](https://github.com/great-expectations/great_expectations/pull/7560))
* [BUGFIX] `dataset_name` made optional parameter for Expectations ([#7603](https://github.com/great-expectations/great_expectations/pull/7603))
* [BUGFIX] Misc gallery bugfixes ([#7611](https://github.com/great-expectations/great_expectations/pull/7611))
* [BUGFIX] Remove spark from bic Expectations since it never worked for them ([#7619](https://github.com/great-expectations/great_expectations/pull/7619))
* [DOCS] Use current minor version number in drop down instead of "Current" ([#7581](https://github.com/great-expectations/great_expectations/pull/7581))
* [DOCS] Adds deprecation policy to changelog page ([#7585](https://github.com/great-expectations/great_expectations/pull/7585))
* [DOCS] Use the actual version after release ([#7583](https://github.com/great-expectations/great_expectations/pull/7583))
* [DOCS] Update some docs_rtd requirements so the venv can be created successfully ([#7580](https://github.com/great-expectations/great_expectations/pull/7580))
* [DOCS] Add Cloud quickstart ([#7441](https://github.com/great-expectations/great_expectations/pull/7441))
* [DOCS] Updates how the GX Cloud Beta is referenced in the Quickstart guide. ([#7594](https://github.com/great-expectations/great_expectations/pull/7594))
* [DOCS]  Corrects typo in code block within in-memory Pandas guide ([#7600](https://github.com/great-expectations/great_expectations/pull/7600))
* [DOCS] Updates to Contributing through GitHub ([#7601](https://github.com/great-expectations/great_expectations/pull/7601))
* [DOCS] Correct expectation documentation for expect_column_max_to_be_between ([#7597](https://github.com/great-expectations/great_expectations/pull/7597))
* [DOCS] Add scripts under test for "How to create and edit Expectations with instant feedback from a sample Batch of data" ([#7615](https://github.com/great-expectations/great_expectations/pull/7615))
* [DOCS] Corrects Step Numbering in How to instantiate a specific Filesystem Data Context ([#7612](https://github.com/great-expectations/great_expectations/pull/7612))
* [DOCS] Corrects Heading Issue in How to host and share Data Docs on Azure Blob Storage ([#7620](https://github.com/great-expectations/great_expectations/pull/7620))
* [MAINTENANCE] Warning non integer slice on row for SQLAlchemy 2.0 Compatibility ([#7501](https://github.com/great-expectations/great_expectations/pull/7501))
* [MAINTENANCE] Warning MetaData.bind argument deprecated for SQLAlchemy 2.0 Compatibility ([#7502](https://github.com/great-expectations/great_expectations/pull/7502))
* [MAINTENANCE] Capitalize "If" in rendering of conditional Expectations ([#7588](https://github.com/great-expectations/great_expectations/pull/7588))
* [MAINTENANCE] Remove pip pins in CI and in contributing_setup.md ([#7587](https://github.com/great-expectations/great_expectations/pull/7587))
* [MAINTENANCE] Remove ignore of warning deprecated api features detected sqlalchemy 2 ([#7584](https://github.com/great-expectations/great_expectations/pull/7584))
* [MAINTENANCE] Fix sqlalchemy 2.0 incompatible warnings ([#7589](https://github.com/great-expectations/great_expectations/pull/7589))
* [MAINTENANCE] Increase minimum scipy version package to 1.6.0 to take advantage of available capabilities. ([#7591](https://github.com/great-expectations/great_expectations/pull/7591))
* [MAINTENANCE] Remove s3fs dependency and upper bound for boto3 ([#7598](https://github.com/great-expectations/great_expectations/pull/7598))
* [MAINTENANCE] Move Fluent Datasources Sorters into `TYPE_CHECKING` block ([#7602](https://github.com/great-expectations/great_expectations/pull/7602))
* [MAINTENANCE] Bump terser from 5.10.0 to 5.16.8 in /docs/docusaurus ([#7486](https://github.com/great-expectations/great_expectations/pull/7486)) (thanks @dependabot[bot])
* [MAINTENANCE] Bump cookiecutter from 1.7.3 to 2.1.1 in /contrib/cli ([#7510](https://github.com/great-expectations/great_expectations/pull/7510)) (thanks @dependabot[bot])
* [MAINTENANCE] Polish and ratchet requirements pins and upper bounds ([#7604](https://github.com/great-expectations/great_expectations/pull/7604))
* [MAINTENANCE] small documentation updates ([#7606](https://github.com/great-expectations/great_expectations/pull/7606))
* [MAINTENANCE] SqlAlchemy 2 Compatibility - `engine.execute()` ([#7469](https://github.com/great-expectations/great_expectations/pull/7469))
* [MAINTENANCE]  Deprecate ColumnExpectation in favor of ColumnAggregateExpectation ([#7609](https://github.com/great-expectations/great_expectations/pull/7609))
* [MAINTENANCE] Deprecate TableExpectation in favor of BatchExpectation ([#7610](https://github.com/great-expectations/great_expectations/pull/7610))
* [MAINTENANCE] Explicitly test relevant modules in Sqlalchemy compatibility pipeline ([#7613](https://github.com/great-expectations/great_expectations/pull/7613))
* [MAINTENANCE] Fluent Datasources: Eliminate redundant Datasource name and DataAsset name from dictionary and JSON configuration ([#7573](https://github.com/great-expectations/great_expectations/pull/7573))
* [CONTRIB] add check to calculate difference between 2 dates in month ([#7576](https://github.com/great-expectations/great_expectations/pull/7576)) (thanks @tb102122)
* [CONTRIB] Expect Column Values to be Valid UUID - Added SqlAlchemyExecutionEngine support ([#7592](https://github.com/great-expectations/great_expectations/pull/7592)) (thanks @asafla)

0.16.6
-----------------
* [FEATURE] Fluent `DataAsset` `batch_metadata` config variables ([#7513](https://github.com/great-expectations/great_expectations/pull/7513))
* [FEATURE] Add batch metadata to spark add_*_asset methods ([#7534](https://github.com/great-expectations/great_expectations/pull/7534))
* [BUGFIX] Fluent Datasource load from config fixes for remaining Pandas Datasources ([#7442](https://github.com/great-expectations/great_expectations/pull/7442))
* [BUGFIX] Address `pandas==2.0.0` test failures ([#7553](https://github.com/great-expectations/great_expectations/pull/7553))
* [BUGFIX] Render prescriptive `ExpectationConfiguration`s with evaluation parameters inline ([#7552](https://github.com/great-expectations/great_expectations/pull/7552))
* [BUGFIX] Release Pipeline Fix ([#7575](https://github.com/great-expectations/great_expectations/pull/7575))
* [DOCS] Update GX version in `_data.jsx` component ([#7549](https://github.com/great-expectations/great_expectations/pull/7549))
* [DOCS] Adds guides on using Ephemeral Data Contexts and updates Quickstart Next Steps ([#7500](https://github.com/great-expectations/great_expectations/pull/7500))
* [DOCS] Fixes broken code block and incorrectly numbered steps in "How to organize Batches in a SQL-based Data Asset" ([#7533](https://github.com/great-expectations/great_expectations/pull/7533))
* [DOCS] Update nav to match gx.io site ([#7557](https://github.com/great-expectations/great_expectations/pull/7557))
* [DOCS] Corrects step numbers in "How to organize Batches in a file-based Data Asset" ([#7559](https://github.com/great-expectations/great_expectations/pull/7559))
* [DOCS] Delete SLACK_GUIDELINES.md ([#7566](https://github.com/great-expectations/great_expectations/pull/7566))
* [DOCS] Update syntax highlighting of code blocks in GX Cloud Getting Started guide ([#7563](https://github.com/great-expectations/great_expectations/pull/7563))
* [DOCS] Fix code snippets for earlier versions ([#7554](https://github.com/great-expectations/great_expectations/pull/7554))
* [DOCS]  Fix typo in docs ([#7568](https://github.com/great-expectations/great_expectations/pull/7568))
* [DOCS] Moar typo fix ([#7569](https://github.com/great-expectations/great_expectations/pull/7569))
* [DOCS] removes the original getting started tutorial pages and redirects to the quickstart guide ([#7548](https://github.com/great-expectations/great_expectations/pull/7548))
* [DOCS] Fix integral typo ([#7578](https://github.com/great-expectations/great_expectations/pull/7578))
* [DOCS] Prepare earlier versions using develop ([#7567](https://github.com/great-expectations/great_expectations/pull/7567))
* [DOCS] Use orange in docs logs ([#7579](https://github.com/great-expectations/great_expectations/pull/7579))
* [DOCS] Add GX Cloud Onboarding Script ([#7517](https://github.com/great-expectations/great_expectations/pull/7517))
* [MAINTENANCE] release prep for 0.16.5 ([#7545](https://github.com/great-expectations/great_expectations/pull/7545))
* [MAINTENANCE] Test Pandas 2.0 prerelease in CI/CD ([#7343](https://github.com/great-expectations/great_expectations/pull/7343))
* [MAINTENANCE] Add noqa directives for existing sqlalchemy imports ([#7564](https://github.com/great-expectations/great_expectations/pull/7564))
* [MAINTENANCE] Add ruff rule for sqlalchemy imports ([#7562](https://github.com/great-expectations/great_expectations/pull/7562))
* [MAINTENANCE] adding a footer to data docs with a link to the cloud page ([#7532](https://github.com/great-expectations/great_expectations/pull/7532))
* [MAINTENANCE] Harden tests for `CloudDataContext` always `include_rendered_content` ([#7558](https://github.com/great-expectations/great_expectations/pull/7558))
* [MAINTENANCE] FluentDatasources - Quickstart Snippets converted to Named Snippets ([#7550](https://github.com/great-expectations/great_expectations/pull/7550))
* [MAINTENANCE] Simplify `GXCloudStoreBackend._has_key` check ([#7561](https://github.com/great-expectations/great_expectations/pull/7561))
* [MAINTENANCE] Temporarily Pin `pandas<2.0.0` for compatibility ([#7571](https://github.com/great-expectations/great_expectations/pull/7571))
* [MAINTENANCE] SqlAlchemy 2.0 Compatibility - branched connection + `bind` argument now required ([#7529](https://github.com/great-expectations/great_expectations/pull/7529))
* [MAINTENANCE]  Add missing docstrings to fluent `sql_datasource` splitter methods. ([#7577](https://github.com/great-expectations/great_expectations/pull/7577))

0.16.5
-----------------
* [FEATURE] Add batch metadata to sql datasources. ([#7499](https://github.com/great-expectations/great_expectations/pull/7499))
* [BUGFIX] Fix issue running quickstart ([#7539](https://github.com/great-expectations/great_expectations/pull/7539))
* [DOCS] doc 508 Updates footer links on docs pages ([#7521](https://github.com/great-expectations/great_expectations/pull/7521))
* [DOCS] DSB-64 removes outdated v2/v3 references from the docs ([#7519](https://github.com/great-expectations/great_expectations/pull/7519))
* [DOCS] Update CODEOWNERS ([#7528](https://github.com/great-expectations/great_expectations/pull/7528))
* [DOCS] Quickstart code under test ([#7542](https://github.com/great-expectations/great_expectations/pull/7542))
* [MAINTENANCE] SqlAlchemy2 Compatibility - `Row.keys()` ([#7520](https://github.com/great-expectations/great_expectations/pull/7520))
* [MAINTENANCE] Refactoring of CapitalOne Metrics and Profiler-Based DataAssistant for Enhanced Code Elegance ([#7522](https://github.com/great-expectations/great_expectations/pull/7522))
* [MAINTENANCE] SqlAlchemy 2 Compatibility - Autoload Parameter deprecation ([#7526](https://github.com/great-expectations/great_expectations/pull/7526))
* [MAINTENANCE] Bump notebook from 6.4.1 to 6.4.12 in /docs_rtd ([#7511](https://github.com/great-expectations/great_expectations/pull/7511))
* [MAINTENANCE] Break out unit tests to own stage. ([#7530](https://github.com/great-expectations/great_expectations/pull/7530))
* [MAINTENANCE] Bump wheel from 0.37.1 to 0.38.1 in /contrib/cli ([#7493](https://github.com/great-expectations/great_expectations/pull/7493))
* [MAINTENANCE] Simplifying CapitalOne DataProfilerColumnDomainBuilder Using Default "profile_path" Argument ([#7535](https://github.com/great-expectations/great_expectations/pull/7535))
* [MAINTENANCE] : Clean up ununsed imports ([#7537](https://github.com/great-expectations/great_expectations/pull/7537))
* [MAINTENANCE] Fix Type-Checking steps ([#7536](https://github.com/great-expectations/great_expectations/pull/7536))
* [MAINTENANCE] Disable UserConfigurableProfiler tests relying on deprecated V2 functionality ([#7541](https://github.com/great-expectations/great_expectations/pull/7541))
* [MAINTENANCE] : replace ColumnMetricProvider with ColumnAggregateMetricProvider ([#7538](https://github.com/great-expectations/great_expectations/pull/7538))
* [MAINTENANCE] Exclude files from deprecation warning check ([#7544](https://github.com/great-expectations/great_expectations/pull/7544))

0.16.4
-----------------
* [FEATURE] Add package, contributors and metrics filter in Algolia script for expectation ([#7000](https://github.com/great-expectations/great_expectations/pull/7000)) (thanks @kod-er)
* [FEATURE] `BatchMetadata` for all fluent `DataAsset`s ([#7392](https://github.com/great-expectations/great_expectations/pull/7392))
* [FEATURE] Introducing CapitalOne DataProfilerColumnDomainBuilder as well as multiple improvements to CapitalOne codebase and testability. ([#7498](https://github.com/great-expectations/great_expectations/pull/7498))
* [BUGFIX] Repair SparkSession initialization behavior to disallow restarting, unless explicitly instructed through configuration ([#7444](https://github.com/great-expectations/great_expectations/pull/7444))
* [BUGFIX] Skip dialect specific tests if no flag passed or flag not available ([#7443](https://github.com/great-expectations/great_expectations/pull/7443))
* [BUGFIX] Ensure that MetricStore Records "data_asset_name" Properly ([#7458](https://github.com/great-expectations/great_expectations/pull/7458))
* [BUGFIX] Fix incorrect type hint and correct typographical errors in DomainBuilder docstrings and fill in missing docstrings ([#7467](https://github.com/great-expectations/great_expectations/pull/7467))
* [BUGFIX] Reset Metrics Registry in order to keep state of Metrics Registry test cases Runs mutually consistent ([#7473](https://github.com/great-expectations/great_expectations/pull/7473))
* [BUGFIX] Corrected typographical errors in two docstrings ([#7506](https://github.com/great-expectations/great_expectations/pull/7506))
* [BUGFIX] Typo in min versions install ([#7516](https://github.com/great-expectations/great_expectations/pull/7516))
* [DOCS] New ADR proposal for patch version support ([#7451](https://github.com/great-expectations/great_expectations/pull/7451))
* [DOCS] Remove outdated instructions for building documentation ([#7457](https://github.com/great-expectations/great_expectations/pull/7457))
* [DOCS] Updating the docs to gx_dev ([#7455](https://github.com/great-expectations/great_expectations/pull/7455))
* [DOCS] Fixes typo in code snippet for "How to organize Batches in a file-based Data Asset" guide ([#7465](https://github.com/great-expectations/great_expectations/pull/7465))
* [DOCS] Postgresql drivername fix for SQLAlchemy compatibility. Closes #7464 ([#7466](https://github.com/great-expectations/great_expectations/pull/7466)) (thanks @Itzblend)
* [DOCS] Corrects code snippets ([#7470](https://github.com/great-expectations/great_expectations/pull/7470))
* [DOCS] Add a note about installing version of pyspark that matches Spark version ([#7483](https://github.com/great-expectations/great_expectations/pull/7483))
* [DOCS] adding cloud language to quickstart ([#7484](https://github.com/great-expectations/great_expectations/pull/7484))
* [DOCS] doc-409 Corrects links in databricks guide ([#7485](https://github.com/great-expectations/great_expectations/pull/7485))
* [DOCS] Doc-472 Corrects numbering of steps in guide ([#7478](https://github.com/great-expectations/great_expectations/pull/7478))
* [DOCS] DOC-474 Updates URL for usage statistics page ([#7477](https://github.com/great-expectations/great_expectations/pull/7477))
* [DOCS] Testing ADR ([#7495](https://github.com/great-expectations/great_expectations/pull/7495))
* [DOCS] corrects typo in GCS setup guide ([#7514](https://github.com/great-expectations/great_expectations/pull/7514))
* [MAINTENANCE] Case whens argument change for SQLAlchemy 2.0 compatibility ([#7416](https://github.com/great-expectations/great_expectations/pull/7416))
* [MAINTENANCE] `mypy` `1.1.1` update ([#7452](https://github.com/great-expectations/great_expectations/pull/7452))
* [MAINTENANCE] Remove v2 api CLI ([#7440](https://github.com/great-expectations/great_expectations/pull/7440))
* [MAINTENANCE] Bump http-cache-semantics from 4.1.0 to 4.1.1 in /docs/docusaurus ([#7447](https://github.com/great-expectations/great_expectations/pull/7447))
* [MAINTENANCE] Updating language per issue 3572 ([#7456](https://github.com/great-expectations/great_expectations/pull/7456))
* [MAINTENANCE] Remove v2 api expectations tests ([#7439](https://github.com/great-expectations/great_expectations/pull/7439))
* [MAINTENANCE] Move docs_link_checker.py and create new docs-specific pipeline ([#7422](https://github.com/great-expectations/great_expectations/pull/7422))
* [MAINTENANCE] select call style change for SQLAlchemy 2 compatibility ([#7378](https://github.com/great-expectations/great_expectations/pull/7378))
* [MAINTENANCE] Decruft map_metric_provider.py ([#7460](https://github.com/great-expectations/great_expectations/pull/7460))
* [MAINTENANCE] Add tests for `_register_metric_functions` in the `MetricProvider` class hierarchy. ([#7459](https://github.com/great-expectations/great_expectations/pull/7459))
* [MAINTENANCE] SqlAlchemy2 Compatibility - implicit autocommit ([#7400](https://github.com/great-expectations/great_expectations/pull/7400))
* [MAINTENANCE] Bump ua-parser-js from 0.7.31 to 0.7.34 in /docs/docusaurus ([#7474](https://github.com/great-expectations/great_expectations/pull/7474))
* [MAINTENANCE] Remove SQLAlchemyDataset/Datasource ([#7471](https://github.com/great-expectations/great_expectations/pull/7471))
* [MAINTENANCE] Bump json5 from 1.0.1 to 1.0.2 in /docs/docusaurus ([#7475](https://github.com/great-expectations/great_expectations/pull/7475))
* [MAINTENANCE] Bump @sideway/formula from 3.0.0 to 3.0.1 in /docs/docusaurus ([#7487](https://github.com/great-expectations/great_expectations/pull/7487))
* [MAINTENANCE] Bump ipython from 7.31.1 to 8.10.0 in /docs_rtd ([#7491](https://github.com/great-expectations/great_expectations/pull/7491))
* [MAINTENANCE] Bump cross-fetch from 3.1.4 to 3.1.5 in /docs/docusaurus ([#7488](https://github.com/great-expectations/great_expectations/pull/7488))
* [MAINTENANCE] Deprecated API features detected warning for SQLAlchemy 2.0 compatibility ([#7490](https://github.com/great-expectations/great_expectations/pull/7490))
* [MAINTENANCE] type-checking implementation files ([#7454](https://github.com/great-expectations/great_expectations/pull/7454))
* [MAINTENANCE] Small Refactor of ColumnDomainBuilder for code elegance and computational performance improvements ([#7492](https://github.com/great-expectations/great_expectations/pull/7492))
* [MAINTENANCE] Lower pydantic requirement to v1.9.2 or greater ([#7482](https://github.com/great-expectations/great_expectations/pull/7482))
* [MAINTENANCE] Connection.connect warning for SQLAlchemy 2.0 compatibility ([#7489](https://github.com/great-expectations/great_expectations/pull/7489))
* [MAINTENANCE] Pass `PandasDatasource` `batch_metadata` as `kwargs` to remove possibility of `None` on `DataAsset` model ([#7503](https://github.com/great-expectations/great_expectations/pull/7503))
* [MAINTENANCE] Make `dataset_name` a parameter for Expectations tests or create name from `Expectation` name, which ensures only limited number of tables created. ([#7476](https://github.com/great-expectations/great_expectations/pull/7476))
* [MAINTENANCE] Fix sqlalchemy warnings for pandas + sql fluent datasources ([#7504](https://github.com/great-expectations/great_expectations/pull/7504))
* [MAINTENANCE] Bump gitpython from 3.1.7 to 3.1.30 in /docs_rtd ([#7494](https://github.com/great-expectations/great_expectations/pull/7494))
* [MAINTENANCE] Bump certifi from 2020.6.20 to 2022.12.7 in /docs_rtd ([#7497](https://github.com/great-expectations/great_expectations/pull/7497))
* [MAINTENANCE] Bump jupyter-core from 4.6.3 to 4.11.2 in /docs_rtd ([#7496](https://github.com/great-expectations/great_expectations/pull/7496))
* [MAINTENANCE] Bump nbconvert from 5.6.1 to 6.5.1 in /docs_rtd ([#7508](https://github.com/great-expectations/great_expectations/pull/7508))
* [MAINTENANCE] Bump numpy from 1.21.0 to 1.22.0 in /docs_rtd ([#7509](https://github.com/great-expectations/great_expectations/pull/7509))
* [MAINTENANCE] Revert PR 7490 ([#7515](https://github.com/great-expectations/great_expectations/pull/7515))
* [MAINTENANCE] Use YAMLHandler in tests and docs ([#7507](https://github.com/great-expectations/great_expectations/pull/7507))
* [MAINTENANCE] Dedicated airflow 2.2.0 async test ([#7518](https://github.com/great-expectations/great_expectations/pull/7518))
* [MAINTENANCE] Remove airflow2 min depdency test. ([#7524](https://github.com/great-expectations/great_expectations/pull/7524))
* [CONTRIB] - Add new column expectation not be null and empty ([#7449](https://github.com/great-expectations/great_expectations/pull/7449)) (thanks @tmilitino)

0.16.3
-----------------
* [BUGFIX] Fix LegacyRow import. ([#7446](https://github.com/great-expectations/great_expectations/pull/7446))

0.16.2
-----------------
* [FEATURE] Develop PandasDBFSDatasource (as part of Fluent Datasources) ([#7372](https://github.com/great-expectations/great_expectations/pull/7372))
* [FEATURE] Make SQL datasources add asset methods public. ([#7387](https://github.com/great-expectations/great_expectations/pull/7387))
* [FEATURE] Develop SparkDBFSDatasource (as part of Fluent Datasources) ([#7380](https://github.com/great-expectations/great_expectations/pull/7380))
* [FEATURE] add optional `id` to Fluent Datasources and DataAsset schemas ([#7334](https://github.com/great-expectations/great_expectations/pull/7334))
* [FEATURE] Fluent SQLDatasource accepts arbitrary `kwargs` ([#7394](https://github.com/great-expectations/great_expectations/pull/7394))
* [FEATURE] Fluent `SQLDatasource` `create_temp_table` ([#7407](https://github.com/great-expectations/great_expectations/pull/7407))
* [FEATURE] F/great 1463/add updates with datasource obj ([#7401](https://github.com/great-expectations/great_expectations/pull/7401))
* [FEATURE] Fluent SparkDataframeDatasource with DataframeDataAsset ([#7425](https://github.com/great-expectations/great_expectations/pull/7425))
* [BUGFIX] Add FluentBatchRequest early exit to convert_to_json_serializable ([#7381](https://github.com/great-expectations/great_expectations/pull/7381))
* [BUGFIX] Handle non-string fluent batch request options in convert_to_json_serializable ([#7386](https://github.com/great-expectations/great_expectations/pull/7386))
* [BUGFIX] Fix bug with case sensitive execution env ([#7393](https://github.com/great-expectations/great_expectations/pull/7393))
* [BUGFIX] Fixing typographical errors and argument omissions ([#7398](https://github.com/great-expectations/great_expectations/pull/7398))
* [BUGFIX] Remove Query ID from exception for query.template_values metric ([#7373](https://github.com/great-expectations/great_expectations/pull/7373)) (thanks @itaise)
* [BUGFIX] Fluent `PandasFilesytemDatasources` data_connector fixes ([#7414](https://github.com/great-expectations/great_expectations/pull/7414))
* [DOCS] Add back GX logo to README ([#7391](https://github.com/great-expectations/great_expectations/pull/7391))
* [DOCS] DOC-473: Adds shared components for fluent and state management updates ([#7404](https://github.com/great-expectations/great_expectations/pull/7404))
* [DOCS] DOC-473 Adds guide "How to set up GX to work with SQL databases" ([#7409](https://github.com/great-expectations/great_expectations/pull/7409))
* [DOCS] DOC-473 Adds guide "How to set up GX to work with data on GCS" ([#7408](https://github.com/great-expectations/great_expectations/pull/7408))
* [DOCS] Pending doc updates for Data Context state management and fluent Datasource configuration ([#7301](https://github.com/great-expectations/great_expectations/pull/7301))
* [DOCS] Put data_context.md code examples under test ([#7417](https://github.com/great-expectations/great_expectations/pull/7417))
* [MAINTENANCE] Make sure sqlalchemy 2.0 warnings are emitted when running pipelines ([#7379](https://github.com/great-expectations/great_expectations/pull/7379))
* [MAINTENANCE] Make sure all existing warnings are ignored in full CI pipeline ([#7389](https://github.com/great-expectations/great_expectations/pull/7389))
* [MAINTENANCE] Add PR title checker GitHub Action ([#7365](https://github.com/great-expectations/great_expectations/pull/7365))
* [MAINTENANCE] Re-enable warnings as errors ([#7383](https://github.com/great-expectations/great_expectations/pull/7383))
* [MAINTENANCE] Test against minimum SQLAlchemy versions ([#7396](https://github.com/great-expectations/great_expectations/pull/7396))
* [MAINTENANCE] : split up map_metric_provider.py ([#7402](https://github.com/great-expectations/great_expectations/pull/7402))
* [MAINTENANCE] Consolidate Cloud tutorials ([#7395](https://github.com/great-expectations/great_expectations/pull/7395))
* [MAINTENANCE] Change for `connection.execute()` for SQLAlchemy 2 compatibility ([#7384](https://github.com/great-expectations/great_expectations/pull/7384))
* [MAINTENANCE] Bump SQLAlchemy lower bound to 1.4.0 ([#7413](https://github.com/great-expectations/great_expectations/pull/7413))
* [MAINTENANCE] Validate `ExpectationConfiguration` before adding to suite ([#7366](https://github.com/great-expectations/great_expectations/pull/7366))
* [MAINTENANCE] Convert to python built in warning categories ([#7415](https://github.com/great-expectations/great_expectations/pull/7415))
* [MAINTENANCE] Move NotImported to optional_imports.py and start using it. ([#7421](https://github.com/great-expectations/great_expectations/pull/7421))
* [MAINTENANCE] Bump minimist from 1.2.5 to 1.2.8 in /docs/docusaurus ([#7419](https://github.com/great-expectations/great_expectations/pull/7419))
* [MAINTENANCE] PandasFilesystemDatasource stubs and Schema corrections ([#7428](https://github.com/great-expectations/great_expectations/pull/7428))
* [MAINTENANCE] Bump loader-utils from 2.0.2 to 2.0.4 in /docs/docusaurus ([#7429](https://github.com/great-expectations/great_expectations/pull/7429))
* [MAINTENANCE] Bump webpack from 5.74.0 to 5.76.3 in /docs/docusaurus ([#7430](https://github.com/great-expectations/great_expectations/pull/7430))
* [MAINTENANCE] Fix some failing tests when running pytest with no args locally ([#7426](https://github.com/great-expectations/great_expectations/pull/7426))
* [MAINTENANCE] only provide `py.typed` files for fully typed sub-packages ([#7438](https://github.com/great-expectations/great_expectations/pull/7438))
* [MAINTENANCE] Some fluent datasource methods should be private ([#7437](https://github.com/great-expectations/great_expectations/pull/7437))
* [CONTRIB] Adding support for date for the row condition parser ([#7359](https://github.com/great-expectations/great_expectations/pull/7359)) (thanks @maayaniti)
* [CONTRIB] Limit results for two expectations ([#7403](https://github.com/great-expectations/great_expectations/pull/7403)) (thanks @itaise)
* [CONTRIB] [MAINTENANCE] Custom query expectation and editing query.template_values metric ([#7390](https://github.com/great-expectations/great_expectations/pull/7390)) (thanks @mantasmy)

0.16.1
-----------------
* [FEATURE] Fluent CRUD operation stubs ([#7347](https://github.com/great-expectations/great_expectations/pull/7347))
* [FEATURE] Implement DataBricks (DBFS) DataConnector for Fluent Datasources needs ([#7355](https://github.com/great-expectations/great_expectations/pull/7355))
* [BUGFIX] BigQuery performance uses updated `add_or_update_expectation_suite()` method ([#7325](https://github.com/great-expectations/great_expectations/pull/7325))
* [BUGFIX] Ensure Correct JSON and Dictionary Dump Output of Serialized Fluent Objects ([#7336](https://github.com/great-expectations/great_expectations/pull/7336))
* [BUGFIX] Fluent Datasources - empty "assets" key on serialization ([#7341](https://github.com/great-expectations/great_expectations/pull/7341))
* [BUGFIX] Use Path().glob Instead of Path(). Issue #7239 ([#7327](https://github.com/great-expectations/great_expectations/pull/7327)) (thanks @richardohara)
* [BUGFIX] Patch misc errors in advance of v0.16.1 release ([#7371](https://github.com/great-expectations/great_expectations/pull/7371))
* [BUGFIX] `#ephemeral_data_asset` broken data docs links ([#7367](https://github.com/great-expectations/great_expectations/pull/7367))
* [BUGFIX] Fluent `batch_request_options` ignore `None` values ([#7368](https://github.com/great-expectations/great_expectations/pull/7368))
* [BUGFIX] Add FluentBatchRequest early exit to convert_to_json_serializable ([#7381](https://github.com/great-expectations/great_expectations/pull/7381))
* [DOCS] Adding ADR ([#7314](https://github.com/great-expectations/great_expectations/pull/7314))
* [DOCS] Add Cloud onboarding tutorial ([#7333](https://github.com/great-expectations/great_expectations/pull/7333))
* [DOCS] Fix onboarding cloud tutorial ([#7348](https://github.com/great-expectations/great_expectations/pull/7348))
* [DOCS] SQL Alchemy 2 Warnigns ([#7292](https://github.com/great-expectations/great_expectations/pull/7292))
* [DOCS] Update Cloud Getting Started Guide ([#7364](https://github.com/great-expectations/great_expectations/pull/7364))
* [MAINTENANCE] In Fluent Datasources: Configuration Serialization Methods Do Not Need to be Public ([#7332](https://github.com/great-expectations/great_expectations/pull/7332))
* [MAINTENANCE] Add crud methods to context.sources ([#7328](https://github.com/great-expectations/great_expectations/pull/7328))
* [MAINTENANCE] Split out mysql and multi db docs integration tests into a separate job ([#7331](https://github.com/great-expectations/great_expectations/pull/7331))
* [MAINTENANCE] [MAINTENANCE ] Include all `.pyi` files in package data ([#7340](https://github.com/great-expectations/great_expectations/pull/7340))
* [MAINTENANCE] Separate docs_integrations tests by backend ([#7342](https://github.com/great-expectations/great_expectations/pull/7342))
* [MAINTENANCE] Parallelize integration tests - move test definitions ([#7345](https://github.com/great-expectations/great_expectations/pull/7345))
* [MAINTENANCE] Update test around unneeded deprecation warning threshold ([#7351](https://github.com/great-expectations/great_expectations/pull/7351))
* [MAINTENANCE] Remove deprecated code from `Validator` ([#7353](https://github.com/great-expectations/great_expectations/pull/7353))
* [MAINTENANCE] ruff 0.0.255 ([#7349](https://github.com/great-expectations/great_expectations/pull/7349))
* [MAINTENANCE] add sqla deps to type-checking CI step ([#7350](https://github.com/great-expectations/great_expectations/pull/7350))
* [MAINTENANCE] Remove deprecated code around `generator_asset` ([#7356](https://github.com/great-expectations/great_expectations/pull/7356))
* [MAINTENANCE] Revert accidental changes pushed to `develop` ([#7363](https://github.com/great-expectations/great_expectations/pull/7363))
* [MAINTENANCE] D/sql alchemy 2 warnings ([#7362](https://github.com/great-expectations/great_expectations/pull/7362))
* [MAINTENANCE] Warnings are errors + Suppress warnings in preparation for supporting SQLAlchemy 2.x ([#7352](https://github.com/great-expectations/great_expectations/pull/7352))
* [MAINTENANCE] Clean up miscellaneous deprecated code ([#7358](https://github.com/great-expectations/great_expectations/pull/7358))
* [MAINTENANCE] Rename misc internal uses of `ge_cloud_id` ([#7360](https://github.com/great-expectations/great_expectations/pull/7360))
* [MAINTENANCE] Patch deprecation warning in `EVR.__eq__` ([#7374](https://github.com/great-expectations/great_expectations/pull/7374))
* [MAINTENANCE] remove imprecise wording in the new datasource notebook ([#7369](https://github.com/great-expectations/great_expectations/pull/7369))
* [MAINTENANCE] Add additional warning ignores to pyproject.toml ([#7375](https://github.com/great-expectations/great_expectations/pull/7375))
* [MAINTENANCE] Enable `snowflake` V3 Expectations Tests ([#7370](https://github.com/great-expectations/great_expectations/pull/7370))
* [MAINTENANCE] Temporarily disable warnings as errors for v0.16.1 release ([#7382](https://github.com/great-expectations/great_expectations/pull/7382))

0.16.0
-----------------
* [FEATURE] Provide S3 access/operations to new PandasDatasource ([#7197](https://github.com/great-expectations/great_expectations/pull/7197))
* [FEATURE] F/great 1393/add more zep column splitters ([#7203](https://github.com/great-expectations/great_expectations/pull/7203))
* [FEATURE] Fluent datasources have separate asset registries ([#7193](https://github.com/great-expectations/great_expectations/pull/7193))
* [FEATURE] Improve Trino types support ([#6588](https://github.com/great-expectations/great_expectations/pull/6588)) (thanks @ms32035)
* [FEATURE] F/great 1393/add sql multi col splitter ([#7236](https://github.com/great-expectations/great_expectations/pull/7236))
* [FEATURE] `EphemeralDataContext.convert_to_file_context()` ([#7175](https://github.com/great-expectations/great_expectations/pull/7175))
* [FEATURE] New Datasources: Support S3 access for SparkDatasource ([#7232](https://github.com/great-expectations/great_expectations/pull/7232))
* [FEATURE] Implementation of Microsoft Azure Blob Storage DataConnector ([#7246](https://github.com/great-expectations/great_expectations/pull/7246))
* [FEATURE] Implementation of Google Cloud Storage DataConnector ([#7249](https://github.com/great-expectations/great_expectations/pull/7249))
* [FEATURE] Develop PandasGoogleCloudStorageDatasource (as part of New Datasources) ([#7253](https://github.com/great-expectations/great_expectations/pull/7253))
* [FEATURE] Develop PandasAzureBlobStorageDatasource (as part of New Datasources) ([#7254](https://github.com/great-expectations/great_expectations/pull/7254))
* [FEATURE] Develop SparkGoogleCloudStorageDatasource SparkAzureBlobStorageDatasource (as part of New Datasources) ([#7255](https://github.com/great-expectations/great_expectations/pull/7255))
* [FEATURE] Enable creating Checkpoint and SimpleCheckpoint with Validator ([#7275](https://github.com/great-expectations/great_expectations/pull/7275))
* [FEATURE] Editor support for Fluent Datasources dynamic `.add_<DS_TYPE>()` methods ([#7273](https://github.com/great-expectations/great_expectations/pull/7273))
* [FEATURE] M/great 1708/move fluent datasources out of experimental ([#7294](https://github.com/great-expectations/great_expectations/pull/7294))
* [FEATURE] `PandasDatasource` in-memory `DataFrameAsset` ([#7280](https://github.com/great-expectations/great_expectations/pull/7280))
* [FEATURE] Fluent Datasources - `ConfigStr` config substitution support ([#7309](https://github.com/great-expectations/great_expectations/pull/7309))
* [BUGFIX] Ensure that Marshmallow UUIDs are converted to strings before usage ([#7219](https://github.com/great-expectations/great_expectations/pull/7219))
* [BUGFIX] `docs-integration` tests failing after CRUD updates ([#7220](https://github.com/great-expectations/great_expectations/pull/7220))
* [BUGFIX] Adding exception logging to store-related failures ([#7202](https://github.com/great-expectations/great_expectations/pull/7202)) (thanks @ciguaran)
* [BUGFIX] Patch outdated Azure relative paths ([#7247](https://github.com/great-expectations/great_expectations/pull/7247))
* [BUGFIX] `params_with_json_schema` is undefined in `ExpectSelectColumnValuesToBeUniqueWithinRecord._prescriptive_renderer` ([#7261](https://github.com/great-expectations/great_expectations/pull/7261))
* [BUGFIX] Patch Cloud workflow for `add_or_update_datasource` ([#7242](https://github.com/great-expectations/great_expectations/pull/7242))
* [BUGFIX] Stop modifying input batch request when getting a batch list. ([#7269](https://github.com/great-expectations/great_expectations/pull/7269))
* [BUGFIX] Single dynamic pandas model failures don't result in all models failing when used ([#7277](https://github.com/great-expectations/great_expectations/pull/7277))
* [BUGFIX] Fix typographical error in type used in "isinstance()" comparison in BatchManager (was generating "must be formal [...] Batch" warning erroneously) ([#7291](https://github.com/great-expectations/great_expectations/pull/7291))
* [BUGFIX] Correct a typographical error in specific path-forming template name for SparkDatasource-Microsoft Azure Blob Storage combination ([#7302](https://github.com/great-expectations/great_expectations/pull/7302))
* [BUGFIX] Use timezone-aware datetimes in checkpoint run information by default. ([#7244](https://github.com/great-expectations/great_expectations/pull/7244))
* [BUGFIX] `row_conditions` now allow whitespace ([#7313](https://github.com/great-expectations/great_expectations/pull/7313))
* [BUGFIX] Scope `PandasDatasource` reader method types and serialization (1 of 2) ([#7306](https://github.com/great-expectations/great_expectations/pull/7306))
* [BUGFIX] AssertError Duing Great Expectations Installation ([#7285](https://github.com/great-expectations/great_expectations/pull/7285)) (thanks @richardohara)
* [BUGFIX] Provide Error Checking for "expectation_suite_name" in Checkpoint Constructor and Run Methods ([#7320](https://github.com/great-expectations/great_expectations/pull/7320))
* [BUGFIX] Scope `PandasDatasource` reader method types and serialization (2 of 2) ([#7318](https://github.com/great-expectations/great_expectations/pull/7318))
* [BUGFIX] raise error if no identifier provided to get checkpoint/expectation suite ([#7321](https://github.com/great-expectations/great_expectations/pull/7321))
* [BUGFIX] Fluent Datasources: Ensure that Datasource and DataAsset Model Serialization Does Not Include `"name"` Field ([#7323](https://github.com/great-expectations/great_expectations/pull/7323))
* [DOCS] Versioning instructions and fix references for versioning ([#7221](https://github.com/great-expectations/great_expectations/pull/7221))
* [DOCS] Fix links to images in welcome page ([#7222](https://github.com/great-expectations/great_expectations/pull/7222))
* [DOCS] Add API docs build to versioning instructions ([#7230](https://github.com/great-expectations/great_expectations/pull/7230))
* [DOCS] Move readme_assets under docs/ ([#7231](https://github.com/great-expectations/great_expectations/pull/7231))
* [DOCS] Fix hyperlinks in docs ([#7264](https://github.com/great-expectations/great_expectations/pull/7264))
* [DOCS] Scan yaml examples for class names that should be part of the public API ([#7267](https://github.com/great-expectations/great_expectations/pull/7267))
* [DOCS] Update location to run yarn commands ([#7276](https://github.com/great-expectations/great_expectations/pull/7276))
* [DOCS] Fix reference to M1 Mac installation guide ([#7279](https://github.com/great-expectations/great_expectations/pull/7279))
* [DOCS] Remove additional warnings from API docs build. ([#7282](https://github.com/great-expectations/great_expectations/pull/7282))
* [DOCS] Fix blog links in `parse_strings_as_datetimes` warnings ([#7288](https://github.com/great-expectations/great_expectations/pull/7288))
* [DOCS] Fix unsupported chars in API docs ([#7310](https://github.com/great-expectations/great_expectations/pull/7310))
* [DOCS] Add instructions to cli for creating data assets ([#7326](https://github.com/great-expectations/great_expectations/pull/7326))
* [MAINTENANCE] No line number snippets checker ([#7216](https://github.com/great-expectations/great_expectations/pull/7216))
* [MAINTENANCE] Re-enable snippet checker ([#7217](https://github.com/great-expectations/great_expectations/pull/7217))
* [MAINTENANCE] Refactor New SparkDatasource in order to prepare for adding support for Cloud Files Storage environments ([#7223](https://github.com/great-expectations/great_expectations/pull/7223))
* [MAINTENANCE] Repo Cleanup: Move docs related files under docs dir ([#7227](https://github.com/great-expectations/great_expectations/pull/7227))
* [MAINTENANCE] Time series expectations ([#7182](https://github.com/great-expectations/great_expectations/pull/7182))
* [MAINTENANCE] Contrib  time series generators ([#7235](https://github.com/great-expectations/great_expectations/pull/7235))
* [MAINTENANCE] ci & local type-checking parity - pyspark ([#7237](https://github.com/great-expectations/great_expectations/pull/7237))
* [MAINTENANCE] Fix CI dev pipeline - skip orphaned schema check on min pandas version ([#7241](https://github.com/great-expectations/great_expectations/pull/7241))
* [MAINTENANCE] Make a copy of azure pipeline definition files in new locations ([#7233](https://github.com/great-expectations/great_expectations/pull/7233))
* [MAINTENANCE] Complete migration of Azure CI/CD config to `ci` directory ([#7245](https://github.com/great-expectations/great_expectations/pull/7245))
* [MAINTENANCE] ruff v0.0.253 - enable `PYI` rules ([#7243](https://github.com/great-expectations/great_expectations/pull/7243))
* [MAINTENANCE] Optionally allow `None` values in `RenderedAtomicContent` ([#7240](https://github.com/great-expectations/great_expectations/pull/7240))
* [MAINTENANCE] `PandasDatasource` `read_DataAsset` methods return a `Validator` ([#7226](https://github.com/great-expectations/great_expectations/pull/7226))
* [MAINTENANCE] Rename default pandas ephemeral data asset ([#7251](https://github.com/great-expectations/great_expectations/pull/7251))
* [MAINTENANCE] Fix linting errors in `contrib/` ([#7259](https://github.com/great-expectations/great_expectations/pull/7259))
* [MAINTENANCE] Keep repo root consistent ([#7260](https://github.com/great-expectations/great_expectations/pull/7260))
* [MAINTENANCE] Threshold for public API report ([#7262](https://github.com/great-expectations/great_expectations/pull/7262))
* [MAINTENANCE] Update the signature of Fluent datasource factory methods ([#7266](https://github.com/great-expectations/great_expectations/pull/7266))
* [MAINTENANCE] Move some scripts into ci folder ([#7271](https://github.com/great-expectations/great_expectations/pull/7271))
* [MAINTENANCE] `_PandasDataAsset` positional argument support ([#7258](https://github.com/great-expectations/great_expectations/pull/7258))
* [MAINTENANCE] Refactor to utilize common DataConnector instantiation and Connection Test Error Message templates for New FilePath Datasources ([#7268](https://github.com/great-expectations/great_expectations/pull/7268))
* [MAINTENANCE] Merge `PandasDatasource` read method signatures with associated `_PandasDataAsset`s ([#7272](https://github.com/great-expectations/great_expectations/pull/7272))
* [MAINTENANCE] Use ruff linting on scripts folder ([#7270](https://github.com/great-expectations/great_expectations/pull/7270))
* [MAINTENANCE] Fix for docs build warnings ([#7229](https://github.com/great-expectations/great_expectations/pull/7229))
* [MAINTENANCE] Add maybe imports ([#7274](https://github.com/great-expectations/great_expectations/pull/7274))
* [MAINTENANCE] Proper mocking of AbstractDataContext for testing ([#7281](https://github.com/great-expectations/great_expectations/pull/7281))
* [MAINTENANCE] Warn if sqlalchemy version is >= 2.0.0 ([#7283](https://github.com/great-expectations/great_expectations/pull/7283))
* [MAINTENANCE] Remove Prefix "Batch" from "BatchSorter" and "BatchSortersDefinition" (in New Datasources) ([#7284](https://github.com/great-expectations/great_expectations/pull/7284))
* [MAINTENANCE] Call the correct sqlalchemy method to eliminate deprecation warning ([#7293](https://github.com/great-expectations/great_expectations/pull/7293))
* [MAINTENANCE] Fluent Datasources - initial snippet tests ([#7278](https://github.com/great-expectations/great_expectations/pull/7278))
* [MAINTENANCE] add `ruff` `PTH` `use-pathlib` `# noqa` comments ([#7290](https://github.com/great-expectations/great_expectations/pull/7290))
* [MAINTENANCE] Enable SparkDatasource add_asset() methods to accept "header" and "infer_schema" arguments; fix typos in docstrings. ([#7296](https://github.com/great-expectations/great_expectations/pull/7296))
* [MAINTENANCE] enable `ruff` `use-pathlib` `PTH` rules ([#7297](https://github.com/great-expectations/great_expectations/pull/7297))
* [MAINTENANCE] Replace fluent data connector names with a constant ([#7299](https://github.com/great-expectations/great_expectations/pull/7299))
* [MAINTENANCE] Apply ruff path rules for contrib ([#7300](https://github.com/great-expectations/great_expectations/pull/7300))
* [MAINTENANCE] Rename column splitter to splitter. ([#7303](https://github.com/great-expectations/great_expectations/pull/7303))
* [MAINTENANCE] Run airflow operator tests in GX pipeline ([#7298](https://github.com/great-expectations/great_expectations/pull/7298))
* [MAINTENANCE] Add build docs to block PR pipeline ([#7307](https://github.com/great-expectations/great_expectations/pull/7307))
* [MAINTENANCE] Linting for `tests/datasource` ([#7308](https://github.com/great-expectations/great_expectations/pull/7308))
* [MAINTENANCE] Fix test_build_docs stage ([#7311](https://github.com/great-expectations/great_expectations/pull/7311))
* [MAINTENANCE] Elide Duplication of "name" Key from Fluent Datasource and DataAsset Configuration ([#7312](https://github.com/great-expectations/great_expectations/pull/7312))
* [MAINTENANCE] Remove nonexistent pypi ref in README. Add WIP warning in README. ([#7304](https://github.com/great-expectations/great_expectations/pull/7304))
* [MAINTENANCE] Fix a bug in the hourly generator. Add hourly functionality to genera… ([#7305](https://github.com/great-expectations/great_expectations/pull/7305))
* [MAINTENANCE] Update allowed deprecation warning threshold in advance of `0.16.0` ([#7317](https://github.com/great-expectations/great_expectations/pull/7317))
* [MAINTENANCE] Fluent Datasource stubs for dynamic Pandas add_asset methods ([#7315](https://github.com/great-expectations/great_expectations/pull/7315))
* [MAINTENANCE] Stub files for Fluent `PandasDatasource` and `py.typed` ([#7322](https://github.com/great-expectations/great_expectations/pull/7322))
* [MAINTENANCE] `row-condition` also includes tabs in conditional expectation ([#7324](https://github.com/great-expectations/great_expectations/pull/7324))
* [CONTRIB] -add athena credential support ([#7186](https://github.com/great-expectations/great_expectations/pull/7186)) (thanks @tmilitino)
* [CONTRIB] expect_multicolumn_sum_values_to_be_equal_to_single_column ([#7224](https://github.com/great-expectations/great_expectations/pull/7224)) (thanks @swittchawa)
* [CONTRIB] [BUGFIX] Update custom multi-column expectation logic and default kwargs ([#7252](https://github.com/great-expectations/great_expectations/pull/7252)) (thanks @yussaaa)
* [CONTRIB] Feature/expect column values to match thai ([#7238](https://github.com/great-expectations/great_expectations/pull/7238)) (thanks @swittchawa)

0.15.50
-----------------
* [FEATURE] Utilize DataConnector in service of new DataAsset implementations ([#7094](https://github.com/great-expectations/great_expectations/pull/7094))
* [FEATURE] F/great 1393/add initial non datetime sql splitters ([#7183](https://github.com/great-expectations/great_expectations/pull/7183))
* [FEATURE] Experimental `PandasDatasource` with single-batch `_PandasDataAsset`s ([#7173](https://github.com/great-expectations/great_expectations/pull/7173))
* [FEATURE] Experimental filesystem `DataAsset`s `path` in batch request options and batch metadata ([#7129](https://github.com/great-expectations/great_expectations/pull/7129))
* [FEATURE] Default `PandasDatasource` ([#7196](https://github.com/great-expectations/great_expectations/pull/7196))
* [BUGFIX] : Allow CLI to work with `RuntimeDataConnector` ([#7187](https://github.com/great-expectations/great_expectations/pull/7187)) (thanks @luke321321)
* [BUGFIX] Patch GX Cloud `validator.save_expectation_suite()` workflow ([#7189](https://github.com/great-expectations/great_expectations/pull/7189))
* [BUGFIX] Dynamic pandas asset model field substitution ([#7212](https://github.com/great-expectations/great_expectations/pull/7212))
* [DOCS] Use named snippets part 5 ([#7181](https://github.com/great-expectations/great_expectations/pull/7181))
* [DOCS] Use named snippets part 4 ([#7176](https://github.com/great-expectations/great_expectations/pull/7176))
* [DOCS] Use named snippets part 6 ([#7171](https://github.com/great-expectations/great_expectations/pull/7171))
* [DOCS] Use named snippets part 7 ([#7192](https://github.com/great-expectations/great_expectations/pull/7192))
* [DOCS] Use named snippets part 9 ([#7195](https://github.com/great-expectations/great_expectations/pull/7195))
* [DOCS] Use named snippets part 11 ([#7201](https://github.com/great-expectations/great_expectations/pull/7201))
* [DOCS] Use named snippets part 8 ([#7194](https://github.com/great-expectations/great_expectations/pull/7194))
* [DOCS] Use named snippets part 10 ([#7199](https://github.com/great-expectations/great_expectations/pull/7199))
* [DOCS] Fix broken link in anonymous_usage_statistics.md ([#7211](https://github.com/great-expectations/great_expectations/pull/7211)) (thanks @Erin-GX)
* [DOCS] Use named snippets part 12 ([#7214](https://github.com/great-expectations/great_expectations/pull/7214))
* [MAINTENANCE] Update changelog when updated release 0.15.49 ([#7179](https://github.com/great-expectations/great_expectations/pull/7179))
* [MAINTENANCE] Raise store config `ClassInstantiationError` from original `DataContextError` ([#7174](https://github.com/great-expectations/great_expectations/pull/7174))
* [MAINTENANCE] New Datasources: Delineate "SparkFilesystemDatasource" (instead of "SparkDatasource") -- to be congruent with "PandasFilesystemDatasource" ([#7178](https://github.com/great-expectations/great_expectations/pull/7178))
* [MAINTENANCE] Small Refactor to Enable PandasDatsource for multiple Storage Environments ([#7190](https://github.com/great-expectations/great_expectations/pull/7190))
* [MAINTENANCE] Replace `regex` with `batching_regex` for fluent filesystem-like datasources ([#7207](https://github.com/great-expectations/great_expectations/pull/7207))
* [MAINTENANCE] Misc `DataContext` state management & API cleanup ([#7215](https://github.com/great-expectations/great_expectations/pull/7215))

0.15.49
-----------------
* [FEATURE] Enable customization of candidate Regular Expression patterns when running OnboardingDataAssistant ([#7104](https://github.com/great-expectations/great_expectations/pull/7104))
* [FEATURE] Enable `gx.get_context()` to work without any inputs ([#7074](https://github.com/great-expectations/great_expectations/pull/7074))
* [FEATURE] Add `datasource` arg to `DataContext` `Datasource` CRUD ([#7070](https://github.com/great-expectations/great_expectations/pull/7070))
* [FEATURE] Update zep to use sqlalchemy_data_splitter.py ([#7151](https://github.com/great-expectations/great_expectations/pull/7151))
* [FEATURE] ZEP - Dynamically define `add_<ASSET_TYPE>_asset()` methods if needed ([#7121](https://github.com/great-expectations/great_expectations/pull/7121))
* [FEATURE] add expectation_column_values_to_be_continuous ([#5861](https://github.com/great-expectations/great_expectations/pull/5861)) (thanks @jmoskovc)
* [BUGFIX] Rename experimental `get_batch_request` to `build_batch_request` ([#7107](https://github.com/great-expectations/great_expectations/pull/7107))
* [BUGFIX] Remove version from versions.json ([#7109](https://github.com/great-expectations/great_expectations/pull/7109))
* [BUGFIX] Properly Enable/Disable Spark Integration Tests Depending on pyspark Installation for New Datasources ([#7132](https://github.com/great-expectations/great_expectations/pull/7132))
* [BUGFIX] Copy previous versions after checking out the the current commit ([#7142](https://github.com/great-expectations/great_expectations/pull/7142))
* [BUGFIX] `TupleAzureBlobStoreBackend` no longer gives warning when obfuscating connection string ([#7139](https://github.com/great-expectations/great_expectations/pull/7139))
* [BUGFIX] Patch inconsistent ordering within GCP test asserts ([#7130](https://github.com/great-expectations/great_expectations/pull/7130))
* [BUGFIX] Parse pandas version correctly for development builds ([#7147](https://github.com/great-expectations/great_expectations/pull/7147)) (thanks @jtilly)
* [BUGFIX] Patch broken rendered content Cloud tests ([#7155](https://github.com/great-expectations/great_expectations/pull/7155))
* [BUGFIX] pydantic>=1.10.4 - ImportError: cannot import name dataclass_transform ([#7163](https://github.com/great-expectations/great_expectations/pull/7163))
* [BUGFIX] ID/PK Spark and Sql fall back when `unexpected_index_column_names` have not been defined ([#7150](https://github.com/great-expectations/great_expectations/pull/7150))
* [BUGFIX] Patch broken Cloud test blocking 0.15.49 release ([#7177](https://github.com/great-expectations/great_expectations/pull/7177))
* [DOCS] Add CRUD API matrix to `AbstractDataContext` docstring ([#7079](https://github.com/great-expectations/great_expectations/pull/7079))
* [DOCS] Build API docs using latest released version ([#7067](https://github.com/great-expectations/great_expectations/pull/7067))
* [DOCS] Add displayHTML method to view Data Docs ([#7125](https://github.com/great-expectations/great_expectations/pull/7125)) (thanks @swittchawa)
* [DOCS] Use named snippets part 1 ([#7131](https://github.com/great-expectations/great_expectations/pull/7131))
* [DOCS] : fix capitalization of Slack ([#7136](https://github.com/great-expectations/great_expectations/pull/7136)) (thanks @JoelGritter)
* [DOCS] Remove sitemap.xml ([#7141](https://github.com/great-expectations/great_expectations/pull/7141))
* [DOCS] doc-464 consolidating and standardizing snippets ([#7154](https://github.com/great-expectations/great_expectations/pull/7154))
* [DOCS] Use named snippets part 2 ([#7143](https://github.com/great-expectations/great_expectations/pull/7143))
* [DOCS] Use named snippets part 3 ([#7169](https://github.com/great-expectations/great_expectations/pull/7169)) (thanks @jmoskovc)
* [MAINTENANCE] Remove Extra Character from ID/PK Example README ([#7098](https://github.com/great-expectations/great_expectations/pull/7098))
* [MAINTENANCE] Rename experimental `get_batch_request` to `build_batch_request` ([#7095](https://github.com/great-expectations/great_expectations/pull/7095))
* [MAINTENANCE] Fix incorrect label on "How to configure a SQL Datasource" docs page ([#7106](https://github.com/great-expectations/great_expectations/pull/7106))
* [MAINTENANCE] Update dependency on pydantic ([#7111](https://github.com/great-expectations/great_expectations/pull/7111))
* [MAINTENANCE] Move experimental `base_directory` from `_FilesystemDataAsset` to `PandasDatasource` and `SparkDatasource` ([#7078](https://github.com/great-expectations/great_expectations/pull/7078))
* [MAINTENANCE] Use secret to store algolia api key ([#7115](https://github.com/great-expectations/great_expectations/pull/7115))
* [MAINTENANCE] Fluent Datasources - don't register "private" Datasource classes ([#7124](https://github.com/great-expectations/great_expectations/pull/7124))
* [MAINTENANCE] ZEP - Realign pandas asset args for `Datasource` level `base_directory` ([#7123](https://github.com/great-expectations/great_expectations/pull/7123))
* [MAINTENANCE] format notebooks with `black` ([#7054](https://github.com/great-expectations/great_expectations/pull/7054))
* [MAINTENANCE] mypy `v1.0.0` ([#7138](https://github.com/great-expectations/great_expectations/pull/7138))
* [MAINTENANCE] Output Consistent Data Format from "table.head" Metric for every ExecutionEngine ([#7134](https://github.com/great-expectations/great_expectations/pull/7134))
* [MAINTENANCE] ruff 0.0.246 update ([#7137](https://github.com/great-expectations/great_expectations/pull/7137))
* [MAINTENANCE] Refactor sql splitter to take selectable instead of str. ([#7133](https://github.com/great-expectations/great_expectations/pull/7133))
* [MAINTENANCE] Update V3 DataConnector utilities to support New Datasources (ZEP) ([#7144](https://github.com/great-expectations/great_expectations/pull/7144))
* [MAINTENANCE] Change all instances of `create_expectation_suite` to `add_expectation_suite` in tests, docs, and source code ([#7117](https://github.com/great-expectations/great_expectations/pull/7117))
* [MAINTENANCE] Clean up pathlib.Path() usage in DataConnector utilities and restore tighter formatting in great_expectations/util.py ([#7149](https://github.com/great-expectations/great_expectations/pull/7149))
* [MAINTENANCE] Clean up `mypy` violations in `CardinalityChecker` ([#7146](https://github.com/great-expectations/great_expectations/pull/7146))
* [MAINTENANCE] Remove unused dockerfile ([#7152](https://github.com/great-expectations/great_expectations/pull/7152))
* [MAINTENANCE] Delete cli v012 tests. ([#7159](https://github.com/great-expectations/great_expectations/pull/7159))
* [MAINTENANCE] ZEP - update asset factories method signatures from asset models ([#7096](https://github.com/great-expectations/great_expectations/pull/7096))
* [MAINTENANCE] Bump minimum version of `pytest` ([#7164](https://github.com/great-expectations/great_expectations/pull/7164))
* [MAINTENANCE] Clean up additional deprecation warnings from outdated CRUD API ([#7156](https://github.com/great-expectations/great_expectations/pull/7156))
* [MAINTENANCE] Experimental `PandasDatasource`, single-batch `_PandasDataAsset`s, related schemas ([#7158](https://github.com/great-expectations/great_expectations/pull/7158))
* [MAINTENANCE] Removing path for `--v2-api upgrade` and informative message ([#7170](https://github.com/great-expectations/great_expectations/pull/7170))
* [CONTRIB] Add experimental expectation to check column values after split ([#7120](https://github.com/great-expectations/great_expectations/pull/7120)) (thanks @ace-racer)
* [CONTRIB] added new Expectations  - India_zip_code expectation and not_to_be_future_date expectation ([#6086](https://github.com/great-expectations/great_expectations/pull/6086)) (thanks @prachijain136)
* [CONTRIB] Update the rendered text for min and max values to be clearer. ([#7166](https://github.com/great-expectations/great_expectations/pull/7166))

0.15.48
-----------------
* [FEATURE] Place FilesystemDataAsset into separate module (its functionality is used by both PandasDatasource and SparkDatasource) ([#7025](https://github.com/great-expectations/great_expectations/pull/7025))
* [FEATURE] Add SQL query data asset for new experimental datasources ([#6999](https://github.com/great-expectations/great_expectations/pull/6999))
* [FEATURE] Experimental `DataAsset` `test_connection` ([#7019](https://github.com/great-expectations/great_expectations/pull/7019))
* [FEATURE] ZEP - generate pandas assets ([#7044](https://github.com/great-expectations/great_expectations/pull/7044))
* [FEATURE] Experimental Splitter connection testing ([#7051](https://github.com/great-expectations/great_expectations/pull/7051))
* [FEATURE] ID/PK `ColumnPairExpectations` and `MultiColumnMapExpectations` - Spark ([#7001](https://github.com/great-expectations/great_expectations/pull/7001))
* [FEATURE] Add `expectation_suite` arg to `DataContext` `ExpectationSuite` CRUD ([#7059](https://github.com/great-expectations/great_expectations/pull/7059))
* [FEATURE] ID/PK ColumnPairExpectations and MultiColumnMapExpectations - SQL ([#7046](https://github.com/great-expectations/great_expectations/pull/7046))
* [FEATURE] Introducing General-Purpose Wrapper for Regular Expressions Parsing and incorporating it in "_FilesystemDataAsset" ([#7062](https://github.com/great-expectations/great_expectations/pull/7062))
* [FEATURE] Add `checkpoint` arg to `DataContext` `Checkpoint` CRUD ([#7066](https://github.com/great-expectations/great_expectations/pull/7066))
* [FEATURE] Add `profiler` arg to `DataContext` `Profiler` CRUD ([#7060](https://github.com/great-expectations/great_expectations/pull/7060))
* [FEATURE] Add API action ([#6902](https://github.com/great-expectations/great_expectations/pull/6902)) (thanks @itaise)
* [BUGFIX] ID/PK - Rendering `ColumnPair` and `MultiColumn` Expectations in DataDocs ([#7041](https://github.com/great-expectations/great_expectations/pull/7041))
* [BUGFIX] `ColumnPairExpectation` tests need to consider 2 possible GroupBy results ([#7045](https://github.com/great-expectations/great_expectations/pull/7045))
* [BUGFIX] zep - always serialize type field ([#7056](https://github.com/great-expectations/great_expectations/pull/7056))
* [BUGFIX] ZEP - html asset generation on pandas `1.1` ([#7068](https://github.com/great-expectations/great_expectations/pull/7068))
* [BUGFIX] fix ZEP pandas min tests ([#7084](https://github.com/great-expectations/great_expectations/pull/7084))
* [BUGFIX] Skip all ZEP pandas datasource tests for min pandas ([#7091](https://github.com/great-expectations/great_expectations/pull/7091))
* [DOCS] Add new `DataContext` CRUD to public API ([#7058](https://github.com/great-expectations/great_expectations/pull/7058))
* [DOCS] DOC-461 remove unlinked link ([#7083](https://github.com/great-expectations/great_expectations/pull/7083))
* [DOCS] Adding algolia click events ([#7085](https://github.com/great-expectations/great_expectations/pull/7085))
* [DOCS] Versioning for documentation ([#7033](https://github.com/great-expectations/great_expectations/pull/7033))
* [MAINTENANCE] linting for `/contrib` ([#7005](https://github.com/great-expectations/great_expectations/pull/7005))
* [MAINTENANCE] Deprecate old `DataContext` CRUD methods ([#7031](https://github.com/great-expectations/great_expectations/pull/7031))
* [MAINTENANCE] Simplify logic for `add_or_update` ([#7035](https://github.com/great-expectations/great_expectations/pull/7035))
* [MAINTENANCE] ZEP - test type-checking ([#7028](https://github.com/great-expectations/great_expectations/pull/7028))
* [MAINTENANCE] ZEP put schemas under source control ([#6988](https://github.com/great-expectations/great_expectations/pull/6988))
* [MAINTENANCE] Add `id` as a param to any CRUD methods with `ge_cloud_id` ([#7036](https://github.com/great-expectations/great_expectations/pull/7036))
* [MAINTENANCE] Minor Cleanup ([#7047](https://github.com/great-expectations/great_expectations/pull/7047))
* [MAINTENANCE] replace `isort` with `ruff` sorting rules ([#6907](https://github.com/great-expectations/great_expectations/pull/6907))
* [MAINTENANCE] Standardize `Checkpoint` CRUD ([#6962](https://github.com/great-expectations/great_expectations/pull/6962))
* [MAINTENANCE] ruff `0.0.241` ([#7048](https://github.com/great-expectations/great_expectations/pull/7048))
* [MAINTENANCE] finish linting `great_expectations` ([#7050](https://github.com/great-expectations/great_expectations/pull/7050))
* [MAINTENANCE] fix - `FutureWarning: pandas.Float64Index is deprecated` when importing `great_expectations` ([#7055](https://github.com/great-expectations/great_expectations/pull/7055))
* [MAINTENANCE] Move path mapping out of ExecutionEngine into DataConnector ([#7065](https://github.com/great-expectations/great_expectations/pull/7065))
* [MAINTENANCE] Add ruff TCH001 noqa annotations ([#7072](https://github.com/great-expectations/great_expectations/pull/7072))
* [MAINTENANCE] Enable ruff `TCH` rules ([#7073](https://github.com/great-expectations/great_expectations/pull/7073))
* [MAINTENANCE] Cache dependency installation during build of `Dockerfile.tests` ([#7071](https://github.com/great-expectations/great_expectations/pull/7071))
* [MAINTENANCE] Fix most typing errors in `DataAssistantResult` ([#7010](https://github.com/great-expectations/great_expectations/pull/7010))
* [MAINTENANCE] add `ge_dev` + `gx_dev` to `.gitignore` ([#6860](https://github.com/great-expectations/great_expectations/pull/6860))
* [MAINTENANCE] Refactor Filesystem DataAsset into FilePath DataAsset and Filesystem DataAsset (later inherits former) ([#7075](https://github.com/great-expectations/great_expectations/pull/7075))
* [MAINTENANCE] Refactor `Store` and `StoreBackend` to leverage new CRUD methods ([#7081](https://github.com/great-expectations/great_expectations/pull/7081))
* [MAINTENANCE] Delete `gx_venv` from project root ([#7080](https://github.com/great-expectations/great_expectations/pull/7080))
* [MAINTENANCE] correct typo in data assistants portion of the getting started tutorial ([#7088](https://github.com/great-expectations/great_expectations/pull/7088))
* [MAINTENANCE] ID/PK - CompoundColumnsUnique is filtered only for SQL ([#7087](https://github.com/great-expectations/great_expectations/pull/7087))
* [MAINTENANCE] Minor clean up to make `DataConnector` method names less confusing. ([#7089](https://github.com/great-expectations/great_expectations/pull/7089))
* [MAINTENANCE] Refactor DataConnector Path Format Utilities For Better Encapsulation ([#7092](https://github.com/great-expectations/great_expectations/pull/7092))
* [MAINTENANCE] Temporarily xfail ID/PK tests due to Pandas min version conflicts ([#7097](https://github.com/great-expectations/great_expectations/pull/7097))
* [MAINTENANCE] Remove Extra Character from ID/PK Example README ([#7098](https://github.com/great-expectations/great_expectations/pull/7098))
* [CONTRIB] Row condition parser sqlalchemy: adding support for != operator & adding support all operators for string ([#7053](https://github.com/great-expectations/great_expectations/pull/7053)) (thanks @maayaniti)

0.15.47
-----------------
* [FEATURE] ZEP - dynamic pandas asset schema definitions ([#6780](https://github.com/great-expectations/great_expectations/pull/6780))
* [FEATURE] ID/PK `ColumnPairExpectations` and `MultiColumnMapExpectations` - Pandas ([#6941](https://github.com/great-expectations/great_expectations/pull/6941))
* [FEATURE] Experimental `Datasource` and `DataAsset` connection testing ([#6844](https://github.com/great-expectations/great_expectations/pull/6844))
* [FEATURE] Implement Experimental SparkDatasource with CSVDataAsset ([#6981](https://github.com/great-expectations/great_expectations/pull/6981))
* [FEATURE] Place FilesystemDataAsset into separate module (its functionality is used by both PandasDatasource and SparkDatasource) ([#7025](https://github.com/great-expectations/great_expectations/pull/7025))
* [BUGFIX] Snowflake/Oracle/DB2 <--> SQLAlchemy table and column names case insensitivity representation ([#6951](https://github.com/great-expectations/great_expectations/pull/6951))
* [BUGFIX] try except import of pandas types ([#6983](https://github.com/great-expectations/great_expectations/pull/6983))
* [BUGFIX] fix jsonschema - altair conflict ([#6984](https://github.com/great-expectations/great_expectations/pull/6984))
* [BUGFIX] Temporarily disable items with issues rendering ([#6997](https://github.com/great-expectations/great_expectations/pull/6997))
* [BUGFIX] Fix Renderer Configuration for expectation expect_column_values_to_not_be_in_set #6963 ([#6990](https://github.com/great-expectations/great_expectations/pull/6990)) (thanks @jmcorreia)
* [BUGFIX] Patch logic error in new `add_or_update` methods ([#7021](https://github.com/great-expectations/great_expectations/pull/7021))
* [BUGFIX] Pandas ID/PK - bugfix for column name and update tests ([#7015](https://github.com/great-expectations/great_expectations/pull/7015))
* [DOCS] Regex-Based, Set-Based, Query-Based, & Actions Docstrings ([#6863](https://github.com/great-expectations/great_expectations/pull/6863))
* [DOCS] Documentation for classes and methods within ExecutionEngine class hierarchy ([#6936](https://github.com/great-expectations/great_expectations/pull/6936))
* [DOCS] Enable use of code blocks in Returns: section ([#6946](https://github.com/great-expectations/great_expectations/pull/6946))
* [DOCS] Add missing data connectors and data contexts ([#6945](https://github.com/great-expectations/great_expectations/pull/6945))
* [DOCS] DOC-280: How to use GX with AWS S3 and Spark ([#6782](https://github.com/great-expectations/great_expectations/pull/6782))
* [DOCS] Adding docstrings per the list ([#6931](https://github.com/great-expectations/great_expectations/pull/6931))
* [DOCS] Docstrings for `DataContext` child classes and `DataAssistantResult.to_json_dict` ([#6956](https://github.com/great-expectations/great_expectations/pull/6956))
* [DOCS] batch docstring ([#6939](https://github.com/great-expectations/great_expectations/pull/6939))
* [DOCS] BatchDefinition ([#6940](https://github.com/great-expectations/great_expectations/pull/6940))
* [DOCS] Add metric provider to public api report ([#6958](https://github.com/great-expectations/great_expectations/pull/6958))
* [DOCS] BatchRequest ([#6943](https://github.com/great-expectations/great_expectations/pull/6943))
* [DOCS] head ([#6944](https://github.com/great-expectations/great_expectations/pull/6944))
* [DOCS] Add public_api. Docstring is fine already ([#6955](https://github.com/great-expectations/great_expectations/pull/6955))
* [DOCS] Add public API docstring for `RuleBasedProfiler` ([#6947](https://github.com/great-expectations/great_expectations/pull/6947))
* [DOCS] Adding docstrings for metric providers ([#6960](https://github.com/great-expectations/great_expectations/pull/6960))
* [DOCS] Add docstrings for several data connectors ([#6949](https://github.com/great-expectations/great_expectations/pull/6949))
* [DOCS] Adds docstring to class configured data connector classes ([#6961](https://github.com/great-expectations/great_expectations/pull/6961))
* [DOCS] Add public API docstring for `validate_configuration` on `expect_column_value_z_scores_to_be_less_than` and `expect_column_values_to_match_json_schema` ([#6873](https://github.com/great-expectations/great_expectations/pull/6873))
* [DOCS] Expectations Class DocStrings ([#6950](https://github.com/great-expectations/great_expectations/pull/6950))
* [DOCS] D/dx 237/tal docstrings ([#6959](https://github.com/great-expectations/great_expectations/pull/6959))
* [DOCS] Add delete_checkpoint to public API ([#6965](https://github.com/great-expectations/great_expectations/pull/6965))
* [DOCS] Use markdown style code blocks ([#6970](https://github.com/great-expectations/great_expectations/pull/6970))
* [DOCS] DataContext and CheckpointConfig DocString ([#6911](https://github.com/great-expectations/great_expectations/pull/6911))
* [DOCS] Either Documentation tag style acceptable ([#6974](https://github.com/great-expectations/great_expectations/pull/6974))
* [DOCS] DocStrings for Column, Query, & Table Metric Providers & register_metric ([#6971](https://github.com/great-expectations/great_expectations/pull/6971))
* [DOCS] render utils ([#6975](https://github.com/great-expectations/great_expectations/pull/6975))
* [DOCS] Add public API docstring for `UserConfigurableProfiler` ([#6904](https://github.com/great-expectations/great_expectations/pull/6904))
* [DOCS] Add docstring for `ExpectationValidationResult` ([#6968](https://github.com/great-expectations/great_expectations/pull/6968))
* [DOCS] Add some json serialization docstrings. ([#6880](https://github.com/great-expectations/great_expectations/pull/6880))
* [DOCS] DOC-285 new guide: how to use self initializing expectations ([#5205](https://github.com/great-expectations/great_expectations/pull/5205))
* [DOCS] DOC-286 how to add support for the auto initializing framework to a custom expectation ([#5300](https://github.com/great-expectations/great_expectations/pull/5300))
* [DOCS] ExpectationConfiguration, get_success_kwargs and validate api docs ([#6982](https://github.com/great-expectations/great_expectations/pull/6982))
* [DOCS] rule_based_profiler_result ([#6977](https://github.com/great-expectations/great_expectations/pull/6977))
* [DOCS] metric_value, metric_partial ([#6978](https://github.com/great-expectations/great_expectations/pull/6978))
* [DOCS] Actions, Checkpoint, ExpectationSuiteValidationResult, RunIdentifier related docstrings ([#6986](https://github.com/great-expectations/great_expectations/pull/6986))
* [DOCS] API docs support self referential links ([#6998](https://github.com/great-expectations/great_expectations/pull/6998))
* [DOCS] Add rendering docstrings ([#6992](https://github.com/great-expectations/great_expectations/pull/6992))
* [DOCS] `Expectations` related DocStrings ([#6994](https://github.com/great-expectations/great_expectations/pull/6994))
* [DOCS] MetricConfiguration DocString ([#6996](https://github.com/great-expectations/great_expectations/pull/6996))
* [DOCS] Updates typo in prerequisites section ([#7004](https://github.com/great-expectations/great_expectations/pull/7004)) (thanks @ruankie)
* [DOCS] Update API docs landing page ([#6972](https://github.com/great-expectations/great_expectations/pull/6972))
* [DOCS] Remove BaseDataContext and DataContext from the public API ([#7008](https://github.com/great-expectations/great_expectations/pull/7008))
* [DOCS] Fix setup instructions for email validation ([#7007](https://github.com/great-expectations/great_expectations/pull/7007)) (thanks @ruankie)
* [DOCS] DOC-348 corrects typos in the aws+athena guide intro and congratulations sections ([#6989](https://github.com/great-expectations/great_expectations/pull/6989))
* [DOCS] DOC-420 updates to screenshots ([#7012](https://github.com/great-expectations/great_expectations/pull/7012))
* [DOCS] DOC-416 How to use GX with AWS using Redshift ([#6985](https://github.com/great-expectations/great_expectations/pull/6985))
* [DOCS] Fix metric provider and reorganize sidebar ([#7022](https://github.com/great-expectations/great_expectations/pull/7022))
* [DOCS] Typo - Update api_reference.md ([#7024](https://github.com/great-expectations/great_expectations/pull/7024))
* [DOCS] Nest sidebar by shortest import path ([#7032](https://github.com/great-expectations/great_expectations/pull/7032))
* [MAINTENANCE] Parameterized tests for ID/PK at `ColumnMapExpectation` level ([#6925](https://github.com/great-expectations/great_expectations/pull/6925))
* [MAINTENANCE] `ruff` -> `0.0.236` ([#6948](https://github.com/great-expectations/great_expectations/pull/6948))
* [MAINTENANCE] docstring for expect_column_values_to_not_match_regex_list's validate_configuration ([#6877](https://github.com/great-expectations/great_expectations/pull/6877))
* [MAINTENANCE] Remove handrolled linters/checkers from `scripts/` and CI ([#6964](https://github.com/great-expectations/great_expectations/pull/6964))
* [MAINTENANCE] Remove refs to old scripts from `invoke` calls ([#6967](https://github.com/great-expectations/great_expectations/pull/6967))
* [MAINTENANCE] Fix some linting issues ([#6973](https://github.com/great-expectations/great_expectations/pull/6973))
* [MAINTENANCE] Fix variable name error associated with adding typing and docstrings ([#6980](https://github.com/great-expectations/great_expectations/pull/6980))
* [MAINTENANCE] Add test to ensure that all types in the `DataContext` hierarchy emit expected usage stats ([#6915](https://github.com/great-expectations/great_expectations/pull/6915))
* [MAINTENANCE] Standardize `Datasource` CRUD ([#6892](https://github.com/great-expectations/great_expectations/pull/6892))
* [MAINTENANCE] Typing `histogram_single_batch_parameter_builder` ([#6916](https://github.com/great-expectations/great_expectations/pull/6916))
* [MAINTENANCE] Add `add_expectation_suite` to `DataContext` CRUD ([#6926](https://github.com/great-expectations/great_expectations/pull/6926))
* [MAINTENANCE] ColumnExpectation, render_evaluation_parameter_string and validate method ([#6995](https://github.com/great-expectations/great_expectations/pull/6995))
* [MAINTENANCE] Add `update_expectation_suite` and `add_or_update_expectation_suite` to `DataContext` CRUD ([#6987](https://github.com/great-expectations/great_expectations/pull/6987))
* [MAINTENANCE] Standardize `RuleBasedProfiler` CRUD ([#6991](https://github.com/great-expectations/great_expectations/pull/6991))
* [MAINTENANCE] Make Pandas installation with Python 3.10 less restrictive ([#7013](https://github.com/great-expectations/great_expectations/pull/7013))
* [MAINTENANCE] ZEP - postgres test typing ([#7023](https://github.com/great-expectations/great_expectations/pull/7023))
* [MAINTENANCE] [BUGFIX ] ZEP - pandas serde fix ([#7009](https://github.com/great-expectations/great_expectations/pull/7009))
* [MAINTENANCE] add preview image for twitter and other social preview images ([#7027](https://github.com/great-expectations/great_expectations/pull/7027))
* [MAINTENANCE] Update `update_` methods in `DataContext` to return persisted object ([#7034](https://github.com/great-expectations/great_expectations/pull/7034))
* [MAINTENANCE] ZEP - use parameter that exists on min pandas version ([#7037](https://github.com/great-expectations/great_expectations/pull/7037))
* [MAINTENANCE] xfail ZEP async spark tests for release ([#7038](https://github.com/great-expectations/great_expectations/pull/7038))
* [CONTRIB] expect_multicolumn_values_not_to_be_all_null ([#6912](https://github.com/great-expectations/great_expectations/pull/6912)) (thanks @yussaaa)
* [CONTRIB] Adding support for punctuation in column_value for the row_condition parser ([#7018](https://github.com/great-expectations/great_expectations/pull/7018)) (thanks @maayaniti)

0.15.46
-----------------
* [BUGFIX] Disable `RendererConfiguration` constraint to support legacy renderer fallback behavior ([#6938](https://github.com/great-expectations/great_expectations/pull/6938))
* [DOCS] Remove the `great_expectations` path prefix for API docs ([#6934](https://github.com/great-expectations/great_expectations/pull/6934))
* [DOCS] Updates Custom Expectation docs w/ code snippets ([#6365](https://github.com/great-expectations/great_expectations/pull/6365))
* [DOCS] Regex-Based, Set-Based, Query-Based, & Actions Docstrings ([#6863](https://github.com/great-expectations/great_expectations/pull/6863))
* [DOCS] Documentation for classes and methods within ExecutionEngine class hierarchy ([#6936](https://github.com/great-expectations/great_expectations/pull/6936))

0.15.45
-----------------
* [FEATURE] Experimental datasources `batch.head()` ([#6765](https://github.com/great-expectations/great_expectations/pull/6765))
* [FEATURE] Add Validation Result URL to Checkpoint Result ([#6908](https://github.com/great-expectations/great_expectations/pull/6908))
* [BUGFIX] Fix issues rendering code blocks in API docs ([#6917](https://github.com/great-expectations/great_expectations/pull/6917))
* [BUGFIX] Fix list_keys method for TupleS3StoreBackend ([#6901](https://github.com/great-expectations/great_expectations/pull/6901)) (thanks @enagovitsyn)
* [BUGFIX] Fix rendering issue with api docs ([#6924](https://github.com/great-expectations/great_expectations/pull/6924))
* [BUGFIX] Render bar graph with boolean values ([#6910](https://github.com/great-expectations/great_expectations/pull/6910)) (thanks @tmilitino)
* [BUGFIX] Capital one contrib/micdavis/import hotfix ([#6922](https://github.com/great-expectations/great_expectations/pull/6922)) (thanks @micdavis)
* [DOCS] Adding docstring for `Checkpoint.self_check()` ([#6841](https://github.com/great-expectations/great_expectations/pull/6841))
* [DOCS] `AbstractDataContext.add_store` docstring ([#6851](https://github.com/great-expectations/great_expectations/pull/6851))
* [DOCS] Doc Strings for ExpectationSuite Display Methods ([#6856](https://github.com/great-expectations/great_expectations/pull/6856))
* [DOCS] `DataAssistantResult.get_expectation_suite()` docstring ([#6862](https://github.com/great-expectations/great_expectations/pull/6862))
* [DOCS] Misc docstrings around `DataAssistant` ([#6866](https://github.com/great-expectations/great_expectations/pull/6866))
* [DOCS] enable running `invoke docstrings` on select modules ([#6868](https://github.com/great-expectations/great_expectations/pull/6868))
* [DOCS] Adds docstring for expect_column_distinct_values_to_contain_set ([#6855](https://github.com/great-expectations/great_expectations/pull/6855))
* [DOCS] Documentation Strings for Metric Domain Types and Metric Function Types ([#6872](https://github.com/great-expectations/great_expectations/pull/6872))
* [DOCS] added docstrings for the public API ([#6884](https://github.com/great-expectations/great_expectations/pull/6884)) (thanks @sujensen)
* [DOCS] Add public API docstring for `expect_column_values_to_be_unique` `validate_configuration` ([#6897](https://github.com/great-expectations/great_expectations/pull/6897))
* [DOCS] Miscellaneous docstrings for `DataContext` and utils ([#6852](https://github.com/great-expectations/great_expectations/pull/6852))
* [DOCS] Add public API docstring for `expect_column_values_to_be_of_type` `validate_configuration` ([#6896](https://github.com/great-expectations/great_expectations/pull/6896))
* [DOCS] Add public API docstring for `JsonSchemaProflier.validate` ([#6900](https://github.com/great-expectations/great_expectations/pull/6900))
* [DOCS] Exclude DataAssistantRunner.run() ([#6919](https://github.com/great-expectations/great_expectations/pull/6919))
* [DOCS] StoreValidationResultAction, StoreEvaluationParametersAction and StoreMetricsAction api docs ([#6879](https://github.com/great-expectations/great_expectations/pull/6879))
* [DOCS] Add public API docstring for `expect_column_values_to_be_dateutil_parseable` `validate_configuration` ([#6864](https://github.com/great-expectations/great_expectations/pull/6864))
* [DOCS] YAML docs ([#6861](https://github.com/great-expectations/great_expectations/pull/6861))
* [DOCS] Add public API docstring for `expect_column_values_to_be_decreasing` `validate_configuration` ([#6865](https://github.com/great-expectations/great_expectations/pull/6865))
* [DOCS] Docstrings for `Checkpoint` and related classes ([#6882](https://github.com/great-expectations/great_expectations/pull/6882))
* [DOCS] Add public API docstring for expect_table_row_count_to_be_between validate_configuration ([#6883](https://github.com/great-expectations/great_expectations/pull/6883)) (thanks @lockettks)
* [DOCS] `Validator.get_expectation_suite()` docstring ([#6886](https://github.com/great-expectations/great_expectations/pull/6886))
* [DOCS] Fix Checkpoint docstring whitespace ([#6927](https://github.com/great-expectations/great_expectations/pull/6927))
* [DOCS] `DataAssistantResult` docstring ([#6887](https://github.com/great-expectations/great_expectations/pull/6887))
* [DOCS] Add public API docstring for `expect_column_values_to_be_in_set` `validate_configuration` ([#6890](https://github.com/great-expectations/great_expectations/pull/6890))
* [DOCS] Add public API docstring for `expect_column_values_to_be_in_type_list` and `expect_column_values_to_be_increasing` `validate_configuration` ([#6891](https://github.com/great-expectations/great_expectations/pull/6891))
* [DOCS] Deprecate `util.render_evaluation_parameter_string` function ([#6894](https://github.com/great-expectations/great_expectations/pull/6894))
* [DOCS] Add public API docstring for `Profiler.validate` ([#6898](https://github.com/great-expectations/great_expectations/pull/6898))
* [DOCS] Add public API docstring for `expect_column_values_to_be_between` `validate_configuration` ([#6858](https://github.com/great-expectations/great_expectations/pull/6858))
* [DOCS] Add public API docstring for `expect_column_values_to_be_in_json_parseable` `validate_configuration` ([#6893](https://github.com/great-expectations/great_expectations/pull/6893))
* [DOCS] Add public API docstring for `expect_column_values_to_be_null` `validate_configuration` ([#6895](https://github.com/great-expectations/great_expectations/pull/6895))
* [DOCS] Update docstrings for some of actions.py ([#6853](https://github.com/great-expectations/great_expectations/pull/6853))
* [DOCS] /typo correction ([#6920](https://github.com/great-expectations/great_expectations/pull/6920)) (thanks @mingyyy)
* [DOCS] DOC-417 How to use GX with AWS using Athena ([#6828](https://github.com/great-expectations/great_expectations/pull/6828))
* [DOCS] Adding docstrings ([#6854](https://github.com/great-expectations/great_expectations/pull/6854))
* [MAINTENANCE] Update `teams.yml` ([#6839](https://github.com/great-expectations/great_expectations/pull/6839))
* [MAINTENANCE] invoke 2.0 and `schema` task (for zep types) ([#6836](https://github.com/great-expectations/great_expectations/pull/6836))
* [MAINTENANCE] Build hierarchy in sidebars for API docs ([#6842](https://github.com/great-expectations/great_expectations/pull/6842))
* [MAINTENANCE] Change public_api task name to avoid confusion ([#6843](https://github.com/great-expectations/great_expectations/pull/6843))
* [MAINTENANCE] Add the fragment back to internal references ([#6845](https://github.com/great-expectations/great_expectations/pull/6845))
* [MAINTENANCE] Clean up public_api excludes ([#6846](https://github.com/great-expectations/great_expectations/pull/6846))
* [MAINTENANCE] Fix the error message for invalid batch request options ([#6848](https://github.com/great-expectations/great_expectations/pull/6848))
* [MAINTENANCE] Standardize Store CRUD ([#6826](https://github.com/great-expectations/great_expectations/pull/6826))
* [MAINTENANCE] Fix scripts not found error in invoke ([#6867](https://github.com/great-expectations/great_expectations/pull/6867))
* [MAINTENANCE] Fix argument name typo ([#6850](https://github.com/great-expectations/great_expectations/pull/6850)) (thanks @KirillUlich)
* [MAINTENANCE] more clearly specifies range of supported python versions ([#6870](https://github.com/great-expectations/great_expectations/pull/6870))
* [MAINTENANCE] add validate_configuration docstring ([#6857](https://github.com/great-expectations/great_expectations/pull/6857))
* [MAINTENANCE] docstring for expect_column_values_to_not_be_null#validate_configuration ([#6859](https://github.com/great-expectations/great_expectations/pull/6859))
* [MAINTENANCE] Standardize project config CRUD ([#6837](https://github.com/great-expectations/great_expectations/pull/6837))
* [MAINTENANCE] update docstring in validator.py and checkpoint_result.py ([#6875](https://github.com/great-expectations/great_expectations/pull/6875))
* [MAINTENANCE] updated docstring on validate configuration ([#6871](https://github.com/great-expectations/great_expectations/pull/6871))
* [MAINTENANCE] Exclude unit tests from `comprehensive` stage of `dev` CI ([#6903](https://github.com/great-expectations/great_expectations/pull/6903))
* [MAINTENANCE] Refactor `file_relative_path` util ([#6778](https://github.com/great-expectations/great_expectations/pull/6778))
* [MAINTENANCE] switch to `ruff` linter ([#6888](https://github.com/great-expectations/great_expectations/pull/6888))
* [MAINTENANCE] Use docusaurus style code block in api docs ([#6906](https://github.com/great-expectations/great_expectations/pull/6906))
* [MAINTENANCE] metrics linting ([#6889](https://github.com/great-expectations/great_expectations/pull/6889))
* [MAINTENANCE] Add exception message to `RenderedAtomicContent` failure renderer ([#6795](https://github.com/great-expectations/great_expectations/pull/6795))
* [MAINTENANCE] Remove CloudNotificationAction ([#6881](https://github.com/great-expectations/great_expectations/pull/6881))
* [MAINTENANCE] Use ruff linter for docstring linting ([#6913](https://github.com/great-expectations/great_expectations/pull/6913))
* [MAINTENANCE] Add validate_configuration method docstrings ([#6899](https://github.com/great-expectations/great_expectations/pull/6899))
* [MAINTENANCE] docstring for expect_column_values_to_not_match_like_pattern_list's validate_configuration ([#6874](https://github.com/great-expectations/great_expectations/pull/6874))
* [MAINTENANCE] docstring for expect_column_values_to_not_match_like_pattern validate_configuration ([#6876](https://github.com/great-expectations/great_expectations/pull/6876))
* [MAINTENANCE] docstring for expect_compound_columns_to_be_unique validate_configuration ([#6878](https://github.com/great-expectations/great_expectations/pull/6878))
* [MAINTENANCE] Add docstrings for Validator and its save_expectation_suite and validate methods ([#6885](https://github.com/great-expectations/great_expectations/pull/6885))
* [MAINTENANCE] Type Hints Correction in New Datasources; Additional DocStrings ([#6918](https://github.com/great-expectations/great_expectations/pull/6918))

0.15.44
-----------------
* [FEATURE] Add pandas datasource sorter by refactoring into DataAsset ([#6787](https://github.com/great-expectations/great_expectations/pull/6787))
* [FEATURE] ID/PK Demo Files ([#6833](https://github.com/great-expectations/great_expectations/pull/6833))
* [BUGFIX] Fix missing not operator ~ ([#6808](https://github.com/great-expectations/great_expectations/pull/6808))
* [BUGFIX] Implemented lowercase function to check what type of file endswith ([#6810](https://github.com/great-expectations/great_expectations/pull/6810)) (thanks @tmilitino)
* [BUGFIX] : expect_day_count_to_be_close_to_equivalent_week_day_mean ([#6811](https://github.com/great-expectations/great_expectations/pull/6811)) (thanks @HadasManor)
* [BUGFIX] Pandas ID/PK query was causing DataDocs error ([#6832](https://github.com/great-expectations/great_expectations/pull/6832))
* [DOCS] Link to gh issue #4152 for ruamel.yaml ([#6799](https://github.com/great-expectations/great_expectations/pull/6799)) (thanks @jamesmyatt)
* [DOCS] ExpectationSuite and remove_expectation api docs ([#6785](https://github.com/great-expectations/great_expectations/pull/6785))
* [DOCS] Add GitHub PR links to changelogs ([#6818](https://github.com/great-expectations/great_expectations/pull/6818))
* [DOCS] Update `yarn-snippet-check` to only target specific source code dirs ([#6825](https://github.com/great-expectations/great_expectations/pull/6825))
* [DOCS] Adding docstring for ExpectationSuite.add_expectation ([#6829](https://github.com/great-expectations/great_expectations/pull/6829))
* [DOCS] DOC-394: Fix broken redirect links ([#6835](https://github.com/great-expectations/great_expectations/pull/6835))
* [MAINTENANCE] Enable more backends for some contrib expectations ([#6775](https://github.com/great-expectations/great_expectations/pull/6775))
* [MAINTENANCE] Change execution_engine_type from method to property. ([#6788](https://github.com/great-expectations/great_expectations/pull/6788))
* [MAINTENANCE] More backends for expect_yesterday_count_compared_to_avg_equivalent_days_of_week ([#6790](https://github.com/great-expectations/great_expectations/pull/6790))
* [MAINTENANCE] Update gallery pipeline to only have one scheduled run per day (early AM) ([#6791](https://github.com/great-expectations/great_expectations/pull/6791))
* [MAINTENANCE] Convert the validation results to JSON serializable ([#6776](https://github.com/great-expectations/great_expectations/pull/6776)) (thanks @lu-lz)
* [MAINTENANCE] Propagate "runtime_configuration" argument throughout Validator flow ([#6767](https://github.com/great-expectations/great_expectations/pull/6767))
* [MAINTENANCE] Only include relevant diagnostics info in gallery JSON ([#6797](https://github.com/great-expectations/great_expectations/pull/6797))
* [MAINTENANCE] Clean up public api report part 1 ([#6784](https://github.com/great-expectations/great_expectations/pull/6784))
* [MAINTENANCE] Clean up public api report part 2 ([#6792](https://github.com/great-expectations/great_expectations/pull/6792))
* [MAINTENANCE] Shift daily gallery run by 6 hours ([#6802](https://github.com/great-expectations/great_expectations/pull/6802))
* [MAINTENANCE] Misc docstrings in `AbstractDataContext` ([#6801](https://github.com/great-expectations/great_expectations/pull/6801))
* [MAINTENANCE] Add checkpoint and datadoc integration test for zep pandas datasource. ([#6793](https://github.com/great-expectations/great_expectations/pull/6793))
* [MAINTENANCE] Use environment variables for expectation gallery data paths ([#6805](https://github.com/great-expectations/great_expectations/pull/6805))
* [MAINTENANCE] Suppress 2 kl_divergence datasets for bigquery that took 90 minutes to insert ([#6807](https://github.com/great-expectations/great_expectations/pull/6807))
* [MAINTENANCE] Improve type hints in ExecutionEngine.resolve_metrics() flow and delete unnecessary checks ([#6804](https://github.com/great-expectations/great_expectations/pull/6804))
* [MAINTENANCE] Fixes for column_values_to_be_between tests ([#6809](https://github.com/great-expectations/great_expectations/pull/6809))
* [MAINTENANCE] Clean up public api report part 3 ([#6803](https://github.com/great-expectations/great_expectations/pull/6803))
* [MAINTENANCE] Add docstring for `AbstractDataContext.add_checkpoint` ([#6728](https://github.com/great-expectations/great_expectations/pull/6728))
* [MAINTENANCE] Use Enum classes for all metric name suffixes ([#6819](https://github.com/great-expectations/great_expectations/pull/6819))
* [MAINTENANCE] Use shortened_dotted_paths in API docs ([#6820](https://github.com/great-expectations/great_expectations/pull/6820))
* [MAINTENANCE] Update batch request option validation error message ([#6821](https://github.com/great-expectations/great_expectations/pull/6821))
* [MAINTENANCE] Add docstring to DataAsset.add_sorters ([#6822](https://github.com/great-expectations/great_expectations/pull/6822))
* [MAINTENANCE] Misc type cleanup within`checkpoint/` and `validator/` ([#6817](https://github.com/great-expectations/great_expectations/pull/6817))
* [MAINTENANCE] Update algolia indexing ([#6827](https://github.com/great-expectations/great_expectations/pull/6827))
* [MAINTENANCE] When running our test suite, suppress warnings `result_format` configuration in Expectations and Validators ([#6823](https://github.com/great-expectations/great_expectations/pull/6823))
* [MAINTENANCE] ZEP - lower logging levels from `INFO` -> `DEBUG` ([#6830](https://github.com/great-expectations/great_expectations/pull/6830))
* [MAINTENANCE] Use shortened dotted paths in api docs ([#6831](https://github.com/great-expectations/great_expectations/pull/6831))
* [MAINTENANCE] Remove outdated refs to Superconductive ([#6816](https://github.com/great-expectations/great_expectations/pull/6816))
* [CONTRIB] Improve contrib schwifty expectations ([#6812](https://github.com/great-expectations/great_expectations/pull/6812)) (thanks @mkopec87)

0.15.43
-----------------
* [FEATURE] ZEP - Synchronize & save XDatasources ([#6717](https://github.com/great-expectations/great_expectations/pull/6717))
* [FEATURE] Official Python 3.10 support ([#6763](https://github.com/great-expectations/great_expectations/pull/6763))
* [FEATURE] F/great 1313/zep pandas poc ([#6745](https://github.com/great-expectations/great_expectations/pull/6745))
* [FEATURE] Add GX Cloud hyperlink to slack notification ([#6740](https://github.com/great-expectations/great_expectations/pull/6740))
* [FEATURE] Get ExpectationSuite, Checkpoint by name ([#6774](https://github.com/great-expectations/great_expectations/pull/6774))
* [FEATURE] API docs ([#6766](https://github.com/great-expectations/great_expectations/pull/6766))
* [BUGFIX] - Implementing deep copy of runtime_configuration variable ([#6682](https://github.com/great-expectations/great_expectations/pull/6682)) (thanks @tmilitino)
* [BUGFIX] Patch broken `test_data_context_ge_cloud_mode_with_incomplete_cloud_config_should_throw_error` ([#6741](https://github.com/great-expectations/great_expectations/pull/6741))
* [BUGFIX] reformatting `setup.py` ([#6756](https://github.com/great-expectations/great_expectations/pull/6756))
* [BUGFIX] Fix observed value ([#6759](https://github.com/great-expectations/great_expectations/pull/6759)) (thanks @itaise)
* [BUGFIX] fix comment stripping when saving a zep configuration ([#6783](https://github.com/great-expectations/great_expectations/pull/6783))
* [DOCS] DOC-414: Remove guide for use of outdated docker images ([#6718](https://github.com/great-expectations/great_expectations/pull/6718))
* [DOCS] Convert docs snippets to named snippets ([#6735](https://github.com/great-expectations/great_expectations/pull/6735))
* [DOCS] Update documentation to reference `get_context` ([#6738](https://github.com/great-expectations/great_expectations/pull/6738))
* [DOCS] Convert remaining snippets to named snippets ([#6736](https://github.com/great-expectations/great_expectations/pull/6736))
* [DOCS] Convert line number references to named references in docs ([#6748](https://github.com/great-expectations/great_expectations/pull/6748))
* [DOCS] Doc-280 AWS golden path with S3 cloud storage and Pandas ([#6618](https://github.com/great-expectations/great_expectations/pull/6618))
* [DOCS] Preparation for building api docs ([#6737](https://github.com/great-expectations/great_expectations/pull/6737))
* [DOCS] Change prefix reference for tutorial folder/directory ([#6751](https://github.com/great-expectations/great_expectations/pull/6751)) (thanks @medeirosthiago)
* [DOCS] Fix line-links in 4th step's 5th and 6th block ([#6752](https://github.com/great-expectations/great_expectations/pull/6752)) (thanks @OnkarMadli)
* [DOCS] - fixed code reference in documentation ([#6732](https://github.com/great-expectations/great_expectations/pull/6732)) (thanks @tmilitino)
* [DOCS] validator.head docstring ([#6762](https://github.com/great-expectations/great_expectations/pull/6762))
* [MAINTENANCE] Update docstrings for experimental SQL datasources. ([#6714](https://github.com/great-expectations/great_expectations/pull/6714))
* [MAINTENANCE] update `cli` `DataContext` types ([#6703](https://github.com/great-expectations/great_expectations/pull/6703))
* [MAINTENANCE] Fix missing exclamation marks in API docs admonitions ([#6721](https://github.com/great-expectations/great_expectations/pull/6721))
* [MAINTENANCE] ID/PK Tests at Expectations-level with Warnings caught ([#6713](https://github.com/great-expectations/great_expectations/pull/6713))
* [MAINTENANCE] Refactor tests to leverage `get_context` instead of `BaseDataContext` ([#6720](https://github.com/great-expectations/great_expectations/pull/6720))
* [MAINTENANCE] Update remaining atomic prescriptive templates (1 of 2) ([#6696](https://github.com/great-expectations/great_expectations/pull/6696))
* [MAINTENANCE] Refactor tests to leverage `get_context` instead of `DataContext` ([#6723](https://github.com/great-expectations/great_expectations/pull/6723))
* [MAINTENANCE] Update remaining atomic prescriptive templates (2 of 2) ([#6724](https://github.com/great-expectations/great_expectations/pull/6724))
* [MAINTENANCE] `execution_engine`  typing ([#6730](https://github.com/great-expectations/great_expectations/pull/6730))
* [MAINTENANCE] `core/expectation_` type checking ([#6731](https://github.com/great-expectations/great_expectations/pull/6731))
* [MAINTENANCE] Remove printing of entire snippet map in `remark-named-snippet` hook ([#6749](https://github.com/great-expectations/great_expectations/pull/6749))
* [MAINTENANCE] Rename all instances of `ge_exceptions` to `gx_exceptions` ([#6742](https://github.com/great-expectations/great_expectations/pull/6742))
* [MAINTENANCE] Remove `base_data_context` mark in tests ([#6750](https://github.com/great-expectations/great_expectations/pull/6750))
* [MAINTENANCE] Consolidate different Metric Types definition Enums ([#6746](https://github.com/great-expectations/great_expectations/pull/6746))
* [MAINTENANCE] exclude scripts directory from package ([#6744](https://github.com/great-expectations/great_expectations/pull/6744)) (thanks @cburroughs)
* [MAINTENANCE] Force cryptography version installed where snowflake runs to be v38.0.4 ([#6755](https://github.com/great-expectations/great_expectations/pull/6755))
* [MAINTENANCE] ID/PK - Adding semi-colon to SQL Query output ([#6743](https://github.com/great-expectations/great_expectations/pull/6743))
* [MAINTENANCE] ID/PK result_format documentation update ([#6716](https://github.com/great-expectations/great_expectations/pull/6716))
* [MAINTENANCE] Consistent use of Metric Name Enum values ([#6757](https://github.com/great-expectations/great_expectations/pull/6757))
* [MAINTENANCE] Fix min version test requirements install on azure async pipeline. ([#6753](https://github.com/great-expectations/great_expectations/pull/6753))
* [MAINTENANCE] expectations linting & bug fixes ([#6739](https://github.com/great-expectations/great_expectations/pull/6739))
* [MAINTENANCE] Add Python 3.10 to async Azure pipeline ([#6760](https://github.com/great-expectations/great_expectations/pull/6760))
* [MAINTENANCE] Unset cloud vars when running pytest from a mac ([#6747](https://github.com/great-expectations/great_expectations/pull/6747))
* [MAINTENANCE] Update CheckChanges for dev pipeline ([#6768](https://github.com/great-expectations/great_expectations/pull/6768))
* [MAINTENANCE] Update contrib pipeline to track package changes ([#6770](https://github.com/great-expectations/great_expectations/pull/6770))
* [MAINTENANCE] Update docstring for `AbstractDataContext.add_batch_kwargs_generator` ([#6727](https://github.com/great-expectations/great_expectations/pull/6727))
* [MAINTENANCE] Update docstring for add_datasource ([#6729](https://github.com/great-expectations/great_expectations/pull/6729))
* [MAINTENANCE] Remove chunk of code in build_gallery.py to skip processing some Expectations ([#6772](https://github.com/great-expectations/great_expectations/pull/6772))
* [MAINTENANCE] Update docstring for `AbstractDataContext.build_data_docs` ([#6726](https://github.com/great-expectations/great_expectations/pull/6726))
* [MAINTENANCE] Move `constraints-test` dir within `azure` dir to clean up project root ([#6764](https://github.com/great-expectations/great_expectations/pull/6764))
* [MAINTENANCE] Misc cleanup of `SerializableDataContext` ([#6777](https://github.com/great-expectations/great_expectations/pull/6777))
* [MAINTENANCE] Removed some 30 type hint violations ([#6771](https://github.com/great-expectations/great_expectations/pull/6771))
* [MAINTENANCE] Adjust gallery schedule and timeout ([#6781](https://github.com/great-expectations/great_expectations/pull/6781))
* [MAINTENANCE] type-checking - `metrics/util.py` ([#6754](https://github.com/great-expectations/great_expectations/pull/6754))
* [MAINTENANCE] Update `requirements.txt` to reflect 3.10 support ([#6786](https://github.com/great-expectations/great_expectations/pull/6786))
* [MAINTENANCE] Enable more backends for some contrib expectations ([#6775](https://github.com/great-expectations/great_expectations/pull/6775))
* [CONTRIB] added condition to ExpectQueriedColumnListToBeUnique ([#6702](https://github.com/great-expectations/great_expectations/pull/6702)) (thanks @maayaniti)
* [CONTRIB] Implement Spark backend for several expectations ([#6683](https://github.com/great-expectations/great_expectations/pull/6683)) (thanks @mkopec87)
* [CONTRIB] Improve Spark backend support for contrib query based expectations ([#6733](https://github.com/great-expectations/great_expectations/pull/6733)) (thanks @mkopec87)
* [CONTRIB] Refactor ExpectColumnValuesToBeHexadecimal expectation to be RegexBased ([#6734](https://github.com/great-expectations/great_expectations/pull/6734)) (thanks @mkopec87)
* [CONTRIB] Fix regex based expectations for spark ([#6725](https://github.com/great-expectations/great_expectations/pull/6725)) (thanks @mkopec87)

0.15.42
-----------------
* [FEATURE] ZEP - PG `BatchSorter` loading + dumping ([#6580](https://github.com/great-expectations/great_expectations/pull/6580))
* [FEATURE] Ensure `result_format` accessed is through Checkpoint, and warns users if `Expectation` or `Validator`-level ([#6562](https://github.com/great-expectations/great_expectations/pull/6562))
* [FEATURE] ZEP - PG `SqlYearMonthSplitter` serialization + deserialization ([#6595](https://github.com/great-expectations/great_expectations/pull/6595))
* [FEATURE] ID/PK - `unexpected_index_list` updated to include actual unexpected value, and EVR to include `unexpected_index_column_names` ([#6586](https://github.com/great-expectations/great_expectations/pull/6586))
* [FEATURE] Atomic rendering of Evaluation Parameters ([#6232](https://github.com/great-expectations/great_expectations/pull/6232))
* [FEATURE] Add zep datasource data assistant e2e tests. ([#6612](https://github.com/great-expectations/great_expectations/pull/6612))
* [FEATURE] F/great 1400/sql datasource ([#6623](https://github.com/great-expectations/great_expectations/pull/6623))
* [FEATURE] Accept a `pathlib.Path` `context_root_dir` ([#6613](https://github.com/great-expectations/great_expectations/pull/6613))
* [FEATURE] Atomic rendering of meta notes ([#6627](https://github.com/great-expectations/great_expectations/pull/6627))
* [FEATURE] Docstring linter for public api ([#6638](https://github.com/great-expectations/great_expectations/pull/6638))
* [FEATURE]  ZEP - Load/dump new style config from DataContext ([#6631](https://github.com/great-expectations/great_expectations/pull/6631))
* [FEATURE] ID/PK Rendering in DataDocs ([#6637](https://github.com/great-expectations/great_expectations/pull/6637))
* [FEATURE] Use docstring linter for public api to catch missing parameters ([#6642](https://github.com/great-expectations/great_expectations/pull/6642))
* [FEATURE] ZEP - load from shared config ([#6655](https://github.com/great-expectations/great_expectations/pull/6655))
* [FEATURE] Added new expectation: ExpectYesterdayCountComparedToAvgEquivalentDaysOfWeek… ([#6622](https://github.com/great-expectations/great_expectations/pull/6622)) (thanks @HadasManor)
* [FEATURE] Add sqlite datasource ([#6657](https://github.com/great-expectations/great_expectations/pull/6657))
* [FEATURE] ExpectDaySumToBeCloseToEquivalentWeekDayMean ([#6664](https://github.com/great-expectations/great_expectations/pull/6664)) (thanks @HadasManor)
* [FEATURE] ID/PK flag `return_unexpected_index_query` that allows `QUERY` output to be suppressed ([#6660](https://github.com/great-expectations/great_expectations/pull/6660))
* [FEATURE] F/great 1400/postgres constr ([#6674](https://github.com/great-expectations/great_expectations/pull/6674))
* [FEATURE] Ensure Pandas ID/PK can use named indices ([#6656](https://github.com/great-expectations/great_expectations/pull/6656))
* [FEATURE] Support to include ID/PK in validation result for each row - Spark ([#6676](https://github.com/great-expectations/great_expectations/pull/6676))
* [FEATURE] ID/PK Pandas query returned as all unexpected indices ([#6692](https://github.com/great-expectations/great_expectations/pull/6692))
* [BUGFIX] Support non-string `datetime` evaluation parameters ([#6571](https://github.com/great-expectations/great_expectations/pull/6571))
* [BUGFIX] Use v3.3.6 or higher of google-cloud-bigquery (with shapely bugfix) ([#6590](https://github.com/great-expectations/great_expectations/pull/6590))
* [BUGFIX] Remove rendered header from Cloud-rendering tests ([#6597](https://github.com/great-expectations/great_expectations/pull/6597))
* [BUGFIX] Patch broken `Validator` test after `DataContext` refactor ([#6605](https://github.com/great-expectations/great_expectations/pull/6605))
* [BUGFIX] Column value counts metric `dtype` inference due to `numpy` deprecation of `object` `dtype` ([#6604](https://github.com/great-expectations/great_expectations/pull/6604))
* [BUGFIX] `delete_datasource()` was getting passed in incorrect parameter for Spark Docs test ([#6601](https://github.com/great-expectations/great_expectations/pull/6601))
* [BUGFIX] Stop overwriting query with static string in RuntimeBatchRequests for SQL ([#6614](https://github.com/great-expectations/great_expectations/pull/6614))
* [BUGFIX] Simplify metric results processing and improve detection of Decimal types in columns ([#6610](https://github.com/great-expectations/great_expectations/pull/6610))
* [BUGFIX] Do not round output of proportion computing metrics ([#6619](https://github.com/great-expectations/great_expectations/pull/6619))
* [BUGFIX] Add sqrt on connect to sqlite database. ([#6635](https://github.com/great-expectations/great_expectations/pull/6635))
* [BUGFIX] `RendererConfiguration` `min_value` and `max_value` with `datetime`s ([#6632](https://github.com/great-expectations/great_expectations/pull/6632))
* [BUGFIX] Fix a typo in contrib queried expectation (and add type hints to its implementation) ([#6650](https://github.com/great-expectations/great_expectations/pull/6650))
* [BUGFIX] Avoid key collisions between Rule-Based Profiler terminal literals and MetricConfiguration value keys ([#6675](https://github.com/great-expectations/great_expectations/pull/6675))
* [BUGFIX] Add connect args to execution engine schema ([#6663](https://github.com/great-expectations/great_expectations/pull/6663)) (thanks @itaise)
* [BUGFIX] Increase minimum `numpy` versions for Python 3.8 and 3.9 due to support in latest release of `scipy` ([#6704](https://github.com/great-expectations/great_expectations/pull/6704))
* [BUGFIX] Format current branch name properly for tag branches in docker tests ([#6711](https://github.com/great-expectations/great_expectations/pull/6711))
* [DOCS] Patch broken snippet around Validation Actions ([#6606](https://github.com/great-expectations/great_expectations/pull/6606))
* [DOCS] Fix formatting of 0.15.35 and 0.15.36 in changelogs ([#6603](https://github.com/great-expectations/great_expectations/pull/6603))
* [DOCS] Convert broken snippet to named snippets ([#6611](https://github.com/great-expectations/great_expectations/pull/6611))
* [DOCS] - add anonymous_usage_statistics configutation in documentation ([#6626](https://github.com/great-expectations/great_expectations/pull/6626)) (thanks @tmilitino)
* [DOCS] fixing wrong line reference on docs ([#6599](https://github.com/great-expectations/great_expectations/pull/6599)) (thanks @wagneralbjr)
* [DOCS] Sidebar changes for Integrations and how-tos ([#6649](https://github.com/great-expectations/great_expectations/pull/6649))
* [DOCS] edit term(data_conext, checkpoints)-link in with airflow ([#6646](https://github.com/great-expectations/great_expectations/pull/6646)) (thanks @jx2lee)
* [DOCS] DOC-400 remove an outdated video link ([#6667](https://github.com/great-expectations/great_expectations/pull/6667))
* [DOCS] doc-356 importable prerequisite box with correct theme applied and default entries ([#6666](https://github.com/great-expectations/great_expectations/pull/6666))
* [MAINTENANCE] `mypy` config update ([#6589](https://github.com/great-expectations/great_expectations/pull/6589))
* [MAINTENANCE] Small refactor of ExecutionEngine.resolve_metrics() for better code readability (and miscellaneous additional clean up) ([#6587](https://github.com/great-expectations/great_expectations/pull/6587))
* [MAINTENANCE] Remove `ExplorerDataContext` ([#6592](https://github.com/great-expectations/great_expectations/pull/6592))
* [MAINTENANCE] Leverage `RendererConfiguration` in existing prescriptive templates (2 of 3) ([#6488](https://github.com/great-expectations/great_expectations/pull/6488))
* [MAINTENANCE] Leverage `RendererConfiguration` in existing prescriptive templates (3 of 3) ([#6530](https://github.com/great-expectations/great_expectations/pull/6530))
* [MAINTENANCE] Add docs snippet checker to `dev` CI ([#6594](https://github.com/great-expectations/great_expectations/pull/6594))
* [MAINTENANCE] Utilize a `StrEnum` for `ConfigPeer` modes ([#6596](https://github.com/great-expectations/great_expectations/pull/6596))
* [MAINTENANCE] Refactor `BaseDataContext` and `DataContext` into factory functions ([#6531](https://github.com/great-expectations/great_expectations/pull/6531))
* [MAINTENANCE] flake8 coverage - `render`, `juptyer_ux`, `checkpoint` sub-packages ([#6607](https://github.com/great-expectations/great_expectations/pull/6607))
* [MAINTENANCE] filter `RemovedInMarshmallow4` warnings ([#6602](https://github.com/great-expectations/great_expectations/pull/6602))
* [MAINTENANCE] Generate public API candidates ([#6600](https://github.com/great-expectations/great_expectations/pull/6600))
* [MAINTENANCE] partial `cli` + `usage_stats` typing ([#6335](https://github.com/great-expectations/great_expectations/pull/6335))
* [MAINTENANCE] update pip installs in pipelines ([#6609](https://github.com/great-expectations/great_expectations/pull/6609))
* [MAINTENANCE] create cache as part of `--ci` type-checking step ([#6621](https://github.com/great-expectations/great_expectations/pull/6621))
* [MAINTENANCE] Add `row_condition` logic to `RendererConfiguration` and remove from atomic renderer implementations ([#6616](https://github.com/great-expectations/great_expectations/pull/6616))
* [MAINTENANCE] install `pydantic` in develop pipeline ([#6624](https://github.com/great-expectations/great_expectations/pull/6624))
* [MAINTENANCE] Fix develop static type-check stage ([#6628](https://github.com/great-expectations/great_expectations/pull/6628))
* [MAINTENANCE] Unexpected Counts table in DataDocs able to show counts for sampled values ([#6634](https://github.com/great-expectations/great_expectations/pull/6634))
* [MAINTENANCE] CI - install from `requirements-types.txt` ([#6639](https://github.com/great-expectations/great_expectations/pull/6639))
* [MAINTENANCE] Add docstring linter for public api to CI ([#6641](https://github.com/great-expectations/great_expectations/pull/6641))
* [MAINTENANCE] Batch ID must incorporate batch_spec_passthrough.  Instantiate Validator with DataContext in test modules.  Query metrics/expectations types cleanup. ([#6636](https://github.com/great-expectations/great_expectations/pull/6636))
* [MAINTENANCE] Skip postgres tests in spark. ([#6643](https://github.com/great-expectations/great_expectations/pull/6643))
* [MAINTENANCE] Enrich `RendererConfiguration` primitive types ([#6629](https://github.com/great-expectations/great_expectations/pull/6629))
* [MAINTENANCE] M/great 1225/async builds branch ([#6644](https://github.com/great-expectations/great_expectations/pull/6644))
* [MAINTENANCE] Comment out calling _disable_progress_bars in build_gallery.py ([#6648](https://github.com/great-expectations/great_expectations/pull/6648))
* [MAINTENANCE] Update generate_expectation_tests func to only log an ERROR message if there is an error ([#6651](https://github.com/great-expectations/great_expectations/pull/6651))
* [MAINTENANCE] Use the correct test for positive_test__exact_min_and_max on trino ([#6652](https://github.com/great-expectations/great_expectations/pull/6652))
* [MAINTENANCE] Update evaluate_json_test_v3_api func to use the debug_logger with useful info when exception occurs ([#6653](https://github.com/great-expectations/great_expectations/pull/6653))
* [MAINTENANCE] Make only column y data_alt different in col_pair_equal tests ([#6661](https://github.com/great-expectations/great_expectations/pull/6661))
* [MAINTENANCE] Add separate tests for exact stdev for redshift and snowflake ([#6658](https://github.com/great-expectations/great_expectations/pull/6658))
* [MAINTENANCE] Add redshift/snowflake casting for sample data on expect_column_values_to_be_of_type ([#6659](https://github.com/great-expectations/great_expectations/pull/6659))
* [MAINTENANCE] Add redshift/snowflake casting for sample data on expect_column_values_to_be_in_type_list ([#6668](https://github.com/great-expectations/great_expectations/pull/6668))
* [MAINTENANCE] Make only column y data_alt different in col_pair_in_set tests ([#6670](https://github.com/great-expectations/great_expectations/pull/6670))
* [MAINTENANCE] Only spark v2 for special test in not_be_in_set ([#6669](https://github.com/great-expectations/great_expectations/pull/6669))
* [MAINTENANCE] Don't attempt any regex Expectation tests with snowflake ([#6672](https://github.com/great-expectations/great_expectations/pull/6672))
* [MAINTENANCE] Clean up returns style and type hints in CardinalityChecker utility ([#6677](https://github.com/great-expectations/great_expectations/pull/6677))
* [MAINTENANCE] begin flake8 linting on tests ([#6679](https://github.com/great-expectations/great_expectations/pull/6679))
* [MAINTENANCE] Clean up packaging & installation pipeline ([#6687](https://github.com/great-expectations/great_expectations/pull/6687))
* [MAINTENANCE] Misc updates to dev Azure pipeline ([#6686](https://github.com/great-expectations/great_expectations/pull/6686))
* [MAINTENANCE] `mypy` typing for `core/util.py` ([#6617](https://github.com/great-expectations/great_expectations/pull/6617))
* [MAINTENANCE] Update `get_context` return type ([#6684](https://github.com/great-expectations/great_expectations/pull/6684))
* [MAINTENANCE] Get datetime tests working for trino/snowflake/spark in values_to_be_in_set ([#6671](https://github.com/great-expectations/great_expectations/pull/6671))
* [MAINTENANCE] Cleanup typing errors. ([#6691](https://github.com/great-expectations/great_expectations/pull/6691))
* [MAINTENANCE] Remove unused Metric and BatchMetric classes and consolidate ValidationMetricIdentifier with other identifiers ([#6693](https://github.com/great-expectations/great_expectations/pull/6693))
* [MAINTENANCE] Refactor `BaseDataContext` to leverage `get_context` ([#6689](https://github.com/great-expectations/great_expectations/pull/6689))
* [MAINTENANCE] expect day count to be close to equivalent week day mean ([#6680](https://github.com/great-expectations/great_expectations/pull/6680)) (thanks @HadasManor)
* [MAINTENANCE] ID/PK squashed tests re-added ([#6694](https://github.com/great-expectations/great_expectations/pull/6694))
* [MAINTENANCE] initial type checking for `rules_based_profiler` ([#6681](https://github.com/great-expectations/great_expectations/pull/6681))
* [MAINTENANCE] Improve type checking for Expectations with atomic renderers leveraging `RendererConfiguration` ([#6633](https://github.com/great-expectations/great_expectations/pull/6633))
* [MAINTENANCE] Add deprecated Cloud variables to `_CloudConfigurationProvider.get_values()` output ([#6708](https://github.com/great-expectations/great_expectations/pull/6708))
* [MAINTENANCE] Autobuild markdown stubs ([#6700](https://github.com/great-expectations/great_expectations/pull/6700))
* [MAINTENANCE] API docs styling ([#6712](https://github.com/great-expectations/great_expectations/pull/6712))

0.15.41
-----------------
* [FEATURE] enable mostly for expect_compound_columns_to_be_unique ([#6533](https://github.com/great-expectations/great_expectations/pull/6533)) (thanks @kimfrie)
* [BUGFIX] Return unique list of batch_definitions ([#6579](https://github.com/great-expectations/great_expectations/pull/6579)) (thanks @tanelk)
* [BUGFIX] convert_to_json_serializable does not accept numpy datetime ([#6553](https://github.com/great-expectations/great_expectations/pull/6553)) (thanks @tmilitino)
* [DOCS] Clean up misc snippet violations ([#6582](https://github.com/great-expectations/great_expectations/pull/6582))
* [MAINTENANCE] Update json schema validation on usage stats to filter based on format. ([#6502](https://github.com/great-expectations/great_expectations/pull/6502))
* [MAINTENANCE] Renaming Metric Name Suffixes using Enum Values for Better Code Readability ([#6575](https://github.com/great-expectations/great_expectations/pull/6575))
* [MAINTENANCE] M/great 1433/cloud tests to async ([#6543](https://github.com/great-expectations/great_expectations/pull/6543))
* [MAINTENANCE] Add static type checking to `rule.py` and `rule_based_profiler_result.py` ([#6573](https://github.com/great-expectations/great_expectations/pull/6573))
* [MAINTENANCE] Update most contrib Expectation docstrings to be consistent and decently formatted for gallery ([#6577](https://github.com/great-expectations/great_expectations/pull/6577))
* [MAINTENANCE] Update changelogs to reflect PyPI yanks (0.15.37-0.15.39) ([#6581](https://github.com/great-expectations/great_expectations/pull/6581))
* [MAINTENANCE] Refactor ExecutionEngine.resolve_metrics() for better code readability ([#6578](https://github.com/great-expectations/great_expectations/pull/6578))
* [MAINTENANCE] adding googletag manager to docusaurus ([#6584](https://github.com/great-expectations/great_expectations/pull/6584))
* [MAINTENANCE] typo in method name ([#6585](https://github.com/great-expectations/great_expectations/pull/6585))

0.15.40
-----------------
* [FEATURE] F/great 1397/zep checkpoints ([#6525](https://github.com/great-expectations/great_expectations/pull/6525))
* [FEATURE] Add integration test for zep sqlalchemy datasource with renderering. ([#6564](https://github.com/great-expectations/great_expectations/pull/6564))
* [BUGFIX] Patch additional deprecated call to `GXCloudIdentifier.ge_cloud_id` attr ([#6555](https://github.com/great-expectations/great_expectations/pull/6555))
* [BUGFIX] Patch `packaging_and_installation` Azure pipeline test failures ([#6559](https://github.com/great-expectations/great_expectations/pull/6559))
* [BUGFIX] Fix dependency issues to reenable RTD builds ([#6560](https://github.com/great-expectations/great_expectations/pull/6560))
* [BUGFIX] Add missing `raise` statement in `RuntimeDataConnector` logic ([#6569](https://github.com/great-expectations/great_expectations/pull/6569))
* [DOCS] doc 383: bring sql datasource configuration examples under test ([#6466](https://github.com/great-expectations/great_expectations/pull/6466))
* [MAINTENANCE] Add error handling to docs snippet checker ([#6556](https://github.com/great-expectations/great_expectations/pull/6556))
* [MAINTENANCE] ID/PK tests at `Checkpoint`-level ([#6539](https://github.com/great-expectations/great_expectations/pull/6539))
* [MAINTENANCE] Improve DataAssistant Parameter Builder Naming/Sanitization Mechanism and Enhance TableDomainBuilder ([#6554](https://github.com/great-expectations/great_expectations/pull/6554))
* [MAINTENANCE] Simplify computational graph assembly from metric configurations ([#6563](https://github.com/great-expectations/great_expectations/pull/6563))
* [MAINTENANCE] RTD Mobile header brand adjustment ([#6557](https://github.com/great-expectations/great_expectations/pull/6557))
* [MAINTENANCE] Use MetricsCalculator methods for ValidationGraph construction and resolution operations in Validator ([#6566](https://github.com/great-expectations/great_expectations/pull/6566))
* [MAINTENANCE] Cast type in `execution_environment.py` to bypass flaky `mypy` warnings ([#6572](https://github.com/great-expectations/great_expectations/pull/6572))
* [MAINTENANCE] Additional patch for `mypy` issue in `execution_environment.py` ([#6574](https://github.com/great-expectations/great_expectations/pull/6574))
* [MAINTENANCE] Clean up GX rename artifacts ([#6561](https://github.com/great-expectations/great_expectations/pull/6561))
* [CONTRIB] fix observed value in custom expectation ([#6515](https://github.com/great-expectations/great_expectations/pull/6515)) (thanks @itaise)

0.15.39 - YANKED
-----------------
* [BUGFIX] Patch faulty GX Cloud arg resolution logic ([#6542](https://github.com/great-expectations/great_expectations/pull/6542))
* [BUGFIX] Fix resolution of cloud variables. ([#6546](https://github.com/great-expectations/great_expectations/pull/6546))
* [DOCS] Fix line numbers in snippets part 2 ([#6537](https://github.com/great-expectations/great_expectations/pull/6537))
* [DOCS] Convert nested snippets to named snippets ([#6541](https://github.com/great-expectations/great_expectations/pull/6541))
* [DOCS] Simplify snippet checker logic to catch stray tags in CI ([#6538](https://github.com/great-expectations/great_expectations/pull/6538))
* [MAINTENANCE] v2 Docs link ([#6534](https://github.com/great-expectations/great_expectations/pull/6534))
* [MAINTENANCE] Fix logic around cloud_mode and ge_cloud_mode. ([#6550](https://github.com/great-expectations/great_expectations/pull/6550))

0.15.38 - YANKED
-----------------
* [BUGFIX] Patch broken Cloud E2E test around `Datasource` CRUD ([#6520](https://github.com/great-expectations/great_expectations/pull/6520))
* [BUGFIX] Patch outdated `ge_cloud_id` attribute call in `ValidationOperator` ([#6529](https://github.com/great-expectations/great_expectations/pull/6529))
* [BUGFIX] Revert refactor to `Datasource` instantiation logic in `DataContext` ([#6535](https://github.com/great-expectations/great_expectations/pull/6535))
* [BUGFIX] Patch faulty GX Cloud arg resolution logic ([#6542](https://github.com/great-expectations/great_expectations/pull/6542))
* [DOCS] Fix line numbers in snippets ([#6536](https://github.com/great-expectations/great_expectations/pull/6536))
* [DOCS] Fix line numbers in snippets part 2 ([#6537](https://github.com/great-expectations/great_expectations/pull/6537))
* [DOCS] Convert nested snippets to named snippets ([#6541](https://github.com/great-expectations/great_expectations/pull/6541))
* [MAINTENANCE] Update Data Assistant plot images ([#6521](https://github.com/great-expectations/great_expectations/pull/6521))
* [MAINTENANCE] Clean up type hints and make test generation more elegant ([#6523](https://github.com/great-expectations/great_expectations/pull/6523))
* [MAINTENANCE] Clean up `Datasource` instantiation logic in `DataContext` ([#6517](https://github.com/great-expectations/great_expectations/pull/6517))
* [MAINTENANCE] Update `Domain` computation in MetricConfiguration ([#6528](https://github.com/great-expectations/great_expectations/pull/6528))
* [MAINTENANCE] v2 Docs link ([#6534](https://github.com/great-expectations/great_expectations/pull/6534))

0.15.37 - YANKED
-----------------
* [FEATURE] Support to include ID/PK in validation result for each row - SQL ([#6448](https://github.com/great-expectations/great_expectations/pull/6448))
* [FEATURE] Build process and example API docs (part 1) ([#6474](https://github.com/great-expectations/great_expectations/pull/6474))
* [FEATURE] Add temp_table_schema_name support for BigQuery ([#6303](https://github.com/great-expectations/great_expectations/pull/6303)) (thanks @BobbyRyterski)
* [FEATURE] Decorators for API docs (part 2) ([#6497](https://github.com/great-expectations/great_expectations/pull/6497))
* [FEATURE] Decorators for API docs (part 3) ([#6504](https://github.com/great-expectations/great_expectations/pull/6504))
* [BUGFIX] Support slack channel name with webhook also ([#6481](https://github.com/great-expectations/great_expectations/pull/6481)) (thanks @Kozehh)
* [BUGFIX] Airflow operator package conflict for `jsonschema` ([#6495](https://github.com/great-expectations/great_expectations/pull/6495))
* [BUGFIX] Validator uses proper arguments to show progress bar at Metrics resolution-level ([#6510](https://github.com/great-expectations/great_expectations/pull/6510)) (thanks @tommy-watts-depop)
* [DOCS] Schedule Algolia Crawler daily at midnight ([#6323](https://github.com/great-expectations/great_expectations/pull/6323))
* [DOCS] fix(gh-6512): fix rendering of Batch definition ([#6513](https://github.com/great-expectations/great_expectations/pull/6513)) (thanks @JoelGritter)
* [MAINTENANCE] Add pretty representations for zep pydantic models ([#6472](https://github.com/great-expectations/great_expectations/pull/6472))
* [MAINTENANCE] Misc updates to PR template ([#6479](https://github.com/great-expectations/great_expectations/pull/6479))
* [MAINTENANCE] Minor cleanup for better code readability ([#6478](https://github.com/great-expectations/great_expectations/pull/6478))
* [MAINTENANCE] Move zep method from datasource to data asset. ([#6477](https://github.com/great-expectations/great_expectations/pull/6477))
* [MAINTENANCE] Staging for build gallery ([#6480](https://github.com/great-expectations/great_expectations/pull/6480))
* [MAINTENANCE] Reformat core expectation docstrings ([#6423](https://github.com/great-expectations/great_expectations/pull/6423))
* [MAINTENANCE] Move "Domain" to "great_expectations/core" to avoid circular imports; also add MetricConfiguration tests; and other clean up. ([#6484](https://github.com/great-expectations/great_expectations/pull/6484))
* [MAINTENANCE] Query the database for datetime column splitter defaults ([#6482](https://github.com/great-expectations/great_expectations/pull/6482))
* [MAINTENANCE] Placing metrics test db under try-except  ([#6489](https://github.com/great-expectations/great_expectations/pull/6489))
* [MAINTENANCE] Clean up tests for more formal Batch and Validator instantiation ([#6491](https://github.com/great-expectations/great_expectations/pull/6491))
* [MAINTENANCE] Rename `ge` to `gx` across the codebase ([#6487](https://github.com/great-expectations/great_expectations/pull/6487))
* [MAINTENANCE] Upgrade CodeSee workflow to version 2 ([#6498](https://github.com/great-expectations/great_expectations/pull/6498)) (thanks @codesee-maps[bot])
* [MAINTENANCE]  Rename `GE` to `GX` across codebase (GREAT-1352) ([#6494](https://github.com/great-expectations/great_expectations/pull/6494))
* [MAINTENANCE] Resolve `mypy` issues in `cli/docs.py` ([#6500](https://github.com/great-expectations/great_expectations/pull/6500))
* [MAINTENANCE] Increase timeout to 15 minutes for the 2 jobs in manual-staging-json-to-prod pipeline ([#6509](https://github.com/great-expectations/great_expectations/pull/6509))
* [MAINTENANCE] Update Data Assistant plot color scheme and fonts ([#6496](https://github.com/great-expectations/great_expectations/pull/6496))
* [MAINTENANCE] Update `RendererConfiguration` to `pydantic` model ([#6452](https://github.com/great-expectations/great_expectations/pull/6452))
* [MAINTENANCE] Message for how to install Great Expectations in Cloud Composer by pinning packages ([#6492](https://github.com/great-expectations/great_expectations/pull/6492))
* [MAINTENANCE] Leverage `RendererConfiguration` in existing prescriptive templates (1 of 3) ([#6460](https://github.com/great-expectations/great_expectations/pull/6460))
* [MAINTENANCE] Clean up `teams.yml` ([#6511](https://github.com/great-expectations/great_expectations/pull/6511))
* [MAINTENANCE] Make Generated Integration Tests More Robust Using BatchDefinition and InMemoryDataContext In Validator and ExecutionEngine Instantiation ([#6505](https://github.com/great-expectations/great_expectations/pull/6505))
* [MAINTENANCE] DO NOT MERGE UNTIL DEC 8: [MAINTENANCE] Brand changes in docs ([#6427](https://github.com/great-expectations/great_expectations/pull/6427))
* [MAINTENANCE] fixed typo in nav ([#6518](https://github.com/great-expectations/great_expectations/pull/6518))
* [MAINTENANCE] Clean up GX Cloud environment variable usage (GREAT-1352) ([#6501](https://github.com/great-expectations/great_expectations/pull/6501))
* [MAINTENANCE] Update Data Assistant plot images ([#6521](https://github.com/great-expectations/great_expectations/pull/6521))
* [CONTRIB] Add uniqueness expectation ([#6473](https://github.com/great-expectations/great_expectations/pull/6473)) (thanks @itaise)

0.15.36
-----------------
[BUGFIX] Contrib Expectation tracebacks ([#6471](https://github.com/great-expectations/great_expectations/pull/6471))
[BUGFIX] Add additional error checking to `ExpectationAnonymizer` ([#6467](https://github.com/great-expectations/great_expectations/pull/6467))
[MAINTENANCE] Add docstring for context.sources.add_postgres ([#6459](https://github.com/great-expectations/great_expectations/pull/6459))
[MAINTENANCE] fixing type hints in metrics utils module ([#6469](https://github.com/great-expectations/great_expectations/pull/6469))
[MAINTENANCE] Moving tutorials to great-expectations repo ([#6464](https://github.com/great-expectations/great_expectations/pull/6464))

0.15.35
-----------------
[FEATURE] add multiple input metric ([#6373](https://github.com/great-expectations/great_expectations/pull/6373)) (thanks @CarstenFrommhold)
[FEATURE] add multiple column metric ([#6372](https://github.com/great-expectations/great_expectations/pull/6372)) (thanks @CarstenFrommhold)
[FEATURE]: DataProfilerUnstructuredDataAssistant Integration ([#6400](https://github.com/great-expectations/great_expectations/pull/6400)) (thanks @micdavis)
[FEATURE] add new metric - query template values ([#5994](https://github.com/great-expectations/great_expectations/pull/5994)) (thanks @itaise)
[FEATURE] ZEP Config serialize as YAML ([#6398](https://github.com/great-expectations/great_expectations/pull/6398))
[BUGFIX] Patch issue with call to `ExpectationAnonymizer` to ensure `DataContext` init events are captured ([#6458](https://github.com/great-expectations/great_expectations/pull/6458))
[BUGFIX] Support Table and Column Names Case Non-Sensitivity Relationship Between Snowflake, Oracle, DB2, etc. DBMSs (Upper Case) and SQLAlchemy (Lower Case) Representations ([#6450](https://github.com/great-expectations/great_expectations/pull/6450))
[BUGFIX] Metrics return value no longer returns None for `unexpected_index_list` - Sql and Spark ([#6392](https://github.com/great-expectations/great_expectations/pull/6392))
[BUGFIX] Fix for `mssql` tests that depend on `datetime` to `string` conversion ([#6449](https://github.com/great-expectations/great_expectations/pull/6449))
[BUGFIX] issue-4295-fix-issue ([#6164](https://github.com/great-expectations/great_expectations/pull/6164)) (thanks @YevgeniyaLee)
[BUGFIX] updated capitalone setup.py file ([#6410](https://github.com/great-expectations/great_expectations/pull/6410)) (thanks @micdavis)
[BUGFIX] Patch key-generation issue with `DataContext.save_profiler()` ([#6405](https://github.com/great-expectations/great_expectations/pull/6405))
[DOCS] add configuration of anonymous_usage_statistics for documentation ([#6293](https://github.com/great-expectations/great_expectations/pull/6293)) (thanks @milithino)
[DOCS] add boto3 explanations on document ([#6407](https://github.com/great-expectations/great_expectations/pull/6407)) (thanks @tiruka)
[MAINTENANCE] [CONTRIB] Multicolumns sum equal to single column ([#6446](https://github.com/great-expectations/great_expectations/pull/6446)) (thanks @asafla)
[MAINTENANCE] [CONTRIB] add expectation - check gaps in SCD tables ([#6433](https://github.com/great-expectations/great_expectations/pull/6433)) (thanks @itaise)
[MAINTENANCE] [CONTRIB] Add no days missing expectation ([#6432](https://github.com/great-expectations/great_expectations/pull/6432)) (thanks @itaise)
[MAINTENANCE] [CONTRIB] Feature/add two tables expectation ([#6429](https://github.com/great-expectations/great_expectations/pull/6429)) (thanks @itaise)
[MAINTENANCE] [CONTRIB] Add number of unique values expectation ([#6425](https://github.com/great-expectations/great_expectations/pull/6425)) (thanks @itaise)
[MAINTENANCE] Add sorters to zep postgres datasource. ([#6456](https://github.com/great-expectations/great_expectations/pull/6456))
[MAINTENANCE] Bump ubuntu version in CI ([#6457](https://github.com/great-expectations/great_expectations/pull/6457))
[MAINTENANCE] Remove anticipatory multi-language support from renderers ([#6426](https://github.com/great-expectations/great_expectations/pull/6426))
[MAINTENANCE] Remove yaml user_flow_scripts ([#6454](https://github.com/great-expectations/great_expectations/pull/6454))
[MAINTENANCE] Additional `sqlite` database fixture for `taxi_data` - All 2020 data in single table ([#6455](https://github.com/great-expectations/great_expectations/pull/6455))
[MAINTENANCE] Clean Up Variable Names In Test Modules, Type Hints, and Minor Refactoring For Better Code Elegance/Readability ([#6444](https://github.com/great-expectations/great_expectations/pull/6444))
[MAINTENANCE] Update and Simplify Pandas tests for MapMetrics ([#6443](https://github.com/great-expectations/great_expectations/pull/6443))
[MAINTENANCE] Add metadata to experimental datasource Batch class ([#6442](https://github.com/great-expectations/great_expectations/pull/6442))
[MAINTENANCE] Small refactor ([#6422](https://github.com/great-expectations/great_expectations/pull/6422))
[MAINTENANCE] Sorting batch IDs and typehints clean up ([#6421](https://github.com/great-expectations/great_expectations/pull/6421))
[MAINTENANCE] Clean Up Type Hints and Minor Refactoring For Better Code Elegance/Readability ([#6418](https://github.com/great-expectations/great_expectations/pull/6418))
[MAINTENANCE] Implement `RendererConfiguration` ([#6412](https://github.com/great-expectations/great_expectations/pull/6412))
[MAINTENANCE] Cleanup For Better Code Elegance/Readability ([#6406](https://github.com/great-expectations/great_expectations/pull/6406))
[MAINTENANCE] ZEP - `GxConfig` cleanup ([#6404](https://github.com/great-expectations/great_expectations/pull/6404))
[MAINTENANCE] Migrate remaining methods from `BaseDataContext` ([#6403](https://github.com/great-expectations/great_expectations/pull/6403))
[MAINTENANCE] Migrate additional CRUD methods from `BaseDataContext` to `AbstractDataContext` ([#6395](https://github.com/great-expectations/great_expectations/pull/6395))
[MAINTENANCE] ZEP add yaml methods to all experimental models ([#6401](https://github.com/great-expectations/great_expectations/pull/6401))
[MAINTENANCE] Remove call to verify_library_dependent_modules for pybigquery ([#6394](https://github.com/great-expectations/great_expectations/pull/6394))
[MAINTENANCE] Make "IDDict.to_id()" serialization more efficient. ([#6389](https://github.com/great-expectations/great_expectations/pull/6389))

0.15.34
-----------------
* [BUGFIX] Ensure `packaging_and_installation` CI tests against latest tag ([#6386](https://github.com/great-expectations/great_expectations/pull/6386))
* [BUGFIX] Fixed missing comma in pydantic constraints ([#6391](https://github.com/great-expectations/great_expectations/pull/6391)) (thanks @awburgess)
* [BUGFIX] fix pydantic dev req file entries ([#6396](https://github.com/great-expectations/great_expectations/pull/6396))
* [DOCS] DOC-379 bring spark datasource configuration example scripts under test ([#6362](https://github.com/great-expectations/great_expectations/pull/6362))
* [MAINTENANCE] Handle both `ExpectationConfiguration` and `ExpectationValidationResult` in default Atomic renderers and cleanup `include_column_name` ([#6380](https://github.com/great-expectations/great_expectations/pull/6380))
* [MAINTENANCE] Add type annotations to all existing atomic renderer signatures ([#6385](https://github.com/great-expectations/great_expectations/pull/6385))
* [MAINTENANCE] move `zep` -> `experimental` package ([#6378](https://github.com/great-expectations/great_expectations/pull/6378))
* [MAINTENANCE] Migrate additional methods from `BaseDataContext` to other parts of context hierarchy ([#6388](https://github.com/great-expectations/great_expectations/pull/6388))

0.15.33
-----------------
* [FEATURE] POC ZEP Config Loading ([#6320](https://github.com/great-expectations/great_expectations/pull/6320))
* [BUGFIX] Fix issue with misaligned indentation in docs snippets ([#6339](https://github.com/great-expectations/great_expectations/pull/6339))
* [BUGFIX] Use `requirements.txt` file when installing linting/static check dependencies in CI ([#6368](https://github.com/great-expectations/great_expectations/pull/6368))
* [BUGFIX] Patch nested snippet indentation issues within `remark-named-snippets` plugin ([#6376](https://github.com/great-expectations/great_expectations/pull/6376))
* [BUGFIX] Ensure `packaging_and_installation` CI tests against latest tag ([#6386](https://github.com/great-expectations/great_expectations/pull/6386))
* [DOCS] DOC-308 update CLI command in docs when working with RBPs instead of Data Assistants ([#6222](https://github.com/great-expectations/great_expectations/pull/6222))
* [DOCS] DOC-366 updates to docs in support of branding updates ([#5766](https://github.com/great-expectations/great_expectations/pull/5766))
* [DOCS] Add `yarn snippet-check` command ([#6351](https://github.com/great-expectations/great_expectations/pull/6351))
* [MAINTENANCE] Add missing one-line docstrings and try to make the others consistent ([#6340](https://github.com/great-expectations/great_expectations/pull/6340))
* [MAINTENANCE] Refactor variable aggregation/substitution logic into `ConfigurationProvider` hierarchy ([#6321](https://github.com/great-expectations/great_expectations/pull/6321))
* [MAINTENANCE] In ExecutionEngine: Make variable names and usage more descriptive of their purpose. ([#6342](https://github.com/great-expectations/great_expectations/pull/6342))
* [MAINTENANCE] Move Cloud-specific enums to `cloud_constants.py` ([#6349](https://github.com/great-expectations/great_expectations/pull/6349))
* [MAINTENANCE] Refactor out `termcolor` dependency ([#6348](https://github.com/great-expectations/great_expectations/pull/6348))
* [MAINTENANCE] Zep PostgresDatasource returns a list of batches. ([#6341](https://github.com/great-expectations/great_expectations/pull/6341))
* [MAINTENANCE] Refactor `usage_stats_opt_out` method in DataContext ([#5339](https://github.com/great-expectations/great_expectations/pull/5339))
* [MAINTENANCE] Fix computed metrics type hint in ExecutionEngine.resolve_metrics() method ([#6347](https://github.com/great-expectations/great_expectations/pull/6347))
* [MAINTENANCE] Subject: Support to include ID/PK in validation result for each row t… ([#5876](https://github.com/great-expectations/great_expectations/pull/5876)) (thanks @abekfenn)
* [MAINTENANCE] Pin `mypy` to `0.990` ([#6361](https://github.com/great-expectations/great_expectations/pull/6361))
* [MAINTENANCE] Misc cleanup of GX Cloud helpers ([#6352](https://github.com/great-expectations/great_expectations/pull/6352))
* [MAINTENANCE] Update column_reflection_fallback to also use schema name for Trino ([#6350](https://github.com/great-expectations/great_expectations/pull/6350))
* [MAINTENANCE] Bump version of `mypy` in contrib CLI ([#6370](https://github.com/great-expectations/great_expectations/pull/6370))
* [MAINTENANCE] Move config variable substitution logic into `ConfigurationProvider` ([#6345](https://github.com/great-expectations/great_expectations/pull/6345))
* [MAINTENANCE] Removes comment in code that was causing confusion to some users. ([#6366](https://github.com/great-expectations/great_expectations/pull/6366))
* [MAINTENANCE] minor metrics typing ([#6374](https://github.com/great-expectations/great_expectations/pull/6374))
* [MAINTENANCE] Make `ConfigurationProvider` and `ConfigurationSubstitutor` private ([#6375](https://github.com/great-expectations/great_expectations/pull/6375))
* [MAINTENANCE] Rename `GeCloudStoreBackend` to `GXCloudStoreBackend` ([#6377](https://github.com/great-expectations/great_expectations/pull/6377))
* [MAINTENANCE] Cleanup Metrics and ExecutionEngine methods ([#6371](https://github.com/great-expectations/great_expectations/pull/6371))
* [MAINTENANCE] F/great 1314/integrate zep in core ([#6358](https://github.com/great-expectations/great_expectations/pull/6358))
* [MAINTENANCE] Loosen `pydantic` version requirement ([#6384](https://github.com/great-expectations/great_expectations/pull/6384))

0.15.32
-----------------
* [BUGFIX] Patch broken `CloudNotificationAction` tests ([#6327](https://github.com/great-expectations/great_expectations/pull/6327))
* [BUGFIX] add create_temp_table flag to ExecutionEngineConfigSchema ([#6331](https://github.com/great-expectations/great_expectations/pull/6331)) (thanks @tommy-watts-depop)
* [BUGFIX] MapMetrics now return `partial_unexpected` values for `SUMMARY` format ([#6334](https://github.com/great-expectations/great_expectations/pull/6334))
* [DOCS] Re-writes "how to implement custom notifications" as "How to get Data Docs URLs for use in custom Validation Actions" ([#6281](https://github.com/great-expectations/great_expectations/pull/6281))
* [DOCS] Removes deprecated expectation notebook exploration doc ([#6298](https://github.com/great-expectations/great_expectations/pull/6298))
* [DOCS] Removes a number of unused & deprecated docs ([#6300](https://github.com/great-expectations/great_expectations/pull/6300))
* [DOCS] Prioritizes Onboarding Data Assistant in ToC ([#6302](https://github.com/great-expectations/great_expectations/pull/6302))
* [DOCS] Add ZenML into integration table in Readme ([#6144](https://github.com/great-expectations/great_expectations/pull/6144)) (thanks @dnth)
* [DOCS] add `pypi` release badge ([#6324](https://github.com/great-expectations/great_expectations/pull/6324))
* [MAINTENANCE] Remove unneeded `BaseDataContext.get_batch_list` ([#6291](https://github.com/great-expectations/great_expectations/pull/6291))
* [MAINTENANCE] Clean up implicit `Optional` errors flagged by `mypy` ([#6319](https://github.com/great-expectations/great_expectations/pull/6319))
* [MAINTENANCE] Add manual prod flags to core Expectations ([#6278](https://github.com/great-expectations/great_expectations/pull/6278))
* [MAINTENANCE] Fallback to isnot method if is_not is not available (old sqlalchemy) ([#6318](https://github.com/great-expectations/great_expectations/pull/6318))
* [MAINTENANCE] Add ZEP postgres datasource. ([#6274](https://github.com/great-expectations/great_expectations/pull/6274))
* [MAINTENANCE] Delete "metric_dependencies" from MetricConfiguration constructor arguments ([#6305](https://github.com/great-expectations/great_expectations/pull/6305))
* [MAINTENANCE] Clean up `DataContext` ([#6304](https://github.com/great-expectations/great_expectations/pull/6304))
* [MAINTENANCE] Deprecate `save_changes` flag on `Datasource` CRUD ([#6258](https://github.com/great-expectations/great_expectations/pull/6258))
* [MAINTENANCE] Deprecate `great_expectations.render.types` package ([#6315](https://github.com/great-expectations/great_expectations/pull/6315))
* [MAINTENANCE] Update range of allowable sqlalchemy versions ([#6328](https://github.com/great-expectations/great_expectations/pull/6328))
* [MAINTENANCE] Fixing checkpoint types ([#6325](https://github.com/great-expectations/great_expectations/pull/6325))
* [MAINTENANCE] Fix column_reflection_fallback for Trino and minor logging/testing improvements ([#6218](https://github.com/great-expectations/great_expectations/pull/6218))
* [MAINTENANCE] Change the number of expected Expectations in the 'quick check' stage of build_gallery pipeline ([#6333](https://github.com/great-expectations/great_expectations/pull/6333))

0.15.31
-----------------
* [BUGFIX] Include all requirement files in the sdist ([#6292](https://github.com/great-expectations/great_expectations/pull/6292)) (thanks @xhochy)
* [DOCS] Updates outdated batch_request snippet in Terms ([#6283](https://github.com/great-expectations/great_expectations/pull/6283))
* [DOCS] Update Conditional Expectations doc w/ current availability  ([#6279](https://github.com/great-expectations/great_expectations/pull/6279))
* [DOCS] Remove outdated Data Discovery page and all references ([#6288](https://github.com/great-expectations/great_expectations/pull/6288))
* [DOCS] Remove reference/evaluation_parameters page and all references ([#6294](https://github.com/great-expectations/great_expectations/pull/6294))
* [DOCS] Removing deprecated Custom Metrics doc ([#6282](https://github.com/great-expectations/great_expectations/pull/6282))
* [DOCS] Re-writes "how to implement custom notifications" as "How to get Data Docs URLs for use in custom Validation Actions" ([#6281](https://github.com/great-expectations/great_expectations/pull/6281))
* [DOCS] Removes deprecated expectation notebook exploration doc ([#6298](https://github.com/great-expectations/great_expectations/pull/6298))
* [MAINTENANCE] Move RuleState into rule directory. ([#6284](https://github.com/great-expectations/great_expectations/pull/6284))

0.15.30
-----------------
* [FEATURE] Add zep datasources to data context. ([#6255](https://github.com/great-expectations/great_expectations/pull/6255))
* [BUGFIX] Iterate through `GeCloudIdentifiers` to find the suite ID from the name ([#6243](https://github.com/great-expectations/great_expectations/pull/6243))
* [BUGFIX] Update default base url for cloud API ([#6176](https://github.com/great-expectations/great_expectations/pull/6176))
* [BUGFIX] Pin `termcolor` to below `2.1.0` due to breaking changes in lib's TTY parsing logic ([#6257](https://github.com/great-expectations/great_expectations/pull/6257))
* [BUGFIX] `InferredAssetSqlDataConnector` `include_schema_name` introspection of identical table names in different schemas ([#6166](https://github.com/great-expectations/great_expectations/pull/6166))
* [BUGFIX] Fix`docs-integration` tests, and temporarily pin `sqlalchemy` ([#6268](https://github.com/great-expectations/great_expectations/pull/6268))
* [BUGFIX] Fix serialization for contrib packages ([#6266](https://github.com/great-expectations/great_expectations/pull/6266))
* [BUGFIX] Ensure that `Datasource` credentials are not persisted to Cloud/disk ([#6254](https://github.com/great-expectations/great_expectations/pull/6254))
* [DOCS] Updates package contribution references ([#5885](https://github.com/great-expectations/great_expectations/pull/5885))
* [MAINTENANCE] Maintenance/great 1103/great 1318/alexsherstinsky/validation graph/refactor validation graph usage 2022 10 20 248 ([#6228](https://github.com/great-expectations/great_expectations/pull/6228))
* [MAINTENANCE] Refactor instances of `noqa: F821` Flake8 directive ([#6220](https://github.com/great-expectations/great_expectations/pull/6220))
* [MAINTENANCE] Logo URI ref in `data_docs` ([#6246](https://github.com/great-expectations/great_expectations/pull/6246))
* [MAINTENANCE] fix typos in docstrings ([#6247](https://github.com/great-expectations/great_expectations/pull/6247))
* [MAINTENANCE] Isolate Trino/MSSQL/MySQL tests in `dev` CI ([#6231](https://github.com/great-expectations/great_expectations/pull/6231))
* [MAINTENANCE] Split up `compatability` and `comprehensive` stages in `dev` CI to improve performance ([#6245](https://github.com/great-expectations/great_expectations/pull/6245))
* [MAINTENANCE] ZEP POC - Asset Type Registration ([#6194](https://github.com/great-expectations/great_expectations/pull/6194))
* [MAINTENANCE] Add Trino CLI support and bump Trino version ([#6215](https://github.com/great-expectations/great_expectations/pull/6215)) (thanks @hovaesco)
* [MAINTENANCE] Delete unneeded Rule attribute property ([#6264](https://github.com/great-expectations/great_expectations/pull/6264))
* [MAINTENANCE] Small clean-up of `Marshmallow` warnings (`missing` parameter changed to `load_default` as of 3.13) ([#6213](https://github.com/great-expectations/great_expectations/pull/6213))
* [MAINTENANCE] Move `.png` files out of project root ([#6249](https://github.com/great-expectations/great_expectations/pull/6249))
* [MAINTENANCE] Cleanup `expectation.py` attributes ([#6265](https://github.com/great-expectations/great_expectations/pull/6265))
* [MAINTENANCE] Further parallelize test runs in `dev` CI ([#6267](https://github.com/great-expectations/great_expectations/pull/6267))
* [MAINTENANCE] GCP Integration Pipeline fix ([#6259](https://github.com/great-expectations/great_expectations/pull/6259))
* [MAINTENANCE] mypy `warn_unused_ignores` ([#6270](https://github.com/great-expectations/great_expectations/pull/6270))
* [MAINTENANCE] ZEP - Datasource base class ([#6263](https://github.com/great-expectations/great_expectations/pull/6263))
* [MAINTENANCE] Reverting `marshmallow` version bump ([#6271](https://github.com/great-expectations/great_expectations/pull/6271))
* [MAINTENANCE] type hints cleanup in Rule-Based Profiler ([#6272](https://github.com/great-expectations/great_expectations/pull/6272))
* [MAINTENANCE] Remove unused f-strings ([#6248](https://github.com/great-expectations/great_expectations/pull/6248))
* [MAINTENANCE] Make ParameterBuilder.resolve_evaluation_dependencies() into instance (rather than utility) method ([#6273](https://github.com/great-expectations/great_expectations/pull/6273))
* [MAINTENANCE] Test definition for `ExpectColumnValueZScoresToBeLessThan` ([#6229](https://github.com/great-expectations/great_expectations/pull/6229))
* [MAINTENANCE] Make RuleState constructor argument ordering consistent with standard pattern. ([#6275](https://github.com/great-expectations/great_expectations/pull/6275))
* [MAINTENANCE] [REQUEST] Please allow Rachel to unblock blockers ([#6253](https://github.com/great-expectations/great_expectations/pull/6253))

0.15.29
-----------------
* [FEATURE] Add support to AWS Glue Data Catalog ([#5123](https://github.com/great-expectations/great_expectations/pull/5123)) (thanks @lccasagrande)
* [FEATURE] / Added pairwise expectation 'expect_column_pair_values_to_be_in_set' ([#6097](https://github.com/great-expectations/great_expectations/pull/6097)) (thanks @Arnavkar)
* [BUGFIX] Adjust condition in RenderedAtomicValueSchema.clean_null_attrs ([#6168](https://github.com/great-expectations/great_expectations/pull/6168))
* [BUGFIX] Add `py` to dev dependencies to circumvent compatability issues with `pytest==7.2.0` ([#6202](https://github.com/great-expectations/great_expectations/pull/6202))
* [BUGFIX] Fix `test_package_dependencies.py` to include `py` lib ([#6204](https://github.com/great-expectations/great_expectations/pull/6204))
* [BUGFIX] Fix logic in ExpectationDiagnostics._check_renderer_methods method ([#6208](https://github.com/great-expectations/great_expectations/pull/6208))
* [BUGFIX] Patch issue with empty config variables file raising `TypeError` ([#6216](https://github.com/great-expectations/great_expectations/pull/6216))
* [BUGFIX] Release patch for Azure env vars ([#6233](https://github.com/great-expectations/great_expectations/pull/6233))
* [BUGFIX] Cloud Data Context should overwrite existing suites based on `ge_cloud_id` instead of name ([#6234](https://github.com/great-expectations/great_expectations/pull/6234))
* [BUGFIX] Add env vars to Pytest min versions Azure stage ([#6239](https://github.com/great-expectations/great_expectations/pull/6239))
* [DOCS] doc-297: update the create Expectations overview page for Data Assistants ([#6212](https://github.com/great-expectations/great_expectations/pull/6212))
* [DOCS] DOC-378: bring example scripts for pandas configuration guide under test ([#6141](https://github.com/great-expectations/great_expectations/pull/6141))
* [MAINTENANCE] Add unit test for MetricsCalculator.get_metric() Method -- as an example template ([#6179](https://github.com/great-expectations/great_expectations/pull/6179))
* [MAINTENANCE] ZEP MetaDatasource POC ([#6178](https://github.com/great-expectations/great_expectations/pull/6178))
* [MAINTENANCE] Update `scope_check` in Azure CI to trigger on changed `.py` source code files ([#6185](https://github.com/great-expectations/great_expectations/pull/6185))
* [MAINTENANCE] Move test_yaml_config to a separate class ([#5487](https://github.com/great-expectations/great_expectations/pull/5487))
* [MAINTENANCE] Changed profiler to Data Assistant in CLI, docs, and tests ([#6189](https://github.com/great-expectations/great_expectations/pull/6189))
* [MAINTENANCE] Update default GE_USAGE_STATISTICS_URL in test docker image. ([#6192](https://github.com/great-expectations/great_expectations/pull/6192))
* [MAINTENANCE] Re-add a renamed test definition file ([#6182](https://github.com/great-expectations/great_expectations/pull/6182))
* [MAINTENANCE] Refactor method `parse_evaluation_parameter` ([#6191](https://github.com/great-expectations/great_expectations/pull/6191))
* [MAINTENANCE] Migrate methods from `BaseDataContext` to `AbstractDataContext` ([#6188](https://github.com/great-expectations/great_expectations/pull/6188))
* [MAINTENANCE] Rename cfe to v3_api ([#6190](https://github.com/great-expectations/great_expectations/pull/6190))
* [MAINTENANCE] Test Trino doc examples with test_script_runner.py ([#6198](https://github.com/great-expectations/great_expectations/pull/6198))
* [MAINTENANCE] Cleanup of Regex ParameterBuilder ([#6196](https://github.com/great-expectations/great_expectations/pull/6196))
* [MAINTENANCE] Apply static type checking to `expectation.py` ([#6173](https://github.com/great-expectations/great_expectations/pull/6173))
* [MAINTENANCE] Remove version matrix from `dev` CI pipeline to improve performance ([#6203](https://github.com/great-expectations/great_expectations/pull/6203))
* [MAINTENANCE] Rename `CloudMigrator.retry_unsuccessful_validations` ([#6206](https://github.com/great-expectations/great_expectations/pull/6206))
* [MAINTENANCE] Add validate_configuration method to expect_table_row_count_to_equal_other_table ([#6209](https://github.com/great-expectations/great_expectations/pull/6209))
* [MAINTENANCE] Replace deprecated `iteritems` with `items` ([#6205](https://github.com/great-expectations/great_expectations/pull/6205))
* [MAINTENANCE] Add instructions for setting up the test_ci database ([#6211](https://github.com/great-expectations/great_expectations/pull/6211))
* [MAINTENANCE] Add E2E tests for Cloud-backed `Datasource` CRUD ([#6186](https://github.com/great-expectations/great_expectations/pull/6186))
* [MAINTENANCE] Execution Engine linting & partial typing ([#6210](https://github.com/great-expectations/great_expectations/pull/6210))
* [MAINTENANCE] Test definition for `ExpectColumnValuesToBeJsonParsable`, including a fix for Spark ([#6207](https://github.com/great-expectations/great_expectations/pull/6207))
* [MAINTENANCE] Port over usage statistics enabled methods from `BaseDataContext` to `AbstractDataContext` ([#6201](https://github.com/great-expectations/great_expectations/pull/6201))
* [MAINTENANCE] Remove temporary dependency on `py` ([#6217](https://github.com/great-expectations/great_expectations/pull/6217))
* [MAINTENANCE] Adding type hints to DataAssistant implementations ([#6224](https://github.com/great-expectations/great_expectations/pull/6224))
* [MAINTENANCE] Remove AWS config file dependencies and use existing env vars in CI/CD ([#6227](https://github.com/great-expectations/great_expectations/pull/6227))
* [MAINTENANCE] Make `UsageStatsEvents` a `StrEnum` ([#6225](https://github.com/great-expectations/great_expectations/pull/6225))
* [MAINTENANCE] Move all `requirements-dev*.txt` files to separate dir ([#6223](https://github.com/great-expectations/great_expectations/pull/6223))
* [MAINTENANCE] Maintenance/great 1103/great 1318/alexsherstinsky/validation graph/refactor validation graph usage 2022 10 20 248 ([#6228](https://github.com/great-expectations/great_expectations/pull/6228))

0.15.28
-----------------
* [FEATURE] Initial zep datasource protocol. ([#6153](https://github.com/great-expectations/great_expectations/pull/6153))
* [FEATURE] Introduce BatchManager to manage Batch objects used by Validator and BatchData used by ExecutionEngine ([#6156](https://github.com/great-expectations/great_expectations/pull/6156))
* [FEATURE] Add support for Vertica dialect ([#6145](https://github.com/great-expectations/great_expectations/pull/6145)) (thanks @viplazylmht)
* [FEATURE] Introduce MetricsCalculator and Refactor Redundant Code out of Validator ([#6165](https://github.com/great-expectations/great_expectations/pull/6165))
* [BUGFIX] SQLAlchemy selectable Bug fix ([#6159](https://github.com/great-expectations/great_expectations/pull/6159)) (thanks @tommy-watts-depop)
* [BUGFIX] Parameterize usage stats endpoint in test dockerfile. ([#6169](https://github.com/great-expectations/great_expectations/pull/6169))
* [BUGFIX] B/great 1305/usage stats endpoint ([#6170](https://github.com/great-expectations/great_expectations/pull/6170))
* [BUGFIX] Ensure that spaces are recognized in named snippets ([#6172](https://github.com/great-expectations/great_expectations/pull/6172))
* [DOCS] Clarify wording for interactive mode in databricks ([#6154](https://github.com/great-expectations/great_expectations/pull/6154))
* [DOCS] fix source activate command ([#6161](https://github.com/great-expectations/great_expectations/pull/6161)) (thanks @JGrzywacz)
* [DOCS] Update version in `runtime.txt` to fix breaking Netlify builds ([#6181](https://github.com/great-expectations/great_expectations/pull/6181))
* [DOCS] Clean up snippets and line number validation in docs ([#6142](https://github.com/great-expectations/great_expectations/pull/6142))
* [MAINTENANCE] Add Enums for renderer types ([#6112](https://github.com/great-expectations/great_expectations/pull/6112))
* [MAINTENANCE] Minor cleanup in preparation for Validator refactoring into separate concerns ([#6155](https://github.com/great-expectations/great_expectations/pull/6155))
* [MAINTENANCE] add the internal `GE_DATA_CONTEXT_ID` env var to the docker file ([#6122](https://github.com/great-expectations/great_expectations/pull/6122))
* [MAINTENANCE] Rollback setting GE_DATA_CONTEXT_ID in docker image. ([#6163](https://github.com/great-expectations/great_expectations/pull/6163))
* [MAINTENANCE] disable ge_cloud_mode when specified, detect misconfiguration ([#6162](https://github.com/great-expectations/great_expectations/pull/6162))
* [MAINTENANCE] Re-add missing Expectations to gallery and include package names ([#6171](https://github.com/great-expectations/great_expectations/pull/6171))
* [MAINTENANCE] Use `from __future__ import annotations` to clean up type hints ([#6127](https://github.com/great-expectations/great_expectations/pull/6127))
* [MAINTENANCE] Make sure that quick stage check returns 0 if there are no problems ([#6177](https://github.com/great-expectations/great_expectations/pull/6177))
* [MAINTENANCE] Remove SQL for expect_column_discrete_entropy_to_be_between ([#6180](https://github.com/great-expectations/great_expectations/pull/6180))

0.15.27
-----------------
* [FEATURE] Add logging/warnings to GX Cloud migration process ([#6106](https://github.com/great-expectations/great_expectations/pull/6106))
* [FEATURE] Introduction of updated `gx.get_context()` method that returns correct DataContext-type ([#6104](https://github.com/great-expectations/great_expectations/pull/6104))
* [FEATURE] Contribute StatisticsDataAssistant and GrowthNumericDataAssistant (both experimental)  ([#6115](https://github.com/great-expectations/great_expectations/pull/6115))
* [BUGFIX] add OBJECT_TYPE_NAMES to the JsonSchemaProfiler - issue [#6109](https://github.com/great-expectations/great_expectations/pull/6109) ([#6110](https://github.com/great-expectations/great_expectations/pull/6110)) (thanks @OphelieC)
* [BUGFIX] Fix example `Set-Based Column Map Expectation` template import ([#6134](https://github.com/great-expectations/great_expectations/pull/6134))
* [BUGFIX] Regression due to `GESqlDialect` `Enum` for Hive ([#6149](https://github.com/great-expectations/great_expectations/pull/6149))
* [DOCS] Support for named snippets in documentation ([#6087](https://github.com/great-expectations/great_expectations/pull/6087))
* [MAINTENANCE] Clean up `test_migrate=True` Cloud migrator output ([#6119](https://github.com/great-expectations/great_expectations/pull/6119))
* [MAINTENANCE] Creation of Hackathon Packages ([#4587](https://github.com/great-expectations/great_expectations/pull/4587))
* [MAINTENANCE] Rename GCP Integration Pipeline ([#6121](https://github.com/great-expectations/great_expectations/pull/6121))
* [MAINTENANCE] Change log levels used in `CloudMigrator` ([#6125](https://github.com/great-expectations/great_expectations/pull/6125))
* [MAINTENANCE] Bump version of `sqlalchemy-redshift` from `0.7.7` to `0.8.8` ([#6082](https://github.com/great-expectations/great_expectations/pull/6082))
* [MAINTENANCE] self_check linting & initial type-checking ([#6126](https://github.com/great-expectations/great_expectations/pull/6126))
* [MAINTENANCE] Update per Clickhouse multiple same aliases Bug ([#6128](https://github.com/great-expectations/great_expectations/pull/6128)) (thanks @adammrozik)
* [MAINTENANCE] Only update existing `rendered_content` if rendering does not fail with new `InlineRenderer` failure message ([#6091](https://github.com/great-expectations/great_expectations/pull/6091))

0.15.26
-----------------
* [FEATURE] Enable sending of `ConfigurationBundle` payload in HTTP request to Cloud backend ([#6083](https://github.com/great-expectations/great_expectations/pull/6083))
* [FEATURE] Send user validation results to Cloud backend during migration ([#6102](https://github.com/great-expectations/great_expectations/pull/6102))
* [BUGFIX] Fix bigquery crash when using "in" with a boolean column ([#6071](https://github.com/great-expectations/great_expectations/pull/6071))
* [BUGFIX] Fix serialization error when rendering kl_divergence ([#6084](https://github.com/great-expectations/great_expectations/pull/6084)) (thanks @roblim)
* [BUGFIX] Enable top-level parameters in Data Assistants accessed via dispatcher ([#6077](https://github.com/great-expectations/great_expectations/pull/6077))
* [BUGFIX] Patch issue around `DataContext.save_datasource` not sending `class_name` in result payload ([#6108](https://github.com/great-expectations/great_expectations/pull/6108))
* [DOCS] DOC-377 add missing dictionary in configured asset datasource portion of Pandas and Spark configuration guides ([#6081](https://github.com/great-expectations/great_expectations/pull/6081))
* [DOCS] DOC-376 finalize definition for Data Assistants in technical terms ([#6080](https://github.com/great-expectations/great_expectations/pull/6080))
* [DOCS] Update `docs-integration` test due to new `whole_table` splitter behavior ([#6103](https://github.com/great-expectations/great_expectations/pull/6103))
* [DOCS] How to create a Custom Multicolumn Map Expectation ([#6101](https://github.com/great-expectations/great_expectations/pull/6101))
* [MAINTENANCE] Patch broken Cloud E2E test ([#6079](https://github.com/great-expectations/great_expectations/pull/6079))
* [MAINTENANCE] Bundle data context config and other artifacts for migration ([#6068](https://github.com/great-expectations/great_expectations/pull/6068))
* [MAINTENANCE] Add datasources to ConfigurationBundle ([#6092](https://github.com/great-expectations/great_expectations/pull/6092))
* [MAINTENANCE] Remove unused config files from root of GX repo ([#6090](https://github.com/great-expectations/great_expectations/pull/6090))
* [MAINTENANCE] Add `data_context_id` property to `ConfigurationBundle` ([#6094](https://github.com/great-expectations/great_expectations/pull/6094))
* [MAINTENANCE] Move all Cloud migrator logic to separate directory ([#6100](https://github.com/great-expectations/great_expectations/pull/6100))
* [MAINTENANCE] Update aloglia scripts for new fields and replica indices ([#6049](https://github.com/great-expectations/great_expectations/pull/6049)) (thanks @winrp17)
* [MAINTENANCE] initial Datasource typings ([#6099](https://github.com/great-expectations/great_expectations/pull/6099))
* [MAINTENANCE] Data context migrate to cloud event ([#6095](https://github.com/great-expectations/great_expectations/pull/6095))
* [MAINTENANCE] Bundling tests with empty context configs ([#6107](https://github.com/great-expectations/great_expectations/pull/6107))
* [MAINTENANCE] Fixing a typo ([#6113](https://github.com/great-expectations/great_expectations/pull/6113))

0.15.25
-----------------
* [FEATURE] Since value set in expectation kwargs is list of strings, do not emit expect_column_values_to_be_in_set for datetime valued columns ([#6046](https://github.com/great-expectations/great_expectations/pull/6046))
* [FEATURE] add failed expectations list to slack message ([#5812](https://github.com/great-expectations/great_expectations/pull/5812)) (thanks @itaise)
* [FEATURE] Enable only ExactNumericRangeEstimator and QuantilesNumericRangeEstimator in "datetime_columns_rule" of OnboardingDataAssistant ([#6063](https://github.com/great-expectations/great_expectations/pull/6063))
* [BUGFIX] numpy typing behind `if TYPE_CHECKING` ([#6076](https://github.com/great-expectations/great_expectations/pull/6076))
* [DOCS] Update "How to create an Expectation Suite with the Onboarding Data Assistant" ([#6050](https://github.com/great-expectations/great_expectations/pull/6050))
* [DOCS] How to get one or more Batches of data from a configured Datasource ([#6043](https://github.com/great-expectations/great_expectations/pull/6043))
* [DOCS] DOC-298 Data Assistant technical term page ([#6057](https://github.com/great-expectations/great_expectations/pull/6057))
* [DOCS] Update OnboardingDataAssistant documentation ([#6059](https://github.com/great-expectations/great_expectations/pull/6059))
* [MAINTENANCE] Clean up of DataAssistant tests that depend on Jupyter notebooks ([#6039](https://github.com/great-expectations/great_expectations/pull/6039))
* [MAINTENANCE] AbstractDataContext.datasource_save() test simplifications ([#6052](https://github.com/great-expectations/great_expectations/pull/6052))
* [MAINTENANCE] Rough architecture for cloud migration tool ([#6054](https://github.com/great-expectations/great_expectations/pull/6054))
* [MAINTENANCE] Include git commit info when building docker image. ([#6060](https://github.com/great-expectations/great_expectations/pull/6060))
* [MAINTENANCE] Allow `CloudDataContext` to retrieve and initialize its own project config ([#6006](https://github.com/great-expectations/great_expectations/pull/6006))
* [MAINTENANCE] Removing Jupyter notebook-based tests for DataAssistants ([#6062](https://github.com/great-expectations/great_expectations/pull/6062))
* [MAINTENANCE] pinned dremio, fixed linting ([#6067](https://github.com/great-expectations/great_expectations/pull/6067))
* [MAINTENANCE] usage-stats, & utils.py typing ([#5925](https://github.com/great-expectations/great_expectations/pull/5925))
* [MAINTENANCE] Refactor external HTTP request logic into a `Session` factory function ([#6007](https://github.com/great-expectations/great_expectations/pull/6007))
* [MAINTENANCE] Remove tag validity stage from release pipeline ([#6069](https://github.com/great-expectations/great_expectations/pull/6069))
* [MAINTENANCE] Remove unused test fixtures from test suite ([#6058](https://github.com/great-expectations/great_expectations/pull/6058))
* [MAINTENANCE] Remove outdated release files ([#6074](https://github.com/great-expectations/great_expectations/pull/6074))

0.15.24
-----------------
* [FEATURE] context.save_datasource ([#6009](https://github.com/great-expectations/great_expectations/pull/6009))
* [BUGFIX] Standardize `ConfiguredAssetSqlDataConnector` config in `datasource new` CLI workflow ([#6044](https://github.com/great-expectations/great_expectations/pull/6044))
* [DOCS] DOC-371 update the getting started tutorial for data assistants ([#6024](https://github.com/great-expectations/great_expectations/pull/6024))
* [DOCS] DOCS-369 sql data connector configuration guide ([#6002](https://github.com/great-expectations/great_expectations/pull/6002))
* [MAINTENANCE] Remove outdated entry from release schedule JSON ([#6032](https://github.com/great-expectations/great_expectations/pull/6032))
* [MAINTENANCE] Clean up Spark schema tests to have proper names ([#6033](https://github.com/great-expectations/great_expectations/pull/6033))

0.15.23
-----------------
* [FEATURE] do not require expectation_suite_name in DataAssistantResult.show_expectations_by...() methods ([#5976](https://github.com/great-expectations/great_expectations/pull/5976))
* [FEATURE] Refactor PartitionParameterBuilder into dedicated ValueCountsParameterBuilder and HistogramParameterBuilder ([#5975](https://github.com/great-expectations/great_expectations/pull/5975))
* [FEATURE] Implement default sorting for batches based on selected splitter method ([#5924](https://github.com/great-expectations/great_expectations/pull/5924))
* [FEATURE] Make OnboardingDataAssistant default profiler in CLI SUITE NEW ([#6012](https://github.com/great-expectations/great_expectations/pull/6012))
* [FEATURE] Enable omission of rounding of decimals in NumericMetricRangeMultiBatchParameterBuilder ([#6017](https://github.com/great-expectations/great_expectations/pull/6017))
* [FEATURE] Enable non-default sorters for `ConfiguredAssetSqlDataConnector` ([#5993](https://github.com/great-expectations/great_expectations/pull/5993))
* [FEATURE] Data Assistant plot method indication of total metrics and expectations count ([#6016](https://github.com/great-expectations/great_expectations/pull/6016))
* [BUGFIX] Addresses issue with ExpectCompoundColumnsToBeUnique renderer ([#5970](https://github.com/great-expectations/great_expectations/pull/5970))
* [BUGFIX] Fix failing `run_profiler_notebook` test ([#5983](https://github.com/great-expectations/great_expectations/pull/5983))
* [BUGFIX] Handle case when only one unique "column.histogram" bin value is found ([#5987](https://github.com/great-expectations/great_expectations/pull/5987))
* [BUGFIX] Update `get_validator` test assertions due to change in fixture batches ([#5989](https://github.com/great-expectations/great_expectations/pull/5989))
* [BUGFIX] Fix use of column.partition metric in HistogramSingleBatchParameterBuilder to more accurately handle errors ([#5990](https://github.com/great-expectations/great_expectations/pull/5990))
* [BUGFIX] Make Spark implementation of "column.value_counts" metric more robust to None/NaN column values ([#5996](https://github.com/great-expectations/great_expectations/pull/5996))
* [BUGFIX] Filter out np.nan values (just like None values) as part of ColumnValueCounts._spark() implementation ([#5998](https://github.com/great-expectations/great_expectations/pull/5998))
* [BUGFIX] Handle case when only one unique "column.histogram" bin value is found with proper type casting ([#6001](https://github.com/great-expectations/great_expectations/pull/6001))
* [BUGFIX] ColumnMedian._sqlalchemy() needs to handle case of single-value column ([#6011](https://github.com/great-expectations/great_expectations/pull/6011))
* [BUGFIX] Patch broken `save_expectation_suite` behavior with Cloud-backed `DataContext` ([#6004](https://github.com/great-expectations/great_expectations/pull/6004))
* [BUGFIX] Clean quantitative metrics DataFrames in Data Assistant plotting ([#6023](https://github.com/great-expectations/great_expectations/pull/6023))
* [BUGFIX] Defer `pprint` in `ExpectationSuite.show_expectations_by_expectation_type()` due to Jupyter rate limit ([#6026](https://github.com/great-expectations/great_expectations/pull/6026))
* [BUGFIX] Use UTC TimeZone (rather than Local Time Zone) for Rule-Based Profiler DateTime Conversions ([#6028](https://github.com/great-expectations/great_expectations/pull/6028))
* [DOCS] Update snippet refs in "How to create an Expectation Suite with the Onboarding Data Assistant" ([#6014](https://github.com/great-expectations/great_expectations/pull/6014))
* [MAINTENANCE] Randomize the non-comprehensive tests ([#5968](https://github.com/great-expectations/great_expectations/pull/5968))
* [MAINTENANCE] DatasourceStore refactoring ([#5941](https://github.com/great-expectations/great_expectations/pull/5941))
* [MAINTENANCE] Expectation suite init unit tests + types ([#5957](https://github.com/great-expectations/great_expectations/pull/5957))
* [MAINTENANCE] Expectation suite new unit tests for add_citation ([#5966](https://github.com/great-expectations/great_expectations/pull/5966))
* [MAINTENANCE] Updated release schedule ([#5977](https://github.com/great-expectations/great_expectations/pull/5977))
* [MAINTENANCE] Unit tests for `CheckpointStore` ([#5967](https://github.com/great-expectations/great_expectations/pull/5967))
* [MAINTENANCE] Enhance unit tests for ExpectationSuite.isEquivalentTo ([#5979](https://github.com/great-expectations/great_expectations/pull/5979))
* [MAINTENANCE] Remove unused fixtures from test suite ([#5965](https://github.com/great-expectations/great_expectations/pull/5965))
* [MAINTENANCE] Update to MultiBatch Notebook to include Configured - Sql ([#5945](https://github.com/great-expectations/great_expectations/pull/5945))
* [MAINTENANCE] Update to MultiBatch Notebook to include Inferred - Sql  ([#5958](https://github.com/great-expectations/great_expectations/pull/5958))
* [MAINTENANCE] Add reverse assertion for isEquivalentTo tests ([#5982](https://github.com/great-expectations/great_expectations/pull/5982))
* [MAINTENANCE] Unit test enhancements ExpectationSuite.__eq__() ([#5984](https://github.com/great-expectations/great_expectations/pull/5984))
* [MAINTENANCE] Refactor `DataContext.__init__` to move Cloud-specific logic to `CloudDataContext` ([#5981](https://github.com/great-expectations/great_expectations/pull/5981))
* [MAINTENANCE] Set up cloud integration tests with Azure Pipelines ([#5995](https://github.com/great-expectations/great_expectations/pull/5995))
* [MAINTENANCE] Example of `splitter_method` at `Asset` and `DataConnector` level ([#6000](https://github.com/great-expectations/great_expectations/pull/6000))
* [MAINTENANCE] Replace `splitter_method` strings with `SplitterMethod` Enum and leverage `GESqlDialect` Enum where applicable ([#5980](https://github.com/great-expectations/great_expectations/pull/5980))
* [MAINTENANCE] Ensure that `DataContext.add_datasource` works with nested `DataConnector` ids ([#5992](https://github.com/great-expectations/great_expectations/pull/5992))
* [MAINTENANCE] Remove cloud integration tests from azure-pipelines.yml ([#5997](https://github.com/great-expectations/great_expectations/pull/5997))
* [MAINTENANCE] Unit tests for `GeCloudStoreBackend` ([#5999](https://github.com/great-expectations/great_expectations/pull/5999))
* [MAINTENANCE] Parameterize pg hostname in jupyter notebooks ([#6005](https://github.com/great-expectations/great_expectations/pull/6005))
* [MAINTENANCE] Unit tests for `Validator` ([#5988](https://github.com/great-expectations/great_expectations/pull/5988))
* [MAINTENANCE] Add unit tests for SimpleSqlalchemyDatasource ([#6008](https://github.com/great-expectations/great_expectations/pull/6008))
* [MAINTENANCE] Remove `dgtest` from dev pipeline ([#6003](https://github.com/great-expectations/great_expectations/pull/6003))
* [MAINTENANCE] Remove deprecated `account_id` from GX Cloud integrations ([#6010](https://github.com/great-expectations/great_expectations/pull/6010))
* [MAINTENANCE] Added perf considerations to onboarding assistant notebook ([#6022](https://github.com/great-expectations/great_expectations/pull/6022))
* [MAINTENANCE] Redshift specific temp table code path ([#6021](https://github.com/great-expectations/great_expectations/pull/6021))
* [MAINTENANCE] Update `datasource new` workflow to enable `ConfiguredAssetDataConnector` usage with SQL-backed `Datasources` ([#6019](https://github.com/great-expectations/great_expectations/pull/6019))

0.15.22
-----------------
* [FEATURE] Allowing `schema`  to be passed in as `batch_spec_passthrough` in Spark ([#5900](https://github.com/great-expectations/great_expectations/pull/5900))
* [FEATURE] DataAssistants Example Notebook - Spark ([#5919](https://github.com/great-expectations/great_expectations/pull/5919))
* [FEATURE] Improve slack error condition ([#5818](https://github.com/great-expectations/great_expectations/pull/5818)) (thanks @itaise)
* [BUGFIX] Ensure that ParameterBuilder implementations in Rule Based Profiler properly handle SQL DECIMAL type ([#5896](https://github.com/great-expectations/great_expectations/pull/5896))
* [BUGFIX] Making an all-NULL column handling in RuleBasedProfiler more robust ([#5937](https://github.com/great-expectations/great_expectations/pull/5937))
* [BUGFIX] Don't include abstract Expectation classes in _retrieve_expectations_from_module ([#5947](https://github.com/great-expectations/great_expectations/pull/5947))
* [BUGFIX] Data Assistant plotting with zero expectations produced ([#5934](https://github.com/great-expectations/great_expectations/pull/5934))
* [BUGFIX] prefix and suffix asset names are only relevant for InferredSqlAlchemyDataConnector ([#5950](https://github.com/great-expectations/great_expectations/pull/5950))
* [BUGFIX] Prevent "division by zero" errors in Rule-Based Profiler calculations when Batch has zero rows ([#5960](https://github.com/great-expectations/great_expectations/pull/5960))
* [BUGFIX] Spark column.distinct_values no longer returns entire table distinct values ([#5969](https://github.com/great-expectations/great_expectations/pull/5969))
* [DOCS] DOC-368 spelling correction ([#5912](https://github.com/great-expectations/great_expectations/pull/5912))
* [MAINTENANCE] Mark all tests within `tests/data_context/stores` dir ([#5913](https://github.com/great-expectations/great_expectations/pull/5913))
* [MAINTENANCE] Cleanup to allow docker test target to run tests in random order ([#5915](https://github.com/great-expectations/great_expectations/pull/5915))
* [MAINTENANCE] Use datasource config in add_datasource support methods ([#5901](https://github.com/great-expectations/great_expectations/pull/5901))
* [MAINTENANCE] Cleanup up some new datasource sql data connector tests. ([#5918](https://github.com/great-expectations/great_expectations/pull/5918))
* [MAINTENANCE] Unit tests for `data_context/store` ([#5923](https://github.com/great-expectations/great_expectations/pull/5923))
* [MAINTENANCE] Mark all tests within `tests/validator` ([#5926](https://github.com/great-expectations/great_expectations/pull/5926))
* [MAINTENANCE]  Certify InferredAssetSqlDataConnector and ConfiguredAssetSqlDataConnector ([#5847](https://github.com/great-expectations/great_expectations/pull/5847))
* [MAINTENANCE] Mark DBFS tests with `@pytest.mark.integration` ([#5931](https://github.com/great-expectations/great_expectations/pull/5931))
* [MAINTENANCE] Reset globals modified in tests ([#5936](https://github.com/great-expectations/great_expectations/pull/5936))
* [MAINTENANCE] Move `Store` test utils from source code to tests ([#5932](https://github.com/great-expectations/great_expectations/pull/5932))
* [MAINTENANCE] Mark tests within `tests/rule_based_profiler` ([#5930](https://github.com/great-expectations/great_expectations/pull/5930))
* [MAINTENANCE] Add missing import for ConfigurationIdentifier ([#5943](https://github.com/great-expectations/great_expectations/pull/5943))
* [MAINTENANCE] Update to OnboardingDataAssistant Notebook - Sql ([#5939](https://github.com/great-expectations/great_expectations/pull/5939))
* [MAINTENANCE] Run comprehensive tests in a random order ([#5942](https://github.com/great-expectations/great_expectations/pull/5942))
* [MAINTENANCE] Unit tests for `ConfigurationStore` ([#5948](https://github.com/great-expectations/great_expectations/pull/5948))
* [MAINTENANCE] Add a dev-tools requirements option ([#5944](https://github.com/great-expectations/great_expectations/pull/5944))
* [MAINTENANCE] Run spark and onboarding data assistant test in their own jobs. ([#5951](https://github.com/great-expectations/great_expectations/pull/5951))
* [MAINTENANCE] Unit tests for `ValidationGraph` and related classes ([#5954](https://github.com/great-expectations/great_expectations/pull/5954))
* [MAINTENANCE] More unit tests for `Stores`  ([#5953](https://github.com/great-expectations/great_expectations/pull/5953))
* [MAINTENANCE] Add x-fails to flaky Cloud tests for purposes of 0.15.22 ([#5964](https://github.com/great-expectations/great_expectations/pull/5964))
* [MAINTENANCE] Bump `Marshmallow` upper bound to work with Airflow operator ([#5952](https://github.com/great-expectations/great_expectations/pull/5952))
* [MAINTENANCE] Use DataContext to ignore progress bars ([#5959](https://github.com/great-expectations/great_expectations/pull/5959))

0.15.21
-----------------
* [FEATURE] Add `include_rendered_content` to `get_expectation_suite` and `get_validation_result` ([#5853](https://github.com/great-expectations/great_expectations/pull/5853))
* [FEATURE] Add tags as an optional setting for the OpsGenieAlertAction ([#5855](https://github.com/great-expectations/great_expectations/pull/5855)) (thanks @stevewb1993)
* [BUGFIX] Ensure that `delete_expectation_suite` returns proper boolean result ([#5878](https://github.com/great-expectations/great_expectations/pull/5878))
* [BUGFIX] many small bugfixes ([#5881](https://github.com/great-expectations/great_expectations/pull/5881))
* [BUGFIX] Fix typo in default value of "ignore_row_if" kwarg for MulticolumnMapExpectation ([#5860](https://github.com/great-expectations/great_expectations/pull/5860)) (thanks @mkopec87)
* [BUGFIX] Patch issue with `checkpoint_identifier` within `Checkpoint.run` workflow ([#5894](https://github.com/great-expectations/great_expectations/pull/5894))
* [BUGFIX] Ensure that `DataContext.add_checkpoint()` updates existing objects in GX Cloud ([#5895](https://github.com/great-expectations/great_expectations/pull/5895))
* [DOCS] DOC-364 how to configure a spark datasource ([#5840](https://github.com/great-expectations/great_expectations/pull/5840))
* [MAINTENANCE] Unit Tests Pipeline step ([#5838](https://github.com/great-expectations/great_expectations/pull/5838))
* [MAINTENANCE] Unit tests to ensure coverage over `Datasource` caching in `DataContext` ([#5839](https://github.com/great-expectations/great_expectations/pull/5839))
* [MAINTENANCE] Add entries to release schedule ([#5833](https://github.com/great-expectations/great_expectations/pull/5833))
* [MAINTENANCE] Properly label `DataAssistant` tests with `@pytest.mark.integration` ([#5845](https://github.com/great-expectations/great_expectations/pull/5845))
* [MAINTENANCE] Add additional unit tests around `Datasource` caching ([#5844](https://github.com/great-expectations/great_expectations/pull/5844))
* [MAINTENANCE] Mark miscellaneous tests with `@pytest.mark.unit` ([#5846](https://github.com/great-expectations/great_expectations/pull/5846))
* [MAINTENANCE] `datasource`, `data_context`, `core` typing, lint fixes ([#5824](https://github.com/great-expectations/great_expectations/pull/5824))
* [MAINTENANCE] add --ignore-suppress and --ignore-only-for to build_gallery.py with bugfixes ([#5802](https://github.com/great-expectations/great_expectations/pull/5802))
* [MAINTENANCE] Remove pyparsing pin for <3.0 ([#5849](https://github.com/great-expectations/great_expectations/pull/5849))
* [MAINTENANCE] Finer type exclude ([#5848](https://github.com/great-expectations/great_expectations/pull/5848))
* [MAINTENANCE] use `id` instead `id_`  ([#5775](https://github.com/great-expectations/great_expectations/pull/5775))
* [MAINTENANCE] Add data connector names in datasource config ([#5778](https://github.com/great-expectations/great_expectations/pull/5778))
* [MAINTENANCE] init tests for dict and json serializers ([#5854](https://github.com/great-expectations/great_expectations/pull/5854))
* [MAINTENANCE] Remove Partitioning and Quantiles metrics computations from DateTime Rule of OnboardingDataAssistant ([#5862](https://github.com/great-expectations/great_expectations/pull/5862))
* [MAINTENANCE] Update `ExpectationSuite` CRUD on `DataContext` to recognize Cloud ids ([#5836](https://github.com/great-expectations/great_expectations/pull/5836))
* [MAINTENANCE] Handle Pandas warnings in Data Assistant plots ([#5863](https://github.com/great-expectations/great_expectations/pull/5863))
* [MAINTENANCE] Misc cleanup of `test_expectation_suite_crud.py` ([#5868](https://github.com/great-expectations/great_expectations/pull/5868))
* [MAINTENANCE] Remove vendored `marshmallow__shade` ([#5866](https://github.com/great-expectations/great_expectations/pull/5866))
* [MAINTENANCE] don't force using the stand alone mock ([#5871](https://github.com/great-expectations/great_expectations/pull/5871))
* [MAINTENANCE] Update expectation_gallery pipeline ([#5874](https://github.com/great-expectations/great_expectations/pull/5874))
* [MAINTENANCE] run unit-tests on a target package ([#5869](https://github.com/great-expectations/great_expectations/pull/5869))
* [MAINTENANCE] add `pytest-timeout` ([#5857](https://github.com/great-expectations/great_expectations/pull/5857))
* [MAINTENANCE] Label tests in `tests/core` with `@pytest.mark.unit` and `@pytest.mark.integration` ([#5879](https://github.com/great-expectations/great_expectations/pull/5879))
* [MAINTENANCE] new invoke test flags ([#5880](https://github.com/great-expectations/great_expectations/pull/5880))
* [MAINTENANCE] JSON Serialize RowCondition and MetricBundle computation result to enable IDDict.to_id() for SparkDFExecutionEngine ([#5883](https://github.com/great-expectations/great_expectations/pull/5883))
* [MAINTENANCE] increase the `pytest-timeout` timeout value during unit-testing step ([#5884](https://github.com/great-expectations/great_expectations/pull/5884))
* [MAINTENANCE] Add `@pytest.mark.slow` throughout test suite ([#5882](https://github.com/great-expectations/great_expectations/pull/5882))
* [MAINTENANCE] Add test_expectation_suite_send_usage_message ([#5886](https://github.com/great-expectations/great_expectations/pull/5886))
* [MAINTENANCE] Mark existing tests as unit or integration ([#5890](https://github.com/great-expectations/great_expectations/pull/5890))
* [MAINTENANCE] Convert integration tests to unit ([#5891](https://github.com/great-expectations/great_expectations/pull/5891))
* [MAINTENANCE] Update distinct metric dependencies and implementations ([#5811](https://github.com/great-expectations/great_expectations/pull/5811))
* [MAINTENANCE] Add slow pytest marker to config and sort them alphabetically. ([#5892](https://github.com/great-expectations/great_expectations/pull/5892))
* [MAINTENANCE] Adding serialization tests for Spark ([#5897](https://github.com/great-expectations/great_expectations/pull/5897))
* [MAINTENANCE] Improve existing expectation suite unit tests (phase 1) ([#5898](https://github.com/great-expectations/great_expectations/pull/5898))
* [MAINTENANCE] `SqlAlchemyExecutionEngine` case for SQL Alchemy `Select` and `TextualSelect` due to `SADeprecationWarning` ([#5902](https://github.com/great-expectations/great_expectations/pull/5902))

0.15.20
-----------------
* [FEATURE] `query.pair_column` Metric ([#5743](https://github.com/great-expectations/great_expectations/pull/5743))
* [FEATURE] Enhance execution time measurement utility, and save `DomainBuilder` execution time per Rule of Rule-Based Profiler ([#5796](https://github.com/great-expectations/great_expectations/pull/5796))
* [FEATURE] Support single-batch mode in MetricMultiBatchParameterBuilder ([#5808](https://github.com/great-expectations/great_expectations/pull/5808))
* [FEATURE] Inline `ExpectationSuite` Rendering ([#5726](https://github.com/great-expectations/great_expectations/pull/5726))
* [FEATURE] Better error for missing expectation ([#5750](https://github.com/great-expectations/great_expectations/pull/5750)) (thanks @tylertrussell)
* [FEATURE] DataAssistants Example Notebook - Pandas ([#5820](https://github.com/great-expectations/great_expectations/pull/5820))
* [BUGFIX] Ensure name not persisted ([#5813](https://github.com/great-expectations/great_expectations/pull/5813))
* [DOCS] Change the selectable to a list ([#5780](https://github.com/great-expectations/great_expectations/pull/5780)) (thanks @itaise)
* [DOCS] Fix how to create custom table expectation ([#5807](https://github.com/great-expectations/great_expectations/pull/5807)) (thanks @itaise)
* [DOCS] DOC-363 how to configure a pandas datasource ([#5779](https://github.com/great-expectations/great_expectations/pull/5779))
* [MAINTENANCE] Remove xfail markers on cloud tests ([#5793](https://github.com/great-expectations/great_expectations/pull/5793))
* [MAINTENANCE] build-gallery enhancements ([#5616](https://github.com/great-expectations/great_expectations/pull/5616))
* [MAINTENANCE] Refactor `save_profiler` to remove explicit `name` and `ge_cloud_id` args ([#5792](https://github.com/great-expectations/great_expectations/pull/5792))
* [MAINTENANCE] Add v2_api flag for v2_api specific tests ([#5803](https://github.com/great-expectations/great_expectations/pull/5803))
* [MAINTENANCE] Clean up `ge_cloud_id` reference from `DataContext` `ExpectationSuite` CRUD ([#5791](https://github.com/great-expectations/great_expectations/pull/5791))
* [MAINTENANCE] Refactor convert_dictionary_to_parameter_node ([#5805](https://github.com/great-expectations/great_expectations/pull/5805))
* [MAINTENANCE] Remove `ge_cloud_id` from `DataContext.add_profiler()` signature ([#5804](https://github.com/great-expectations/great_expectations/pull/5804))
* [MAINTENANCE] Remove "copy.deepcopy()" calls from ValidationGraph ([#5809](https://github.com/great-expectations/great_expectations/pull/5809))
* [MAINTENANCE] Add vectorized is_between for common numpy dtypes ([#5711](https://github.com/great-expectations/great_expectations/pull/5711))
* [MAINTENANCE] Make partitioning directives of PartitionParameterBuilder configurable ([#5810](https://github.com/great-expectations/great_expectations/pull/5810))
* [MAINTENANCE] Write E2E Cloud test for `RuleBasedProfiler` creation and retrieval ([#5815](https://github.com/great-expectations/great_expectations/pull/5815))
* [MAINTENANCE] Change recursion to iteration for function in parameter_container.py ([#5817](https://github.com/great-expectations/great_expectations/pull/5817))
* [MAINTENANCE] add `pytest-mock` & `pytest-icdiff` plugins ([#5819](https://github.com/great-expectations/great_expectations/pull/5819))
* [MAINTENANCE] Surface cloud errors ([#5797](https://github.com/great-expectations/great_expectations/pull/5797))
* [MAINTENANCE] Clean up build_parameter_container_for_variables ([#5823](https://github.com/great-expectations/great_expectations/pull/5823))
* [MAINTENANCE] Bugfix/snowflake temp table schema name ([#5814](https://github.com/great-expectations/great_expectations/pull/5814))
* [MAINTENANCE] Update `list_` methods on `DataContext` to emit names along with object ids ([#5826](https://github.com/great-expectations/great_expectations/pull/5826))
* [MAINTENANCE] xfail Cloud E2E tests due to schema issue with `DataContextVariables` ([#5828](https://github.com/great-expectations/great_expectations/pull/5828))
* [MAINTENANCE] Clean up xfails in preparation for 0.15.20 release ([#5835](https://github.com/great-expectations/great_expectations/pull/5835))
* [MAINTENANCE] Add back xfails for E2E Cloud tests that fail on env var retrieval in Docker ([#5837](https://github.com/great-expectations/great_expectations/pull/5837))

0.15.19
-----------------
* [FEATURE] `DataAssistantResult` plot multiple metrics per expectation ([#5556](https://github.com/great-expectations/great_expectations/pull/5556))
* [FEATURE] Enable passing "exact_estimation" boolean at `DataAssistant.run()` level (default value is True) ([#5744](https://github.com/great-expectations/great_expectations/pull/5744))
* [FEATURE] Example notebook for Onboarding DataAssistant - `postgres` ([#5776](https://github.com/great-expectations/great_expectations/pull/5776))
* [BUGFIX] dir update for data_assistant_result ([#5751](https://github.com/great-expectations/great_expectations/pull/5751))
* [BUGFIX] Fix docs_integration pipeline ([#5734](https://github.com/great-expectations/great_expectations/pull/5734))
* [BUGFIX] Patch flaky E2E Cloud test with randomized suite names ([#5752](https://github.com/great-expectations/great_expectations/pull/5752))
* [BUGFIX] Fix RegexPatternStringParameterBuilder to use legal character repetition.  Remove median, mean, and standard deviation features from OnboardingDataAssistant "datetime_columns_rule" definition. ([#5757](https://github.com/great-expectations/great_expectations/pull/5757))
* [BUGFIX] Move `SuiteValidationResult.meta` validation id propogation before `ValidationOperator._run_action` ([#5760](https://github.com/great-expectations/great_expectations/pull/5760))
* [BUGFIX] Update "column.partition" Metric to handle DateTime Arithmetic Properly ([#5764](https://github.com/great-expectations/great_expectations/pull/5764))
* [BUGFIX] JSON-serialize RowCondition and enable IDDict to support comparison operations ([#5765](https://github.com/great-expectations/great_expectations/pull/5765))
* [BUGFIX] Insure all estimators properly handle datetime-float conversion ([#5774](https://github.com/great-expectations/great_expectations/pull/5774))
* [BUGFIX] Return appropriate subquery type to Query Metrics for SA version ([#5783](https://github.com/great-expectations/great_expectations/pull/5783))
* [DOCS] added guide how to use gx with emr serverless ([#5623](https://github.com/great-expectations/great_expectations/pull/5623)) (thanks @bvolodarskiy)
* [DOCS] DOC-362: how to choose between working with a single or multiple batches of data ([#5745](https://github.com/great-expectations/great_expectations/pull/5745))
* [MAINTENANCE] Temporarily xfail E2E Cloud tests due to Azure env var issues ([#5787](https://github.com/great-expectations/great_expectations/pull/5787))
* [MAINTENANCE] Add ids to `DataConnectorConfig` ([#5740](https://github.com/great-expectations/great_expectations/pull/5740))
* [MAINTENANCE] Rename GX Cloud "contract" resource to "checkpoint" ([#5748](https://github.com/great-expectations/great_expectations/pull/5748))
* [MAINTENANCE] Rename GX Cloud "suite_validation_result" resource to "validation_result" ([#5749](https://github.com/great-expectations/great_expectations/pull/5749))
* [MAINTENANCE] Store Refactor - cloud store return types & http-errors ([#5730](https://github.com/great-expectations/great_expectations/pull/5730))
* [MAINTENANCE] profile_numeric_columns_diff_expectation ([#5741](https://github.com/great-expectations/great_expectations/pull/5741)) (thanks @stevensecreti)
* [MAINTENANCE] Clean up type hints around class constructors ([#5738](https://github.com/great-expectations/great_expectations/pull/5738))
* [MAINTENANCE] invoke docker ([#5703](https://github.com/great-expectations/great_expectations/pull/5703))
* [MAINTENANCE] Add plist to build docker test image daily. ([#5754](https://github.com/great-expectations/great_expectations/pull/5754))
* [MAINTENANCE] opt-out type-checking  ([#5713](https://github.com/great-expectations/great_expectations/pull/5713))
* [MAINTENANCE] Enable Algolia UI ([#5753](https://github.com/great-expectations/great_expectations/pull/5753))
* [MAINTENANCE] Linting & initial typing for data context ([#5756](https://github.com/great-expectations/great_expectations/pull/5756))
* [MAINTENANCE] Update `oneshot` estimator to `quantiles` estimator ([#5737](https://github.com/great-expectations/great_expectations/pull/5737))
* [MAINTENANCE] Update Auto-Initializing Expectations to use `exact` estimator by default ([#5759](https://github.com/great-expectations/great_expectations/pull/5759))
* [MAINTENANCE] Send a Gx-Version header set to __version__ in requests to cloud ([#5758](https://github.com/great-expectations/great_expectations/pull/5758)) (thanks @wookasz)
* [MAINTENANCE]  invoke docker --detach and more typing ([#5770](https://github.com/great-expectations/great_expectations/pull/5770))
* [MAINTENANCE] In ParameterBuilder implementations, enhance handling of numpy.ndarray metric values, whose elements are or can be converted into datetime.datetime type. ([#5771](https://github.com/great-expectations/great_expectations/pull/5771))
* [MAINTENANCE] Config/Schema round_tripping ([#5697](https://github.com/great-expectations/great_expectations/pull/5697))
* [MAINTENANCE] Add experimental label to MetricStore Doc ([#5782](https://github.com/great-expectations/great_expectations/pull/5782))
* [MAINTENANCE] Remove `GeCloudIdentifier` creation in `Checkpoint.run()` ([#5784](https://github.com/great-expectations/great_expectations/pull/5784))

0.15.18
-----------------
* [FEATURE] Example notebooks for multi-batch Spark ([#5683](https://github.com/great-expectations/great_expectations/pull/5683))
* [FEATURE] Introduce top-level `default_validation_id` in `CheckpointConfig` ([#5693](https://github.com/great-expectations/great_expectations/pull/5693))
* [FEATURE] Pass down validation ids to `ExpectationSuiteValidationResult.meta` within `Checkpoint.run()` ([#5725](https://github.com/great-expectations/great_expectations/pull/5725))
* [FEATURE] Refactor data assistant runner to compute formal parameters for data assistant run method signatures ([#5727](https://github.com/great-expectations/great_expectations/pull/5727))
* [BUGFIX] Restored sqlite database for tests ([#5742](https://github.com/great-expectations/great_expectations/pull/5742))
* [BUGFIX] Fixing a typo in variable name for default profiler for auto-initializing expectation "expect_column_mean_to_be_between" ([#5687](https://github.com/great-expectations/great_expectations/pull/5687))
* [BUGFIX] Remove `resource_type` from call to `StoreBackend.build_key` ([#5690](https://github.com/great-expectations/great_expectations/pull/5690))
* [BUGFIX] Update how_to_use_great_expectations_in_aws_glue.md ([#5685](https://github.com/great-expectations/great_expectations/pull/5685)) (thanks @bvolodarskiy)
* [BUGFIX] Updated how_to_use_great_expectations_in_aws_glue.md again ([#5696](https://github.com/great-expectations/great_expectations/pull/5696)) (thanks @bvolodarskiy)
* [BUGFIX] Update how_to_use_great_expectations_in_aws_glue.md ([#5722](https://github.com/great-expectations/great_expectations/pull/5722)) (thanks @bvolodarskiy)
* [BUGFIX] Update aws_glue_deployment_patterns.py ([#5721](https://github.com/great-expectations/great_expectations/pull/5721)) (thanks @bvolodarskiy)
* [DOCS] added guide how to use great expectations with aws glue ([#5536](https://github.com/great-expectations/great_expectations/pull/5536)) (thanks @bvolodarskiy)
* [DOCS] Document the ZenML integration for Great Expectations ([#5672](https://github.com/great-expectations/great_expectations/pull/5672)) (thanks @stefannica)
* [DOCS] Converts broken ZenML md refs to Technical Tags ([#5714](https://github.com/great-expectations/great_expectations/pull/5714))
* [DOCS] How to create a Custom Query Expectation ([#5460](https://github.com/great-expectations/great_expectations/pull/5460))
* [MAINTENANCE] Pin makefun package to version range for support assurance ([#5746](https://github.com/great-expectations/great_expectations/pull/5746))
* [MAINTENANCE] s3 link for logo ([#5731](https://github.com/great-expectations/great_expectations/pull/5731))
* [MAINTENANCE] Assign `resource_type` in `InlineStoreBackend` constructor ([#5671](https://github.com/great-expectations/great_expectations/pull/5671))
* [MAINTENANCE] Add mysql client to Dockerfile.tests ([#5681](https://github.com/great-expectations/great_expectations/pull/5681))
* [MAINTENANCE] `RuleBasedProfiler` corner case configuration changes ([#5631](https://github.com/great-expectations/great_expectations/pull/5631))
* [MAINTENANCE] Update teams.yml ([#5684](https://github.com/great-expectations/great_expectations/pull/5684))
* [MAINTENANCE] Utilize `e2e` mark on E2E Cloud tests ([#5691](https://github.com/great-expectations/great_expectations/pull/5691))
* [MAINTENANCE] pyproject.tooml build-system typo ([#5692](https://github.com/great-expectations/great_expectations/pull/5692))
* [MAINTENANCE] expand flake8 coverage ([#5676](https://github.com/great-expectations/great_expectations/pull/5676))
* [MAINTENANCE] Ensure Cloud E2E tests are isolated to `gx-cloud-e2e` stage of CI ([#5695](https://github.com/great-expectations/great_expectations/pull/5695))
* [MAINTENANCE] Add usage stats and initial database docker tests to CI ([#5682](https://github.com/great-expectations/great_expectations/pull/5682))
* [MAINTENANCE] Add `e2e` mark to `pyproject.toml` ([#5699](https://github.com/great-expectations/great_expectations/pull/5699))
* [MAINTENANCE] Update docker readme to mount your repo over the builtin one. ([#5701](https://github.com/great-expectations/great_expectations/pull/5701))
* [MAINTENANCE] Combine packages `rule_based_profiler` and `rule_based_profiler.types` ([#5680](https://github.com/great-expectations/great_expectations/pull/5680))
* [MAINTENANCE] ExpectColumnValuesToBeInSetSparkOptimized ([#5702](https://github.com/great-expectations/great_expectations/pull/5702))
* [MAINTENANCE] expect_column_pair_values_to_have_difference_of_custom_perc… ([#5661](https://github.com/great-expectations/great_expectations/pull/5661)) (thanks @exteli)
* [MAINTENANCE] Remove non-docker version of CI tests that are now running in docker. ([#5700](https://github.com/great-expectations/great_expectations/pull/5700))
* [MAINTENANCE] Add back `integration` mark to tests in `test_datasource_crud.py` ([#5708](https://github.com/great-expectations/great_expectations/pull/5708))
* [MAINTENANCE] DEVREL-2289/Stale/Triage ([#5694](https://github.com/great-expectations/great_expectations/pull/5694))
* [MAINTENANCE] revert expansive flake8 pre-commit checking - flake8 5.0.4 ([#5706](https://github.com/great-expectations/great_expectations/pull/5706))
* [MAINTENANCE] Bugfix for `cloud-db-integration-pipeline` ([#5704](https://github.com/great-expectations/great_expectations/pull/5704))
* [MAINTENANCE] Remove pytest-azurepipelines ([#5716](https://github.com/great-expectations/great_expectations/pull/5716))
* [MAINTENANCE] Remove deprecation warning from `DataConnector`-level `batch_identifiers` for `RuntimeDataConnector` ([#5717](https://github.com/great-expectations/great_expectations/pull/5717))
* [MAINTENANCE] Refactor `AbstractConfig` to make `name` and `id_` consistent attrs ([#5698](https://github.com/great-expectations/great_expectations/pull/5698))
* [MAINTENANCE] Move CLI tests to docker ([#5719](https://github.com/great-expectations/great_expectations/pull/5719))
* [MAINTENANCE] Leverage `DataContextVariables` in `DataContext` hierarchy to automatically determine how to persist changes ([#5715](https://github.com/great-expectations/great_expectations/pull/5715))
* [MAINTENANCE] Refactor `InMemoryStoreBackend` out of `store_backend.py` ([#5679](https://github.com/great-expectations/great_expectations/pull/5679))
* [MAINTENANCE] Move compatibility matrix tests to docker ([#5728](https://github.com/great-expectations/great_expectations/pull/5728))
* [MAINTENANCE] Adds additional file extensions for Parquet assets ([#5729](https://github.com/great-expectations/great_expectations/pull/5729))
* [MAINTENANCE] MultiBatch SqlExample notebook Update.  ([#5718](https://github.com/great-expectations/great_expectations/pull/5718))
* [MAINTENANCE] Introduce NumericRangeEstimator class hierarchy and encapsulate existing estimator implementations ([#5735](https://github.com/great-expectations/great_expectations/pull/5735))

0.15.17
-----------------
* [FEATURE] Improve estimation histogram computation in NumericMetricRangeMultiBatchParameterBuilder to include both counts and bin edges ([#5628](https://github.com/great-expectations/great_expectations/pull/5628))
* [FEATURE] Enable retrieve by name for datasource with cloud store backend ([#5640](https://github.com/great-expectations/great_expectations/pull/5640))
* [FEATURE] Update `DataContext.add_checkpoint()` to ensure validations within `CheckpointConfig` contain ids ([#5638](https://github.com/great-expectations/great_expectations/pull/5638))
* [FEATURE] Add `expect_column_values_to_be_valid_crc32` ([#5580](https://github.com/great-expectations/great_expectations/pull/5580)) (thanks @sp1thas)
* [FEATURE] Enable showing expectation suite by domain and by expectation_type -- from DataAssistantResult ([#5673](https://github.com/great-expectations/great_expectations/pull/5673))
* [BUGFIX] Patch flaky E2E GX Cloud tests ([#5629](https://github.com/great-expectations/great_expectations/pull/5629))
* [BUGFIX] Pass `--cloud` flag to `dgtest-cloud-overrides` section of Azure YAML ([#5632](https://github.com/great-expectations/great_expectations/pull/5632))
* [BUGFIX] Remove datasource from config on delete ([#5636](https://github.com/great-expectations/great_expectations/pull/5636))
* [BUGFIX] Patch issue with usage stats sync not respecting usage stats opt-out ([#5644](https://github.com/great-expectations/great_expectations/pull/5644))
* [BUGFIX] SlackRenderer / EmailRenderer links to deprecated doc ([#5648](https://github.com/great-expectations/great_expectations/pull/5648))
* [BUGFIX] Fix table.head metric issue when using BQ without temp tables ([#5630](https://github.com/great-expectations/great_expectations/pull/5630))
* [BUGFIX] Quick bugfix on all profile numeric column diff bounds expectations ([#5651](https://github.com/great-expectations/great_expectations/pull/5651)) (thanks @stevensecreti)
* [BUGFIX] Patch bug with `id` vs `id_` in Cloud integration tests ([#5677](https://github.com/great-expectations/great_expectations/pull/5677))
* [DOCS] Fix a typo in batch_request_parameters variable ([#5612](https://github.com/great-expectations/great_expectations/pull/5612)) (thanks @StasDeep)
* [MAINTENANCE] CloudDataContext add_datasource test ([#5626](https://github.com/great-expectations/great_expectations/pull/5626))
* [MAINTENANCE] Update stale.yml ([#5602](https://github.com/great-expectations/great_expectations/pull/5602))
* [MAINTENANCE] Add `id` to `CheckpointValidationConfig` ([#5603](https://github.com/great-expectations/great_expectations/pull/5603))
* [MAINTENANCE] Better error message for RuntimeDataConnector for BatchIdentifiers ([#5635](https://github.com/great-expectations/great_expectations/pull/5635))
* [MAINTENANCE] type-checking round 2 ([#5576](https://github.com/great-expectations/great_expectations/pull/5576))
* [MAINTENANCE] minor cleanup of old comments ([#5641](https://github.com/great-expectations/great_expectations/pull/5641))
* [MAINTENANCE] add `--clear-cache` flag for `invoke type-check` ([#5639](https://github.com/great-expectations/great_expectations/pull/5639))
* [MAINTENANCE] Install `dgtest` test runner utilizing Git URL in CI ([#5645](https://github.com/great-expectations/great_expectations/pull/5645))
* [MAINTENANCE] Make comparisons of aggregate values date aware ([#5642](https://github.com/great-expectations/great_expectations/pull/5642)) (thanks @jcampbell)
* [MAINTENANCE] Add E2E Cloud test for `DataContext.add_checkpoint()` ([#5653](https://github.com/great-expectations/great_expectations/pull/5653))
* [MAINTENANCE] Use docker to run tests in the Azure CI pipeline. ([#5646](https://github.com/great-expectations/great_expectations/pull/5646))
* [MAINTENANCE] add new invoke tasks to `tasks.py` and create new file `usage_stats_utils.py` ([#5593](https://github.com/great-expectations/great_expectations/pull/5593))
* [MAINTENANCE] Don't include 'test-pipeline' in extras_require dict ([#5659](https://github.com/great-expectations/great_expectations/pull/5659))
* [MAINTENANCE] move tool config to pyproject.toml ([#5649](https://github.com/great-expectations/great_expectations/pull/5649))
* [MAINTENANCE] Refactor docker test CI steps into jobs. ([#5665](https://github.com/great-expectations/great_expectations/pull/5665))
* [MAINTENANCE] Only run Cloud E2E tests in primary pipeline ([#5670](https://github.com/great-expectations/great_expectations/pull/5670))
* [MAINTENANCE] Improve DateTime Conversion Candling in Comparison Metrics & Expectations and Provide a Clean Object Model for Metrics Computation Bundling ([#5656](https://github.com/great-expectations/great_expectations/pull/5656))
* [MAINTENANCE] Ensure that `id_` fields in Marshmallow schema serialize as `id` ([#5660](https://github.com/great-expectations/great_expectations/pull/5660))
* [MAINTENANCE] data_context initial type checking ([#5662](https://github.com/great-expectations/great_expectations/pull/5662))

0.15.16
-----------------
* [FEATURE] Multi-Batch Example Notebook - SqlDataConnector examples ([#5575](https://github.com/great-expectations/great_expectations/pull/5575))
* [FEATURE] Implement "is_close()" for making equality comparisons "reasonably close" for each ExecutionEngine subclass ([#5597](https://github.com/great-expectations/great_expectations/pull/5597))
* [FEATURE] expect_profile_numeric_columns_percent_diff_(inclusive bounds) ([#5586](https://github.com/great-expectations/great_expectations/pull/5586)) (thanks @stevensecreti)
* [FEATURE] DataConnector Query enabled for `SimpleSqlDatasource` ([#5610](https://github.com/great-expectations/great_expectations/pull/5610))
* [FEATURE] Implement the exact metric range estimate for NumericMetricRangeMultiBatchParameterBuilder ([#5620](https://github.com/great-expectations/great_expectations/pull/5620))
* [FEATURE] Ensure that id propogates from RuleBasedProfilerConfig to RuleBasedProfiler ([#5617](https://github.com/great-expectations/great_expectations/pull/5617))
* [BUGFIX] Pass cloud base url to datasource store ([#5595](https://github.com/great-expectations/great_expectations/pull/5595))
* [BUGFIX] Temporarily disable Trino `0.315.0` from requirements ([#5606](https://github.com/great-expectations/great_expectations/pull/5606))
* [BUGFIX] Update _create_trino_engine to check for schema before creating it ([#5607](https://github.com/great-expectations/great_expectations/pull/5607))
* [BUGFIX] Support `ExpectationSuite` CRUD at `BaseDataContext` level ([#5604](https://github.com/great-expectations/great_expectations/pull/5604))
* [BUGFIX] Update test due to change in postgres stdev calculation method ([#5624](https://github.com/great-expectations/great_expectations/pull/5624))
* [BUGFIX] Patch issue with `get_validator` on Cloud-backed `DataContext` ([#5619](https://github.com/great-expectations/great_expectations/pull/5619))
* [MAINTENANCE] Add name and id to DatasourceConfig ([#5560](https://github.com/great-expectations/great_expectations/pull/5560))
* [MAINTENANCE] Clear datasources in `test_data_context_datasources` to improve test performance and narrow test scope ([#5588](https://github.com/great-expectations/great_expectations/pull/5588))
* [MAINTENANCE] Fix tests that rely on guessing pytest generated random file paths. ([#5589](https://github.com/great-expectations/great_expectations/pull/5589))
* [MAINTENANCE] Do not set google cloud credentials for lifetime of pytest process. ([#5592](https://github.com/great-expectations/great_expectations/pull/5592))
* [MAINTENANCE] Misc updates to `Datasource` CRUD on `DataContext` to ensure consistent behavior ([#5584](https://github.com/great-expectations/great_expectations/pull/5584))
* [MAINTENANCE] Add id to `RuleBasedProfiler` config ([#5590](https://github.com/great-expectations/great_expectations/pull/5590))
* [MAINTENANCE] refactor to enable customization of quantile bias correction threshold for bootstrap estimation method ([#5587](https://github.com/great-expectations/great_expectations/pull/5587))
* [MAINTENANCE] Ensure that `resource_type` used in `GeCloudStoreBackend` is converted to `GeCloudRESTResource` enum as needed ([#5601](https://github.com/great-expectations/great_expectations/pull/5601))
* [MAINTENANCE] Create datasource with id ([#5591](https://github.com/great-expectations/great_expectations/pull/5591))
* [MAINTENANCE] Enable Azure blob storage integration tests ([#5594](https://github.com/great-expectations/great_expectations/pull/5594))
* [MAINTENANCE] Increase expectation kwarg line stroke width ([#5608](https://github.com/great-expectations/great_expectations/pull/5608))
* [MAINTENANCE] Added Algolia Scripts ([#5544](https://github.com/great-expectations/great_expectations/pull/5544)) (thanks @devanshdixit)
* [MAINTENANCE] Handle `numpy` deprecation warnings ([#5615](https://github.com/great-expectations/great_expectations/pull/5615))
* [MAINTENANCE] remove approximate comparisons -- they will be replaced by estimator alternatives ([#5618](https://github.com/great-expectations/great_expectations/pull/5618))
* [MAINTENANCE] Making the dependency on dev-lite clearer ([#5514](https://github.com/great-expectations/great_expectations/pull/5514))
* [MAINTENANCE] Fix tests in tests/integration/profiling/rule_based_profiler/ and tests/render/renderer/ ([#5611](https://github.com/great-expectations/great_expectations/pull/5611))
* [MAINTENANCE] DataContext in cloud mode test add_datasource ([#5625](https://github.com/great-expectations/great_expectations/pull/5625))

0.15.15
-----------------
* [FEATURE] Integrate `DataContextVariables` with `DataContext` ([#5466](https://github.com/great-expectations/great_expectations/pull/5466))
* [FEATURE] Add mostly to MulticolumnMapExpectation ([#5481](https://github.com/great-expectations/great_expectations/pull/5481))
* [FEATURE] [MAINTENANCE] Revamped expect_profile_numeric_columns_diff_between_exclusive_threshold_range ([#5493](https://github.com/great-expectations/great_expectations/pull/5493)) (thanks @stevensecreti)
* [FEATURE] [CONTRIB] expect_profile_numeric_columns_diff_(less/greater)_than_or_equal_to_threshold ([#5522](https://github.com/great-expectations/great_expectations/pull/5522)) (thanks @stevensecreti)
* [FEATURE] Provide methods for returning ExpectationConfiguration list grouped by expectation_type and by domain_type ([#5532](https://github.com/great-expectations/great_expectations/pull/5532))
* [FEATURE] add support for Azure authentication methods ([#5229](https://github.com/great-expectations/great_expectations/pull/5229)) (thanks @sdebruyn)
* [FEATURE] Show grouped sorted expectations by Domain and by expectation_type ([#5539](https://github.com/great-expectations/great_expectations/pull/5539))
* [FEATURE] Categorical Rule in VolumeDataAssistant Should Use Same Cardinality As Categorical Rule in OnboardingDataAssistant ([#5551](https://github.com/great-expectations/great_expectations/pull/5551))
* [BUGFIX] Handle "division by zero" in "ColumnPartition" metric when all column values are NULL ([#5507](https://github.com/great-expectations/great_expectations/pull/5507))
* [BUGFIX] Use string dialect name if not found in enum ([#5546](https://github.com/great-expectations/great_expectations/pull/5546))
* [BUGFIX] Add `try/except` around `DataContext._save_project_config` to mitigate issues with permissions ([#5550](https://github.com/great-expectations/great_expectations/pull/5550))
* [BUGFIX] Explicitly pass in mostly as 1 if not set in configuration. ([#5548](https://github.com/great-expectations/great_expectations/pull/5548))
* [BUGFIX] Increase precision for categorical rule for fractional comparisons ([#5552](https://github.com/great-expectations/great_expectations/pull/5552))
* [DOCS] DOC-340 partition local installation guide ([#5425](https://github.com/great-expectations/great_expectations/pull/5425))
* [DOCS] Add DataHub Ingestion docs  ([#5330](https://github.com/great-expectations/great_expectations/pull/5330)) (thanks @maggiehays)
* [DOCS] toc update for DataHub integration doc ([#5518](https://github.com/great-expectations/great_expectations/pull/5518))
* [DOCS] Updating discourse to GitHub Discussions in Docs ([#4953](https://github.com/great-expectations/great_expectations/pull/4953))
* [MAINTENANCE] Clean up payload for `/data-context-variables` endpoint to adhere to desired chema ([#5509](https://github.com/great-expectations/great_expectations/pull/5509))
* [MAINTENANCE] DataContext Refactor: DataAssistants ([#5472](https://github.com/great-expectations/great_expectations/pull/5472))
* [MAINTENANCE] Ensure that validation operators are omitted from Cloud variables payload ([#5510](https://github.com/great-expectations/great_expectations/pull/5510))
* [MAINTENANCE] Add end-to-end tests for multicolumn map expectations ([#5517](https://github.com/great-expectations/great_expectations/pull/5517))
* [MAINTENANCE] Ensure that *_store_name attrs are omitted from Cloud variables payload ([#5519](https://github.com/great-expectations/great_expectations/pull/5519))
* [MAINTENANCE] Refactor `key` arg out of `Store.serialize/deserialize` ([#5511](https://github.com/great-expectations/great_expectations/pull/5511))
* [MAINTENANCE] Fix links to documentation ([#5177](https://github.com/great-expectations/great_expectations/pull/5177)) (thanks @andyjessen)
* [MAINTENANCE] Readme Update ([#4952](https://github.com/great-expectations/great_expectations/pull/4952))
* [MAINTENANCE] E2E test for `FileDataContextVariables` ([#5516](https://github.com/great-expectations/great_expectations/pull/5516))
* [MAINTENANCE] Cleanup/refactor prerequisite for group/filter/sort Expectations by domain ([#5523](https://github.com/great-expectations/great_expectations/pull/5523))
* [MAINTENANCE] Refactor `GeCloudStoreBackend` to use PUT and DELETE HTTP verbs instead of PATCH ([#5527](https://github.com/great-expectations/great_expectations/pull/5527))
* [MAINTENANCE] `/profiler` Cloud endpoint support ([#5499](https://github.com/great-expectations/great_expectations/pull/5499))
* [MAINTENANCE] Add type hints to `Store` ([#5529](https://github.com/great-expectations/great_expectations/pull/5529))
* [MAINTENANCE] Move MetricDomainTypes to core (it is used more widely now than previously). ([#5530](https://github.com/great-expectations/great_expectations/pull/5530))
* [MAINTENANCE] Remove dependency pins on pyarrow and snowflake-connector-python ([#5533](https://github.com/great-expectations/great_expectations/pull/5533))
* [MAINTENANCE] use invoke for common contrib/dev tasks ([#5506](https://github.com/great-expectations/great_expectations/pull/5506))
* [MAINTENANCE] Add snowflake-connector-python dependency lower bound. ([#5538](https://github.com/great-expectations/great_expectations/pull/5538))
* [MAINTENANCE] enforce pre-commit in ci ([#5526](https://github.com/great-expectations/great_expectations/pull/5526))
* [MAINTENANCE] Providing more robust error handling for determining `domain_type` of an `ExpectationConfiguration` object ([#5542](https://github.com/great-expectations/great_expectations/pull/5542))
* [MAINTENANCE] Remove extra indentation from store backend test ([#5545](https://github.com/great-expectations/great_expectations/pull/5545))
* [MAINTENANCE] Plot-level dropdown for `DataAssistantResult` display charts ([#5528](https://github.com/great-expectations/great_expectations/pull/5528))
* [MAINTENANCE] Make DataAssistantResult.batch_id_to_batch_identifier_display_name_map private (in order to optimize auto-complete for ease of use) ([#5549](https://github.com/great-expectations/great_expectations/pull/5549))
* [MAINTENANCE] Initial Dockerfile for running tests and associated README. ([#5541](https://github.com/great-expectations/great_expectations/pull/5541))
* [MAINTENANCE] Other dialect test ([#5547](https://github.com/great-expectations/great_expectations/pull/5547))

0.15.14
-----------------
* [FEATURE] QueryExpectations ([#5223](https://github.com/great-expectations/great_expectations/pull/5223))
* [FEATURE] Control volume of metadata output when running DataAssistant classes. ([#5483](https://github.com/great-expectations/great_expectations/pull/5483))
* [BUGFIX] Snowflake Docs Integration Test Fix ([#5463](https://github.com/great-expectations/great_expectations/pull/5463))
* [BUGFIX] DataProfiler Linting Fix ([#5468](https://github.com/great-expectations/great_expectations/pull/5468))
* [BUGFIX] Update renderer snapshots with `None` values removed ([#5474](https://github.com/great-expectations/great_expectations/pull/5474))
* [BUGFIX] Rendering Test failures ([#5475](https://github.com/great-expectations/great_expectations/pull/5475))
* [BUGFIX] Update `dependency-graph` pipeline YAML to ensure `--spark` gets passed to `dgtest` ([#5477](https://github.com/great-expectations/great_expectations/pull/5477))
* [BUGFIX] Make sure the profileReport obj does not have defaultdicts (breaks gallery JSON) ([#5491](https://github.com/great-expectations/great_expectations/pull/5491))
* [BUGFIX] Use Pandas.isnull() instead of NumPy.isnan() to check for empty values in TableExpectation._validate_metric_value_between(), due to wider types applicability. ([#5502](https://github.com/great-expectations/great_expectations/pull/5502))
* [BUGFIX] Spark Schema has unexpected field for `spark.sql.warehouse.dir` ([#5490](https://github.com/great-expectations/great_expectations/pull/5490))
* [BUGFIX] Conditionally pop values from Spark config in tests ([#5508](https://github.com/great-expectations/great_expectations/pull/5508))
* [DOCS] DOC-349 re-write and partition interactive mode expectations guide ([#5448](https://github.com/great-expectations/great_expectations/pull/5448))
* [DOCS] DOC-344 partition data docs on s3 guide ([#5437](https://github.com/great-expectations/great_expectations/pull/5437))
* [DOCS] DOC-342 partition how to configure a validation result store in amazon s3 guide ([#5428](https://github.com/great-expectations/great_expectations/pull/5428))
* [DOCS] link fix in onboarding data assistant guide ([#5469](https://github.com/great-expectations/great_expectations/pull/5469))
* [DOCS] Integrate great-expectation with ydata-synthetic ([#4568](https://github.com/great-expectations/great_expectations/pull/4568)) (thanks @arunnthevapalan)
* [DOCS] Add 'test' extra to setup.py with docs ([#5415](https://github.com/great-expectations/great_expectations/pull/5415))
* [DOCS] DOC-343 partition how to configure expectation store for aws s3 guide ([#5429](https://github.com/great-expectations/great_expectations/pull/5429))
* [DOCS] DOC-357 partition the how to create a new checkpoint guide ([#5458](https://github.com/great-expectations/great_expectations/pull/5458))
* [DOCS] Remove outdated release process docs. ([#5484](https://github.com/great-expectations/great_expectations/pull/5484))
* [MAINTENANCE] Update `teams.yml` ([#5457](https://github.com/great-expectations/great_expectations/pull/5457))
* [MAINTENANCE] Clean up GitHub Actions ([#5461](https://github.com/great-expectations/great_expectations/pull/5461))
* [MAINTENANCE] Adds documentation and examples changes for snowflake connection string ([#5447](https://github.com/great-expectations/great_expectations/pull/5447))
* [MAINTENANCE] DOC-345 partition the connect to s3 cloud storage with Pandas guide ([#5439](https://github.com/great-expectations/great_expectations/pull/5439))
* [MAINTENANCE] Add unit and integration tests for Splitting on Mod Integer  ([#5452](https://github.com/great-expectations/great_expectations/pull/5452))
* [MAINTENANCE] Remove `InlineRenderer` invocation feature flag from `ExpectationValidationResult` ([#5441](https://github.com/great-expectations/great_expectations/pull/5441))
* [MAINTENANCE] `DataContext` Refactor. Migration of datasource and store ([#5404](https://github.com/great-expectations/great_expectations/pull/5404))
* [MAINTENANCE] Add unit and integration tests for Splitting on Multi-Column Values ([#5464](https://github.com/great-expectations/great_expectations/pull/5464))
* [MAINTENANCE] Refactor `DataContextVariables` to leverage `@property` and `@setter` ([#5446](https://github.com/great-expectations/great_expectations/pull/5446))
* [MAINTENANCE] expect_profile_numeric_columns_diff_between_threshold_range ([#5467](https://github.com/great-expectations/great_expectations/pull/5467)) (thanks @stevensecreti)
* [MAINTENANCE] Make `DataAssistantResult` fixtures module scoped ([#5465](https://github.com/great-expectations/great_expectations/pull/5465))
* [MAINTENANCE] Remove keyword arguments within table row count expectations ([#4874](https://github.com/great-expectations/great_expectations/pull/4874)) (thanks @andyjessen)
* [MAINTENANCE] Add unit tests for Splitting on Converted DateTime ([#5470](https://github.com/great-expectations/great_expectations/pull/5470))
* [MAINTENANCE] Rearrange integration tests to insure categorization into proper deployment-style based lists ([#5471](https://github.com/great-expectations/great_expectations/pull/5471))
* [MAINTENANCE] Provide better error messaging if batch_request is not supplied to DataAssistant.run() ([#5473](https://github.com/great-expectations/great_expectations/pull/5473))
* [MAINTENANCE] Adds run time envvar for Snowflake Partner ID ([#5485](https://github.com/great-expectations/great_expectations/pull/5485))
* [MAINTENANCE] fixed algolia search page ([#5099](https://github.com/great-expectations/great_expectations/pull/5099))
* [MAINTENANCE] Remove pyspark<3.0.0 constraint for python 3.7 ([#5496](https://github.com/great-expectations/great_expectations/pull/5496))
* [MAINTENANCE] Ensure that `parter-integration` pipeline only runs on cronjob ([#5500](https://github.com/great-expectations/great_expectations/pull/5500))
* [MAINTENANCE] Adding fixtures Query Expectations tests  ([#5486](https://github.com/great-expectations/great_expectations/pull/5486))
* [MAINTENANCE] Misc updates to `GeCloudStoreBackend` to better integrate with GE Cloud ([#5497](https://github.com/great-expectations/great_expectations/pull/5497))
* [MAINTENANCE] Update automated release schedule ([#5488](https://github.com/great-expectations/great_expectations/pull/5488))
* [MAINTENANCE] Update core-team in `teams.yml` ([#5489](https://github.com/great-expectations/great_expectations/pull/5489))
* [MAINTENANCE] Update how_to_create_a_new_expectation_suite_using_rule_based_profile… ([#5495](https://github.com/great-expectations/great_expectations/pull/5495))
* [MAINTENANCE] Remove pypandoc pin in constraints-dev.txt. ([#5501](https://github.com/great-expectations/great_expectations/pull/5501))
* [MAINTENANCE] Ensure that `add_datasource` method on `AbstractDataContext` does not persist by default ([#5482](https://github.com/great-expectations/great_expectations/pull/5482))

0.15.13
-----------------
* [FEATURE] Add atomic `rendered_content` to `ExpectationValidationResult` and `ExpectationConfiguration` ([#5369](https://github.com/great-expectations/great_expectations/pull/5369))
* [FEATURE] Add `DataContext.update_datasource` CRUD method ([#5417](https://github.com/great-expectations/great_expectations/pull/5417))
* [FEATURE] Refactor Splitter Testing Modules so as to Make them More General and Add Unit and Integration Tests for "split_on_whole_table" and "split_on_column_value" on SQLite and All Supported Major SQL Backends ([#5430](https://github.com/great-expectations/great_expectations/pull/5430))
* [FEATURE] Support underscore in the `condition_value` of a `row_condition` ([#5393](https://github.com/great-expectations/great_expectations/pull/5393)) (thanks @sp1thas)
* [DOCS] DOC-322 update terminology to v3 ([#5326](https://github.com/great-expectations/great_expectations/pull/5326))
* [MAINTENANCE] Change property name of TaxiSplittingTestCase to make it more general ([#5419](https://github.com/great-expectations/great_expectations/pull/5419))
* [MAINTENANCE] Ensure that `BaseDataContext` does not persist `Datasource` changes by default ([#5423](https://github.com/great-expectations/great_expectations/pull/5423))
* [MAINTENANCE] Migration of `project_config_with_variables_substituted` to `AbstractDataContext` ([#5385](https://github.com/great-expectations/great_expectations/pull/5385))
* [MAINTENANCE] Improve type hinting in `GeCloudStoreBackend` ([#5427](https://github.com/great-expectations/great_expectations/pull/5427))
* [MAINTENANCE] Test serialization of text, table, and bulleted list `rendered_content` in `ExpectationValidationResult` ([#5438](https://github.com/great-expectations/great_expectations/pull/5438))
* [MAINTENANCE] Refactor `datasource_name` out of `DataContext.update_datasource` ([#5440](https://github.com/great-expectations/great_expectations/pull/5440))
* [MAINTENANCE] Add checkpoint name to validation results ([#5442](https://github.com/great-expectations/great_expectations/pull/5442))
* [MAINTENANCE] Remove checkpoint from top level of schema since it is captured in `meta` ([#5445](https://github.com/great-expectations/great_expectations/pull/5445))
* [MAINTENANCE] Add unit and integration tests for Splitting on Divided Integer ([#5449](https://github.com/great-expectations/great_expectations/pull/5449))
* [MAINTENANCE] Update cli with new default simple checkpoint name ([#5450](https://github.com/great-expectations/great_expectations/pull/5450))

0.15.12
-----------------
* [FEATURE] Add Rule Statistics to DataAssistantResult for display in Jupyter notebook ([#5368](https://github.com/great-expectations/great_expectations/pull/5368))
* [FEATURE] Include detailed Rule Execution statistics in jupyter notebook "repr" style output ([#5375](https://github.com/great-expectations/great_expectations/pull/5375))
* [FEATURE] Support datetime/date-part splitters on Amazon Redshift ([#5408](https://github.com/great-expectations/great_expectations/pull/5408))
* [DOCS] Capital One DataProfiler Expectations README Update ([#5365](https://github.com/great-expectations/great_expectations/pull/5365)) (thanks @stevensecreti)
* [DOCS] Add Trino guide ([#5287](https://github.com/great-expectations/great_expectations/pull/5287))
* [DOCS] DOC-339 remove redundant how-to guide ([#5396](https://github.com/great-expectations/great_expectations/pull/5396))
* [DOCS] Capital One Data Profiler README update ([#5387](https://github.com/great-expectations/great_expectations/pull/5387)) (thanks @taylorfturner)
* [DOCS] Add sqlalchemy-redshfit to dependencies in redshift doc ([#5386](https://github.com/great-expectations/great_expectations/pull/5386))
* [MAINTENANCE] Reduce output amount in Jupyter notebooks when displaying DataAssistantResult ([#5362](https://github.com/great-expectations/great_expectations/pull/5362))
* [MAINTENANCE] Update linter thresholds ([#5367](https://github.com/great-expectations/great_expectations/pull/5367))
* [MAINTENANCE] Move `_apply_global_config_overrides()` to AbstractDataContext ([#5285](https://github.com/great-expectations/great_expectations/pull/5285))
* [MAINTENANCE] WIP: [MAINTENANCE] stalebot configuration ([#5301](https://github.com/great-expectations/great_expectations/pull/5301))
* [MAINTENANCE] expect_column_values_to_be_equal_to_or_greater_than_profile_min ([#5372](https://github.com/great-expectations/great_expectations/pull/5372)) (thanks @stevensecreti)
* [MAINTENANCE] expect_column_values_to_be_equal_to_or_less_than_profile_max ([#5380](https://github.com/great-expectations/great_expectations/pull/5380)) (thanks @stevensecreti)
* [MAINTENANCE] Replace string formatting with f-string ([#5225](https://github.com/great-expectations/great_expectations/pull/5225)) (thanks @andyjessen)
* [MAINTENANCE] Fix links in docs ([#5340](https://github.com/great-expectations/great_expectations/pull/5340)) (thanks @andyjessen)
* [MAINTENANCE] Caching of `config_variables` in `DataContext` ([#5376](https://github.com/great-expectations/great_expectations/pull/5376))
* [MAINTENANCE] StaleBot Half DryRun ([#5390](https://github.com/great-expectations/great_expectations/pull/5390))
* [MAINTENANCE] StaleBot DryRun 2  ([#5391](https://github.com/great-expectations/great_expectations/pull/5391))
* [MAINTENANCE] file extentions applied to rel links ([#5399](https://github.com/great-expectations/great_expectations/pull/5399))
* [MAINTENANCE] Allow installing jinja2 version 3.1.0 and higher ([#5382](https://github.com/great-expectations/great_expectations/pull/5382))
* [MAINTENANCE] expect_column_values_confidence_for_data_label_to_be_less_than_or_equal_to_threshold ([#5392](https://github.com/great-expectations/great_expectations/pull/5392)) (thanks @stevensecreti)
* [MAINTENANCE] Add warnings to internal linters if actual error count does not match threshold ([#5401](https://github.com/great-expectations/great_expectations/pull/5401))
* [MAINTENANCE] Ensure that changes made to env vars / config vars are recognized within subsequent calls of the same process ([#5410](https://github.com/great-expectations/great_expectations/pull/5410))
* [MAINTENANCE] Stack `RuleBasedProfiler` progress bars for better user experience ([#5400](https://github.com/great-expectations/great_expectations/pull/5400))
* [MAINTENANCE] Keep all Pandas Splitter Tests in a Dedicated Module ([#5411](https://github.com/great-expectations/great_expectations/pull/5411))
* [MAINTENANCE] Refactor DataContextVariables to only persist state to Store using explicit save command ([#5366](https://github.com/great-expectations/great_expectations/pull/5366))
* [MAINTENANCE] Refactor to put tests for splitting and sampling into modules for respective ExecutionEngine implementation ([#5412](https://github.com/great-expectations/great_expectations/pull/5412))

0.15.11
-----------------
* [FEATURE] Enable NumericMetricRangeMultiBatchParameterBuilder to use evaluation dependencies ([#5323](https://github.com/great-expectations/great_expectations/pull/5323))
* [FEATURE] Improve Trino Support ([#5261](https://github.com/great-expectations/great_expectations/pull/5261)) (thanks @aezomz)
* [FEATURE] added support to Aws Athena quantiles ([#5114](https://github.com/great-expectations/great_expectations/pull/5114)) (thanks @kuhnen)
* [FEATURE] Implement the "column.standard_deviation" metric for sqlite database ([#5338](https://github.com/great-expectations/great_expectations/pull/5338))
* [FEATURE] Update `add_datasource` to leverage the `DatasourceStore` ([#5334](https://github.com/great-expectations/great_expectations/pull/5334))
* [FEATURE] Provide ability for DataAssistant to return its effective underlying BaseRuleBasedProfiler configuration ([#5359](https://github.com/great-expectations/great_expectations/pull/5359))
* [BUGFIX] Fix Netlify build issue that was being caused by entry in changelog ([#5322](https://github.com/great-expectations/great_expectations/pull/5322))
* [BUGFIX] Numpy dtype.float64 formatted floating point numbers must be converted to Python float for use in SQLAlchemy Boolean clauses ([#5336](https://github.com/great-expectations/great_expectations/pull/5336))
* [BUGFIX] Fix for failing Expectation test in `cloud_db_integration` pipeline ([#5321](https://github.com/great-expectations/great_expectations/pull/5321))
* [DOCS] revert getting started tutorial to RBP process ([#5307](https://github.com/great-expectations/great_expectations/pull/5307))
* [DOCS] mark onboarding assistant guide as experimental and update cli command ([#5308](https://github.com/great-expectations/great_expectations/pull/5308))
* [DOCS] Fix line numbers in getting started guide ([#5324](https://github.com/great-expectations/great_expectations/pull/5324))
* [DOCS] DOC-337 automate updates to the version information displayed in the getting started tutorial. ([#5348](https://github.com/great-expectations/great_expectations/pull/5348))
* [MAINTENANCE] Fix link in suite profile renderer ([#5242](https://github.com/great-expectations/great_expectations/pull/5242)) (thanks @andyjessen)
* [MAINTENANCE] Refactor of `_apply_global_config_overrides()` method to return config ([#5286](https://github.com/great-expectations/great_expectations/pull/5286))
* [MAINTENANCE] Remove "json_serialize" directive from ParameterBuilder computations ([#5320](https://github.com/great-expectations/great_expectations/pull/5320))
* [MAINTENANCE] Misc cleanup post `0.15.10` release ([#5325](https://github.com/great-expectations/great_expectations/pull/5325))
* [MAINTENANCE] Standardize instantiation of NumericMetricRangeMultibatchParameterBuilder throughout the codebase. ([#5327](https://github.com/great-expectations/great_expectations/pull/5327))
* [MAINTENANCE] Reuse MetricMultiBatchParameterBuilder computation results as evaluation dependencies for performance enhancement ([#5329](https://github.com/great-expectations/great_expectations/pull/5329))
* [MAINTENANCE] clean up type declarations ([#5331](https://github.com/great-expectations/great_expectations/pull/5331))
* [MAINTENANCE] Maintenance/great 761/great 1010/great 1011/alexsherstinsky/rule based profiler/data assistant/include only essential public methods in data assistant dispatcher class 2022 06 21 177 ([#5351](https://github.com/great-expectations/great_expectations/pull/5351))
* [MAINTENANCE] Update release schedule JSON ([#5349](https://github.com/great-expectations/great_expectations/pull/5349))
* [MAINTENANCE] Include only essential public methods in DataAssistantResult class (and its descendants) ([#5360](https://github.com/great-expectations/great_expectations/pull/5360))

0.15.10
-----------------
* [FEATURE] `DataContextVariables` CRUD for `stores` ([#5268](https://github.com/great-expectations/great_expectations/pull/5268))
* [FEATURE] `DataContextVariables` CRUD for `data_docs_sites` ([#5269](https://github.com/great-expectations/great_expectations/pull/5269))
* [FEATURE] `DataContextVariables` CRUD for `anonymous_usage_statistics` ([#5271](https://github.com/great-expectations/great_expectations/pull/5271))
* [FEATURE] `DataContextVariables` CRUD for `notebooks`  ([#5272](https://github.com/great-expectations/great_expectations/pull/5272))
* [FEATURE] `DataContextVariables` CRUD for `concurrency` ([#5273](https://github.com/great-expectations/great_expectations/pull/5273))
* [FEATURE] `DataContextVariables` CRUD for `progress_bars` ([#5274](https://github.com/great-expectations/great_expectations/pull/5274))
* [FEATURE] Integrate `DatasourceStore` with `DataContext` ([#5292](https://github.com/great-expectations/great_expectations/pull/5292))
* [FEATURE] Support both UserConfigurableProfiler and OnboardingDataAssistant in "CLI SUITE NEW --PROFILE name" command ([#5306](https://github.com/great-expectations/great_expectations/pull/5306))
* [BUGFIX] Fix ColumnPartition metric handling of the number of bins (must always be integer). ([#5282](https://github.com/great-expectations/great_expectations/pull/5282))
* [BUGFIX] Add new high precision rule for mean and stdev in `OnboardingDataAssistant` ([#5276](https://github.com/great-expectations/great_expectations/pull/5276))
* [BUGFIX] Warning in Getting Started Guide notebook. ([#5297](https://github.com/great-expectations/great_expectations/pull/5297))
* [DOCS] how to create an expectation suite with the onboarding assistant ([#5266](https://github.com/great-expectations/great_expectations/pull/5266))
* [DOCS] update getting started tutorial for onboarding assistant ([#5294](https://github.com/great-expectations/great_expectations/pull/5294))
* [DOCS] getting started tutorial doc standards updates ([#5295](https://github.com/great-expectations/great_expectations/pull/5295))
* [DOCS] Update standard arguments doc for Expectations to not reference datasets. ([#5052](https://github.com/great-expectations/great_expectations/pull/5052))
* [MAINTENANCE] Add check to `check_type_hint_coverage` script to ensure proper `mypy` installation ([#5291](https://github.com/great-expectations/great_expectations/pull/5291))
* [MAINTENANCE] `DataAssistantResult` cleanup and extensibility enhancements ([#5259](https://github.com/great-expectations/great_expectations/pull/5259))
* [MAINTENANCE] Handle compare Expectation in presence of high precision floating point numbers and NaN values ([#5298](https://github.com/great-expectations/great_expectations/pull/5298))
* [MAINTENANCE] Suppress persisting of temporary ExpectationSuite configurations in Rule-Based Profiler computations ([#5305](https://github.com/great-expectations/great_expectations/pull/5305))
* [MAINTENANCE] Adds column values github user validation ([#5302](https://github.com/great-expectations/great_expectations/pull/5302))
* [MAINTENANCE] Adds column values IATA code validation ([#5303](https://github.com/great-expectations/great_expectations/pull/5303))
* [MAINTENANCE] Adds column values ARN validation ([#5304](https://github.com/great-expectations/great_expectations/pull/5304))
* [MAINTENANCE] Fixing a typo in a comment (in several files) ([#5310](https://github.com/great-expectations/great_expectations/pull/5310))
* [MAINTENANCE] Adds column scientific notation string validation ([#5309](https://github.com/great-expectations/great_expectations/pull/5309))
* [MAINTENANCE] lint fixes ([#5312](https://github.com/great-expectations/great_expectations/pull/5312))
* [MAINTENANCE] Adds column value JSON validation ([#5313](https://github.com/great-expectations/great_expectations/pull/5313))
* [MAINTENANCE] Expect column values to be valid scientific notation ([#5311](https://github.com/great-expectations/great_expectations/pull/5311))

0.15.9
-----------------
* [FEATURE] Add new expectation: expect column values to match powers of a base g… ([#5219](https://github.com/great-expectations/great_expectations/pull/5219)) (thanks @rifatKomodoDragon)
* [FEATURE] Replace UserConfigurableProfiler with OnboardingDataAssistant in "CLI suite new --profile" Jupyter Notebooks ([#5236](https://github.com/great-expectations/great_expectations/pull/5236))
* [FEATURE] `DatasourceStore` ([#5206](https://github.com/great-expectations/great_expectations/pull/5206))
* [FEATURE] add new expectation on validating hexadecimals ([#5188](https://github.com/great-expectations/great_expectations/pull/5188)) (thanks @andrewsx)
* [FEATURE] Usage Statistics Events for Profiler and DataAssistant "get_expectation_suite()" methods. ([#5251](https://github.com/great-expectations/great_expectations/pull/5251))
* [FEATURE] `InlineStoreBackend` ([#5216](https://github.com/great-expectations/great_expectations/pull/5216))
* [FEATURE] The "column.histogram" metric must support integer values of the "bins" parameter for all execution engine options. ([#5258](https://github.com/great-expectations/great_expectations/pull/5258))
* [FEATURE] Initial implementation of `DataContextVariables` accessors ([#5238](https://github.com/great-expectations/great_expectations/pull/5238))
* [FEATURE] `OnboardingDataAssistant` plots for `expect_table_columns_to_match_set` ([#5208](https://github.com/great-expectations/great_expectations/pull/5208))
* [FEATURE] `DataContextVariables` CRUD for `config_variables_file_path` ([#5262](https://github.com/great-expectations/great_expectations/pull/5262))
* [FEATURE] `DataContextVariables` CRUD for `plugins_directory` ([#5263](https://github.com/great-expectations/great_expectations/pull/5263))
* [FEATURE] `DataContextVariables` CRUD for store name accessors ([#5264](https://github.com/great-expectations/great_expectations/pull/5264))
* [BUGFIX] Hive temporary tables creation fix ([#4956](https://github.com/great-expectations/great_expectations/pull/4956)) (thanks @jaume-ferrarons)
* [BUGFIX] Provide error handling when metric fails for all Batch data samples ([#5256](https://github.com/great-expectations/great_expectations/pull/5256))
* [BUGFIX] Patch automated release test date comparisons ([#5278](https://github.com/great-expectations/great_expectations/pull/5278))
* [DOCS] How to compare two tables with the UserConfigurableProfiler ([#5050](https://github.com/great-expectations/great_expectations/pull/5050))
* [DOCS] How to create a Custom Column Pair Map Expectation w/ supporting template & example ([#4926](https://github.com/great-expectations/great_expectations/pull/4926))
* [DOCS] Auto API documentation script ([#4964](https://github.com/great-expectations/great_expectations/pull/4964))
* [DOCS] Update formatting of links to public methods in class docs generated by auto API script ([#5247](https://github.com/great-expectations/great_expectations/pull/5247))
* [DOCS] In the reference section of the ToC remove duplicates and update category pages  ([#5248](https://github.com/great-expectations/great_expectations/pull/5248))
* [DOCS] Update DataContext docstring ([#5250](https://github.com/great-expectations/great_expectations/pull/5250))
* [MAINTENANCE] Add CodeSee architecture diagram workflow to repository ([#5235](https://github.com/great-expectations/great_expectations/pull/5235)) (thanks @codesee-maps[bot])
* [MAINTENANCE] Fix links to API docs ([#5246](https://github.com/great-expectations/great_expectations/pull/5246)) (thanks @andyjessen)
* [MAINTENANCE] Unpin cryptography upper bound ([#5249](https://github.com/great-expectations/great_expectations/pull/5249))
* [MAINTENANCE] Don't use jupyter-client 7.3.2 ([#5252](https://github.com/great-expectations/great_expectations/pull/5252))
* [MAINTENANCE] Re-introduce jupyter-client 7.3.2 ([#5253](https://github.com/great-expectations/great_expectations/pull/5253))
* [MAINTENANCE] Add `cloud` mark to `pytest.ini` ([#5254](https://github.com/great-expectations/great_expectations/pull/5254))
* [MAINTENANCE] add partner integration framework ([#5132](https://github.com/great-expectations/great_expectations/pull/5132))
* [MAINTENANCE] `DataContextVariableKey` for use in Stores ([#5255](https://github.com/great-expectations/great_expectations/pull/5255))
* [MAINTENANCE] Clarification of events in test with multiple checkpoint validations ([#5257](https://github.com/great-expectations/great_expectations/pull/5257))
* [MAINTENANCE] Misc updates to improve security and automation of the weekly release process ([#5244](https://github.com/great-expectations/great_expectations/pull/5244))
* [MAINTENANCE] show more test output and minor fixes ([#5239](https://github.com/great-expectations/great_expectations/pull/5239))
* [MAINTENANCE] Add proper unit tests for Column Histogram metric and use Column Value Partitioner in OnboardingDataAssistant ([#5267](https://github.com/great-expectations/great_expectations/pull/5267))
* [MAINTENANCE] Updates contributor docs to reflect updated linting guidance ([#4909](https://github.com/great-expectations/great_expectations/pull/4909))
* [MAINTENANCE] Remove condition from `autoupdate` GitHub action ([#5270](https://github.com/great-expectations/great_expectations/pull/5270))
* [MAINTENANCE] Improve code readability in the processing section of "MapMetricColumnDomainBuilder". ([#5279](https://github.com/great-expectations/great_expectations/pull/5279))

0.15.8
-----------------
* [FEATURE] `OnboardingDataAssistant` plots for `expect_table_row_count_to_be_between` non-sequential batches ([#5212](https://github.com/great-expectations/great_expectations/pull/5212))
* [FEATURE] Limit sampling for spark and pandas ([#5201](https://github.com/great-expectations/great_expectations/pull/5201))
* [FEATURE] Groundwork for DataContext Refactor ([#5203](https://github.com/great-expectations/great_expectations/pull/5203))
* [FEATURE] Implement ability to change rule variable values through DataAssistant run() method arguments at runtime ([#5218](https://github.com/great-expectations/great_expectations/pull/5218))
* [FEATURE] Plot numeric column domains in `OnboardingDataAssistant` ([#5189](https://github.com/great-expectations/great_expectations/pull/5189))
* [BUGFIX] Repair "CLI Suite --Profile" Operation ([#5230](https://github.com/great-expectations/great_expectations/pull/5230))
* [DOCS] Remove leading underscore from sampling docs ([#5214](https://github.com/great-expectations/great_expectations/pull/5214))
* [MAINTENANCE] suppressing type hints in ill-defined situations ([#5213](https://github.com/great-expectations/great_expectations/pull/5213))
* [MAINTENANCE] Change CategoricalColumnDomainBuilder property name from "limit_mode" to "cardinality_limit_mode". ([#5215](https://github.com/great-expectations/great_expectations/pull/5215))
* [MAINTENANCE] Update Note in BigQuery Docs ([#5197](https://github.com/great-expectations/great_expectations/pull/5197))
* [MAINTENANCE] Sampling cleanup refactor (use BatchSpec in sampling methods) ([#5217](https://github.com/great-expectations/great_expectations/pull/5217))
* [MAINTENANCE] Globally increase Azure timeouts to 120 mins ([#5222](https://github.com/great-expectations/great_expectations/pull/5222))
* [MAINTENANCE] Comment out kl_divergence for build_gallery ([#5196](https://github.com/great-expectations/great_expectations/pull/5196))
* [MAINTENANCE] Fix docstring on expectation ([#5204](https://github.com/great-expectations/great_expectations/pull/5204)) (thanks @andyjessen)
* [MAINTENANCE] Improve NaN handling in numeric ParameterBuilder implementations ([#5226](https://github.com/great-expectations/great_expectations/pull/5226))
* [MAINTENANCE] Update type hint and docstring linter thresholds ([#5228](https://github.com/great-expectations/great_expectations/pull/5228))

0.15.7
-----------------
* [FEATURE] Add Rule for TEXT semantic domains within the Onboarding Assistant ([#5144](https://github.com/great-expectations/great_expectations/pull/5144))
* [FEATURE] Helper method to determine whether Expectation is self-initializing  ([#5159](https://github.com/great-expectations/great_expectations/pull/5159))
* [FEATURE] OnboardingDataAssistantResult plotting feature parity with VolumeDataAssistantResult ([#5145](https://github.com/great-expectations/great_expectations/pull/5145))
* [FEATURE] Example Notebook for self-initializing `Expectations` ([#5169](https://github.com/great-expectations/great_expectations/pull/5169))
* [FEATURE] DataAssistant: Enable passing directives to run() method using runtime_environment argument ([#5187](https://github.com/great-expectations/great_expectations/pull/5187))
* [FEATURE] Adding DataAssistantResult.get_expectation_suite(expectation_suite_name) method ([#5191](https://github.com/great-expectations/great_expectations/pull/5191))
* [FEATURE] Cronjob to automatically create release PR ([#5181](https://github.com/great-expectations/great_expectations/pull/5181))
* [BUGFIX] Insure TABLE Domain Metrics Do Not Get Column Key From Column Type Rule Domain Builder ([#5166](https://github.com/great-expectations/great_expectations/pull/5166))
* [BUGFIX] Update name for stdev expectation in `OnboardingDataAssistant` backend ([#5193](https://github.com/great-expectations/great_expectations/pull/5193))
* [BUGFIX] OnboardingDataAssistant and Underlying Metrics: Add Defensive Programming Into Metric Implementations So As To Avoid Warnings About Incompatible Data ([#5195](https://github.com/great-expectations/great_expectations/pull/5195))
* [BUGFIX] Insure that Histogram Metric in Pandas operates on numerical columns that do not have NULL values ([#5199](https://github.com/great-expectations/great_expectations/pull/5199))
* [BUGFIX] RuleBasedProfiler: Ensure that run() method runtime environment directives are handled correctly when existing setting is None (by default) ([#5202](https://github.com/great-expectations/great_expectations/pull/5202))
* [BUGFIX] In aggregate metrics, Spark Implementation already gets Column type as argument -- no need for F.col() as the operand is not a string. ([#5207](https://github.com/great-expectations/great_expectations/pull/5207))
* [DOCS] Update ToC with category links ([#5155](https://github.com/great-expectations/great_expectations/pull/5155))
* [DOCS] update on availability and parameters of conditional expectations ([#5150](https://github.com/great-expectations/great_expectations/pull/5150))
* [MAINTENANCE] Helper method for RBP Notebook tests that does clean-up ([#5171](https://github.com/great-expectations/great_expectations/pull/5171))
* [MAINTENANCE] Increase timeout for longer stages in Azure pipelines ([#5175](https://github.com/great-expectations/great_expectations/pull/5175))
* [MAINTENANCE] Rule-Based Profiler -- In ParameterBuilder insure that metrics are validated for conversion to numpy array (to avoid deprecation warnings) ([#5173](https://github.com/great-expectations/great_expectations/pull/5173))
* [MAINTENANCE] Increase timeout in packaging & installation pipeline ([#5178](https://github.com/great-expectations/great_expectations/pull/5178))
* [MAINTENANCE] OnboardingDataAssistant handle multiple expectations per domain ([#5170](https://github.com/great-expectations/great_expectations/pull/5170))
* [MAINTENANCE] Update timeout in pipelines to fit Azure syntax ([#5180](https://github.com/great-expectations/great_expectations/pull/5180))
* [MAINTENANCE] Error message when `Validator` is instantiated with Incorrect `BatchRequest` ([#5172](https://github.com/great-expectations/great_expectations/pull/5172))
* [MAINTENANCE] Don't include infinity in rendered string for diagnostics ([#5190](https://github.com/great-expectations/great_expectations/pull/5190))
* [MAINTENANCE] Mark Great Expectations Cloud tests and add stage to CI/CD ([#5186](https://github.com/great-expectations/great_expectations/pull/5186))
* [MAINTENANCE] Trigger expectation gallery build with scheduled CI/CD runs ([#5192](https://github.com/great-expectations/great_expectations/pull/5192))
* [MAINTENANCE] `expectation_gallery` Azure pipeline ([#5194](https://github.com/great-expectations/great_expectations/pull/5194))
* [MAINTENANCE] General cleanup/refactor of `DataAssistantResult` ([#5198](https://github.com/great-expectations/great_expectations/pull/5198))

0.15.6
-----------------
* [FEATURE] `NumericMetricRangeMultiBatchParameterBuilder` kernel density estimation ([#5084](https://github.com/great-expectations/great_expectations/pull/5084))
* [FEATURE] Splitters and limit sample work on AWS Athena ([#5024](https://github.com/great-expectations/great_expectations/pull/5024))
* [FEATURE] `ColumnValuesLengthMin` and `ColumnValuesLengthMax` metrics ([#5107](https://github.com/great-expectations/great_expectations/pull/5107))
* [FEATURE] Use `batch_identifiers` in plot tooltips ([#5091](https://github.com/great-expectations/great_expectations/pull/5091))
* [FEATURE] Updated `DataAssistantResult` plotting API ([#5117](https://github.com/great-expectations/great_expectations/pull/5117))
* [FEATURE] Onboarding DataAssistant: Numeric Rules and Relevant Metrics ([#5120](https://github.com/great-expectations/great_expectations/pull/5120))
* [FEATURE] DateTime Rule for OnboardingDataAssistant ([#5121](https://github.com/great-expectations/great_expectations/pull/5121))
* [FEATURE] Categorical Rule is added to OnboardingDataAssistant ([#5134](https://github.com/great-expectations/great_expectations/pull/5134))
* [FEATURE] OnboardingDataAssistant: Introduce MeanTableColumnsSetMatchMultiBatchParameterBuilder (to enable expect_table_columns_to_match_set) ([#5135](https://github.com/great-expectations/great_expectations/pull/5135))
* [FEATURE] Giving the "expect_table_columns_to_match_set" Expectation Self-Initializing Capabilities. ([#5136](https://github.com/great-expectations/great_expectations/pull/5136))
* [FEATURE] For OnboardingDataAssistant: Implement a TABLE Domain level rule to output "expect_table_columns_to_match_set" ([#5137](https://github.com/great-expectations/great_expectations/pull/5137))
* [FEATURE] Enable self-initializing `ExpectColumnValueLengthsToBeBetween` ([#4985](https://github.com/great-expectations/great_expectations/pull/4985))
* [FEATURE] `DataAssistant` plotting for non-sequential batches ([#5126](https://github.com/great-expectations/great_expectations/pull/5126))
* [BUGFIX] Insure that Batch IDs are accessible in the order in which they were loaded in Validator ([#5112](https://github.com/great-expectations/great_expectations/pull/5112))
* [BUGFIX] Update `DataAssistant` notebook for new plotting API ([#5118](https://github.com/great-expectations/great_expectations/pull/5118))
* [BUGFIX] For DataAssistants, added try-except for Notebook tests ([#5124](https://github.com/great-expectations/great_expectations/pull/5124))
* [BUGFIX] CategoricalColumnDomainBuilder needs to accept limit_mode with dictionary type ([#5127](https://github.com/great-expectations/great_expectations/pull/5127))
* [BUGFIX] Use `external_sqldialect` mark to skip during lightweight runs ([#5139](https://github.com/great-expectations/great_expectations/pull/5139))
* [BUGFIX] Use RANDOM_STATE in fixture to make tests deterministic ([#5142](https://github.com/great-expectations/great_expectations/pull/5142))
* [BUGFIX] Read deployment_version instead of using versioneer in deprecation tests ([#5147](https://github.com/great-expectations/great_expectations/pull/5147))
* [MAINTENANCE] DataAssistant: Refactoring Access to common ParameterBuilder instances ([#5108](https://github.com/great-expectations/great_expectations/pull/5108))
* [MAINTENANCE] Refactor of`MetricTypes` and `AttributedResolvedMetrics` ([#5100](https://github.com/great-expectations/great_expectations/pull/5100))
* [MAINTENANCE] Remove references to show_cta_footer except in schemas.py ([#5111](https://github.com/great-expectations/great_expectations/pull/5111))
* [MAINTENANCE] Adding unit tests for sqlalchemy limit sampler part 1 ([#5109](https://github.com/great-expectations/great_expectations/pull/5109))
* [MAINTENANCE] Don't re-raise connection errors in CI ([#5115](https://github.com/great-expectations/great_expectations/pull/5115))
* [MAINTENANCE] Sqlite specific tests for splitting and sampling ([#5119](https://github.com/great-expectations/great_expectations/pull/5119))
* [MAINTENANCE] Add Trino dialect in SqlAlchemyDataset ([#5085](https://github.com/great-expectations/great_expectations/pull/5085)) (thanks @ms32035)
* [MAINTENANCE] Move upper bound on sqlalchemy to <2.0.0. ([#5140](https://github.com/great-expectations/great_expectations/pull/5140))
* [MAINTENANCE] Update primary pipeline to cut releases with tags ([#5128](https://github.com/great-expectations/great_expectations/pull/5128))
* [MAINTENANCE] Improve handling of "expect_column_unique_values_count_to_be_between" in VolumeDataAssistant ([#5146](https://github.com/great-expectations/great_expectations/pull/5146))
* [MAINTENANCE] Simplify DataAssistant Operation to not Depend on Self-Initializing Expectations ([#5148](https://github.com/great-expectations/great_expectations/pull/5148))
* [MAINTENANCE] Improvements to Trino support ([#5152](https://github.com/great-expectations/great_expectations/pull/5152))
* [MAINTENANCE] Update how_to_configure_a_new_checkpoint_using_test_yaml_config.md ([#5157](https://github.com/great-expectations/great_expectations/pull/5157))
* [MAINTENANCE] Speed up the site builder ([#5125](https://github.com/great-expectations/great_expectations/pull/5125)) (thanks @tanelk)
* [MAINTENANCE] remove account id deprecation notice ([#5158](https://github.com/great-expectations/great_expectations/pull/5158))

0.15.5
-----------------
* [FEATURE] Add subset operation to Domain class ([#5049](https://github.com/great-expectations/great_expectations/pull/5049))
* [FEATURE] In DataAssistant: Use Domain instead of domain_type as key for Metrics Parameter Builders ([#5057](https://github.com/great-expectations/great_expectations/pull/5057))
* [FEATURE] Self-initializing `ExpectColumnStddevToBeBetween` ([#5065](https://github.com/great-expectations/great_expectations/pull/5065))
* [FEATURE] Enum used by DateSplitter able to be represented as YAML ([#5073](https://github.com/great-expectations/great_expectations/pull/5073))
* [FEATURE] Implementation of auto-complete for DataAssistant class names in Jupyter notebooks ([#5077](https://github.com/great-expectations/great_expectations/pull/5077))
* [FEATURE] Provide display ("friendly") names for batch identifiers ([#5086](https://github.com/great-expectations/great_expectations/pull/5086))
* [FEATURE] Onboarding DataAssistant -- Initial Rule Implementations (Data Aspects) ([#5101](https://github.com/great-expectations/great_expectations/pull/5101))
* [FEATURE] OnboardingDataAssistant: Implement Nullity/Non-nullity Rules and Associated Metrics ([#5104](https://github.com/great-expectations/great_expectations/pull/5104))
* [BUGFIX] `self_check()` now also checks for `aws_config_file` ([#5040](https://github.com/great-expectations/great_expectations/pull/5040))
* [BUGFIX] `multi_batch_rule_based_profiler` test up to date with RBP changes ([#5066](https://github.com/great-expectations/great_expectations/pull/5066))
* [BUGFIX] Splitting Support at Asset level ([#5026](https://github.com/great-expectations/great_expectations/pull/5026))
* [BUGFIX] Make self-initialization in expect_column_values_to_be_between truly multi batch ([#5068](https://github.com/great-expectations/great_expectations/pull/5068))
* [BUGFIX] databricks engine create temporary view ([#4994](https://github.com/great-expectations/great_expectations/pull/4994)) (thanks @gvillafanetapia)
* [BUGFIX] Patch broken Expectation gallery script ([#5090](https://github.com/great-expectations/great_expectations/pull/5090))
* [BUGFIX] Sampling support at asset level ([#5092](https://github.com/great-expectations/great_expectations/pull/5092))
* [DOCS] Update process and configurations in OpenLineage Action guide. ([#5039](https://github.com/great-expectations/great_expectations/pull/5039))
* [DOCS] Update process and config examples in Opsgenie guide ([#5037](https://github.com/great-expectations/great_expectations/pull/5037))
* [DOCS] Correct name of `openlineage-integration-common` package ([#5041](https://github.com/great-expectations/great_expectations/pull/5041)) (thanks @mobuchowski)
* [DOCS] Remove reference to validation operator process from how to trigger slack notifications guide ([#5034](https://github.com/great-expectations/great_expectations/pull/5034))
* [DOCS] Update process and configuration examples in email Action guide. ([#5036](https://github.com/great-expectations/great_expectations/pull/5036))
* [DOCS] Update Docusaurus version ([#5063](https://github.com/great-expectations/great_expectations/pull/5063))
* [MAINTENANCE] Saved output of usage stats schema script in repo ([#5053](https://github.com/great-expectations/great_expectations/pull/5053))
* [MAINTENANCE] Apply Altair custom themes to return objects ([#5044](https://github.com/great-expectations/great_expectations/pull/5044))
* [MAINTENANCE] Introducing RuleBasedProfilerResult -- neither expectation suite name nor expectation suite must be passed to RuleBasedProfiler.run() ([#5061](https://github.com/great-expectations/great_expectations/pull/5061))
* [MAINTENANCE] Refactor `DataAssistant` plotting to leverage utility dataclasses ([#5022](https://github.com/great-expectations/great_expectations/pull/5022))
* [MAINTENANCE] Check that a passed string is parseable as an integer (mssql limit param) ([#5071](https://github.com/great-expectations/great_expectations/pull/5071))
* [MAINTENANCE] Clean up mssql limit sampling code path and comments ([#5074](https://github.com/great-expectations/great_expectations/pull/5074))
* [MAINTENANCE] Make saving bootstraps histogram for NumericMetricRangeMultiBatchParameterBuilder  optional (absent by default) ([#5075](https://github.com/great-expectations/great_expectations/pull/5075))
* [MAINTENANCE] Make self-initializing expectations return estimated kwargs with auto-generation timestamp and Great Expectation version ([#5076](https://github.com/great-expectations/great_expectations/pull/5076))
* [MAINTENANCE] Adding a unit test for batch_id mapping to batch display names ([#5087](https://github.com/great-expectations/great_expectations/pull/5087))
* [MAINTENANCE] `pypandoc` version constraint added (`< 1.8`) ([#5093](https://github.com/great-expectations/great_expectations/pull/5093))
* [MAINTENANCE] Utilize Rule objects in Profiler construction in DataAssistant ([#5089](https://github.com/great-expectations/great_expectations/pull/5089))
* [MAINTENANCE] Turn off metric calculation progress bars in `RuleBasedProfiler` and `DataAssistant` workflows ([#5080](https://github.com/great-expectations/great_expectations/pull/5080))
* [MAINTENANCE] A small refactor of ParamerBuilder management used in DataAssistant classes ([#5102](https://github.com/great-expectations/great_expectations/pull/5102))
* [MAINTENANCE] Convenience method refactor for Onboarding DataAssistant ([#5103](https://github.com/great-expectations/great_expectations/pull/5103))

0.15.4
-----------------
* [FEATURE] Enable self-initializing `ExpectColumnMeanToBeBetween` ([#4986](https://github.com/great-expectations/great_expectations/pull/4986))
* [FEATURE] Enable self-initializing `ExpectColumnMedianToBeBetween` ([#4987](https://github.com/great-expectations/great_expectations/pull/4987))
* [FEATURE] Enable self-initializing `ExpectColumnSumToBeBetween` ([#4988](https://github.com/great-expectations/great_expectations/pull/4988))
* [FEATURE] New MetricSingleBatchParameterBuilder for specifically single-Batch Rule-Based Profiler scenarios ([#5003](https://github.com/great-expectations/great_expectations/pull/5003))
* [FEATURE] Enable Pandas DataFrame and Series as MetricValues Output of Metric ParameterBuilder Classes ([#5008](https://github.com/great-expectations/great_expectations/pull/5008))
* [FEATURE] Notebook for `VolumeDataAssistant` Example ([#5010](https://github.com/great-expectations/great_expectations/pull/5010))
* [FEATURE] Histogram/Partition Single-Batch ParameterBuilder ([#5011](https://github.com/great-expectations/great_expectations/pull/5011))
* [FEATURE] Update `DataAssistantResult.plot()` return value to emit `PlotResult` wrapper dataclass ([#4962](https://github.com/great-expectations/great_expectations/pull/4962))
* [FEATURE] Limit samplers work with supported sqlalchemy backends ([#5014](https://github.com/great-expectations/great_expectations/pull/5014))
* [FEATURE] trino support ([#5021](https://github.com/great-expectations/great_expectations/pull/5021))
* [BUGFIX] RBP Profiling Dataset ProgressBar Fix ([#4999](https://github.com/great-expectations/great_expectations/pull/4999))
* [BUGFIX] Fix DataAssistantResult serialization issue ([#5020](https://github.com/great-expectations/great_expectations/pull/5020))
* [DOCS] Update slack notification guide to not use validation operators. ([#4978](https://github.com/great-expectations/great_expectations/pull/4978))
* [MAINTENANCE] Update `autoupdate` GitHub action ([#5001](https://github.com/great-expectations/great_expectations/pull/5001))
* [MAINTENANCE] Move `DataAssistant` registry capabilities into `DataAssistantRegistry` to enable user aliasing ([#4991](https://github.com/great-expectations/great_expectations/pull/4991))
* [MAINTENANCE] Fix continuous partition example ([#4939](https://github.com/great-expectations/great_expectations/pull/4939)) (thanks @andyjessen)
* [MAINTENANCE] Preliminary refactors for data samplers. ([#4996](https://github.com/great-expectations/great_expectations/pull/4996))
* [MAINTENANCE] Clean up unused imports and enforce through `flake8` in CI/CD ([#5005](https://github.com/great-expectations/great_expectations/pull/5005))
* [MAINTENANCE] ParameterBuilder tests should maximally utilize polymorphism ([#5007](https://github.com/great-expectations/great_expectations/pull/5007))
* [MAINTENANCE] Clean up type hints in CLI ([#5006](https://github.com/great-expectations/great_expectations/pull/5006))
* [MAINTENANCE] Making ParameterBuilder metric computations robust to failures through logging and exception handling ([#5009](https://github.com/great-expectations/great_expectations/pull/5009))
* [MAINTENANCE] Condense column-level `vconcat` plots into one interactive plot ([#5002](https://github.com/great-expectations/great_expectations/pull/5002))
* [MAINTENANCE] Update version of `black` in pre-commit config ([#5019](https://github.com/great-expectations/great_expectations/pull/5019))
* [MAINTENANCE] Improve tooltips and formatting for distinct column values chart in VolumeDataAssistantResult ([#5017](https://github.com/great-expectations/great_expectations/pull/5017))
* [MAINTENANCE] Enhance configuring serialization for DotDict type classes ([#5023](https://github.com/great-expectations/great_expectations/pull/5023))
* [MAINTENANCE] Pyarrow upper bound ([#5028](https://github.com/great-expectations/great_expectations/pull/5028))

0.15.3
-----------------
* [FEATURE] Enable self-initializing capabilities for `ExpectColumnProportionOfUniqueValuesToBeBetween` ([#4929](https://github.com/great-expectations/great_expectations/pull/4929))
* [FEATURE] Enable support for plotting both Table and Column charts in `VolumeDataAssistant` ([#4930](https://github.com/great-expectations/great_expectations/pull/4930))
* [FEATURE] BigQuery Temp Table Support ([#4925](https://github.com/great-expectations/great_expectations/pull/4925))
* [FEATURE] Registry for DataAssistant classes with ability to execute from DataContext by registered name ([#4966](https://github.com/great-expectations/great_expectations/pull/4966))
* [FEATURE] Enable self-intializing capabilities for `ExpectColumnValuesToMatchRegex`/`ExpectColumnValuesToNotMatchRegex` ([#4958](https://github.com/great-expectations/great_expectations/pull/4958))
* [FEATURE] Provide "estimation histogram" ParameterBuilder output details . ([#4975](https://github.com/great-expectations/great_expectations/pull/4975))
* [FEATURE] Enable self-initializing `ExpectColumnValuesToMatchStrftimeFormat` ([#4977](https://github.com/great-expectations/great_expectations/pull/4977))
* [BUGFIX] check contrib requirements ([#4922](https://github.com/great-expectations/great_expectations/pull/4922))
* [BUGFIX] Use `monkeypatch` to set a consistent bootstrap seed in tests ([#4960](https://github.com/great-expectations/great_expectations/pull/4960))
* [BUGFIX] Make all Builder Configuration classes of Rule-Based Profiler Configuration Serializable ([#4972](https://github.com/great-expectations/great_expectations/pull/4972))
* [BUGFIX] extras_require ([#4968](https://github.com/great-expectations/great_expectations/pull/4968))
* [BUGFIX] Fix broken packaging test and update `dgtest-overrides` ([#4976](https://github.com/great-expectations/great_expectations/pull/4976))
* [MAINTENANCE] Add timeout to `great_expectations` pipeline stages to prevent false positive build failures ([#4957](https://github.com/great-expectations/great_expectations/pull/4957))
* [MAINTENANCE] Defining Common Test Fixtures for DataAssistant Testing ([#4959](https://github.com/great-expectations/great_expectations/pull/4959))
* [MAINTENANCE] Temporarily pin `cryptography` package ([#4963](https://github.com/great-expectations/great_expectations/pull/4963))
* [MAINTENANCE] Type annotate relevant functions with `-> None` (per PEP 484) ([#4969](https://github.com/great-expectations/great_expectations/pull/4969))
* [MAINTENANCE] Handle edge cases where `false_positive_rate` is not in range [0, 1] or very close to bounds ([#4946](https://github.com/great-expectations/great_expectations/pull/4946))
* [MAINTENANCE] fix a typo  ([#4974](https://github.com/great-expectations/great_expectations/pull/4974))

0.15.2
-----------------
* [FEATURE] Split data assets using sql datetime columns ([#4871](https://github.com/great-expectations/great_expectations/pull/4871))
* [FEATURE] Plot metrics with `DataAssistantResult.plot()` ([#4873](https://github.com/great-expectations/great_expectations/pull/4873))
* [FEATURE] RuleBasedProfiler/DataAssistant/MetricMultiBatchParameterBuilder: Enable Returning Metric Computation Results with batch_id Attribution ([#4862](https://github.com/great-expectations/great_expectations/pull/4862))
* [FEATURE] Enable variables to be specified at both Profiler and its constituent individual Rule levels ([#4912](https://github.com/great-expectations/great_expectations/pull/4912))
* [FEATURE] Enable self-initializing `ExpectColumnUniqueValueCountToBeBetween` ([#4902](https://github.com/great-expectations/great_expectations/pull/4902))
* [FEATURE] Improve diagnostic testing process ([#4816](https://github.com/great-expectations/great_expectations/pull/4816))
* [FEATURE] Add Azure CI/CD action to aid with style guide enforcement (type hints) ([#4878](https://github.com/great-expectations/great_expectations/pull/4878))
* [FEATURE] Add Azure CI/CD action to aid with style guide enforcement (docstrings) ([#4617](https://github.com/great-expectations/great_expectations/pull/4617))
* [FEATURE] Use formal interfaces to clean up DataAssistant and DataAssistantResult modules/classes ([#4901](https://github.com/great-expectations/great_expectations/pull/4901))
* [BUGFIX] fix validation issue for column domain type and implement expect_column_unique_value_count_to_be_between for VolumeDataAssistant ([#4914](https://github.com/great-expectations/great_expectations/pull/4914))
* [BUGFIX] Fix issue with not using the generated table name on read ([#4905](https://github.com/great-expectations/great_expectations/pull/4905))
* [BUGFIX] Add deprecation comment to RuntimeDataConnector
* [BUGFIX] Ensure proper class_name within all RuleBasedProfilerConfig instantiations
* [BUGFIX] fix rounding directive handling ([#4887](https://github.com/great-expectations/great_expectations/pull/4887))
* [BUGFIX] `great_expectations` import fails when SQL Alchemy is not installed ([#4880](https://github.com/great-expectations/great_expectations/pull/4880))
* [MAINTENANCE] Altair types cleanup ([#4916](https://github.com/great-expectations/great_expectations/pull/4916))
* [MAINTENANCE] test: update test time ([#4911](https://github.com/great-expectations/great_expectations/pull/4911))
* [MAINTENANCE] Add module docstring and simplify access to DatePart ([#4910](https://github.com/great-expectations/great_expectations/pull/4910))
* [MAINTENANCE] Chip away at type hint violations around data context ([#4897](https://github.com/great-expectations/great_expectations/pull/4897))
* [MAINTENANCE] Improve error message outputted to user in DocstringChecker action ([#4895](https://github.com/great-expectations/great_expectations/pull/4895))
* [MAINTENANCE] Re-enable bigquery tests ([#4903](https://github.com/great-expectations/great_expectations/pull/4903))
* [MAINTENANCE] Unit tests for sqlalchemy splitter methods, docs and other improvements ([#4900](https://github.com/great-expectations/great_expectations/pull/4900))
* [MAINTENANCE] Move plot logic from `DataAssistant` into `DataAssistantResult` ([#4896](https://github.com/great-expectations/great_expectations/pull/4896))
* [MAINTENANCE] Add condition to primary pipeline to ensure `import_ge` stage doesn't cause misleading Slack notifications ([#4898](https://github.com/great-expectations/great_expectations/pull/4898))
* [MAINTENANCE] Refactor `RuleBasedProfilerConfig` ([#4882](https://github.com/great-expectations/great_expectations/pull/4882))
* [MAINTENANCE] Refactor DataAssistant Access to Parameter Computation Results and Plotting Utilities ([#4893](https://github.com/great-expectations/great_expectations/pull/4893))
* [MAINTENANCE] Update `dgtest-overrides` list to include all test files not captured by primary strategy ([#4891](https://github.com/great-expectations/great_expectations/pull/4891))
* [MAINTENANCE] Add dgtest-overrides section to dependency_graph Azure pipeline
* [MAINTENANCE] Datasource and DataContext-level tests for RuntimeDataConnector changes ([#4866](https://github.com/great-expectations/great_expectations/pull/4866))
* [MAINTENANCE] Temporarily disable bigquery tests. ([#4888](https://github.com/great-expectations/great_expectations/pull/4888))
* [MAINTENANCE] Import GE after running `ge init` in packaging CI pipeline ([#4885](https://github.com/great-expectations/great_expectations/pull/4885))
* [MAINTENANCE] Add CI stage importing GE with only required dependencies installed ([#4884](https://github.com/great-expectations/great_expectations/pull/4884))
* [MAINTENANCE] `DataAssistantResult.plot()` conditional formatting and tooltips ([#4881](https://github.com/great-expectations/great_expectations/pull/4881))
* [MAINTENANCE] split data context files ([#4879](https://github.com/great-expectations/great_expectations/pull/4879))
* [MAINTENANCE] Add Tanner to CODEOWNERS for schemas.py ([#4875](https://github.com/great-expectations/great_expectations/pull/4875))
* [MAINTENANCE]  Use defined constants for ParameterNode accessor keys ([#4872](https://github.com/great-expectations/great_expectations/pull/4872))

0.15.1
-----------------
* [FEATURE] Additional Rule-Based Profiler Parameter/Variable Access Methods ([#4814](https://github.com/great-expectations/great_expectations/pull/4814))
* [FEATURE] DataAssistant and VolumeDataAssistant classes (initial implementation -- to be enhanced as part of subsequent work) ([#4844](https://github.com/great-expectations/great_expectations/pull/4844))
* [FEATURE] Add Support for Returning Parameters and Metrics as DataAssistantResult class ([#4848](https://github.com/great-expectations/great_expectations/pull/4848))
* [FEATURE] DataAssistantResult Includes Underlying Profiler Execution Time ([#4854](https://github.com/great-expectations/great_expectations/pull/4854))
* [FEATURE] Add batch_id for every resolved metric_value to ParameterBuilder.get_metrics() result object ([#4860](https://github.com/great-expectations/great_expectations/pull/4860))
* [FEATURE] `RuntimeDataConnector` able to specify `Assets` ([#4861](https://github.com/great-expectations/great_expectations/pull/4861))
* [BUGFIX] Linting error from hackathon automerge ([#4829](https://github.com/great-expectations/great_expectations/pull/4829))
* [BUGFIX] Cleanup contrib ([#4838](https://github.com/great-expectations/great_expectations/pull/4838))
* [BUGFIX] Add `notebook` to `GE_REQUIRED_DEPENDENCIES` ([#4842](https://github.com/great-expectations/great_expectations/pull/4842))
* [BUGFIX] ParameterContainer return value formatting bug fix ([#4840](https://github.com/great-expectations/great_expectations/pull/4840))
* [BUGFIX] Ensure that Parameter Validation/Configuration Dependency Configurations are included in Serialization ([#4843](https://github.com/great-expectations/great_expectations/pull/4843))
* [BUGFIX] Correctly handle SQLA unexpected count metric for empty tables ([#4618](https://github.com/great-expectations/great_expectations/pull/4618)) (thanks @douglascook)
* [BUGFIX] Temporarily adjust Deprecation Warning Count ([#4869](https://github.com/great-expectations/great_expectations/pull/4869))
* [DOCS] How to validate data with an in memory checkpoint ([#4820](https://github.com/great-expectations/great_expectations/pull/4820))
* [DOCS] Update all tutorial redirect fix ([#4841](https://github.com/great-expectations/great_expectations/pull/4841))
* [DOCS] redirect/remove dead links in docs ([#4846](https://github.com/great-expectations/great_expectations/pull/4846))
* [MAINTENANCE] Refactor Rule-Based Profiler instantiation in Validator to make it available as a public method ([#4823](https://github.com/great-expectations/great_expectations/pull/4823))
* [MAINTENANCE] String Type is not needed as Return Type from DomainBuilder.domain_type() ([#4827](https://github.com/great-expectations/great_expectations/pull/4827))
* [MAINTENANCE] Fix Typo in Checkpoint Readme ([#4835](https://github.com/great-expectations/great_expectations/pull/4835)) (thanks @andyjessen)
* [MAINTENANCE] Modify conditional expectations readme ([#4616](https://github.com/great-expectations/great_expectations/pull/4616)) (thanks @andyjessen)
* [MAINTENANCE] Fix links within datasource new notebook ([#4833](https://github.com/great-expectations/great_expectations/pull/4833)) (thanks @andyjessen)
* [MAINTENANCE] Adds missing dependency, which is breaking CLI workflows ([#4839](https://github.com/great-expectations/great_expectations/pull/4839))
* [MAINTENANCE] Update testing and documentation for `oneshot` estimation method ([#4852](https://github.com/great-expectations/great_expectations/pull/4852))
* [MAINTENANCE] Refactor `Datasource` tests that work with `RuntimeDataConnector` by backend.  ([#4853](https://github.com/great-expectations/great_expectations/pull/4853))
* [MAINTENANCE] Update DataAssistant interfaces ([#4857](https://github.com/great-expectations/great_expectations/pull/4857))
* [MAINTENANCE] Improve types returned by DataAssistant interface methods ([#4859](https://github.com/great-expectations/great_expectations/pull/4859))
* [MAINTENANCE] Refactor `DataContext` tests that work with RuntimeDataConnector by backend ([#4858](https://github.com/great-expectations/great_expectations/pull/4858))
* [HACKATHON] `Hackathon PRs in this release <https://github.com/great-expectations/great_expectations/pulls?q=is%3Apr+label%3Ahackathon-2022+is%3Amerged+-updated%3A%3E%3D2022-04-14+-updated%3A%3C%3D2022-04-06>`

0.15.0
-----------------
* [BREAKING] EOL Python 3.6 ([#4567](https://github.com/great-expectations/great_expectations/pull/4567))
* [FEATURE] Implement Multi-Column Domain Builder for Rule-Based Profiler ([#4604](https://github.com/great-expectations/great_expectations/pull/4604))
* [FEATURE] Update RBP notebook to include example for Multi-Column Domain Builder ([#4606](https://github.com/great-expectations/great_expectations/pull/4606))
* [FEATURE] Rule-Based Profiler: ColumnPairDomainBuilder ([#4608](https://github.com/great-expectations/great_expectations/pull/4608))
* [FEATURE] More package contrib info ([#4693](https://github.com/great-expectations/great_expectations/pull/4693))
* [FEATURE] Introducing RuleState class and RuleOutput class for Rule-Based Profiler in support of richer use cases (such as DataAssistant). ([#4704](https://github.com/great-expectations/great_expectations/pull/4704))
* [FEATURE] Add support for returning fully-qualified parameters names/values from RuleOutput object ([#4773](https://github.com/great-expectations/great_expectations/pull/4773))
* [BUGFIX] Pass random seed to bootstrap estimator ([#4605](https://github.com/great-expectations/great_expectations/pull/4605))
* [BUGFIX] Adjust output of `regex` ParameterBuilder to match Expectation ([#4594](https://github.com/great-expectations/great_expectations/pull/4594))
* [BUGFIX] Rule-Based Profiler: Only primitive type based BatchRequest is allowed for Builder classes ([#4614](https://github.com/great-expectations/great_expectations/pull/4614))
* [BUGFIX] Fix DataContext templates test ([#4678](https://github.com/great-expectations/great_expectations/pull/4678))
* [BUGFIX] update module_name in NoteBookConfigSchema from v2 path to v3 ([#4589](https://github.com/great-expectations/great_expectations/pull/4589)) (thanks @Josephmaclean)
* [BUGFIX] request S3 bucket location only when necessary ([#4526](https://github.com/great-expectations/great_expectations/pull/4526)) (thanks @error418)
* [DOCS] Update `ignored_columns` snippet in "Getting Started" ([#4609](https://github.com/great-expectations/great_expectations/pull/4609))
* [DOCS] Fixes import statement.  ([#4694](https://github.com/great-expectations/great_expectations/pull/4694))
* [DOCS] Update tutorial_review.md typo with intended word. ([#4611](https://github.com/great-expectations/great_expectations/pull/4611)) (thanks @cjbramble)
* [DOCS] Correct typo in url in docstring for set_based_column_map_expectation_template.py (example script) ([#4817](https://github.com/great-expectations/great_expectations/pull/4817))
* [MAINTENANCE] Add retries to `requests` in usage stats integration tests ([#4600](https://github.com/great-expectations/great_expectations/pull/4600))
* [MAINTENANCE] Miscellaneous test cleanup ([#4602](https://github.com/great-expectations/great_expectations/pull/4602))
* [MAINTENANCE] Simplify ParameterBuilder.build_parameter() interface ([#4622](https://github.com/great-expectations/great_expectations/pull/4622))
* [MAINTENANCE] War on Warnings - DataContext ([#4572](https://github.com/great-expectations/great_expectations/pull/4572))
* [MAINTENANCE] Update links within great_expectations.yml ([#4549](https://github.com/great-expectations/great_expectations/pull/4549)) (thanks @andyjessen)
* [MAINTENANCE] Provide cardinality limit modes from CategoricalColumnDomainBuilder ([#4662](https://github.com/great-expectations/great_expectations/pull/4662))
* [MAINTENANCE] Rule-Based Profiler: Rename Rule.generate() to Rule.run() ([#4670](https://github.com/great-expectations/great_expectations/pull/4670))
* [MAINTENANCE] Refactor ValidationParameter computation (to be more elegant/compact) and fix a type hint in SimpleDateFormatStringParameterBuilder ([#4687](https://github.com/great-expectations/great_expectations/pull/4687))
* [MAINTENANCE] Remove `pybigquery` check that is no longer needed ([#4681](https://github.com/great-expectations/great_expectations/pull/4681))
* [MAINTENANCE] Rule-Based Profiler: Allow ExpectationConfigurationBuilder to be Optional ([#4698](https://github.com/great-expectations/great_expectations/pull/4698))
* [MAINTENANCE] Slightly Clean Up NumericMetricRangeMultiBatchParameterBuilder ([#4699](https://github.com/great-expectations/great_expectations/pull/4699))
* [MAINTENANCE] ParameterBuilder must not recompute its value, if it already exists in RuleState (ParameterContainer for its Domain). ([#4701](https://github.com/great-expectations/great_expectations/pull/4701))
* [MAINTENANCE] Improve get validator functionality ([#4661](https://github.com/great-expectations/great_expectations/pull/4661))
* [MAINTENANCE] Add checks for mostly=1.0 for all renderers ([#4736](https://github.com/great-expectations/great_expectations/pull/4736))
* [MAINTENANCE] revert to not raising datasource errors on data context init ([#4732](https://github.com/great-expectations/great_expectations/pull/4732))
* [MAINTENANCE] Remove unused bootstrap methods that were migrated to ML Flow ([#4742](https://github.com/great-expectations/great_expectations/pull/4742))
* [MAINTENANCE] Update README.md ([#4595](https://github.com/great-expectations/great_expectations/pull/4595)) (thanks @andyjessen)
* [MAINTENANCE] Check for mostly equals 1 in renderers ([#4815](https://github.com/great-expectations/great_expectations/pull/4815))
* [MAINTENANCE] Remove bootstrap tests that are no longer needed ([#4818](https://github.com/great-expectations/great_expectations/pull/4818))
* [HACKATHON] ExpectColumnValuesToBeIsoLanguages ([#4627](https://github.com/great-expectations/great_expectations/pull/4627)) (thanks @szecsip)
* [HACKATHON] ExpectColumnAverageLatLonPairwiseDistanceToBeLessThan ([#4559](https://github.com/great-expectations/great_expectations/pull/4559)) (thanks @mmi333)
* [HACKATHON] ExpectColumnValuesToBeValidIPv6 ([#4561](https://github.com/great-expectations/great_expectations/pull/4561)) (thanks @voidforall)
* [HACKATHON] ExpectColumnValuesToBeValidMac ([#4562](https://github.com/great-expectations/great_expectations/pull/4562)) (thanks @voidforall)
* [HACKATHON] ExpectColumnValuesToBeValidMIME ([#4563](https://github.com/great-expectations/great_expectations/pull/4563)) (thanks @voidforall)
* [HACKATHON] ExpectColumnValuesToBeValidHexColor ([#4564](https://github.com/great-expectations/great_expectations/pull/4564)) (thanks @voidforall)
* [HACKATHON] ExpectColumnValuesToBeValidIban ([#4565](https://github.com/great-expectations/great_expectations/pull/4565)) (thanks @voidforall)
* [HACKATHON] ExpectColumnValuesToBeValidIsoCountry ([#4566](https://github.com/great-expectations/great_expectations/pull/4566)) (thanks @voidforall)
* [HACKATHON] add expect_column_values_to_be_private_ipv4_class ([#4656](https://github.com/great-expectations/great_expectations/pull/4656)) (thanks @szecsip)
* [HACKATHON] Feature/expect column values url hostname match with cert ([#4649](https://github.com/great-expectations/great_expectations/pull/4649)) (thanks @szecsip)
* [HACKATHON] add expect_column_values_url_has_got_valid_cert ([#4648](https://github.com/great-expectations/great_expectations/pull/4648)) (thanks @szecsip)
* [HACKATHON] add expect_column_values_to_be_valid_us_state_or_territory ([#4655](https://github.com/great-expectations/great_expectations/pull/4655)) (thanks @Derekma73)
* [HACKATHON] ExpectColumnValuesToBeValidSsn ([#4646](https://github.com/great-expectations/great_expectations/pull/4646)) (thanks @voidforall)
* [HACKATHON] ExpectColumnValuesToBeValidHttpStatusName ([#4645](https://github.com/great-expectations/great_expectations/pull/4645)) (thanks @voidforall)
* [HACKATHON] ExpectColumnValuesToBeValidHttpStatusCode ([#4644](https://github.com/great-expectations/great_expectations/pull/4644)) (thanks @voidforall)
* [HACKATHON] Feature/expect column values to be daytime ([#4643](https://github.com/great-expectations/great_expectations/pull/4643)) (thanks @szecsip)
* [HACKATHON] add expect_column_values_ip_address_in_network ([#4640](https://github.com/great-expectations/great_expectations/pull/4640)) (thanks @szecsip)
* [HACKATHON] add expect_column_values_ip_asn_country_code_in_set ([#4638](https://github.com/great-expectations/great_expectations/pull/4638)) (thanks @szecsip)
* [HACKATHON] add expect_column_values_to_be_valid_us_state ([#4654](https://github.com/great-expectations/great_expectations/pull/4654)) (thanks @Derekma73)
* [HACKATHON] add expect_column_values_to_be_valid_us_state_or_territory_abbreviation ([#4653](https://github.com/great-expectations/great_expectations/pull/4653)) (thanks @Derekma73)
* [HACKATHON] add expect_column_values_to_be_weekday ([#4636](https://github.com/great-expectations/great_expectations/pull/4636)) (thanks @szecsip)
* [HACKATHON] add expect_column_values_to_be_valid_us_state_abbrevation ([#4650](https://github.com/great-expectations/great_expectations/pull/4650)) (thanks @Derekma73)
* [HACKATHON] ExpectColumnValuesGeometryDistanceToAddressToBeBetween ([#4652](https://github.com/great-expectations/great_expectations/pull/4652)) (thanks @pjdobson)
* [HACKATHON] ExpectColumnValuesToBeValidUdpPort ([#4635](https://github.com/great-expectations/great_expectations/pull/4635)) (thanks @voidforall)
* [HACKATHON] add expect_column_values_to_be_fibonacci_number ([#4629](https://github.com/great-expectations/great_expectations/pull/4629)) (thanks @szecsip)
* [HACKATHON] add expect_column_values_to_be_slug ([#4628](https://github.com/great-expectations/great_expectations/pull/4628)) (thanks @szecsip)
* [HACKATHON] ExpectColumnValuesGeometryToBeWithinPlace ([#4626](https://github.com/great-expectations/great_expectations/pull/4626)) (thanks @pjdobson)
* [HACKATHON] add expect_column_values_to_be_private_ipv6 ([#4624](https://github.com/great-expectations/great_expectations/pull/4624)) (thanks @szecsip)
* [HACKATHON] add expect_column_values_to_be_private_ip_v4  ([#4623](https://github.com/great-expectations/great_expectations/pull/4623)) (thanks @szecsip)
* [HACKATHON] ExpectColumnValuesToBeValidPrice ([#4593](https://github.com/great-expectations/great_expectations/pull/4593)) (thanks @voidforall)
* [HACKATHON] ExpectColumnValuesToBeValidPhonenumber ([#4592](https://github.com/great-expectations/great_expectations/pull/4592)) (thanks @voidforall)
* [HACKATHON] ExpectColumnValuesToBePolygonAreaBetween ([#4591](https://github.com/great-expectations/great_expectations/pull/4591)) (thanks @mmi333)
* [HACKATHON] ExpectColumnValuesToBeValidTcpPort ([#4634](https://github.com/great-expectations/great_expectations/pull/4634)) (thanks @voidforall)


0.14.13
-----------------
* [FEATURE] Convert Existing Self-Initializing Expectations to Make ExpectationConfigurationBuilder Self-Contained with its own validation_parameter_builder settings ([#4547](https://github.com/great-expectations/great_expectations/pull/4547))
* [FEATURE] Improve diagnostic checklist details ([#4548](https://github.com/great-expectations/great_expectations/pull/4548))
* [BUGFIX] Moves testing dependencies out of core reqs ([#4522](https://github.com/great-expectations/great_expectations/pull/4522))
* [BUGFIX] Adjust output of datetime `ParameterBuilder` to match Expectation ([#4590](https://github.com/great-expectations/great_expectations/pull/4590))
* [DOCS] Technical term tags for Adding features to Expectations section of the ToC ([#4462](https://github.com/great-expectations/great_expectations/pull/4462))
* [DOCS] Contributing integrations ToC update. ([#4551](https://github.com/great-expectations/great_expectations/pull/4551))
* [DOCS] Update intro page overview image ([#4540](https://github.com/great-expectations/great_expectations/pull/4540))
* [DOCS] clarifications on execution engines and scalability ([#4539](https://github.com/great-expectations/great_expectations/pull/4539))
* [DOCS] technical terms for validate data advanced ([#4535](https://github.com/great-expectations/great_expectations/pull/4535))
* [DOCS] technical terms for validate data actions docs ([#4518](https://github.com/great-expectations/great_expectations/pull/4518))
* [DOCS] correct code reference line numbers and snippet tags for how to create a batch of data from an in memory data frame ([#4573](https://github.com/great-expectations/great_expectations/pull/4573))
* [DOCS] Update links in page; fix markdown link in html block ([#4585](https://github.com/great-expectations/great_expectations/pull/4585))
* [MAINTENANCE] Don't return from validate configuration methods ([#4545](https://github.com/great-expectations/great_expectations/pull/4545))
* [MAINTENANCE] Rule-Based Profiler: Refactor utilities into appropriate modules/classes for better separation of concerns ([#4553](https://github.com/great-expectations/great_expectations/pull/4553))
* [MAINTENANCE] Refactor global `conftest` ([#4534](https://github.com/great-expectations/great_expectations/pull/4534))
* [MAINTENANCE] clean up docstrings ([#4554](https://github.com/great-expectations/great_expectations/pull/4554))
* [MAINTENANCE] Small formatting rearrangement for RegexPatternStringParameterBuilder ([#4558](https://github.com/great-expectations/great_expectations/pull/4558))
* [MAINTENANCE] Refactor Anonymizer utilizing the Strategy design pattern ([#4485](https://github.com/great-expectations/great_expectations/pull/4485))
* [MAINTENANCE] Remove duplicate `mistune` dependency ([#4569](https://github.com/great-expectations/great_expectations/pull/4569))
* [MAINTENANCE] Run PEP273 checks on a schedule or release cut ([#4570](https://github.com/great-expectations/great_expectations/pull/4570))
* [MAINTENANCE] Package dependencies usage stats instrumentation - part 1 ([#4546](https://github.com/great-expectations/great_expectations/pull/4546))
* [MAINTENANCE] Add DevRel team to GitHub auto-label action ([#4575](https://github.com/great-expectations/great_expectations/pull/4575))
* [MAINTENANCE] Add GitHub action to conditionally auto-update PR's  ([#4574](https://github.com/great-expectations/great_expectations/pull/4574))
* [MAINTENANCE] Bump version of `black` in response to hotfix for Click v8.1.0 ([#4577](https://github.com/great-expectations/great_expectations/pull/4577))
* [MAINTENANCE] Update overview.md ([#4556](https://github.com/great-expectations/great_expectations/pull/4556))
* [MAINTENANCE] Minor clean-up ([#4571](https://github.com/great-expectations/great_expectations/pull/4571))
* [MAINTENANCE] Instrument package dependencies ([#4583](https://github.com/great-expectations/great_expectations/pull/4583))
* [MAINTENANCE] Standardize DomainBuilder Constructor Arguments Ordering ([#4599](https://github.com/great-expectations/great_expectations/pull/4599))

0.14.12
-----------------
* [FEATURE] Enables Regex-Based Column Map Expectations ([#4315](https://github.com/great-expectations/great_expectations/pull/4315))
* [FEATURE] Update diagnostic checklist to do linting checks ([#4491](https://github.com/great-expectations/great_expectations/pull/4491))
* [FEATURE] format docstrings as markdown for gallery ([#4502](https://github.com/great-expectations/great_expectations/pull/4502))
* [FEATURE] Introduces SetBasedColumnMapExpectation w/ supporting templates & doc ([#4497](https://github.com/great-expectations/great_expectations/pull/4497))
* [FEATURE] `YAMLHandler` Class ([#4510](https://github.com/great-expectations/great_expectations/pull/4510))
* [FEATURE] Remove conflict between filter directives and row_conditions ([#4488](https://github.com/great-expectations/great_expectations/pull/4488))
* [FEATURE] Add SNS as a Validation Action ([#4519](https://github.com/great-expectations/great_expectations/pull/4519)) (thanks @michael-j-thomas)
* [BUGFIX] Fixes ExpectColumnValuesToBeInSet to enable behavior indicated in Parameterized Expectations Doc ([#4455](https://github.com/great-expectations/great_expectations/pull/4455))
* [BUGFIX] Fixes minor typo in custom expectation docs, adds missing link ([#4507](https://github.com/great-expectations/great_expectations/pull/4507))
* [BUGFIX] Removes validate_config from RegexBasedColumnMap templates & doc ([#4506](https://github.com/great-expectations/great_expectations/pull/4506))
* [BUGFIX] Update ExpectColumnValuesToMatchRegex to support parameterized expectations ([#4504](https://github.com/great-expectations/great_expectations/pull/4504))
* [BUGFIX] Add back `nbconvert` to dev dependencies ([#4515](https://github.com/great-expectations/great_expectations/pull/4515))
* [BUGFIX] Account for case where SQLAlchemy dialect is not downloaded when masking a given URL ([#4516](https://github.com/great-expectations/great_expectations/pull/4516))
* [BUGFIX] Fix failing test for `How to Configure Credentials` ([#4525](https://github.com/great-expectations/great_expectations/pull/4525))
* [BUGFIX] Remove Temp Dir ([#4528](https://github.com/great-expectations/great_expectations/pull/4528))
* [BUGFIX] Add pin to Jinja 2 due to API changes in v3.1.0 release ([#4537](https://github.com/great-expectations/great_expectations/pull/4537))
* [BUGFIX] Fixes broken links in How To Write A How-To Guide ([#4536](https://github.com/great-expectations/great_expectations/pull/4536))
* [BUGFIX] Removes cryptography upper bound for general reqs ([#4487](https://github.com/great-expectations/great_expectations/pull/4487))
* [BUGFIX] Don't assume boto3 is installed ([#4542](https://github.com/great-expectations/great_expectations/pull/4542))
* [DOCS] Update tutorial_review.md ([#3981](https://github.com/great-expectations/great_expectations/pull/3981))
* [DOCS] Update AUTHORING_INTRO.md ([#4470](https://github.com/great-expectations/great_expectations/pull/4470)) (thanks @andyjessen)
* [DOCS] Add clarification ([#4477](https://github.com/great-expectations/great_expectations/pull/4477)) (thanks @strickvl)
* [DOCS] Add missing word and fix wrong dataset reference ([#4478](https://github.com/great-expectations/great_expectations/pull/4478)) (thanks @strickvl)
* [DOCS] Adds documentation on how to use Great Expectations with Prefect ([#4433](https://github.com/great-expectations/great_expectations/pull/4433)) (thanks @desertaxle)
* [DOCS] technical terms validate data checkpoints ([#4486](https://github.com/great-expectations/great_expectations/pull/4486))
* [DOCS] How to use a Custom Expectation ([#4467](https://github.com/great-expectations/great_expectations/pull/4467))
* [DOCS] Technical Terms for Validate Data: Overview and Core Skills docs ([#4465](https://github.com/great-expectations/great_expectations/pull/4465))
* [DOCS] technical terms create expectations advanced skills ([#4441](https://github.com/great-expectations/great_expectations/pull/4441))
* [DOCS] Integration documentation ([#4483](https://github.com/great-expectations/great_expectations/pull/4483))
* [DOCS] Adding Meltano implementation pattern to docs ([#4509](https://github.com/great-expectations/great_expectations/pull/4509)) (thanks @pnadolny13)
* [DOCS] Update tutorial_create_expectations.md ([#4512](https://github.com/great-expectations/great_expectations/pull/4512)) (thanks @andyjessen)
* [DOCS] Fix relative links on github ([#4479](https://github.com/great-expectations/great_expectations/pull/4479)) (thanks @andyjessen)
* [DOCS] Update README.md ([#4533](https://github.com/great-expectations/great_expectations/pull/4533)) (thanks @andyjessen)
* [HACKATHON] ExpectColumnValuesToBeValidIPv4 ([#4457](https://github.com/great-expectations/great_expectations/pull/4457)) (thanks @voidforall)
* [HACKATHON] ExpectColumnValuesToBeValidIanaTimezone ([#4532](https://github.com/great-expectations/great_expectations/pull/4532)) (thanks @lucasasmith)
* [MAINTENANCE] Clean up `Checkpoints` documentation and add `snippet`  ([#4474](https://github.com/great-expectations/great_expectations/pull/4474))
* [MAINTENANCE] Finalize Great Expectations contrib JSON structure ([#4482](https://github.com/great-expectations/great_expectations/pull/4482))
* [MAINTENANCE] Update expectation filenames to match snake_case of their defined Expectations ([#4484](https://github.com/great-expectations/great_expectations/pull/4484))
* [MAINTENANCE] Clean Up Types and Rely on "to_json_dict()" where appropriate ([#4489](https://github.com/great-expectations/great_expectations/pull/4489))
* [MAINTENANCE] type hints for Batch Request to be string (which leverages parameter/variable resolution) ([#4494](https://github.com/great-expectations/great_expectations/pull/4494))
* [MAINTENANCE] Insure consistent ordering of arguments to ParameterBuilder instantiations ([#4496](https://github.com/great-expectations/great_expectations/pull/4496))
* [MAINTENANCE] Refactor build_gallery.py script ([#4493](https://github.com/great-expectations/great_expectations/pull/4493))
* [MAINTENANCE] Feature/cloud 385/mask cloud creds ([#4444](https://github.com/great-expectations/great_expectations/pull/4444))
* [MAINTENANCE] Enforce consistent JSON schema through usage stats ([#4499](https://github.com/great-expectations/great_expectations/pull/4499))
* [MAINTENANCE] Applies `camel_to_snake` util to `RegexBasedColumnMapExpectation` ([#4511](https://github.com/great-expectations/great_expectations/pull/4511))
* [MAINTENANCE] Removes unused dependencies ([#4508](https://github.com/great-expectations/great_expectations/pull/4508))
* [MAINTENANCE] Revert changes made to dependencies in [#4508](https://github.com/great-expectations/great_expectations/pull/4508) ([#4520](https://github.com/great-expectations/great_expectations/pull/4520))
* [MAINTENANCE] Add `compatability` stage to `dependency_graph` pipeline ([#4514](https://github.com/great-expectations/great_expectations/pull/4514))
* [MAINTENANCE] Add prod metadata and remove package attribute from library_metadata ([#4517](https://github.com/great-expectations/great_expectations/pull/4517))
* [MAINTENANCE] Move builder instantiation methods to utility module for broader usage among sub-components within Rule-Based Profiler ([#4524](https://github.com/great-expectations/great_expectations/pull/4524))
* [MAINTENANCE] Update package info for Capital One DataProfiler ([#4523](https://github.com/great-expectations/great_expectations/pull/4523))
* [MAINTENANCE] Remove tag 'needs migration to modular expectations api' for some Expectations ([#4521](https://github.com/great-expectations/great_expectations/pull/4521))
* [MAINTENANCE] Add type hints and PyCharm macros in a test module for DefaultExpectationConfigurationBuilder ([#4529](https://github.com/great-expectations/great_expectations/pull/4529))
* [MAINTENANCE] Continue War on Warnings ([#4500](https://github.com/great-expectations/great_expectations/pull/4500))

0.14.11
-----------------
* [FEATURE] Script to validate docs snippets line number refs ([#4377](https://github.com/great-expectations/great_expectations/pull/4377))
* [FEATURE] GitHub action to auto label `core-team` ([#4382](https://github.com/great-expectations/great_expectations/pull/4382))
* [FEATURE] `add_rule()` method for RuleBasedProfilers and tests ([#4358](https://github.com/great-expectations/great_expectations/pull/4358))
* [FEATURE] Enable the passing of an existing suite to `RuleBasedProfiler.run()` ([#4386](https://github.com/great-expectations/great_expectations/pull/4386))
* [FEATURE] Impose Ordering on Marshmallow Schema validated Rule-Based Profiler Configuration fields ([#4388](https://github.com/great-expectations/great_expectations/pull/4388))
* [FEATURE] Use more granular requirements-dev-xxx.txt files ([#4327](https://github.com/great-expectations/great_expectations/pull/4327))
* [FEATURE] Rule-Based Profiler: Implement Utilities for getting all available parameter node names and objects resident in memory ([#4442](https://github.com/great-expectations/great_expectations/pull/4442))
* [BUGFIX] Minor Serialization Correction for MeanUnexpectedMapMetricMultiBatchParameterBuilder ([#4385](https://github.com/great-expectations/great_expectations/pull/4385))
* [BUGFIX] Fix CategoricalColumnDomainBuilder to be compliant with serialization / instantiation interfaces ([#4395](https://github.com/great-expectations/great_expectations/pull/4395))
* [BUGFIX] Fix bug around `get_parent` usage stats utility in `test_yaml_config` ([#4410](https://github.com/great-expectations/great_expectations/pull/4410))
* [BUGFIX] Adding `--spark` flag back to `azure-pipelines.yml` compatibility_matrix stage.  ([#4418](https://github.com/great-expectations/great_expectations/pull/4418))
* [BUGFIX] Remove remaining usage of --no-spark and --no-postgresql flags for pytest ([#4425](https://github.com/great-expectations/great_expectations/pull/4425))
* [BUGFIX] Insure Proper Indexing of Metric Computation Results in ParameterBuilder ([#4426](https://github.com/great-expectations/great_expectations/pull/4426))
* [BUGFIX] Include requirements-dev-contrib.txt in dev-install-matrix.yml for lightweight ([#4430](https://github.com/great-expectations/great_expectations/pull/4430))
* [BUGFIX] Remove `pytest-azurepiplines` usage from `test_cli` stages in Azure pipelines ([#4432](https://github.com/great-expectations/great_expectations/pull/4432))
* [BUGFIX] Updates or deletes broken and deprecated example notebooks ([#4404](https://github.com/great-expectations/great_expectations/pull/4404))
* [BUGFIX] Add any dependencies we import directly, but don't have as explicit requirements ([#4447](https://github.com/great-expectations/great_expectations/pull/4447))
* [BUGFIX] Removes potentially sensitive webhook URLs from logging ([#4440](https://github.com/great-expectations/great_expectations/pull/4440))
* [BUGFIX] Fix packaging test ([#4452](https://github.com/great-expectations/great_expectations/pull/4452))
* [DOCS] Fix typo in how_to_create_custom_metrics ([#4379](https://github.com/great-expectations/great_expectations/pull/4379))
* [DOCS] Add `snippet` tag to gcs data docs ([#4383](https://github.com/great-expectations/great_expectations/pull/4383))
* [DOCS] adjust lines for py reference ([#4390](https://github.com/great-expectations/great_expectations/pull/4390))
* [DOCS] technical tags for connecting to data: core skills docs ([#4403](https://github.com/great-expectations/great_expectations/pull/4403))
* [DOCS] technical term tags for connect to data database documents ([#4413](https://github.com/great-expectations/great_expectations/pull/4413))
* [DOCS] Technical term tags for documentation under Connect to data: Filesystem ([#4411](https://github.com/great-expectations/great_expectations/pull/4411))
* [DOCS] Technical term tags for setup pages ([#4392](https://github.com/great-expectations/great_expectations/pull/4392))
* [DOCS] Technical term tags for Connect to Data: Advanced docs. ([#4406](https://github.com/great-expectations/great_expectations/pull/4406))
* [DOCS] Technical tags: Connect to data:In memory docs ([#4405](https://github.com/great-expectations/great_expectations/pull/4405))
* [DOCS] Add misc `snippet` tags to existing documentation ([#4397](https://github.com/great-expectations/great_expectations/pull/4397))
* [DOCS] technical terms create expectations: core skills ([#4435](https://github.com/great-expectations/great_expectations/pull/4435))
* [DOCS] Creates Custom Table Expectation How-To ([#4399](https://github.com/great-expectations/great_expectations/pull/4399))
* [HACKATHON] ExpectTableLinearFeatureImportancesToBe ([#4400](https://github.com/great-expectations/great_expectations/pull/4400))
* [MAINTENANCE] Group MAP_SERIES and MAP_CONDITION_SERIES with VALUE-type metrics ([#3286](https://github.com/great-expectations/great_expectations/pull/3286))
* [MAINTENANCE] minor imports cleanup ([#4381](https://github.com/great-expectations/great_expectations/pull/4381))
* [MAINTENANCE] Change schedule for `packaging_and_installation` pipeline to run at off-hours ([#4384](https://github.com/great-expectations/great_expectations/pull/4384))
* [MAINTENANCE] Implicitly anonymize object based on __module__ ([#4387](https://github.com/great-expectations/great_expectations/pull/4387))
* [MAINTENANCE] Preparatory cleanup refactoring of get_compute_domain ([#4371](https://github.com/great-expectations/great_expectations/pull/4371))
* [MAINTENANCE] RBP -- make parameter builder configurations for self initializing expectations consistent with ParameterBuilder class interfaces ([#4398](https://github.com/great-expectations/great_expectations/pull/4398))
* [MAINTENANCE] Refactor `ge_class` attr out of Anonymizer and related child classes ([#4393](https://github.com/great-expectations/great_expectations/pull/4393))
* [MAINTENANCE] Removing Custom Expectation Renderer docs from sidebar ([#4401](https://github.com/great-expectations/great_expectations/pull/4401))
* [MAINTENANCE] Enable "rule_based_profiler.run()" Method to Accept Batch Data Arguments Directly ([#4409](https://github.com/great-expectations/great_expectations/pull/4409))
* [MAINTENANCE] Refactor out unnecessary Anonymizer child classes ([#4408](https://github.com/great-expectations/great_expectations/pull/4408))
* [MAINTENANCE] Replace "sampling_method" with "estimator" in Rule-Based Profiler code ([#4420](https://github.com/great-expectations/great_expectations/pull/4420))
* [MAINTENANCE] Add docstrings and type hints to `Anonymizer` ([#4419](https://github.com/great-expectations/great_expectations/pull/4419))
* [MAINTENANCE] Continue chipping away at warnings ([#4422](https://github.com/great-expectations/great_expectations/pull/4422))
* [MAINTENANCE] Rule-Based Profiler: Standardize on Include/Exclude Column Names List ([#4424](https://github.com/great-expectations/great_expectations/pull/4424))
* [MAINTENANCE] Set upper bound on number of allowed warnings in snippet validation script ([#4434](https://github.com/great-expectations/great_expectations/pull/4434))
* [MAINTENANCE] Clean up of `RegexPatternStringParameterBuilder` tests to use unittests ([#4436](https://github.com/great-expectations/great_expectations/pull/4436))

0.14.10
-----------------
* [FEATURE] ParameterBuilder for Computing Average Unexpected Values Fractions for any Map Metric ([#4340](https://github.com/great-expectations/great_expectations/pull/4340))
* [FEATURE] Improve bootstrap quantile method accuracy ([#4270](https://github.com/great-expectations/great_expectations/pull/4270))
* [FEATURE] Decorate RuleBasedProfiler.run() with usage statistics ([#4321](https://github.com/great-expectations/great_expectations/pull/4321))
* [FEATURE] MapMetricColumnDomainBuilder for Rule-Based Profiler ([#4353](https://github.com/great-expectations/great_expectations/pull/4353))
* [FEATURE] Enable expect_column_min/_max_to_be_between expectations to be self-initializing ([#4363](https://github.com/great-expectations/great_expectations/pull/4363))
* [FEATURE] Azure pipeline to perform nightly CI/CD runs around packaging/installation ([#4274](https://github.com/great-expectations/great_expectations/pull/4274))
* [BUGFIX] Fix `IndexError` around data asset pagination from CLI ([#4346](https://github.com/great-expectations/great_expectations/pull/4346))
* [BUGFIX] Upper bound pyathena to <2.5.0 ([#4350](https://github.com/great-expectations/great_expectations/pull/4350))
* [BUGFIX] Fixes PyAthena type checking for core expectations & tests ([#4359](https://github.com/great-expectations/great_expectations/pull/4359))
* [BUGFIX] BatchRequest serialization (CLOUD-743) ([#4352](https://github.com/great-expectations/great_expectations/pull/4352))
* [BUGFIX] Update the favicon on docs site ([#4376](https://github.com/great-expectations/great_expectations/pull/4376))
* [BUGFIX] Fix issue with datetime objects in expecatation args ([#2652](https://github.com/great-expectations/great_expectations/pull/2652)) (thanks @jstammers)
* [DOCS] Universal map TOC update ([#4292](https://github.com/great-expectations/great_expectations/pull/4292))
* [DOCS] add Config section ([#4355](https://github.com/great-expectations/great_expectations/pull/4355))
* [DOCS] Deployment Patterns to Reference Architectures ([#4344](https://github.com/great-expectations/great_expectations/pull/4344))
* [DOCS] Fixes tutorial link in reference architecture prereqs component ([#4360](https://github.com/great-expectations/great_expectations/pull/4360))
* [DOCS] Tag technical terms in getting started tutorial ([#4354](https://github.com/great-expectations/great_expectations/pull/4354))
* [DOCS] Update overview pages to link to updated tutorial pages. ([#4378](https://github.com/great-expectations/great_expectations/pull/4378))
* [HACKATHON] ExpectColumnValuesToBeValidUUID ([#4322](https://github.com/great-expectations/great_expectations/pull/4322))
* [HACKATHON] add expectation core ([#4357](https://github.com/great-expectations/great_expectations/pull/4357))
* [HACKATHON] ExpectColumnAverageToBeWithinRangeOfGivenPoint ([#4356](https://github.com/great-expectations/great_expectations/pull/4356))
* [MAINTENANCE] rule based profiler minor clean up of ValueSetParameterBuilder ([#4332](https://github.com/great-expectations/great_expectations/pull/4332))
* [MAINTENANCE] Adding tests that exercise single and multi-batch BatchRequests ([#4330](https://github.com/great-expectations/great_expectations/pull/4330))
* [MAINTENANCE] Formalize ParameterBuilder contract API usage in ValueSetParameterBuilder ([#4333](https://github.com/great-expectations/great_expectations/pull/4333))
* [MAINTENANCE] Rule-Based Profiler: Create helpers directory; use column domain generation convenience method ([#4335](https://github.com/great-expectations/great_expectations/pull/4335))
* [MAINTENANCE] Deduplicate table domain kwargs splitting ([#4338](https://github.com/great-expectations/great_expectations/pull/4338))
* [MAINTENANCE] Update Azure CI/CD cron schedule to run more frequently ([#4345](https://github.com/great-expectations/great_expectations/pull/4345))
* [MAINTENANCE] Optimize CategoricalColumnDomainBuilder to compute metrics in a single method call ([#4348](https://github.com/great-expectations/great_expectations/pull/4348))
* [MAINTENANCE] Reduce tries to 2 for probabilistic tests ([#4351](https://github.com/great-expectations/great_expectations/pull/4351))
* [MAINTENANCE] Refactor Checkpoint toolkit ([#4342](https://github.com/great-expectations/great_expectations/pull/4342))
* [MAINTENANCE] Refactor all uses of `format` in favor of f-strings ([#4347](https://github.com/great-expectations/great_expectations/pull/4347))
* [MAINTENANCE] Update great_expectations_contrib CLI tool to use existing diagnostic classes ([#4316](https://github.com/great-expectations/great_expectations/pull/4316))
* [MAINTENANCE] Setting stage for removal of `--no-postgresql` and `--no-spark` flags from `pytest`. Enable `--postgresql` and `--spark` ([#4309](https://github.com/great-expectations/great_expectations/pull/4309))
* [MAINTENANCE] convert unexpected_list contents to hashable type ([#4336](https://github.com/great-expectations/great_expectations/pull/4336))
* [MAINTENANCE] add operator and func handling to stores urns ([#4334](https://github.com/great-expectations/great_expectations/pull/4334))
* [MAINTENANCE]  Refactor ParameterBuilder classes to extend parent class where possible; also, minor cleanup ([#4375](https://github.com/great-expectations/great_expectations/pull/4375))

0.14.9
-----------------
* [FEATURE] Enable Simultaneous Execution of all Metric Computations for ParameterBuilder implementations in Rule-Based Profiler ([#4282](https://github.com/great-expectations/great_expectations/pull/4282))
* [FEATURE] Update print_diagnostic_checklist with an option to show any failed tests ([#4288](https://github.com/great-expectations/great_expectations/pull/4288))
* [FEATURE] Self-Initializing Expectations (implemented for three example expectations). ([#4258](https://github.com/great-expectations/great_expectations/pull/4258))
* [FEATURE] ValueSetMultiBatchParameterBuilder and CategoricalColumnDomainBuilder ([#4269](https://github.com/great-expectations/great_expectations/pull/4269))
* [FEATURE] Remove changelog-bot GitHub Action ([#4297](https://github.com/great-expectations/great_expectations/pull/4297))
* [FEATURE] Add requirements-dev-lite.txt and update tests/docs ([#4273](https://github.com/great-expectations/great_expectations/pull/4273))
* [FEATURE] Enable All ParameterBuilder and DomainBuilder classes to accept batch_list generically ([#4302](https://github.com/great-expectations/great_expectations/pull/4302))
* [FEATURE] Enable Probabilistic Tests To Retry upon Assertion Failure ([#4308](https://github.com/great-expectations/great_expectations/pull/4308))
* [FEATURE] Update usage stats schema to account for RBP's run() payload ([#4266](https://github.com/great-expectations/great_expectations/pull/4266))
* [FEATURE] ProfilerRunAnonymizer ([#4264](https://github.com/great-expectations/great_expectations/pull/4264))
* [FEATURE] Enable Expectation "expect_column_values_to_be_in_set" to be Self-Initializing ([#4318](https://github.com/great-expectations/great_expectations/pull/4318))
* [BUGFIX] Add redirect for removed Spark EMR page ([#4280](https://github.com/great-expectations/great_expectations/pull/4280))
* [BUGFIX] `ConfiguredAssetSqlDataConnector` now correctly handles `schema` and `prefix`/`suffix` ([#4268](https://github.com/great-expectations/great_expectations/pull/4268))
* [BUGFIX] Fixes Expectation Diagnostics failing on multi-line docstrings with leading linebreaks ([#4286](https://github.com/great-expectations/great_expectations/pull/4286))
* [BUGFIX] Respect test backends ([#4287](https://github.com/great-expectations/great_expectations/pull/4287))
* [BUGFIX] Skip test__generate_expectations_tests__xxx tests when sqlalchemy isn't there ([#4300](https://github.com/great-expectations/great_expectations/pull/4300))
* [BUGFIX] test_backends integration test fix and supporting docs code ref fixes ([#4306](https://github.com/great-expectations/great_expectations/pull/4306))
* [BUGFIX] Update `deep_filter_properties_iterable` to ensure that empty values are cleaned ([#4298](https://github.com/great-expectations/great_expectations/pull/4298))
* [BUGFIX] Fixes validate_configuration checking in diagnostics ([#4307](https://github.com/great-expectations/great_expectations/pull/4307))
* [BUGFIX] Update test output that should be returned from generate_diagnostic_checklist ([#4317](https://github.com/great-expectations/great_expectations/pull/4317))
* [BUGFIX] Standardizes imports in expectation templates and examples ([#4320](https://github.com/great-expectations/great_expectations/pull/4320))
* [BUGFIX] Only validate row_condition if not None ([#4329](https://github.com/great-expectations/great_expectations/pull/4329))
* [BUGFIX] Fix PEP273 Windows issue ([#4328](https://github.com/great-expectations/great_expectations/pull/4328))
* [DOCS] Fixes misc. verbiage & typos in new Custom Expectation docs ([#4283](https://github.com/great-expectations/great_expectations/pull/4283))
* [DOCS] fix formatting in configuration details block of Getting Started ([#4289](https://github.com/great-expectations/great_expectations/pull/4289)) (thanks @afeld)
* [DOCS] Fixes imports and code refs to expectation templates ([#4314](https://github.com/great-expectations/great_expectations/pull/4314))
* [DOCS] Update creating_custom_expectations/overview.md ([#4278](https://github.com/great-expectations/great_expectations/pull/4278)) (thanks @binarytom)
* [CONTRIB] CapitalOne Dataprofiler expectations ([#4174](https://github.com/great-expectations/great_expectations/pull/4174)) (thanks @taylorfturner)
* [HACKATHON] ExpectColumnValuesToBeLatLonCoordinatesInRangeOfGivenPoint ([#4284](https://github.com/great-expectations/great_expectations/pull/4284))
* [HACKATHON] ExpectColumnValuesToBeValidDegreeDecimalCoordinates ([#4319](https://github.com/great-expectations/great_expectations/pull/4319))
* [MAINTENANCE] Refactor parameter setting for simpler ParameterBuilder interface ([#4299](https://github.com/great-expectations/great_expectations/pull/4299))
* [MAINTENANCE] SimpleDateTimeFormatStringParameterBuilder and general RBP example config updates ([#4304](https://github.com/great-expectations/great_expectations/pull/4304))
* [MAINTENANCE] Make adherence to Marshmallow Schema more robust ([#4325](https://github.com/great-expectations/great_expectations/pull/4325))
* [MAINTENANCE] Refactor rule based profiler to keep objects/utilities within intended scope ([#4331](https://github.com/great-expectations/great_expectations/pull/4331))
* [MAINTENANCE] Dependabot version upgrades ([#4253](https://github.com/great-expectations/great_expectations/pull/4253), [#4231](https://github.com/great-expectations/great_expectations/pull/4231), [#4058](https://github.com/great-expectations/great_expectations/pull/4058), [#4041](https://github.com/great-expectations/great_expectations/pull/4041), [#3916](https://github.com/great-expectations/great_expectations/pull/3916), [#3886](https://github.com/great-expectations/great_expectations/pull/3886), [#3583](https://github.com/great-expectations/great_expectations/pull/3583), [#2856](https://github.com/great-expectations/great_expectations/pull/2856), [#3370](https://github.com/great-expectations/great_expectations/pull/3370), [#3216](https://github.com/great-expectations/great_expectations/pull/3216), [#2935](https://github.com/great-expectations/great_expectations/pull/2935), [#2855](https://github.com/great-expectations/great_expectations/pull/2855), [#3302](https://github.com/great-expectations/great_expectations/pull/3302), [#4008](https://github.com/great-expectations/great_expectations/pull/4008), [#4252](https://github.com/great-expectations/great_expectations/pull/4252))

0.14.8
-----------------
* [FEATURE] Add `run_profiler_on_data` method to DataContext ([#4190](https://github.com/great-expectations/great_expectations/pull/4190))
* [FEATURE] `RegexPatternStringParameterBuilder` for `RuleBasedProfiler` ([#4167](https://github.com/great-expectations/great_expectations/pull/4167))
* [FEATURE] experimental column map expectation checking for vectors ([#3102](https://github.com/great-expectations/great_expectations/pull/3102)) (thanks @manyshapes)
* [FEATURE] Pre-requisites in Rule-Based Profiler for Self-Estimating Expectations ([#4242](https://github.com/great-expectations/great_expectations/pull/4242))
* [FEATURE] Add optional parameter `condition` to DefaultExpectationConfigurationBuilder ([#4246](https://github.com/great-expectations/great_expectations/pull/4246))
* [BUGFIX] Ensure that test result for `RegexPatternStringParameterBuilder` is deterministic ([#4240](https://github.com/great-expectations/great_expectations/pull/4240))
* [BUGFIX] Remove duplicate RegexPatternStringParameterBuilder test ([#4241](https://github.com/great-expectations/great_expectations/pull/4241))
* [BUGFIX] Improve pandas version checking in test_expectations[_cfe].py files ([#4248](https://github.com/great-expectations/great_expectations/pull/4248))
* [BUGFIX] Ensure `test_script_runner.py` actually raises AssertionErrors correctly ([#4239](https://github.com/great-expectations/great_expectations/pull/4239))
* [BUGFIX] Check for pandas>=024 not pandas>=24 ([#4263](https://github.com/great-expectations/great_expectations/pull/4263))
* [BUGFIX] Add support for SqlAlchemyQueryStore connection_string credentials ([#4224](https://github.com/great-expectations/great_expectations/pull/4224)) (thanks @davidvanrooij)
* [BUGFIX] Remove assertion ([#4271](https://github.com/great-expectations/great_expectations/pull/4271))
* [DOCS] Hackathon Contribution Docs ([#3897](https://github.com/great-expectations/great_expectations/pull/3897))
* [MAINTENANCE] Rule-Based Profiler: Fix Circular Imports; Configuration Schema Fixes; Enhanced Unit Tests; Pre-Requisites/Refactoring for Self-Estimating Expectations ([#4234](https://github.com/great-expectations/great_expectations/pull/4234))
* [MAINTENANCE] Reformat contrib expectation with black ([#4244](https://github.com/great-expectations/great_expectations/pull/4244))
* [MAINTENANCE] Resolve cyclic import issue with usage stats ([#4251](https://github.com/great-expectations/great_expectations/pull/4251))
* [MAINTENANCE] Additional refactor to clean up cyclic imports in usage stats ([#4256](https://github.com/great-expectations/great_expectations/pull/4256))
* [MAINTENANCE] Rule-Based Profiler prerequisite: fix quantiles profiler configuration and add comments ([#4255](https://github.com/great-expectations/great_expectations/pull/4255))
* [MAINTENANCE] Introspect Batch Request Dictionary for its kind and instantiate accordingly ([#4259](https://github.com/great-expectations/great_expectations/pull/4259))
* [MAINTENANCE] Minor clean up in style of an RBP test fixture; making variables access more robust ([#4261](https://github.com/great-expectations/great_expectations/pull/4261))
* [MAINTENANCE] define empty sqla_bigquery object ([#4249](https://github.com/great-expectations/great_expectations/pull/4249))

0.14.7
-----------------
* [FEATURE] Support Multi-Dimensional Metric Computations Generically for Multi-Batch Parameter Builders ([#4206](https://github.com/great-expectations/great_expectations/pull/4206))
* [FEATURE] Add support for sqlalchemy-bigquery while falling back on pybigquery ([#4182](https://github.com/great-expectations/great_expectations/pull/4182))
* [BUGFIX] Update validate_configuration for core Expectations that don't return True ([#4216](https://github.com/great-expectations/great_expectations/pull/4216))
* [DOCS] Fixes two references to the Getting Started tutorial ([#4189](https://github.com/great-expectations/great_expectations/pull/4189))
* [DOCS] Deepnote Deployment Pattern Guide ([#4169](https://github.com/great-expectations/great_expectations/pull/4169))
* [DOCS] Allow Data Docs to be rendered in night mode ([#4130](https://github.com/great-expectations/great_expectations/pull/4130))
* [DOCS] Fix datepicker filter on data docs ([#4217](https://github.com/great-expectations/great_expectations/pull/4217))
* [DOCS] Deepnote Deployment Pattern Image Fixes ([#4229](https://github.com/great-expectations/great_expectations/pull/4229))
* [MAINTENANCE] Refactor RuleBasedProfiler toolkit pattern ([#4191](https://github.com/great-expectations/great_expectations/pull/4191))
* [MAINTENANCE] Revert `dependency_graph` pipeline changes to ensure `usage_stats` runs in parallel ([#4198](https://github.com/great-expectations/great_expectations/pull/4198))
* [MAINTENANCE] Refactor relative imports ([#4195](https://github.com/great-expectations/great_expectations/pull/4195))
* [MAINTENANCE] Remove temp file that was accidently committed ([#4201](https://github.com/great-expectations/great_expectations/pull/4201))
* [MAINTENANCE] Update default candidate strings SimpleDateFormatString parameter builder ([#4193](https://github.com/great-expectations/great_expectations/pull/4193))
* [MAINTENANCE] minor type hints clean up ([#4214](https://github.com/great-expectations/great_expectations/pull/4214))
* [MAINTENANCE] RBP testing framework changes ([#4184](https://github.com/great-expectations/great_expectations/pull/4184))
* [MAINTENANCE] add conditional check for 'expect_column_values_to_be_in_type_list' ([#4200](https://github.com/great-expectations/great_expectations/pull/4200))
* [MAINTENANCE] Allow users to pass in any set of polygon points in expectation for point to be within region ([#2520](https://github.com/great-expectations/great_expectations/pull/2520)) (thanks @ryanlindeborg)
* [MAINTENANCE] Better support Hive, better support BigQuery. ([#2624](https://github.com/great-expectations/great_expectations/pull/2624)) (thanks @jacobpgallagher)
* [MAINTENANCE] move process_evaluation_parameters into conditional ([#4109](https://github.com/great-expectations/great_expectations/pull/4109))
* [MAINTENANCE] Type hint usage stats ([#4226](https://github.com/great-expectations/great_expectations/pull/4226))

0.14.6
-----------------
* [FEATURE] Create profiler from DataContext ([#4070](https://github.com/great-expectations/great_expectations/pull/4070))
* [FEATURE] Add read_sas function ([#3972](https://github.com/great-expectations/great_expectations/pull/3972)) (thanks @andyjessen)
* [FEATURE] Run profiler from DataContext ([#4141](https://github.com/great-expectations/great_expectations/pull/4141))
* [FEATURE] Instantiate Rule-Based Profiler Using Typed Configuration Object ([#4150](https://github.com/great-expectations/great_expectations/pull/4150))
* [FEATURE] Provide ability to instantiate Checkpoint using CheckpointConfig typed object ([#4166](https://github.com/great-expectations/great_expectations/pull/4166))
* [FEATURE] Misc cleanup around CLI `suite` command and related utilities ([#4158](https://github.com/great-expectations/great_expectations/pull/4158))
* [FEATURE] Add scheduled runs for primary Azure pipeline ([#4117](https://github.com/great-expectations/great_expectations/pull/4117))
* [FEATURE] Promote dependency graph test strategy to production ([#4124](https://github.com/great-expectations/great_expectations/pull/4124))
* [BUGFIX] minor updates to test definition json files ([#4123](https://github.com/great-expectations/great_expectations/pull/4123))
* [BUGFIX] Fix typo for metric name in expect_column_values_to_be_edtf_parseable ([#4140](https://github.com/great-expectations/great_expectations/pull/4140))
* [BUGFIX] Ensure that CheckpointResult object can be pickled ([#4157](https://github.com/great-expectations/great_expectations/pull/4157))
* [BUGFIX] Custom notebook templates ([#2619](https://github.com/great-expectations/great_expectations/pull/2619)) (thanks @luke321321)
* [BUGFIX] Include public fields in property_names ([#4159](https://github.com/great-expectations/great_expectations/pull/4159))
* [DOCS] Reenable docs-under-test for RuleBasedProfiler ([#4149](https://github.com/great-expectations/great_expectations/pull/4149))
* [DOCS] Provided details for using GE_HOME in commandline. ([#4164](https://github.com/great-expectations/great_expectations/pull/4164))
* [MAINTENANCE] Return Rule-Based Profiler base.py to its dedicated config subdirectory ([#4125](https://github.com/great-expectations/great_expectations/pull/4125))
* [MAINTENANCE] enable filter properties dict to handle both inclusion and exclusion lists  ([#4127](https://github.com/great-expectations/great_expectations/pull/4127))
* [MAINTENANCE] Remove unused Great Expectations imports ([#4135](https://github.com/great-expectations/great_expectations/pull/4135))
* [MAINTENANCE] Update trigger for scheduled Azure runs ([#4134](https://github.com/great-expectations/great_expectations/pull/4134))
* [MAINTENANCE] Maintenance/upgrade black ([#4136](https://github.com/great-expectations/great_expectations/pull/4136))
* [MAINTENANCE] Alter `great_expectations` pipeline trigger to be more consistent ([#4138](https://github.com/great-expectations/great_expectations/pull/4138))
* [MAINTENANCE] Remove remaining unused imports ([#4137](https://github.com/great-expectations/great_expectations/pull/4137))
* [MAINTENANCE] Remove `class_name` as mandatory field from `RuleBasedProfiler` ([#4139](https://github.com/great-expectations/great_expectations/pull/4139))
* [MAINTENANCE] Ensure `AWSAthena` does not create temporary table as part of processing Batch by default, which is currently not supported ([#4103](https://github.com/great-expectations/great_expectations/pull/4103))
* [MAINTENANCE] Remove unused `Exception as e` instances ([#4143](https://github.com/great-expectations/great_expectations/pull/4143))
* [MAINTENANCE] Standardize DictDot Method Behaviors Formally for Consistent Usage Patterns in Subclasses ([#4131](https://github.com/great-expectations/great_expectations/pull/4131))
* [MAINTENANCE] Remove unused f-strings ([#4142](https://github.com/great-expectations/great_expectations/pull/4142))
* [MAINTENANCE] Minor Validator code clean up -- for better code clarity ([#4147](https://github.com/great-expectations/great_expectations/pull/4147))
* [MAINTENANCE] Refactoring of `test_script_runner.py`. Integration and Docs tests ([#4145](https://github.com/great-expectations/great_expectations/pull/4145))
* [MAINTENANCE] Remove `compatability` stage from `dependency-graph` pipeline ([#4161](https://github.com/great-expectations/great_expectations/pull/4161))
* [MAINTENANCE] CLOUD-618: GE Cloud "account" to "organization" rename ([#4146](https://github.com/great-expectations/great_expectations/pull/4146))

0.14.5
-----------------
* [FEATURE] Delete profilers from DataContext ([#4067](https://github.com/great-expectations/great_expectations/pull/4067))
* [FEATURE] [BUGFIX] Support nullable int column types ([#4044](https://github.com/great-expectations/great_expectations/pull/4044)) (thanks @scnerd)
* [FEATURE] Rule-Based Profiler Configuration and Runtime Arguments Reconciliation Logic ([#4111](https://github.com/great-expectations/great_expectations/pull/4111))
* [BUGFIX] Add default BIGQUERY_TYPES ([#4096](https://github.com/great-expectations/great_expectations/pull/4096))
* [BUGFIX] Pin `pip --upgrade` to a specific version for CI/CD pipeline ([#4100](https://github.com/great-expectations/great_expectations/pull/4100))
* [BUGFIX] Use `pip==20.2.4` for usage statistics stage of CI/CD ([#4102](https://github.com/great-expectations/great_expectations/pull/4102))
* [BUGFIX] Fix shared state issue in renderer test ([#4000](https://github.com/great-expectations/great_expectations/pull/4000))
* [BUGFIX] Missing docstrings on validator expect_ methods ([#4062](https://github.com/great-expectations/great_expectations/pull/4062)) ([#4081](https://github.com/great-expectations/great_expectations/pull/4081))
* [BUGFIX] Fix s3 path suffix bug on windows ([#4042](https://github.com/great-expectations/great_expectations/pull/4042)) (thanks @scnerd)
* [MAINTENANCE] fix typos in changelogs ([#4093](https://github.com/great-expectations/great_expectations/pull/4093))
* [MAINTENANCE] Migration of GCP tests to new project ([#4072](https://github.com/great-expectations/great_expectations/pull/4072))
* [MAINTENANCE] Refactor Validator methods ([#4095](https://github.com/great-expectations/great_expectations/pull/4095))
* [MAINTENANCE] Fix Configuration Schema and Refactor Rule-Based Profiler; Initial Implementation of Reconciliation Logic Between Configuration and Runtime Arguments ([#4088](https://github.com/great-expectations/great_expectations/pull/4088))
* [MAINTENANCE] Minor Cleanup -- remove unnecessary default arguments from dictionary cleaner ([#4110](https://github.com/great-expectations/great_expectations/pull/4110))

0.14.4
-----------------
* [BUGFIX] Fix typing_extensions requirement to allow for proper build ([#4083](https://github.com/great-expectations/great_expectations/pull/4083)) (thanks @vojtakopal and @Godoy)
* [DOCS] data docs action rewrite ([#4087](https://github.com/great-expectations/great_expectations/pull/4087))
* [DOCS] metric store how to rewrite ([#4086](https://github.com/great-expectations/great_expectations/pull/4086))
* [MAINTENANCE] Change `logger.warn` to `logger.warning` to remove deprecation warnings ([#4085](https://github.com/great-expectations/great_expectations/pull/4085))

0.14.3
-----------------
* [FEATURE] Profiler Store ([#3990](https://github.com/great-expectations/great_expectations/pull/3990))
* [FEATURE] List profilers from DataContext ([#4023](https://github.com/great-expectations/great_expectations/pull/4023))
* [FEATURE] add bigquery json credentials kwargs for sqlalchemy connect ([#4039](https://github.com/great-expectations/great_expectations/pull/4039))
* [FEATURE] Get profilers from DataContext ([#4033](https://github.com/great-expectations/great_expectations/pull/4033))
* [FEATURE] Add RuleBasedProfiler to `test_yaml_config` utility ([#4038](https://github.com/great-expectations/great_expectations/pull/4038))
* [BUGFIX] Checkpoint Configurator fix to allow notebook logging suppression ([#4057](https://github.com/great-expectations/great_expectations/pull/4057))
* [DOCS] Created a page containing our glossary of terms and definitions. ([#4056](https://github.com/great-expectations/great_expectations/pull/4056))
* [DOCS] swap of old uri for new in data docs generated ([#4013](https://github.com/great-expectations/great_expectations/pull/4013))
* [MAINTENANCE] Refactor `test_yaml_config` ([#4029](https://github.com/great-expectations/great_expectations/pull/4029))
* [MAINTENANCE] Additional distinction made between V2 and V3 upgrade script ([#4046](https://github.com/great-expectations/great_expectations/pull/4046))
* [MAINTENANCE] Correcting Checkpoint Configuration and Execution Implementation ([#4015](https://github.com/great-expectations/great_expectations/pull/4015))
* [MAINTENANCE] Update minimum version for SQL Alchemy ([#4055](https://github.com/great-expectations/great_expectations/pull/4055))
* [MAINTENANCE] Refactor RBP constructor to work with **kwargs instantiation pattern through config objects ([#4043](https://github.com/great-expectations/great_expectations/pull/4043))
* [MAINTENANCE] Remove unnecessary metric dependency evaluations and add common table column types metric. ([#4063](https://github.com/great-expectations/great_expectations/pull/4063))
* [MAINTENANCE] Clean up new RBP types, method signatures, and method names for the long term. ([#4064](https://github.com/great-expectations/great_expectations/pull/4064))
* [MAINTENANCE] fixed broken function call in CLI ([#4068](https://github.com/great-expectations/great_expectations/pull/4068))

0.14.2
-----------------
* [FEATURE] Marshmallow schema for Rule Based Profiler ([#3982](https://github.com/great-expectations/great_expectations/pull/3982))
* [FEATURE] Enable Rule-Based Profile Parameter Access To Collection Typed Values ([#3998](https://github.com/great-expectations/great_expectations/pull/3998))
* [BUGFIX] Docs integration pipeline bugfix  ([#3997](https://github.com/great-expectations/great_expectations/pull/3997))
* [BUGFIX] Enables spark-native null filtering ([#4004](https://github.com/great-expectations/great_expectations/pull/4004))
* [DOCS] Gtm/cta in docs ([#3993](https://github.com/great-expectations/great_expectations/pull/3993))
* [DOCS] Fix incorrect variable name in how_to_configure_an_expectation_store_in_amazon_s3.md ([#3971](https://github.com/great-expectations/great_expectations/pull/3971)) (thanks @moritzkoerber)
* [DOCS] update custom docs css to add a subtle border around tabbed content ([#4001](https://github.com/great-expectations/great_expectations/pull/4001))
* [DOCS] Migration Guide now includes example for Spark data ([#3996](https://github.com/great-expectations/great_expectations/pull/3996))
* [DOCS] Revamp Airflow Deployment Pattern ([#3963](https://github.com/great-expectations/great_expectations/pull/3963)) (thanks @denimalpaca)
* [DOCS] updating redirects to reflect a moved file ([#4007](https://github.com/great-expectations/great_expectations/pull/4007))
* [DOCS] typo in gcp + bigquery tutorial ([#4018](https://github.com/great-expectations/great_expectations/pull/4018))
* [DOCS] Additional description of Kubernetes Operators in GCP Deployment Guide ([#4019](https://github.com/great-expectations/great_expectations/pull/4019))
* [DOCS] Migration Guide now includes example for Databases ([#4005](https://github.com/great-expectations/great_expectations/pull/4005))
* [DOCS] Update how to instantiate without a yml file ([#3995](https://github.com/great-expectations/great_expectations/pull/3995))
* [MAINTENANCE] Refactor of `test_script_runner.py` to break-up test list ([#3987](https://github.com/great-expectations/great_expectations/pull/3987))
* [MAINTENANCE] Small refactor for tests that allows DB setup to be done from all tests ([#4012](https://github.com/great-expectations/great_expectations/pull/4012))

0.14.1
-----------------
* [FEATURE] Add pagination/search to CLI batch request listing ([#3854](https://github.com/great-expectations/great_expectations/pull/3854))
* [BUGFIX] Safeguard against using V2 API with V3 Configuration ([#3954](https://github.com/great-expectations/great_expectations/pull/3954))
* [BUGFIX] Bugfix and refactor for `cloud-db-integration` pipeline ([#3977](https://github.com/great-expectations/great_expectations/pull/3977))
* [BUGFIX] Fixes breaking typo in expect_column_values_to_be_json_parseable ([#3983](https://github.com/great-expectations/great_expectations/pull/3983))
* [BUGFIX] Fixes issue where nested columns could not be addressed properly in spark ([#3986](https://github.com/great-expectations/great_expectations/pull/3986))
* [DOCS] How to connect to your data in `mssql` ([#3950](https://github.com/great-expectations/great_expectations/pull/3950))
* [DOCS] MigrationGuide - Adding note on Migrating Expectation Suites ([#3959](https://github.com/great-expectations/great_expectations/pull/3959))
* [DOCS] Incremental Update: The Universal Map's Getting Started Tutorial ([#3881](https://github.com/great-expectations/great_expectations/pull/3881))
* [DOCS] Note about creating backup of Checkpoints ([#3968](https://github.com/great-expectations/great_expectations/pull/3968))
* [DOCS] Connecting to BigQuery Doc line references fix ([#3974](https://github.com/great-expectations/great_expectations/pull/3974))
* [DOCS] Remove RTD snippet about comments/suggestions from Docusaurus docs ([#3980](https://github.com/great-expectations/great_expectations/pull/3980))
* [DOCS] Add howto for the OpenLineage validation operator ([#3688](https://github.com/great-expectations/great_expectations/pull/3688)) (thanks @rossturk)
* [DOCS] Updates to README.md ([#3964](https://github.com/great-expectations/great_expectations/pull/3964))
* [DOCS] Update migration guide ([#3967](https://github.com/great-expectations/great_expectations/pull/3967))
* [MAINTENANCE] Refactor docs dependency script ([#3952](https://github.com/great-expectations/great_expectations/pull/3952))
* [MAINTENANCE] Use Effective SQLAlchemy for Reflection Fallback Logic and SQL Metrics ([#3958](https://github.com/great-expectations/great_expectations/pull/3958))
* [MAINTENANCE] Remove outdated scripts ([#3953](https://github.com/great-expectations/great_expectations/pull/3953))
* [MAINTENANCE] Add pytest opt to improve collection time ([#3976](https://github.com/great-expectations/great_expectations/pull/3976))
* [MAINTENANCE] Refactor `render` method in PageRenderer ([#3962](https://github.com/great-expectations/great_expectations/pull/3962))
* [MAINTENANCE] Standardize rule based profiler testing directories organization ([#3984](https://github.com/great-expectations/great_expectations/pull/3984))
* [MAINTENANCE] Metrics Cleanup ([#3989](https://github.com/great-expectations/great_expectations/pull/3989))
* [MAINTENANCE] Refactor `render` method of Content Block Renderer ([#3960](https://github.com/great-expectations/great_expectations/pull/3960))

0.14.0
-----------------
* [BREAKING] Change Default CLI Flag To V3 ([#3943](https://github.com/great-expectations/great_expectations/pull/3943))
* [FEATURE] Cloud-399/Cloud-519: Add Cloud Notification Action ([#3891](https://github.com/great-expectations/great_expectations/pull/3891))
* [FEATURE] `great_expectations_contrib` CLI tool ([#3909](https://github.com/great-expectations/great_expectations/pull/3909))
* [FEATURE] Update `dependency_graph` pipeline to use `dgtest` CLI ([#3912](https://github.com/great-expectations/great_expectations/pull/3912))
* [FEATURE] Incorporate updated dgtest CLI tool in experimental pipeline ([#3927](https://github.com/great-expectations/great_expectations/pull/3927))
* [FEATURE] Add YAML config option to disable progress bars ([#3794](https://github.com/great-expectations/great_expectations/pull/3794))
* [BUGFIX] Fix internal links to docs that may be rendered incorrectly ([#3915](https://github.com/great-expectations/great_expectations/pull/3915))
* [BUGFIX] Update SlackNotificationAction to send slack_token and slack_channel to send_slack_notification function ([#3873](https://github.com/great-expectations/great_expectations/pull/3873)) (thanks @Calvo94)
* [BUGFIX] `CheckDocsDependenciesChanges` to only handle `.py` files ([#3936](https://github.com/great-expectations/great_expectations/pull/3936))
* [BUGFIX] Provide ability to capture schema_name for SQL-based datasources; fix method usage bugs. ([#3938](https://github.com/great-expectations/great_expectations/pull/3938))
* [BUGFIX] Ensure that Jupyter Notebook cells convert JSON strings to Python-compliant syntax ([#3939](https://github.com/great-expectations/great_expectations/pull/3939))
* [BUGFIX] Cloud-519/cloud notification action return type ([#3942](https://github.com/great-expectations/great_expectations/pull/3942))
* [BUGFIX] Fix issue with regex groups in `check_docs_deps` ([#3949](https://github.com/great-expectations/great_expectations/pull/3949))
* [DOCS] Created link checker, fixed broken links ([#3930](https://github.com/great-expectations/great_expectations/pull/3930))
* [DOCS] adding the link checker to the build ([#3933](https://github.com/great-expectations/great_expectations/pull/3933))
* [DOCS] Add name to link checker in build ([#3935](https://github.com/great-expectations/great_expectations/pull/3935))
* [DOCS] GCP Deployment Pattern ([#3926](https://github.com/great-expectations/great_expectations/pull/3926))
* [DOCS] remove v3api flag in documentation ([#3944](https://github.com/great-expectations/great_expectations/pull/3944))
* [DOCS] Make corrections in HOWTO Guides for Getting Data from SQL Sources ([#3945](https://github.com/great-expectations/great_expectations/pull/3945))
* [DOCS] Tiny doc fix ([#3948](https://github.com/great-expectations/great_expectations/pull/3948))
* [MAINTENANCE] Fix breaking change caused by the new version of ruamel.yaml ([#3908](https://github.com/great-expectations/great_expectations/pull/3908))
* [MAINTENANCE] Drop extraneous print statement in self_check/util.py. ([#3905](https://github.com/great-expectations/great_expectations/pull/3905))
* [MAINTENANCE] Raise exceptions on init in cloud mode ([#3913](https://github.com/great-expectations/great_expectations/pull/3913))
* [MAINTENANCE] removing commented requirement ([#3920](https://github.com/great-expectations/great_expectations/pull/3920))
* [MAINTENANCE] Patch for atomic renderer snapshot tests ([#3918](https://github.com/great-expectations/great_expectations/pull/3918))
* [MAINTENANCE] Remove types/expectations.py ([#3928](https://github.com/great-expectations/great_expectations/pull/3928))
* [MAINTENANCE] Tests/test data class serializable dot dict ([#3924](https://github.com/great-expectations/great_expectations/pull/3924))
* [MAINTENANCE] Ensure that concurrency is backwards compatible ([#3872](https://github.com/great-expectations/great_expectations/pull/3872))
* [MAINTENANCE] Fix issue where meta was not recognized as a kwarg ([#3852](https://github.com/great-expectations/great_expectations/pull/3852))

0.13.49
-----------------
* [FEATURE] PandasExecutionEngine is able to instantiate Google Storage client in Google Cloud Composer ([#3896](https://github.com/great-expectations/great_expectations/pull/3896))
* [BUGFIX] Revert change to ExpectationSuite constructor ([#3902](https://github.com/great-expectations/great_expectations/pull/3902))
* [MAINTENANCE] SQL statements that are of TextClause type expressed as subqueries ([#3899](https://github.com/great-expectations/great_expectations/pull/3899))

0.13.48
-----------------
* [DOCS] Updates to configuring credentials ([#3856](https://github.com/great-expectations/great_expectations/pull/3856))
* [DOCS] Add docs on creating suites with the UserConfigurableProfiler ([#3877](https://github.com/great-expectations/great_expectations/pull/3877))
* [DOCS] Update how to configure an expectation store in GCS ([#3874](https://github.com/great-expectations/great_expectations/pull/3874))
* [DOCS] Update how to configure a validation result store in GCS ([#3887](https://github.com/great-expectations/great_expectations/pull/3887))
* [DOCS] Update how to host and share data docs on GCS ([#3889](https://github.com/great-expectations/great_expectations/pull/3889))
* [DOCS] Organize metadata store sidebar category by type of store ([#3890](https://github.com/great-expectations/great_expectations/pull/3890))
* [MAINTENANCE] `add_expectation()` in `ExpectationSuite` supports usage statistics for GE.  ([#3824](https://github.com/great-expectations/great_expectations/pull/3824))
* [MAINTENANCE] Clean up Metrics type usage, SQLAlchemyExecutionEngine and SQLAlchemyBatchData implementation, and SQLAlchemy API usage ([#3884](https://github.com/great-expectations/great_expectations/pull/3884))

0.13.47
-----------------
* [FEATURE] Add support for named groups in data asset regex ([#3855](https://github.com/great-expectations/great_expectations/pull/3855))
* [BUGFIX] Fix issue where dependency graph tester picks up non *.py files and add test file ([#3830](https://github.com/great-expectations/great_expectations/pull/3830))
* [BUGFIX] Ensure proper exit code for dependency graph script ([#3839](https://github.com/great-expectations/great_expectations/pull/3839))
* [BUGFIX] Allows GE to work when installed in a zip file (PEP 273). Fixes issue [#3772](https://github.com/great-expectations/great_expectations/pull/3772) ([#3798](https://github.com/great-expectations/great_expectations/pull/3798)) (thanks @joseignaciorc)
* [BUGFIX] Update conditional for TextClause isinstance check in SQLAlchemyExecutionEngine ([#3844](https://github.com/great-expectations/great_expectations/pull/3844))
* [BUGFIX] Fix usage stats events ([#3857](https://github.com/great-expectations/great_expectations/pull/3857))
* [BUGFIX] Make ExpectationContext optional and remove when null to ensure backwards compatability ([#3859](https://github.com/great-expectations/great_expectations/pull/3859))
* [BUGFIX] Fix sqlalchemy expect_compound_columns_to_be_unique ([#3827](https://github.com/great-expectations/great_expectations/pull/3827)) (thanks @harperweaver-dox)
* [BUGFIX] Ensure proper serialization of SQLAlchemy Legacy Row ([#3865](https://github.com/great-expectations/great_expectations/pull/3865))
* [DOCS] Update migration_guide.md ([#3832](https://github.com/great-expectations/great_expectations/pull/3832))
* [MAINTENANCE] Remove the need for DataContext registry in the instrumentation of the Legacy Profiler profiling method. ([#3836](https://github.com/great-expectations/great_expectations/pull/3836))
* [MAINTENANCE] Remove DataContext registry ([#3838](https://github.com/great-expectations/great_expectations/pull/3838))
* [MAINTENANCE] Refactor cli suite conditionals ([#3841](https://github.com/great-expectations/great_expectations/pull/3841))
* [MAINTENANCE] adding hints to stores in data context ([#3849](https://github.com/great-expectations/great_expectations/pull/3849))
* [MAINTENANCE] Improve usage stats testing ([#3858](https://github.com/great-expectations/great_expectations/pull/3858), [#3861](https://github.com/great-expectations/great_expectations/pull/3861))
* [MAINTENANCE] Make checkpoint methods in DataContext pass-through ([#3860](https://github.com/great-expectations/great_expectations/pull/3860))
* [MAINTENANCE] Datasource and ExecutionEngine Anonymizers handle missing module_name ([#3867](https://github.com/great-expectations/great_expectations/pull/3867))
* [MAINTENANCE] Add logging around DatasourceInitializationError in DataContext ([#3846](https://github.com/great-expectations/great_expectations/pull/3846))
* [MAINTENANCE] Use f-string to prevent string concat issue in Evaluation Parameters ([#3864](https://github.com/great-expectations/great_expectations/pull/3864))
* [MAINTENANCE] Test for errors / invalid messages in logs & fix various existing issues ([#3875](https://github.com/great-expectations/great_expectations/pull/3875))

0.13.46
-----------------
* [FEATURE] Instrument Runtime DataConnector for Usage Statistics: Add "checkpoint.run" Event Schema ([#3797](https://github.com/great-expectations/great_expectations/pull/3797))
* [FEATURE] Add suite creation type field to CLI SUITE "new" and "edit" Usage Statistics events ([#3810](https://github.com/great-expectations/great_expectations/pull/3810))
* [FEATURE] [EXPERIMENTAL] Dependency graph based testing strategy and related pipeline ([#3738](https://github.com/great-expectations/great_expectations/pull/3738), [#3815](https://github.com/great-expectations/great_expectations/pull/3815), [#3818](https://github.com/great-expectations/great_expectations/pull/3818))
* [FEATURE] BaseDataContext registry ([#3812](https://github.com/great-expectations/great_expectations/pull/3812), [#3819](https://github.com/great-expectations/great_expectations/pull/3819))
* [FEATURE] Add usage statistics instrumentation to Legacy UserConfigurableProfiler execution ([#3828](https://github.com/great-expectations/great_expectations/pull/3828))
* [BUGFIX] CheckpointConfig.__deepcopy__() must copy all fields, including the null-valued fields ([#3793](https://github.com/great-expectations/great_expectations/pull/3793))
* [BUGFIX] Fix issue where configuration store didn't allow nesting ([#3811](https://github.com/great-expectations/great_expectations/pull/3811))
* [BUGFIX] Fix Minor Bugs in and Clean Up UserConfigurableProfiler ([#3822](https://github.com/great-expectations/great_expectations/pull/3822))
* [BUGFIX] Ensure proper replacement of nulls in Jupyter Notebooks ([#3782](https://github.com/great-expectations/great_expectations/pull/3782))
* [BUGFIX] Fix issue where configuration store didn't allow nesting ([#3811](https://github.com/great-expectations/great_expectations/pull/3811))
* [DOCS] Clean up TOC ([#3783](https://github.com/great-expectations/great_expectations/pull/3783))
* [DOCS] Update Checkpoint and Actions Reference with testing ([#3787](https://github.com/great-expectations/great_expectations/pull/3787))
* [DOCS] Update How to install Great Expectations locally ([#3805](https://github.com/great-expectations/great_expectations/pull/3805))
* [DOCS] How to install Great Expectations in a hosted environment ([#3808](https://github.com/great-expectations/great_expectations/pull/3808))
* [MAINTENANCE] Make BatchData Serialization More Robust ([#3791](https://github.com/great-expectations/great_expectations/pull/3791))
* [MAINTENANCE] Refactor SiteIndexBuilder.build() ([#3789](https://github.com/great-expectations/great_expectations/pull/3789))
* [MAINTENANCE] Update ref to ge-cla-bot in PR template ([#3799](https://github.com/great-expectations/great_expectations/pull/3799))
* [MAINTENANCE] Anonymizer clean up and refactor ([#3801](https://github.com/great-expectations/great_expectations/pull/3801))
* [MAINTENANCE] Certify the expectation "expect_table_row_count_to_equal_other_table" for V3 API ([#3803](https://github.com/great-expectations/great_expectations/pull/3803))
* [MAINTENANCE] Refactor to enable broader use of event emitting method for usage statistics ([#3825](https://github.com/great-expectations/great_expectations/pull/3825))
* [MAINTENANCE] Clean up temp file after CI/CD run ([#3823](https://github.com/great-expectations/great_expectations/pull/3823))
* [MAINTENANCE] Raising exceptions for misconfigured datasources in cloud mode ([#3866](https://github.com/great-expectations/great_expectations/pull/3866))

0.13.45
-----------------
* [FEATURE] Feature/render validation metadata ([#3397](https://github.com/great-expectations/great_expectations/pull/3397)) (thanks @vshind1)
* [FEATURE] Added expectation expect_column_values_to_not_contain_special_characters() ([#2849](https://github.com/great-expectations/great_expectations/pull/2849), [#3771](https://github.com/great-expectations/great_expectations/pull/3771)) (thanks @jaibirsingh)
* [FEATURE] Like and regex-based expectations in Athena dialect ([#3762](https://github.com/great-expectations/great_expectations/pull/3762)) (thanks @josges)
* [FEATURE] Rename `deep_filter_properties_dict()` to `deep_filter_properties_iterable()`
* [FEATURE] Extract validation result failures ([#3552](https://github.com/great-expectations/great_expectations/pull/3552)) (thanks @BenGale93)
* [BUGFIX] Allow now() eval parameter to be used by itself ([#3719](https://github.com/great-expectations/great_expectations/pull/3719))
* [BUGFIX] Fixing broken logo for legacy RTD docs ([#3769](https://github.com/great-expectations/great_expectations/pull/3769))
* [BUGFIX] Adds version-handling to sqlalchemy make_url imports ([#3768](https://github.com/great-expectations/great_expectations/pull/3768))
* [BUGFIX] Integration test to avoid regression of simple PandasExecutionEngine workflow ([#3770](https://github.com/great-expectations/great_expectations/pull/3770))
* [BUGFIX] Fix copying of CheckpointConfig for substitution and printing purposes ([#3759](https://github.com/great-expectations/great_expectations/pull/3759))
* [BUGFIX] Fix evaluation parameter usage with Query Store ([#3763](https://github.com/great-expectations/great_expectations/pull/3763))
* [BUGFIX] Feature/fix row condition quotes ([#3676](https://github.com/great-expectations/great_expectations/pull/3676)) (thanks @benoitLebreton-perso)
* [BUGFIX] Fix incorrect filling out of anonymized event payload ([#3780](https://github.com/great-expectations/great_expectations/pull/3780))
* [BUGFIX] Don't reset_index for conditional expectations ([#3667](https://github.com/great-expectations/great_expectations/pull/3667)) (thanks @abekfenn)
* [DOCS] Update expectations gallery link in V3 notebook documentation ([#3747](https://github.com/great-expectations/great_expectations/pull/3747))
* [DOCS] Correct V3 documentation link in V2 notebooks to point to V2 documentation ([#3750](https://github.com/great-expectations/great_expectations/pull/3750))
* [DOCS] How to pass an in-memory DataFrame to a Checkpoint ([#3756](https://github.com/great-expectations/great_expectations/pull/3756))
* [MAINTENANCE] Fix typo in Getting Started Guide ([#3749](https://github.com/great-expectations/great_expectations/pull/3749))
* [MAINTENANCE] Add proper docstring and type hints to Validator ([#3767](https://github.com/great-expectations/great_expectations/pull/3767))
* [MAINTENANCE] Clean up duplicate logging statements about optional `black` dep ([#3778](https://github.com/great-expectations/great_expectations/pull/3778))

0.13.44
-----------------
* [FEATURE] Add new result_format to include unexpected_row_list ([#3346](https://github.com/great-expectations/great_expectations/pull/3346))
* [FEATURE] Implement "deep_filter_properties_dict()" method ([#3703](https://github.com/great-expectations/great_expectations/pull/3703))
* [FEATURE] Create Constants for GETTING_STARTED Entities (e.g., datasource_name, expectation_suite_name, etc.) ([#3712](https://github.com/great-expectations/great_expectations/pull/3712))
* [FEATURE] Add usage statistics event for DataContext.get_batch_list() method ([#3708](https://github.com/great-expectations/great_expectations/pull/3708))
* [FEATURE] Add data_context.run_checkpoint event to usage statistics ([#3721](https://github.com/great-expectations/great_expectations/pull/3721))
* [FEATURE] Add event_duration to usage statistics events ([#3729](https://github.com/great-expectations/great_expectations/pull/3729))
* [FEATURE] InferredAssetSqlDataConnector's introspection can list external tables in Redshift Spectrum ([#3646](https://github.com/great-expectations/great_expectations/pull/3646))
* [BUGFIX] Using a RuntimeBatchRequest in a Checkpoint with a top-level batch_request instead of validations ([#3680](https://github.com/great-expectations/great_expectations/pull/3680))
* [BUGFIX] Using a RuntimeBatchRequest in a Checkpoint at runtime with Checkpoint.run() ([#3713](https://github.com/great-expectations/great_expectations/pull/3713))
* [BUGFIX] Using a RuntimeBatchRequest in a Checkpoint at runtime with context.run_checkpoint() ([#3718](https://github.com/great-expectations/great_expectations/pull/3718))
* [BUGFIX] Use SQLAlchemy make_url helper where applicable when parsing URLs ([#3722](https://github.com/great-expectations/great_expectations/pull/3722))
* [BUGFIX] Adds check for quantile_ranges to be ordered or unbounded pairs ([#3724](https://github.com/great-expectations/great_expectations/pull/3724))
* [BUGFIX] Updates MST renderer to return JSON-parseable boolean ([#3728](https://github.com/great-expectations/great_expectations/pull/3728))
* [BUGFIX] Removes sqlite suppression for expect_column_quantile_values_to_be_between test definitions ([#3735](https://github.com/great-expectations/great_expectations/pull/3735))
* [BUGFIX] Handle contradictory configurations in checkpoint.yml, checkpoint.run(), and context.run_checkpoint() ([#3723](https://github.com/great-expectations/great_expectations/pull/3723))
* [BUGFIX] fixed a bug where expectation metadata doesn't appear in edit template for table-level expectations ([#3129](https://github.com/great-expectations/great_expectations/pull/3129)) (thanks @olechiw)
* [BUGFIX] Added temp_table creation for Teradata in SqlAlchemyBatchData ([#3731](https://github.com/great-expectations/great_expectations/pull/3731)) (thanks @imamolp)
* [DOCS] Add Databricks video walkthrough link ([#3702](https://github.com/great-expectations/great_expectations/pull/3702), [#3704](https://github.com/great-expectations/great_expectations/pull/3704))
* [DOCS] Update the link to configure a MetricStore ([#3711](https://github.com/great-expectations/great_expectations/pull/3711), [#3714](https://github.com/great-expectations/great_expectations/pull/3714)) (thanks @txblackbird)
* [DOCS] Updated code example to remove deprecated "File" function ([#3632](https://github.com/great-expectations/great_expectations/pull/3632)) (thanks @daccorti)
* [DOCS] Delete how_to_add_a_validation_operator.md as OBE. ([#3734](https://github.com/great-expectations/great_expectations/pull/3734))
* [DOCS] Update broken link in FOOTER.md to point to V3 documentation ([#3745](https://github.com/great-expectations/great_expectations/pull/3745))
* [MAINTENANCE] Improve type hinting (using Optional type) ([#3709](https://github.com/great-expectations/great_expectations/pull/3709))
* [MAINTENANCE] Standardize names for assets that are used in Getting Started Guide ([#3706](https://github.com/great-expectations/great_expectations/pull/3706))
* [MAINTENANCE] Clean up remaining improper usage of Optional type annotation ([#3710](https://github.com/great-expectations/great_expectations/pull/3710))
* [MAINTENANCE] Refinement of Getting Started Guide script ([#3715](https://github.com/great-expectations/great_expectations/pull/3715))
* [MAINTENANCE] cloud-410 - Support for Column Descriptions ([#3707](https://github.com/great-expectations/great_expectations/pull/3707))
* [MAINTENANCE] Types Clean Up in Checkpoint, Batch, and DataContext Classes ([#3737](https://github.com/great-expectations/great_expectations/pull/3737))
* [MAINTENANCE] Remove DeprecationWarning for validator.remove_expectation ([#3744](https://github.com/great-expectations/great_expectations/pull/3744))

0.13.43
-----------------
* [FEATURE] Enable support for Teradata SQLAlchemy dialect ([#3496](https://github.com/great-expectations/great_expectations/pull/3496)) (thanks @imamolp)
* [FEATURE] Dremio connector added (SQLalchemy) ([#3624](https://github.com/great-expectations/great_expectations/pull/3624)) (thanks @chufe-dremio)
* [FEATURE] Adds expect_column_values_to_be_string_integers_increasing ([#3642](https://github.com/great-expectations/great_expectations/pull/3642))
* [FEATURE] Enable "column.quantile_values" and "expect_column_quantile_values_to_be_between" for SQLite; add/enable new tests ([#3695](https://github.com/great-expectations/great_expectations/pull/3695))
* [BUGFIX] Allow glob_directive for DBFS Data Connectors ([#3673](https://github.com/great-expectations/great_expectations/pull/3673))
* [BUGFIX] Update black version in pre-commit config ([#3674](https://github.com/great-expectations/great_expectations/pull/3674))
* [BUGFIX] Make sure to add "mostly_pct" value if "mostly" kwarg present ([#3661](https://github.com/great-expectations/great_expectations/pull/3661))
* [BUGFIX] Fix BatchRequest.to_json_dict() to not overwrite original fields; also type usage cleanup in CLI tests ([#3683](https://github.com/great-expectations/great_expectations/pull/3683))
* [BUGFIX] Fix pyfakefs boto / GCS incompatibility ([#3694](https://github.com/great-expectations/great_expectations/pull/3694))
* [BUGFIX] Update prefix attr assignment in cloud-based DataConnector constructors ([#3668](https://github.com/great-expectations/great_expectations/pull/3668))
* [BUGFIX] Update 'list_keys' signature for all cloud-based tuple store child classes ([#3669](https://github.com/great-expectations/great_expectations/pull/3669))
* [BUGFIX] evaluation parameters from different expectation suites dependencies ([#3684](https://github.com/great-expectations/great_expectations/pull/3684)) (thanks @OmriBromberg)
* [DOCS] Databricks deployment pattern documentation ([#3682](https://github.com/great-expectations/great_expectations/pull/3682))
* [DOCS] Remove how_to_instantiate_a_data_context_on_databricks_spark_cluster ([#3687](https://github.com/great-expectations/great_expectations/pull/3687))
* [DOCS] Updates to Databricks doc based on friction logging ([#3696](https://github.com/great-expectations/great_expectations/pull/3696))
* [MAINTENANCE] Fix checkpoint anonymization and make BatchRequest.to_json_dict() more robust ([#3675](https://github.com/great-expectations/great_expectations/pull/3675))
* [MAINTENANCE] Update kl_divergence domain_type ([#3681](https://github.com/great-expectations/great_expectations/pull/3681))
* [MAINTENANCE] update filter_properties_dict to use set for inclusions and exclusions (instead of list) ([#3698](https://github.com/great-expectations/great_expectations/pull/3698))
* [MAINTENANCE] Adds CITATION.cff ([#3697](https://github.com/great-expectations/great_expectations/pull/3697))

0.13.42
-----------------
* [FEATURE] DBFS Data connectors ([#3659](https://github.com/great-expectations/great_expectations/pull/3659))
* [BUGFIX] Fix "null" appearing in notebooks due to incorrect ExpectationConfigurationSchema serialization ([#3638](https://github.com/great-expectations/great_expectations/pull/3638))
* [BUGFIX] Ensure that result_format from saved expectation suite json file takes effect ([#3634](https://github.com/great-expectations/great_expectations/pull/3634))
* [BUGFIX] Allowing user specified run_id to appear in WarningAndFailureExpectationSuitesValidationOperator validation result ([#3386](https://github.com/great-expectations/great_expectations/pull/3386)) (thanks @wniroshan)
* [BUGFIX] Update black dependency to ensure passing Azure builds on Python 3.9 ([#3664](https://github.com/great-expectations/great_expectations/pull/3664))
* [BUGFIX] fix Issue [#3405](https://github.com/great-expectations/great_expectations/pull/3405) - gcs client init in pandas engine ([#3408](https://github.com/great-expectations/great_expectations/pull/3408)) (thanks @dz-1)
* [BUGFIX] Recursion error when passing RuntimeBatchRequest with query into Checkpoint using validations ([#3654](https://github.com/great-expectations/great_expectations/pull/3654))
* [MAINTENANCE] Cloud 388/supported expectations query ([#3635](https://github.com/great-expectations/great_expectations/pull/3635))
* [MAINTENANCE] Proper separation of concerns between specific File Path Data Connectors and corresponding ExecutionEngine objects ([#3643](https://github.com/great-expectations/great_expectations/pull/3643))
* [MAINTENANCE] Enable Docusaurus tests for S3 ([#3645](https://github.com/great-expectations/great_expectations/pull/3645))
* [MAINTENANCE] Formalize Exception Handling Between DataConnector and ExecutionEngine Implementations, and Update DataConnector Configuration Usage in Tests ([#3644](https://github.com/great-expectations/great_expectations/pull/3644))
* [MAINTENANCE] Adds util for handling SADeprecation warning ([#3651](https://github.com/great-expectations/great_expectations/pull/3651))

0.13.41
-----------------
* [FEATURE] Support median calculation in AWS Athena ([#3596](https://github.com/great-expectations/great_expectations/pull/3596)) (thanks @persiyanov)
* [BUGFIX] Be able to use spark execution engine with spark reuse flag ([#3541](https://github.com/great-expectations/great_expectations/pull/3541)) (thanks @fep2)
* [DOCS] punctuation how_to_contribute_a_new_expectation_to_great_expectations.md ([#3484](https://github.com/great-expectations/great_expectations/pull/3484)) (thanks @plain-jane-gray)
* [DOCS] Update next_steps.md ([#3483](https://github.com/great-expectations/great_expectations/pull/3483)) (thanks @plain-jane-gray)
* [DOCS] Update how_to_configure_a_validation_result_store_in_gcs.md ([#3482](https://github.com/great-expectations/great_expectations/pull/3482)) (thanks @plain-jane-gray)
* [DOCS] Choosing and configuring DataConnectors ([#3533](https://github.com/great-expectations/great_expectations/pull/3533))
* [DOCS] Remove --no-spark flag from docs tests ([#3625](https://github.com/great-expectations/great_expectations/pull/3625))
* [DOCS] DevRel - docs fixes ([#3498](https://github.com/great-expectations/great_expectations/pull/3498))
* [DOCS] Adding a period ([#3627](https://github.com/great-expectations/great_expectations/pull/3627)) (thanks @plain-jane-gray)
* [DOCS] Remove comments that describe Snowflake parameters as optional ([#3639](https://github.com/great-expectations/great_expectations/pull/3639))
* [MAINTENANCE] Update CODEOWNERS ([#3604](https://github.com/great-expectations/great_expectations/pull/3604))
* [MAINTENANCE] Fix logo ([#3598](https://github.com/great-expectations/great_expectations/pull/3598))
* [MAINTENANCE] Add Expectations to docs navbar ([#3597](https://github.com/great-expectations/great_expectations/pull/3597))
* [MAINTENANCE] Remove unused fixtures ([#3218](https://github.com/great-expectations/great_expectations/pull/3218))
* [MAINTENANCE] Remove unnecessary comment ([#3608](https://github.com/great-expectations/great_expectations/pull/3608))
* [MAINTENANCE] Superconductive Warnings hackathon ([#3612](https://github.com/great-expectations/great_expectations/pull/3612))
* [MAINTENANCE] Bring Core Skills Doc for Creating Batch Under Test ([#3629](https://github.com/great-expectations/great_expectations/pull/3629))
* [MAINTENANCE] Refactor and Clean Up Expectations and Metrics Parts of the Codebase (better encapsulation, improved type hints) ([#3633](https://github.com/great-expectations/great_expectations/pull/3633))


0.13.40
-----------------
* [FEATURE] Retrieve data context config through Cloud API endpoint [#3586](https://github.com/great-expectations/great_expectations/pull/3586)
* [FEATURE] Update Batch IDs to match name change in paths included in batch_request [#3587](https://github.com/great-expectations/great_expectations/pull/3587)
* [FEATURE] V2-to-V3 Upgrade/Migration [#3592](https://github.com/great-expectations/great_expectations/pull/3592)
* [FEATURE] table and graph atomic renderers [#3595](https://github.com/great-expectations/great_expectations/pull/3595)
* [FEATURE] V2-to-V3 Upgrade/Migration (Sidebar.js update) [#3603](https://github.com/great-expectations/great_expectations/pull/3603)
* [DOCS] Fixing broken links and linking to Expectation Gallery [#3591](https://github.com/great-expectations/great_expectations/pull/3591)
* [MAINTENANCE] Get TZLocal back to its original version control. [#3585](https://github.com/great-expectations/great_expectations/pull/3585)
* [MAINTENANCE] Add tests for datetime evaluation parameters [#3601](https://github.com/great-expectations/great_expectations/pull/3601)
* [MAINTENANCE] Removed warning for pandas option display.max_colwidth [#3606](https://github.com/great-expectations/great_expectations/pull/3606)

0.13.39
-----------------
* [FEATURE] Migration of Expectations to Atomic Prescriptive Renderers ([#3530](https://github.com/great-expectations/great_expectations/pull/3530), [#3537](https://github.com/great-expectations/great_expectations/pull/3537))
* [FEATURE] Cloud: Editing Expectation Suites programmatically ([#3564](https://github.com/great-expectations/great_expectations/pull/3564))
* [BUGFIX] Fix deprecation warning for importing from collections ([#3546](https://github.com/great-expectations/great_expectations/pull/3546)) (thanks @shpolina)
* [BUGFIX] SQLAlchemy version 1.3.24 compatibility in map metric provider ([#3507](https://github.com/great-expectations/great_expectations/pull/3507)) (thanks @shpolina)
* [DOCS] Clarify how to configure optional Snowflake parameters in CLI datasource new notebook ([#3543](https://github.com/great-expectations/great_expectations/pull/3543))
* [DOCS] Added breaks to code snippets, reordered guidance ([#3514](https://github.com/great-expectations/great_expectations/pull/3514))
* [DOCS] typo in documentation ([#3542](https://github.com/great-expectations/great_expectations/pull/3542)) (thanks @DanielEdu)
* [DOCS] Update how_to_configure_a_new_data_context_with_the_cli.md ([#3556](https://github.com/great-expectations/great_expectations/pull/3556)) (thanks @plain-jane-gray)
* [DOCS] Improved installation instructions, included in-line installation instructions to getting started ([#3509](https://github.com/great-expectations/great_expectations/pull/3509))
* [DOCS] Update contributing_style.md ([#3521](https://github.com/great-expectations/great_expectations/pull/3521)) (thanks @plain-jane-gray)
* [DOCS] Update contributing_test.md ([#3519](https://github.com/great-expectations/great_expectations/pull/3519)) (thanks @plain-jane-gray)
* [DOCS] Revamp style guides ([#3554](https://github.com/great-expectations/great_expectations/pull/3554))
* [DOCS] Update contributing.md ([#3523](https://github.com/great-expectations/great_expectations/pull/3523), [#3524](https://github.com/great-expectations/great_expectations/pull/3524)) (thanks @plain-jane-gray)
* [DOCS] Simplify getting started ([#3555](https://github.com/great-expectations/great_expectations/pull/3555))
* [DOCS] How to introspect and partition an SQL database ([#3465](https://github.com/great-expectations/great_expectations/pull/3465))
* [DOCS] Update contributing_checklist.md ([#3518](https://github.com/great-expectations/great_expectations/pull/3518)) (thanks @plain-jane-gray)
* [DOCS] Removed duplicate prereq, how_to_instantiate_a_data_context_without_a_yml_file.md ([#3481](https://github.com/great-expectations/great_expectations/pull/3481)) (thanks @plain-jane-gray)
* [DOCS] fix link to expectation glossary ([#3558](https://github.com/great-expectations/great_expectations/pull/3558)) (thanks @sephiartlist)
* [DOCS] Minor Friction ([#3574](https://github.com/great-expectations/great_expectations/pull/3574))
* [MAINTENANCE] Make CLI Check-Config and CLI More Robust ([#3562](https://github.com/great-expectations/great_expectations/pull/3562))
* [MAINTENANCE] tzlocal version fix ([#3565](https://github.com/great-expectations/great_expectations/pull/3565))

0.13.38
-----------------
* [FEATURE] Atomic Renderer: Initial framework and Prescriptive renderers ([#3529](https://github.com/great-expectations/great_expectations/pull/3529))
* [FEATURE] Atomic Renderer: Diagnostic renderers ([#3534](https://github.com/great-expectations/great_expectations/pull/3534))
* [BUGFIX] runtime_parameters: {batch_data: <park DF} serialization ([#3502](https://github.com/great-expectations/great_expectations/pull/3502))
* [BUGFIX] Custom query in RuntimeBatchRequest for expectations using table.row_count metric ([#3508](https://github.com/great-expectations/great_expectations/pull/3508))
* [BUGFIX] Transpose \n and , in notebook ([#3463](https://github.com/great-expectations/great_expectations/pull/3463)) (thanks @mccalluc)
* [BUGFIX] Fix contributor link ([#3462](https://github.com/great-expectations/great_expectations/pull/3462)) (thanks @mccalluc)
* [DOCS] How to introspect and partition a files based data store ([#3464](https://github.com/great-expectations/great_expectations/pull/3464))
* [DOCS] fixed duplication of text in code example ([#3503](https://github.com/great-expectations/great_expectations/pull/3503))
* [DOCS] Make content better reflect the document organization. ([#3510](https://github.com/great-expectations/great_expectations/pull/3510))
* [DOCS] Correcting typos and improving the language. ([#3513](https://github.com/great-expectations/great_expectations/pull/3513))
* [DOCS] Better Sections Numbering in Documentation ([#3515](https://github.com/great-expectations/great_expectations/pull/3515))
* [DOCS] Improved wording ([#3516](https://github.com/great-expectations/great_expectations/pull/3516))
* [DOCS] Improved title wording for section heading ([#3517](https://github.com/great-expectations/great_expectations/pull/3517))
* [DOCS] Improve Readability of Documentation Content ([#3536](https://github.com/great-expectations/great_expectations/pull/3536))
* [MAINTENANCE] Content and test script update ([#3532](https://github.com/great-expectations/great_expectations/pull/3532))
* [MAINTENANCE] Provide Deprecation Notice for the "parse_strings_as_datetimes" Expectation Parameter in V3 ([#3539](https://github.com/great-expectations/great_expectations/pull/3539))

0.13.37
-----------------
* [FEATURE] Implement CompoundColumnsUnique metric for SqlAlchemyExecutionEngine ([#3477](https://github.com/great-expectations/great_expectations/pull/3477))
* [FEATURE] add get_available_data_asset_names_and_types ([#3476](https://github.com/great-expectations/great_expectations/pull/3476))
* [FEATURE] add s3_put_options to TupleS3StoreBackend ([#3470](https://github.com/great-expectations/great_expectations/pull/3470)) (Thanks @kj-9)
* [BUGFIX] Fix TupleS3StoreBackend remove_key bug ([#3489](https://github.com/great-expectations/great_expectations/pull/3489))
* [DOCS] Adding Flyte Deployment pattern to docs ([#3383](https://github.com/great-expectations/great_expectations/pull/3383))
* [DOCS] g_e docs branding updates ([#3471](https://github.com/great-expectations/great_expectations/pull/3471))
* [MAINTENANCE] Add type-hints; add utility method for creating temporary DB tables; clean up imports; improve code readability; and add a directory to pre-commit ([#3475](https://github.com/great-expectations/great_expectations/pull/3475))
* [MAINTENANCE] Clean up for a better code readability. ([#3493](https://github.com/great-expectations/great_expectations/pull/3493))
* [MAINTENANCE] Enable SQL for the "expect_compound_columns_to_be_unique" expectation. ([#3488](https://github.com/great-expectations/great_expectations/pull/3488))
* [MAINTENANCE] Fix some typos ([#3474](https://github.com/great-expectations/great_expectations/pull/3474)) (Thanks @mohamadmansourX)
* [MAINTENANCE] Support SQLAlchemy version 1.3.24 for compatibility with Airflow (Airflow does not currently support later versions of SQLAlchemy). ([#3499](https://github.com/great-expectations/great_expectations/pull/3499))
* [MAINTENANCE] Update contributing_checklist.md ([#3478](https://github.com/great-expectations/great_expectations/pull/3478)) (Thanks @plain-jane-gray)
* [MAINTENANCE] Update how_to_configure_a_validation_result_store_in_gcs.md ([#3480](https://github.com/great-expectations/great_expectations/pull/3480)) (Thanks @plain-jane-gray)
* [MAINTENANCE] update implemented_expectations ([#3492](https://github.com/great-expectations/great_expectations/pull/3492))

0.13.36
-----------------
* [FEATURE] GREAT-3439 extended SlackNotificationsAction for slack app tokens ([#3440](https://github.com/great-expectations/great_expectations/pull/3440)) (Thanks @psheets)
* [FEATURE] Implement Integration Test for "Simple SQL Datasource" with Partitioning, Splitting, and Sampling ([#3454](https://github.com/great-expectations/great_expectations/pull/3454))
* [FEATURE] Implement Integration Test for File Path Data Connectors with Partitioning, Splitting, and Sampling ([#3452](https://github.com/great-expectations/great_expectations/pull/3452))
* [BUGFIX] Fix Incorrect Implementation of the "_sample_using_random" Sampling Method in SQLAlchemyExecutionEngine ([#3449](https://github.com/great-expectations/great_expectations/pull/3449))
* [BUGFIX] Handle RuntimeBatchRequest passed to Checkpoint programatically (without yml) ([#3448](https://github.com/great-expectations/great_expectations/pull/3448))
* [DOCS] Fix typo in command to create new checkpoint ([#3434](https://github.com/great-expectations/great_expectations/pull/3434)) (Thanks @joeltone)
* [DOCS] How to validate data by running a Checkpoint ([#3436](https://github.com/great-expectations/great_expectations/pull/3436))
* [ENHANCEMENT] cloud-199 - Update Expectation and ExpectationSuite classes for GE Cloud ([#3453](https://github.com/great-expectations/great_expectations/pull/3453))
* [MAINTENANCE] Does not test numpy.float128 when it doesn't exist ([#3460](https://github.com/great-expectations/great_expectations/pull/3460))
* [MAINTENANCE] Remove Unnecessary SQL OR Condition ([#3469](https://github.com/great-expectations/great_expectations/pull/3469))
* [MAINTENANCE] Remove validation playground notebooks ([#3467](https://github.com/great-expectations/great_expectations/pull/3467))
* [MAINTENANCE] clean up type hints, API usage, imports, and coding style ([#3444](https://github.com/great-expectations/great_expectations/pull/3444))
* [MAINTENANCE] comments ([#3457](https://github.com/great-expectations/great_expectations/pull/3457))

0.13.35
-----------------
* [FEATURE] Create ExpectationValidationGraph class to Maintain Relationship Between Expectation and Metrics and Use it to Associate Exceptions to Expectations ([#3433](https://github.com/great-expectations/great_expectations/pull/3433))
* [BUGFIX] Addresses issue [#2993](https://github.com/great-expectations/great_expectations/pull/2993) ([#3054](https://github.com/great-expectations/great_expectations/pull/3054)) by using configuration when it is available instead of discovering keys (listing keys) in existing sources. ([#3377](https://github.com/great-expectations/great_expectations/pull/3377))
* [BUGFIX] Fix Data asset name rendering ([#3431](https://github.com/great-expectations/great_expectations/pull/3431)) (Thanks @shpolina)
* [DOCS] minor fix to syntax highlighting in how_to_contribute_a_new_expectation… ([#3413](https://github.com/great-expectations/great_expectations/pull/3413)) (Thanks @edjoesu)
* [DOCS] Fix broken links in how_to_create_a_new_expectation_suite_using_rule_based_profile… ([#3410](https://github.com/great-expectations/great_expectations/pull/3410)) (Thanks @edjoesu)
* [ENHANCEMENT] update list_expectation_suite_names and ExpectationSuiteValidationResult payload ([#3419](https://github.com/great-expectations/great_expectations/pull/3419))
* [MAINTENANCE] Clean up Type Hints, JSON-Serialization, ID Generation and Logging in Objects in batch.py Module and its Usage ([#3422](https://github.com/great-expectations/great_expectations/pull/3422))
* [MAINTENANCE] Fix Granularity of Exception Handling in ExecutionEngine.resolve_metrics() and Clean Up Type Hints ([#3423](https://github.com/great-expectations/great_expectations/pull/3423))
* [MAINTENANCE] Fix broken links in how_to_create_a_new_expectation_suite_using_rule_based_profiler ([#3441](https://github.com/great-expectations/great_expectations/pull/3441))
* [MAINTENANCE] Fix issue where BatchRequest object in configuration could cause Checkpoint to fail ([#3438](https://github.com/great-expectations/great_expectations/pull/3438))
* [MAINTENANCE] Insure consistency between implementation of overriding Python __hash__() and internal ID property value ([#3432](https://github.com/great-expectations/great_expectations/pull/3432))
* [MAINTENANCE] Performance improvement refactor for Spark unexpected values ([#3368](https://github.com/great-expectations/great_expectations/pull/3368))
* [MAINTENANCE] Refactor MetricConfiguration out of validation_graph.py to Avoid Future Circular Dependencies in Python ([#3425](https://github.com/great-expectations/great_expectations/pull/3425))
* [MAINTENANCE] Use ExceptionInfo to encapsulate common expectation validation result error information. ([#3427](https://github.com/great-expectations/great_expectations/pull/3427))

0.13.34
-----------------
* [FEATURE] Configurable multi-threaded checkpoint speedup ([#3362](https://github.com/great-expectations/great_expectations/pull/3362)) (Thanks @jdimatteo)
* [BUGFIX] Insure that the "result_format" Expectation Argument is Processed Properly ([#3364](https://github.com/great-expectations/great_expectations/pull/3364))
* [BUGFIX] fix error getting validation result from DataContext ([#3359](https://github.com/great-expectations/great_expectations/pull/3359)) (Thanks @zachzIAM)
* [BUGFIX] fixed typo and added CLA links ([#3347](https://github.com/great-expectations/great_expectations/pull/3347))
* [DOCS] Azure Data Connector Documentation for Pandas and Spark. ([#3378](https://github.com/great-expectations/great_expectations/pull/3378))
* [DOCS] Connecting to GCS using Spark ([#3375](https://github.com/great-expectations/great_expectations/pull/3375))
* [DOCS] Docusaurus - Deploying Great Expectations in a hosted environment without file system or CLI ([#3361](https://github.com/great-expectations/great_expectations/pull/3361))
* [DOCS] How to get a batch from configured datasource ([#3382](https://github.com/great-expectations/great_expectations/pull/3382))
* [MAINTENANCE] Add Flyte to README ([#3387](https://github.com/great-expectations/great_expectations/pull/3387)) (Thanks @samhita-alla)
* [MAINTENANCE] Adds expect_table_columns_to_match_set ([#3329](https://github.com/great-expectations/great_expectations/pull/3329)) (Thanks @viniciusdsmello)
* [MAINTENANCE] Bugfix/skip substitute config variables in ge cloud mode ([#3393](https://github.com/great-expectations/great_expectations/pull/3393))
* [MAINTENANCE] Clean Up ValidationGraph API Usage, Improve Exception Handling for Metrics, Clean Up Type Hints ([#3399](https://github.com/great-expectations/great_expectations/pull/3399))
* [MAINTENANCE] Clean up ValidationGraph API and add Type Hints ([#3392](https://github.com/great-expectations/great_expectations/pull/3392))
* [MAINTENANCE] Enhancement/update _set methods with kwargs ([#3391](https://github.com/great-expectations/great_expectations/pull/3391)) (Thanks @roblim)
* [MAINTENANCE] Fix incorrect ToC section name ([#3395](https://github.com/great-expectations/great_expectations/pull/3395))
* [MAINTENANCE] Insure Correct Processing of the catch_exception Flag in Metrics Resolution ([#3360](https://github.com/great-expectations/great_expectations/pull/3360))
* [MAINTENANCE] exempt batch_data from a deep_copy operation on RuntimeBatchRequest ([#3388](https://github.com/great-expectations/great_expectations/pull/3388))
* [MAINTENANCE] [WIP] Enhancement/cloud 169/update checkpoint.run for ge cloud ([#3381](https://github.com/great-expectations/great_expectations/pull/3381))

0.13.33
-----------------
* [FEATURE] Implement InferredAssetAzureDataConnector with Support for Pandas and Spark Execution Engines ([#3372](https://github.com/great-expectations/great_expectations/pull/3372))
* [FEATURE] Spark connecting to Google Cloud Storage ([#3365](https://github.com/great-expectations/great_expectations/pull/3365))
* [FEATURE] SparkDFExecutionEngine can load data accessed by ConfiguredAssetAzureDataConnector (integration tests are included). ([#3345](https://github.com/great-expectations/great_expectations/pull/3345))
* [FEATURE] [MER-293] GE Cloud Mode for DataContext ([#3262](https://github.com/great-expectations/great_expectations/pull/3262)) (Thanks @roblim)
* [BUGFIX] Allow for RuntimeDataConnector to accept custom query while suppressing temp table creation ([#3335](https://github.com/great-expectations/great_expectations/pull/3335)) (Thanks @NathanFarmer)
* [BUGFIX] Fix issue where multiple validators reused the same execution engine, causing a conflict in active batch (GE-3168) ([#3222](https://github.com/great-expectations/great_expectations/pull/3222)) (Thanks @jcampbell)
* [BUGFIX] Run batch_request dictionary through util function convert_to_json_serializable ([#3349](https://github.com/great-expectations/great_expectations/pull/3349)) (Thanks @NathanFarmer)
* [BUGFIX] added casting of numeric value to fix redshift issue [#3293](https://github.com/great-expectations/great_expectations/pull/3293) ([#3338](https://github.com/great-expectations/great_expectations/pull/3338)) (Thanks @sariabod)
* [DOCS] Docusaurus - How to connect to an MSSQL database ([#3353](https://github.com/great-expectations/great_expectations/pull/3353)) (Thanks @NathanFarmer)
* [DOCS] GREAT-195 Docs remove all stubs and links to them ([#3363](https://github.com/great-expectations/great_expectations/pull/3363))
* [MAINTENANCE] Update azure-pipelines-docs-integration.yml for Azure Pipelines
* [MAINTENANCE] Update implemented_expectations.md ([#3351](https://github.com/great-expectations/great_expectations/pull/3351)) (Thanks @spencerhardwick)
* [MAINTENANCE] Updating to reflect current Expectation dev state ([#3348](https://github.com/great-expectations/great_expectations/pull/3348)) (Thanks @spencerhardwick)
* [MAINTENANCE] docs: Clean up Docusaurus refs ([#3371](https://github.com/great-expectations/great_expectations/pull/3371))

0.13.32
-----------------
* [FEATURE] Add Performance Benchmarks Using BigQuery. (Thanks @jdimatteo)
* [WIP] [FEATURE] add backend args to run_diagnostics ([#3257](https://github.com/great-expectations/great_expectations/pull/3257)) (Thanks @edjoesu)
* [BUGFIX] Addresses Issue 2937. ([#3236](https://github.com/great-expectations/great_expectations/pull/3236)) (Thanks @BenGale93)
* [BUGFIX] SQL dialect doesn't register for BigQuery for V2 ([#3324](https://github.com/great-expectations/great_expectations/pull/3324))
* [DOCS] "How to connect to data on GCS using Pandas" ([#3311](https://github.com/great-expectations/great_expectations/pull/3311))
* [MAINTENANCE] Add CODEOWNERS with a single check for sidebars.js ([#3332](https://github.com/great-expectations/great_expectations/pull/3332))
* [MAINTENANCE] Fix incorrect DataConnector usage of _get_full_file_path() API method. ([#3336](https://github.com/great-expectations/great_expectations/pull/3336))
* [MAINTENANCE] Make Pandas against S3 and GCS integration tests more robust by asserting on number of batches returned and row counts ([#3341](https://github.com/great-expectations/great_expectations/pull/3341))
* [MAINTENANCE] Make integration tests of Pandas against Azure more robust. ([#3339](https://github.com/great-expectations/great_expectations/pull/3339))
* [MAINTENANCE] Prepare AzureUrl to handle WASBS format (for Spark) ([#3340](https://github.com/great-expectations/great_expectations/pull/3340))
* [MAINTENANCE] Renaming default_batch_identifier in examples [#3334](https://github.com/great-expectations/great_expectations/pull/3334)
* [MAINTENANCE] Tests for RuntimeDataConnector at DataContext-level ([#3304](https://github.com/great-expectations/great_expectations/pull/3304))
* [MAINTENANCE] Tests for RuntimeDataConnector at DataContext-level (Spark and Pandas) ([#3325](https://github.com/great-expectations/great_expectations/pull/3325))
* [MAINTENANCE] Tests for RuntimeDataConnector at Datasource-level (Spark and Pandas) ([#3318](https://github.com/great-expectations/great_expectations/pull/3318))
* [MAINTENANCE] Various doc patches ([#3326](https://github.com/great-expectations/great_expectations/pull/3326))
* [MAINTENANCE] clean up imports and method signatures ([#3337](https://github.com/great-expectations/great_expectations/pull/3337))

0.13.31
-----------------
* [FEATURE] Enable `GCS DataConnector` integration with `PandasExecutionEngine` ([#3264](https://github.com/great-expectations/great_expectations/pull/3264))
* [FEATURE] Enable column_pair expectations and tests for Spark ([#3294](https://github.com/great-expectations/great_expectations/pull/3294))
* [FEATURE] Implement `InferredAssetGCSDataConnector` ([#3284](https://github.com/great-expectations/great_expectations/pull/3284))
* [FEATURE]/CHANGE run time format ([#3272](https://github.com/great-expectations/great_expectations/pull/3272)) (Thanks @serialbandicoot)
* [DOCS] Fix misc errors in "How to create renderers for Custom Expectations" ([#3315](https://github.com/great-expectations/great_expectations/pull/3315))
* [DOCS] GDOC-217 remove stub links ([#3314](https://github.com/great-expectations/great_expectations/pull/3314))
* [DOCS] Remove misc TODOs to tidy up docs ([#3313](https://github.com/great-expectations/great_expectations/pull/3313))
* [DOCS] Standardize capitalization of various technologies in `docs` ([#3312](https://github.com/great-expectations/great_expectations/pull/3312))
* [DOCS] Fix broken link to Contributor docs ([#3295](https://github.com/great-expectations/great_expectations/pull/3295)) (Thanks @discdiver)
* [MAINTENANCE] Additional tests for RuntimeDataConnector at Datasource-level (query) ([#3288](https://github.com/great-expectations/great_expectations/pull/3288))
* [MAINTENANCE] Update GCSStoreBackend + tests ([#2630](https://github.com/great-expectations/great_expectations/pull/2630)) (Thanks @hmandsager)
* [MAINTENANCE] Write integration/E2E tests for `ConfiguredAssetAzureDataConnector` ([#3204](https://github.com/great-expectations/great_expectations/pull/3204))
* [MAINTENANCE] Write integration/E2E tests for both `GCSDataConnectors` ([#3301](https://github.com/great-expectations/great_expectations/pull/3301))

0.13.30
-----------------
* [FEATURE] Implement Spark Decorators and Helpers; Demonstrate on MulticolumnSumEqual Metric ([#3289](https://github.com/great-expectations/great_expectations/pull/3289))
* [FEATURE] V3 implement expect_column_pair_values_to_be_in_set for SQL Alchemy execution engine ([#3281](https://github.com/great-expectations/great_expectations/pull/3281))
* [FEATURE] Implement `ConfiguredAssetGCSDataConnector` ([#3247](https://github.com/great-expectations/great_expectations/pull/3247))
* [BUGFIX] Fix import issues around cloud providers (GCS/Azure/S3) ([#3292](https://github.com/great-expectations/great_expectations/pull/3292))
* [MAINTENANCE] Add force_reuse_spark_context to DatasourceConfigSchema ([#3126](https://github.com/great-expectations/great_expectations/pull/3126)) (thanks @gipaetusb and @mbakunze)

0.13.29
-----------------
* [FEATURE] Implementation of the Metric "select_column_values.unique.within_record" for SQLAlchemyExecutionEngine ([#3279](https://github.com/great-expectations/great_expectations/pull/3279))
* [FEATURE] V3 implement ColumnPairValuesInSet for SQL Alchemy execution engine ([#3278](https://github.com/great-expectations/great_expectations/pull/3278))
* [FEATURE] Edtf with support levels ([#2594](https://github.com/great-expectations/great_expectations/pull/2594)) (thanks @mielvds)
* [FEATURE] V3 implement expect_column_pair_values_to_be_equal for SqlAlchemyExecutionEngine ([#3267](https://github.com/great-expectations/great_expectations/pull/3267))
* [FEATURE] add expectation for discrete column entropy  ([#3049](https://github.com/great-expectations/great_expectations/pull/3049)) (thanks @edjoesu)
* [FEATURE] Add SQLAlchemy Provider for the the column_pair_values.a_greater_than_b ([#3268](https://github.com/great-expectations/great_expectations/pull/3268))
* [FEATURE] Expectations tests for BigQuery backend ([#3219](https://github.com/great-expectations/great_expectations/pull/3219)) (Thanks @jdimatteo)
* [FEATURE] Add schema validation for different GCS auth methods ([#3258](https://github.com/great-expectations/great_expectations/pull/3258))
* [FEATURE] V3 - Implement column_pair helpers/providers for SqlAlchemyExecutionEngine ([#3256](https://github.com/great-expectations/great_expectations/pull/3256))
* [FEATURE] V3 implement expect_column_pair_values_to_be_equal expectation for PandasExecutionEngine ([#3252](https://github.com/great-expectations/great_expectations/pull/3252))
* [FEATURE] GCS DataConnector schema validation ([#3253](https://github.com/great-expectations/great_expectations/pull/3253))
* [FEATURE] Implementation of the "expect_select_column_values_to_be_unique_within_record" Expectation ([#3251](https://github.com/great-expectations/great_expectations/pull/3251))
* [FEATURE] Implement the SelectColumnValuesUniqueWithinRecord metric (for PandasExecutionEngine) ([#3250](https://github.com/great-expectations/great_expectations/pull/3250))
* [FEATURE] V3 - Implement ColumnPairValuesEqual for PandasExecutionEngine ([#3243](https://github.com/great-expectations/great_expectations/pull/3243))
* [FEATURE] Set foundation for GCS DataConnectors ([#3220](https://github.com/great-expectations/great_expectations/pull/3220))
* [FEATURE] Implement "expect_column_pair_values_to_be_in_set" expectation (support for PandasExecutionEngine) ([#3242](https://github.com/great-expectations/great_expectations/pull/3242))
* [BUGFIX] Fix deprecation warning for importing from collections ([#3228](https://github.com/great-expectations/great_expectations/pull/3228)) (thanks @ismaildawoodjee)
* [DOCS] Document BigQuery test dataset configuration ([#3273](https://github.com/great-expectations/great_expectations/pull/3273)) (Thanks @jdimatteo)
* [DOCS] Syntax and Link ([#3266](https://github.com/great-expectations/great_expectations/pull/3266))
* [DOCS] API Links and Supporting Docs ([#3265](https://github.com/great-expectations/great_expectations/pull/3265))
* [DOCS] redir and search ([#3249](https://github.com/great-expectations/great_expectations/pull/3249))
* [MAINTENANCE] Update azure-pipelines-docs-integration.yml to include env vars for Azure docs integration tests
* [MAINTENANCE] Allow Wrong ignore_row_if Directive from V2 with Deprecation Warning ([#3274](https://github.com/great-expectations/great_expectations/pull/3274))
* [MAINTENANCE] Refactor test structure for "Connecting to your data" cloud provider integration tests ([#3277](https://github.com/great-expectations/great_expectations/pull/3277))
* [MAINTENANCE] Make test method names consistent for Metrics tests ([#3254](https://github.com/great-expectations/great_expectations/pull/3254))
* [MAINTENANCE] Allow `PandasExecutionEngine` to accept `Azure DataConnectors` ([#3214](https://github.com/great-expectations/great_expectations/pull/3214))
* [MAINTENANCE] Standardize Arguments to MetricConfiguration Constructor; Use {} instead of dict(). ([#3246](https://github.com/great-expectations/great_expectations/pull/3246))

0.13.28
-----------------
* [FEATURE] Implement ColumnPairValuesInSet metric for PandasExecutionEngine
* [BUGFIX] Wrap optional azure imports in data_connector setup

0.13.27
-----------------
* [FEATURE] Accept row_condition (with condition_parser) and ignore_row_if parameters for expect_multicolumn_sum_to_equal ([#3193](https://github.com/great-expectations/great_expectations/pull/3193))
* [FEATURE] ConfiguredAssetDataConnector for Azure Blob Storage ([#3141](https://github.com/great-expectations/great_expectations/pull/3141))
* [FEATURE] Replace MetricFunctionTypes.IDENTITY domain type with convenience method get_domain_records() for SparkDFExecutionEngine ([#3226](https://github.com/great-expectations/great_expectations/pull/3226))
* [FEATURE] Replace MetricFunctionTypes.IDENTITY domain type with convenience method get_domain_records() for SqlAlchemyExecutionEngine ([#3215](https://github.com/great-expectations/great_expectations/pull/3215))
* [FEATURE] Replace MetricFunctionTypes.IDENTITY domain type with convenience method get_full_access_compute_domain() for PandasExecutionEngine ([#3210](https://github.com/great-expectations/great_expectations/pull/3210))
* [FEATURE] Set foundation for Azure-related DataConnectors ([#3188](https://github.com/great-expectations/great_expectations/pull/3188))
* [FEATURE] Update ExpectCompoundColumnsToBeUnique for V3 API ([#3161](https://github.com/great-expectations/great_expectations/pull/3161))
* [BUGFIX] Fix incorrect schema validation for Azure data connectors ([#3200](https://github.com/great-expectations/great_expectations/pull/3200))
* [BUGFIX] Fix incorrect usage of "all()" in the comparison of validation results when executing an Expectation ([#3178](https://github.com/great-expectations/great_expectations/pull/3178))
* [BUGFIX] Fixes an error with expect_column_values_to_be_dateutil_parseable ([#3190](https://github.com/great-expectations/great_expectations/pull/3190))
* [BUGFIX] Improve parsing of .ge_store_backend_id ([#2952](https://github.com/great-expectations/great_expectations/pull/2952))
* [BUGFIX] Remove fixture parameterization for Cloud DBs (Snowflake and BigQuery) ([#3182](https://github.com/great-expectations/great_expectations/pull/3182))
* [BUGFIX] Restore support for V2 API style custom expectation rendering ([#3179](https://github.com/great-expectations/great_expectations/pull/3179)) (Thanks @jdimatteo)
* [DOCS] Add `conda` as installation option in README ([#3196](https://github.com/great-expectations/great_expectations/pull/3196)) (Thanks @rpanai)
* [DOCS] Standardize capitalization of "Python" in "Connecting to your data" section of new docs ([#3209](https://github.com/great-expectations/great_expectations/pull/3209))
* [DOCS] Standardize capitalization of Spark in docs ([#3198](https://github.com/great-expectations/great_expectations/pull/3198))
* [DOCS] Update BigQuery docs to clarify the use of temp tables ([#3184](https://github.com/great-expectations/great_expectations/pull/3184))
* [DOCS] Create _redirects ([#3192](https://github.com/great-expectations/great_expectations/pull/3192))
* [ENHANCEMENT] RuntimeDataConnector messaging is made more clear for `test_yaml_config()` ([#3206](https://github.com/great-expectations/great_expectations/pull/3206))
* [MAINTENANCE] Add `credentials` YAML key support for `DataConnectors` ([#3173](https://github.com/great-expectations/great_expectations/pull/3173))
* [MAINTENANCE] Fix minor typo in S3 DataConnectors ([#3194](https://github.com/great-expectations/great_expectations/pull/3194))
* [MAINTENANCE] Fix typos in argument names and types ([#3207](https://github.com/great-expectations/great_expectations/pull/3207))
* [MAINTENANCE] Update changelog. ([#3189](https://github.com/great-expectations/great_expectations/pull/3189))
* [MAINTENANCE] Update documentation. ([#3203](https://github.com/great-expectations/great_expectations/pull/3203))
* [MAINTENANCE] Update validate_your_data.md ([#3185](https://github.com/great-expectations/great_expectations/pull/3185))
* [MAINTENANCE] update tests across execution engines and clean up coding patterns ([#3223](https://github.com/great-expectations/great_expectations/pull/3223))

0.13.26
-----------------
* [FEATURE] Enable BigQuery tests for Azure CI/CD ([#3155](https://github.com/great-expectations/great_expectations/pull/3155))
* [FEATURE] Implement MulticolumnMapExpectation class ([#3134](https://github.com/great-expectations/great_expectations/pull/3134))
* [FEATURE] Implement the MulticolumnSumEqual Metric for PandasExecutionEngine ([#3130](https://github.com/great-expectations/great_expectations/pull/3130))
* [FEATURE] Support row_condition and ignore_row_if Directives Combined for PandasExecutionEngine ([#3150](https://github.com/great-expectations/great_expectations/pull/3150))
* [FEATURE] Update ExpectMulticolumnSumToEqual for V3 API ([#3136](https://github.com/great-expectations/great_expectations/pull/3136))
* [FEATURE] add python3.9 to python versions ([#3143](https://github.com/great-expectations/great_expectations/pull/3143)) (Thanks @dswalter)
* [FEATURE]/MER-16/MER-75/ADD_ROUTE_FOR_VALIDATION_RESULT ([#3090](https://github.com/great-expectations/great_expectations/pull/3090)) (Thanks @rreinoldsc)
* [BUGFIX] Enable `--v3-api suite edit` to proceed without selecting DataConnectors ([#3165](https://github.com/great-expectations/great_expectations/pull/3165))
* [BUGFIX] Fix error when `RuntimeBatchRequest` is passed to `SimpleCheckpoint` with `RuntimeDataConnector` ([#3152](https://github.com/great-expectations/great_expectations/pull/3152))
* [BUGFIX] allow reader_options in the CLI so can read `.csv.gz` files ([#2695](https://github.com/great-expectations/great_expectations/pull/2695)) (Thanks @luke321321)
* [DOCS] Apply Docusaurus tabs to relevant pages in new docs
* [DOCS] Capitalize python to Python in docs ([#3176](https://github.com/great-expectations/great_expectations/pull/3176))
* [DOCS] Improve Core Concepts - Expectation Concepts ([#2831](https://github.com/great-expectations/great_expectations/pull/2831))
* [MAINTENANCE] Error messages must be friendly. ([#3171](https://github.com/great-expectations/great_expectations/pull/3171))
* [MAINTENANCE] Implement the "compound_columns_unique" metric for PandasExecutionEngine (with a unit test). ([#3159](https://github.com/great-expectations/great_expectations/pull/3159))
* [MAINTENANCE] Improve Coding Practices in "great_expectations/expectations/expectation.py" ([#3151](https://github.com/great-expectations/great_expectations/pull/3151))
* [MAINTENANCE] Update test_script_runner.py ([#3177](https://github.com/great-expectations/great_expectations/pull/3177))

0.13.25
-----------------
* [FEATURE] Pass on meta-data from expectation json to validation result json ([#2881](https://github.com/great-expectations/great_expectations/pull/2881)) (Thanks @sushrut9898)
* [FEATURE] Add sqlalchemy engine support for `column.most_common_value` metric ([#3020](https://github.com/great-expectations/great_expectations/pull/3020)) (Thanks @shpolina)
* [BUGFIX] Added newline to CLI message for consistent formatting ([#3127](https://github.com/great-expectations/great_expectations/pull/3127)) (Thanks @ismaildawoodjee)
* [BUGFIX] fix pip install snowflake build error with python 3.9 ([#3119](https://github.com/great-expectations/great_expectations/pull/3119)) (Thanks @jdimatteo)
* [BUGFIX] Populate (data) asset name in data docs for RuntimeDataConnector ([#3105](https://github.com/great-expectations/great_expectations/pull/3105)) (Thanks @ceshine)
* [DOCS] Correct path to docs_rtd/changelog.rst ([#3120](https://github.com/great-expectations/great_expectations/pull/3120)) (Thanks @jdimatteo)
* [DOCS] Fix broken links in "How to write a 'How to Guide'" ([#3112](https://github.com/great-expectations/great_expectations/pull/3112))
* [DOCS] Port over "How to add comments to Expectations and display them in DataDocs" from RTD to Docusaurus ([#3078](https://github.com/great-expectations/great_expectations/pull/3078))
* [DOCS] Port over "How to create a Batch of data from an in memory Spark or Pandas DF" from RTD to Docusaurus ([#3099](https://github.com/great-expectations/great_expectations/pull/3099))
* [DOCS] Update CLI codeblocks in create_your_first_expectations.md ([#3106](https://github.com/great-expectations/great_expectations/pull/3106)) (Thanks @ories)
* [MAINTENANCE] correct typo in docstring ([#3117](https://github.com/great-expectations/great_expectations/pull/3117))
* [MAINTENANCE] DOCS/GDOC-130/Add Changelog ([#3121](https://github.com/great-expectations/great_expectations/pull/3121))
* [MAINTENANCE] fix docstring for expectation "expect_multicolumn_sum_to_equal" (previous version was not precise) ([#3110](https://github.com/great-expectations/great_expectations/pull/3110))
* [MAINTENANCE] Fix typos in docstrings in map_metric_provider partials ([#3111](https://github.com/great-expectations/great_expectations/pull/3111))
* [MAINTENANCE] Make sure that all imports use column_aggregate_metric_provider (not column_aggregate_metric). ([#3128](https://github.com/great-expectations/great_expectations/pull/3128))
* [MAINTENANCE] Rename column_aggregate_metric.py into column_aggregate_metric_provider.py for better code readability. ([#3123](https://github.com/great-expectations/great_expectations/pull/3123))
* [MAINTENANCE] rename ColumnMetricProvider to ColumnAggregateMetricProvider (with DeprecationWarning) ([#3100](https://github.com/great-expectations/great_expectations/pull/3100))
* [MAINTENANCE] rename map_metric.py to map_metric_provider.py (with DeprecationWarning) for a better code readability/interpretability ([#3103](https://github.com/great-expectations/great_expectations/pull/3103))
* [MAINTENANCE] rename table_metric.py to table_metric_provider.py with a deprecation notice ([#3118](https://github.com/great-expectations/great_expectations/pull/3118))
* [MAINTENANCE] Update CODE_OF_CONDUCT.md ([#3066](https://github.com/great-expectations/great_expectations/pull/3066))
* [MAINTENANCE] Upgrade to modern Python syntax ([#3068](https://github.com/great-expectations/great_expectations/pull/3068)) (Thanks @cclauss)

0.13.24
-----------------
* [FEATURE] Script to automate proper triggering of Docs Azure pipeline ([#3003](https://github.com/great-expectations/great_expectations/pull/3003))
* [BUGFIX] Fix an undefined name that could lead to a NameError ([#3063](https://github.com/great-expectations/great_expectations/pull/3063)) (Thanks @cclauss)
* [BUGFIX] fix incorrect pandas top rows usage ([#3091](https://github.com/great-expectations/great_expectations/pull/3091))
* [BUGFIX] Fix parens in Expectation metric validation method that always returned True assertation ([#3086](https://github.com/great-expectations/great_expectations/pull/3086)) (Thanks @morland96)
* [BUGFIX] Fix run_diagnostics for contrib expectations ([#3096](https://github.com/great-expectations/great_expectations/pull/3096))
* [BUGFIX] Fix typos discovered by codespell ([#3064](https://github.com/great-expectations/great_expectations/pull/3064)) (Thanks cclauss)
* [BUGFIX] Wrap get_view_names in try clause for passing the NotImplemented error ([#2976](https://github.com/great-expectations/great_expectations/pull/2976)) (Thanks @kj-9)
* [DOCS] Ensuring consistent style of directories, files, and related references in docs ([#3053](https://github.com/great-expectations/great_expectations/pull/3053))
* [DOCS] Fix broken link to example DAG ([#3061](https://github.com/great-expectations/great_expectations/pull/3061)) (Thanks fritz-astronomer)
* [DOCS] GDOC-198 cleanup TOC ([#3088](https://github.com/great-expectations/great_expectations/pull/3088))
* [DOCS] Migrating pages under guides/miscellaneous ([#3094](https://github.com/great-expectations/great_expectations/pull/3094)) (Thanks @spbail)
* [DOCS] Port over “How to configure a new Checkpoint using test_yaml_config” from RTD to Docusaurus
* [DOCS] Port over “How to configure an Expectation store in GCS” from RTD to Docusaurus ([#3071](https://github.com/great-expectations/great_expectations/pull/3071))
* [DOCS] Port over “How to create renderers for custom Expectations” from RTD to Docusaurus
* [DOCS] Port over “How to run a Checkpoint in Airflow” from RTD to Docusaurus ([#3074](https://github.com/great-expectations/great_expectations/pull/3074))
* [DOCS] Update how-to-create-and-edit-expectations-in-bulk.md ([#3073](https://github.com/great-expectations/great_expectations/pull/3073))
* [MAINTENANCE] Adding a comment explaining the IDENTITY metric domain type. ([#3057](https://github.com/great-expectations/great_expectations/pull/3057))
* [MAINTENANCE] Change domain key value from “column” to “column_list” in ExecutionEngine implementations ([#3059](https://github.com/great-expectations/great_expectations/pull/3059))
* [MAINTENANCE] clean up metric errors ([#3085](https://github.com/great-expectations/great_expectations/pull/3085))
* [MAINTENANCE] Correct the typo in the naming of the IDENTIFICATION semantic domain type name. ([#3058](https://github.com/great-expectations/great_expectations/pull/3058))
* [MAINTENANCE] disable snowflake tests temporarily ([#3093](https://github.com/great-expectations/great_expectations/pull/3093))
* [MAINTENANCE] [DOCS] Port over “How to host and share Data Docs on GCS” from RTD to Docusaurus ([#3070](https://github.com/great-expectations/great_expectations/pull/3070))
* [MAINTENANCE] Enable repr for MetricConfiguration to assist with troubleshooting. ([#3075](https://github.com/great-expectations/great_expectations/pull/3075))
* [MAINTENANCE] Expand test of a column map metric to underscore functionality. ([#3072](https://github.com/great-expectations/great_expectations/pull/3072))
* [MAINTENANCE] Expectation anonymizer supports v3 expectation registry ([#3092](https://github.com/great-expectations/great_expectations/pull/3092))
* [MAINTENANCE] Fix -- check for column key existence in accessor_domain_kwargsn for condition map partials. ([#3082](https://github.com/great-expectations/great_expectations/pull/3082))
* [MAINTENANCE] Missing import of SparkDFExecutionEngine was added. ([#3062](https://github.com/great-expectations/great_expectations/pull/3062))

0.13.23
-----------------
* [BUGFIX] added expectation_config to ExpectationValidationResult when exception is raised (#2659) (thanks @peterdhansen)
* [BUGFIX] fix update data docs as validation action (#3031)
* [DOCS] Port over "How to configure an Expectation Store in Azure" from RTD to Docusaurus
* [DOCS] Port over "How to host and share DataDocs on a filesystem" from RTD to Docusaurus (#3018)
* [DOCS] Port over "How to instantiate a Data Context w/o YML" from RTD to Docusaurus (#3011)
* [DOCS] Port "How to configure a Validation Result store on a filesystem" from RTD to Docusaurus (#3025)
* [DOCS] how to create multibatch expectations using evaluation parameters (#3039)
* [DOCS] Port "How to create and edit Expectations with a Profiler" from RTD to Docussaurus. (#3048)
* [DOCS] Port RTD adding validations data or suites to checkpoint (#3030)
* [DOCS] Porting "How to create and edit Expectations with instant feedback from a sample Batch of data" from RTD to Docusaurus. (#3046)
* [DOCS] GDOC-172/Add missing pages (#3007)
* [DOCS] Port over "How to configure DataContext components using test_yaml_config" from RTD to Docusaurus
* [DOCS] Port over "How to configure a Validation Result store to Postgres" from RTD to Docusaurus
* [DOCS] Port over "How to configure an Expectation Store in S3" from RTD to Docusaurus
* [DOCS] Port over "How to configure an Expectation Store on a filesystem" from RTD to Docusaurus
* [DOCS] Port over "How to configure credentials using YAML or env vars" from RTD to Docusaurus
* [DOCS] Port over "How to configure credentials using a secrets store" from RTD to Docusaurus
* [DOCS] Port over "How to configure validation result store in GCS" from RTD to Docusaurus (#3019)
* [DOCS] Port over "How to connect to an Athena DB" from RTD to Docusaurus
* [DOCS] Port over "How to create a new ExpectationSuite from jsonschema" from RTD to Docusaurus (#3017)
* [DOCS] Port over "How to deploy a scheduled checkpoint with cron" from RTD to Docusaurus
* [DOCS] Port over "How to dynamically load evaluation parameters from DB" from RTD to Docusaurus (#3052)
* [DOCS] Port over "How to host and share DataDocs on Amazon S3" from RTD to Docusaurus
* [DOCS] Port over "How to implement custom notifications" from RTD to Docusaurus  (#3050)
* [DOCS] Port over "How to instantiate a DataContext on Databricks Spark cluster" from RTD to Docusaurus
* [DOCS] Port over "How to instantiate a DataContext on an EMR Spark Cluster" from RTD to Docusaurus (#3024)
* [DOCS] Port over "How to trigger Opsgenie notifications as a validation action" from RTD to Docusaurus
* [DOCS] Update titles of metadata store docs (#3016)
* [DOCS] Port over "How to configure Expectation store to PostgreSQL" from RTD to Docusaurus (#3010)
* [DOCS] Port over "How to configure a MetricsStore" from RTD to Docusaurus (#3009)
* [DOCS] Port over "How to configure validation result store in Azure" from RTD to Docusaurus (#3014)
* [DOCS] Port over "How to host and share DataDocs on Azure" from RTD to Docusaurus  (#3012)
* [DOCS]Port "How to create and edit Expectations based on domain knowledge, without inspecting data directly" from RTD to Datasaurus. (#3047)
* [DOCS] Ported "How to configure a Validation Result store in Amazon S3" from RTD to Docusaurus. (#3026)
* [DOCS] how to validate without checkpoint (#3013)
* [DOCS] validation action data docs update (convert from RTD to DocuSaurus) (#3015)
* [DOCS] port of 'How to store Validation Results as a Validation Action' from RTD into Docusaurus. (#3023)
* [MAINTENANCE] Cleanup (#3038)
* [MAINTENANCE] Edits (Formatting) (#3022)


0.13.22
-----------------
* [FEATURE] Port over guide for Slack notifications for validation actions (#3005)
* [FEATURE] bootstrap estimator  for NumericMetricRangeMultiBatchParameterBuilder (#3001)
* [BUGFIX] Update naming of confidence_level in integration test fixture (#3002)
* [BUGFIX] [batch.py] fix check for null value (#2994) (thanks @Mohamed Abido)
* [BUGFIX] Fix issue where compression key was added to reader_method for read_parquet (#2506)
* [BUGFIX] Improve support for dates for expect_column_distinct_values_to_contain_set (#2997) (thanks @xaniasd)
* [BUGFIX] Fix bug in getting non-existent parameter (#2986)
* [BUGFIX] Modify read_excel() to handle new optional-dependency openpyxl for pandas >= 1.3.0 (#2989)
* [DOCS] Getting Started - Clean Up and Integration Tests (#2985)
* [DOCS] Adding in url links and style (#2999)
* [DOCS] Adding a missing import to a documentation page (#2983) (thanks @rishabh-bhargava)
* [DOCS]/GDOC-108/GDOC-143/Add in Contributing fields and updates (#2972)
* [DOCS] Update rule-based profiler docs (#2987)
* [DOCS] add image zoom plugin (#2979)
* [MAINTENANCE] fix lint issues for docusaurus (#3004)
* [Maintenance] update header to match GE.io (#2811)
* [MAINTENANCE] Instrument test_yaml_config() (#2981)
* [MAINTENANCE] Remove "mostly" from "bobster" test config (#2996)
* [MAINTENANCE] Update v-0.12 CLI test to reflect Pandas upgrade to version 1.3.0 (#2995)
* [MAINTENANCE] rephrase expectation suite meta profile comment (#2991)
* [MAINTENANCE] make citation cleaner in expectation suite (#2990)
* [MAINTENANCE] Attempt to fix Numpy and Scipy Version Requirements without additional requirements* files (#2982)

0.13.21
-----------------
* [DOCS] correct errors and reference complete example for custom expectations (thanks @jdimatteo)
* [DOCS] How to connect to : in-memory Pandas Dataframe
* [DOCS] How to connect to in memory dataframe with spark
* [DOCS] How to connect to : S3 data using Pandas
* [DOCS] How to connect to : Sqlite database
* [DOCS] no longer show util import to users
* [DOCS] How to connect to data on a filesystem using Spark guide
* [DOCS] GDOC-102/GDOC-127 Port in References and Tutorials
* [DOCS] How to connect to a MySQL database
* [DOCS] improved clarity in how to write guide templates and docs
* [DOCS] Add documentation for Rule Based Profilers
* [BUGFIX] Update mssql image version for Azure
* [MAINTENANCE] Update test-sqlalchemy-latest.yml
* [MAINTENANCE] Clean Up Design for Configuration and Flow of Rules, Domain Builders, and Parameter Builders
* [MAINTENANCE] Update Profiler docstring args
* [MAINTENANCE] Remove date format parameter builder
* [MAINTENANCE] Move metrics computations to top-level ParameterBuilder
* [MAINTENANCE] use tmp dot UUID for discardable expectation suite name
* [MAINTENANCE] Refactor ExpectationSuite to include profiler_config in citations
* [FEATURE] Add citations to Profiler.profile()
* [FEATURE] Bootstrapped Range Parameter Builder

0.13.20
-----------------
* [DOCS] Update pr template and remove enhancement feature type
* [DOCS] Remove broken links
* [DOCS] Fix typo in SlackNotificationAction docstring
* [BUGFIX] Update util.convert_to_json_serializable() to handle UUID type #2805 (thanks @YFGu0618)
* [BUGFIX] Allow decimals without leading zero in evaluation parameter URN
* [BUGFIX] Using cache in order not to fetch already known secrets #2882 (thanks @Cedric-Magnan)
* [BUGFIX] Fix creation of temp tables for unexpected condition
* [BUGFIX] Docs integration tests now only run when `--docs-tests` option is specified
* [BUGFIX] Fix instantiation of PandasExecutionEngine with custom parameters
* [BUGFIX] Fix rendering of observed value in datadocs when the value is 0 #2923 (thanks @shpolina)
* [BUGFIX] Fix serialization error in DataDocs rendering #2908 (thanks @shpolina)
* [ENHANCEMENT] Enable instantiation of a validator with a multiple batch BatchRequest
* [ENHANCEMENT] Adds a batch_request_list parameter to DataContext.get_validator to enable instantiation of a Validator with batches from multiple BatchRequests
* [ENHANCEMENT] Add a Validator.load_batch method to enable loading of additional Batches to an instantiated Validator
* [ENHANCEMENT] Experimental WIP Rule-Based Profiler for single batch workflows (#2788)
* [ENHANCEMENT] Datasources made via the CLI notebooks now include runtime and active data connector
* [ENHANCEMENT] InMemoryStoreBackendDefaults which is useful for testing
* [MAINTENANCE] Improve robustness of integration test_runner
* [MAINTENANCE] CLI tests now support click 8.0 and 7.x
* [MAINTENANCE] Soft launch of alpha docs site
* [MAINTENANCE] DOCS integration tests have moved to a new pipeline
* [MAINTENANCE] Pin json-schema version
* [MAINTENANCE] Allow tests to properly connect to local sqlite db on Windows (thanks @shpolina)
* [FEATURE] Add GeCloudStoreBackend with support for Checkpoints



0.13.19
-----------------
* [BUGFIX] Fix packaging error breaking V3 CLI suite commands (#2719)

0.13.18
-----------------
* [ENHANCEMENT] Improve support for quantiles calculation in Athena
* [ENHANCEMENT] V3 API CLI docs commands have better error messages and more consistent short flags
* [ENHANCEMENT] Update all Data Connectors to allow for `batch_spec_passthrough` in config
* [ENHANCEMENT] Update `DataConnector.build_batch_spec` to use `batch_spec_passthrough` in config
* [ENHANCEMENT] Update `ConfiguredAssetSqlDataConnector.build_batch_spec` and `ConfiguredAssetFilePathDataConnector.build_batch_spec` to properly process `Asset.batch_spec_passthrough`
* [ENHANCEMENT] Update `SqlAlchemyExecutionEngine.get_batch_data_and_markers` to handle `create_temp_table` in `RuntimeQueryBatchSpec`
* [ENHANCEMENT] Usage stats messages for the v3 API CLI are now sent before and after the command runs # 2661
* [ENHANCEMENT} Update the datasource new notebook for improved data asset inference
* [ENHANCEMENT] Update the `datasource new` notebook for improved data asset inference
* [ENHANCEMENT] Made stylistic improvements to the `checkpoint new` notebook
* [ENHANCEMENT] Add mode prompt to suite new and suite edit #2706
* [ENHANCEMENT] Update build_gallery.py script to better-handle user-submitted Expectations failing #2705
* [ENHANCEMENT] Docs + Tests for passing in reader_options to Spark #2670
* [ENHANCEMENT] Adding progressbar to validator loop #2620 (Thanks @peterdhansen!)
* [ENHANCEMENT] Great Expectations Compatibility with SqlAlchemy 1.4 #2641
* [ENHANCEMENT] Athena expect column quantile values to be between #2544 (Thanks @RicardoPedrotti!)
* [BUGFIX] Rename assets in SqlDataConnectors to be consistent with other DataConnectors #2665
* [BUGFIX] V3 API CLI docs build now opens all built sites rather than only the last one
* [BUGFIX] Handle limit for oracle with rownum #2691 (Thanks @NathanFarmer!)
* [BUGFIX] add create table logic for athena #2668 (Thanks @kj-9!)
* [BUGFIX] Add note for user-submitted Expectation that is not compatible with SqlAlchemy 1.4 (uszipcode) #2677
* [BUGFIX] Usage stats cli payload schema #2680
* [BUGFIX] Rename assets in SqlDataConnectors #2665
* [DOCS] Update how_to_create_a_new_checkpoint.rst with description of new CLI functionality
* [DOCS] Update Configuring Datasources documentation for V3 API CLI
* [DOCS] Update Configuring Data Docs documentation for V3 API CLI
* [DOCS] Update Configuring metadata stores documentation for V3 API CLI
* [DOCS] Update How to configure a Pandas/S3 Datasource for V3 API CLI
* [DOCS] Fix typos in "How to load a database table, view, or query result as a batch" guide and update with `create_temp_table` info
* [DOCS] Update "How to add a Validation Operator" guide to make it clear it is only for V2 API
* [DOCS] Update Version Migration Guide to recommend using V3 without caveats
* [DOCS] Formatting fixes for datasource docs #2686
* [DOCS] Add note about v3 API to How to use the Great Expectations command line interface (CLI) #2675
* [DOCS] CLI SUITE Documentation for V3 #2687
* [DOCS] how to share data docs on azure #2589 (Thanks @benoitLebreton-perso!)
* [DOCS] Fix typo in Core concepts/Key Ideas section #2660 (Thanks @svenhofstede!)
* [DOCS] typo in datasource documentation #2654 (Thanks @Gfeuillen!)
* [DOCS] fix grammar #2579 (Thanks @carlsonp!)
* [DOCS] Typo fix in Core Concepts/ Key Ideas section #2644 (Thanks @TremaMiguel!)
* [DOCS] Corrects wrong pypi package in Contrib Packages README #2653 (Thanks @mielvds!)
* [DOCS] Update dividing_data_assets_into_batches.rst #2651 (Thanks @lhayhurst!)
* [MAINTENANCE] Temporarily pin sqlalchemy (1.4.9) and add new CI stage #2708
* [MAINTENANCE] Run CLI tests as a separate stage in Azure pipelines #2672
* [MAINTENANCE] Updates to usage stats messages & tests for new CLI #2689
* [MAINTENANCE] Making user configurable profile test more robust; minor cleanup #2685
* [MAINTENANCE] remove cli.project.upgrade event #2682
* [MAINTENANCE] column reflection fallback should introspect one table (not all tables) #2657 (Thank you @peterdhansen!)
* [MAINTENANCE] Refactor Tests to Use Common Libraries #2663

0.13.17
-----------------
* [BREAKING-EXPERIMENTAL] The ``batch_data`` attribute of ``BatchRequest`` has been removed. To pass in in-memory dataframes at runtime, the new ``RuntimeDataConnector`` should be used
* [BREAKING-EXPERIMENTAL] ``RuntimeDataConnector`` must now be passed Batch Requests of type ``RuntimeBatchRequest``
* [BREAKING-EXPERIMENTAL] The ``PartitionDefinitionSubset`` class has been removed - the parent class ``IDDict`` is used in its place
* [BREAKING-EXPERIMENTAL] ``partition_request`` was renamed ``data_connector_query``. The related ``PartitionRequest`` class has been removed - the parent class ``IDDict`` is used in its place
* [BREAKING-EXPERIMENTAL] ``partition_definition`` was renamed ``batch_identifiers`. The related ``PartitionDefinition`` class has been removed - the parent class ``IDDict`` is used in its place
* [BREAKING-EXPERIMENTAL] The ``PartitionQuery`` class has been renamed to ``BatchFilter``
* [BREAKING-EXPERIMENTAL] The ``batch_identifiers`` key on ``DataConnectorQuery`` (formerly ``PartitionRequest``) has been changed to ``batch_filter_parameters``
* [ENHANCEMENT] Added a new ``RuntimeBatchRequest`` class, which can be used alongside ``RuntimeDataConnector`` to specify batches at runtime with either an in-memory dataframe, path (filesystem or s3), or sql query
* [ENHANCEMENT] Added a new ``RuntimeQueryBatchSpec`` class
* [ENHANCEMENT] CLI store list now lists active stores
* [BUGFIX] Fixed issue where Sorters were not being applied correctly when ``data_connector_query`` contained limit or index  #2617
* [DOCS] Updated docs to reflect above class name changes
* [DOCS] Added the following docs: "How to configure sorting in Data Connectors", "How to configure a Runtime Data Connector", "How to create a Batch Request using an Active Data Connector", "How to load a database table, view, or query result as a Batch"
* [DOCS] Updated the V3 API section of the following docs: "How to load a Pandas DataFrame as a Batch", "How to load a Spark DataFrame as a Batch",

0.13.16
-----------------
* [ENHANCEMENT] CLI `docs list` command implemented for v3 api #2612
* [MAINTENANCE] Add testing for overwrite_existing in sanitize_yaml_and_save_datasource #2613
* [ENHANCEMENT] CLI `docs build` command implemented for v3 api #2614
* [ENHANCEMENT] CLI `docs clean` command implemented for v3 api #2615
* [ENHANCEMENT] DataContext.clean_data_docs now raises helpful errors #2621
* [ENHANCEMENT] CLI `init` command implemented for v3 api #2626
* [ENHANCEMENT] CLI `store list` command implemented for v3 api #2627

0.13.15
-----------------
* [FEATURE] Added support for references to secrets stores for AWS Secrets Manager, GCP Secret Manager and Azure Key Vault in `great_expectations.yml` project config file (Thanks @Cedric-Magnan!)
* [ENHANCEMENT] Datasource CLI functionality for v3 api and global --assume-yes flag #2590
* [ENHANCEMENT] Update UserConfigurableProfiler to increase tolerance for mostly parameter of nullity expectations
* [ENHANCEMENT] Adding tqdm to Profiler (Thanks @peterdhansen). New library in requirements.txt
* [ENHANCEMENT][MAINTENANCE] Use Metrics to Protect Against Wrong Column Names
* [BUGFIX] Remove parentheses call at os.curdir in data_context.py #2566 (thanks @henriquejsfj)
* [BUGFIX] Sorter Configuration Added to DataConnectorConfig and DataConnectorConfigSchema #2572
* [BUGFIX] Remove autosave of Checkpoints in test_yaml_config and store SimpleCheckpoint as Checkpoint #2549
* [ENHANCE] Update UserConfigurableProfiler to increase tolerance for mostly parameter of nullity expectations
* [BUGFIX] Populate (data) asset name in data docs for SimpleSqlalchemy datasource (Thanks @xaniasd)
* [BUGFIX] pandas partial read_ functions not being unwrapped (Thanks @luke321321)
* [BUGFIX] Don't stop SparkContext when running in Databricks (#2587) (Thanks @jarandaf)
* [MAINTENANCE] Oracle listed twice in list of sqlalchemy dialects #2609
* [FEATURE] Oracle support added to sqlalchemy datasource and dataset #2609

0.13.14
-----------------
* [BUGFIX] Use temporary paths in tests #2545
* [FEATURE] Allow custom data_asset_name for in-memory dataframes #2494
* [ENHANCEMENT] Restore cli functionality for legacy checkpoints #2511
* [BUGFIX] Can not create Azure Backend with TupleAzureBlobStoreBackend #2513 (thanks @benoitLebreton-perso)
* [BUGFIX] force azure to set content_type='text/html' if the file is HTML #2539 (thanks @benoitLebreton-perso)
* [BUGFIX] Temporarily pin SqlAlchemy to < 1.4.0 in requirements-dev-sqlalchemy.txt #2547
* [DOCS] Fix documentation links generated within template #2542 (thanks @thejasraju)
* [MAINTENANCE] Remove deprecated automerge config #249

0.13.13
-----------------
* [ENHANCEMENT] Improve support for median calculation in Athena (Thanks @kuhnen!) #2521
* [ENHANCEMENT] Update `suite scaffold` to work with the UserConfigurableProfiler #2519
* [MAINTENANCE] Add support for spark 3 based spark_config #2481

0.13.12
-----------------

* [FEATURE] Added EmailAction as a new Validation Action (Thanks @Cedric-Magnan!) #2479
* [ENHANCEMENT] CLI global options and checkpoint functionality for v3 api #2497
* [DOCS] Renamed the "old" and the "new" APIs to "V2 (Batch Kwargs) API" and "V3 (Batch Request) API" and added an article with recommendations for choosing between them

0.13.11
-----------------
* [FEATURE] Add "table.head" metric
* [FEATURE] Add support for BatchData as a core GE concept for all Execution Engines. #2395
 * NOTE: As part of our improvements to the underlying Batch API, we have refactored BatchSpec to be part of the "core" package in Great Expectations, consistent with its role coordinating communication about Batches between the Datasource and Execution Engine abstractions.
* [ENHANCEMENT] Explicit support for schema_name in the SqlAlchemyBatchData #2465. Issue #2340
* [ENHANCEMENT] Data docs can now be built skipping the index page using the python API #2224
* [ENHANCEMENT] Evaluation parameter runtime values rendering in data docs if arithmetic is present #2447. Issue #2215
* [ENHANCEMENT] When connecting to new Datasource, CLI prompt is consistent with rest of GE #2434
* [ENHANCEMENT] Adds basic test for bad s3 paths generated from regex #2427 (Thanks @lukedyer-peak!)
* [ENHANCEMENT] Updated UserConfigurableProfiler date parsing error handling #2459
* [ENHANCEMENT] Clarification of self_check error messages #2304
* [ENHANCEMENT] Allows gzipped files and other encodings to be read from S3 #2440 (Thanks @luke321321!)
* [BUGFIX] `expect_column_unique_value_count_to_be_between` renderer bug (duplicate "Distinct (%)") #2455. Issue #2423
* [BUGFIX] Fix S3 Test issue by pinning `moto` version < 2.0.0 #2470
* [BUGFIX] Check for datetime-parseable strings in validate_metric_value_between_configuration #2419. Issue #2340 (Thanks @victorwyee!)
* [BUGFIX] `expect_compound_columns_to_be_unique` ExpectationConfig added #2471 Issue #2464
* [BUGFIX] In basic profiler, handle date parsing and overflow exceptions separately #2431 (Thanks @peterdhansen!)
* [BUGFIX] Fix sqlalchemy column comparisons when comparison was done between different datatypes #2443 (Thanks @peterdhansen!)
* [BUGFIX] Fix divide by zero error in expect_compound_columns_to_be_unique #2454 (Thanks @jdimatteo!)
* [DOCS] added how-to guide for user configurable profiler #2452
* [DOCS] Linked videos and minor documentation addition #2388
* [DOCS] Modifying getting started tutorial content to work with 0.13.8+ #2418
* [DOCS] add case studies to header in docs #2430
* [MAINTENANCE] Updates to Azure pipeline configurations #2462
* [MAINTENANCE] Allowing the tests to run with Docker-in-Windows #2402 (Thanks @Patechoc!)
* [MAINTENANCE] Add support for automatically building expectations gallery metadata #2386


0.13.10
-----------------
* [ENHANCEMENT] Optimize tests #2421
* [ENHANCEMENT] Add docstring for _invert_regex_to_data_reference_template #2428
* [ENHANCEMENT] Added expectation to check if data is in alphabetical ordering #2407 (Thanks @sethdmay!)
* [BUGFIX] Fixed a broken docs link #2433
* [BUGFIX] Missing `markown_text.j2` jinja template #2422
* [BUGFIX] parse_strings_as_datetimes error with user_configurable_profiler #2429
* [BUGFIX] Update `suite edit` and `suite scaffold` notebook renderers to output functional validation cells #2432
* [DOCS] Update how_to_create_custom_expectations_for_pandas.rst #2426 (Thanks @henriquejsfj!)
* [DOCS] Correct regex escape for data connectors #2425 (Thanks @lukedyer-peak!)
* [CONTRIB] Expectation: Matches benfords law with 80 percent confidence interval test #2406 (Thanks @vinodkri1!)


0.13.9
-----------------
* [FEATURE] Add TupleAzureBlobStoreBackend (thanks @syahdeini) #1975
* [FEATURE] Add get_metrics interface to Modular Expectations Validator API
* [ENHANCEMENT] Add possibility to pass boto3 configuration to TupleS3StoreBackend (Thanks for #1691 to @mgorsk1!) #2371
* [ENHANCEMENT] Removed the logic that prints the "This configuration object was built using version..." warning when current version of Great Expectations is not the same as the one used to build the suite, since it was not actionable #2366
* [ENHANCEMENT] Update Validator with more informative error message
* [BUGFIX] Ensure that batch_spec_passthrough is handled correctly by properly refactoring build_batch_spec and _generate_batch_spec_parameters_from_batch_definition for all DataConnector classes
* [BUGFIX] Display correct unexpected_percent in DataDocs - corrects the result object from map expectations to return the same "unexpected_percent" as is used to evaluate success (excluding null values from the denominator). The old value is now returned in a key called "unexpected_percent_total" (thanks @mlondschien) #1875
* [BUGFIX] Add python=3.7 argument to conda env creation (thanks @scouvreur!) #2391
* [BUGFIX] Fix issue with temporary table creation in MySQL #2389
* [BUGFIX] Remove duplicate code in data_context.store.tuple_store_backend (Thanks @vanderGoes)
* [BUGFIX] Fix issue where WarningAndFailureExpectationSuitesValidationOperator failing when warning suite fails
* [DOCS] Update How to instantiate a Data Context on Databricks Spark cluster for 0.13+ #2379
* [DOCS] How to load a Pandas DataFrame as a Batch #2327
* [DOCS] Added annotations for Expectations not yet ported to the new Modular Expectations API.
* [DOCS] How to load a Spark DataFrame as a Batch #2385
* [MAINTENANCE] Add checkpoint store to store backend defaults #2378


0.13.8
-----------------
* [FEATURE] New implementation of Checkpoints that uses dedicated CheckpointStore (based on the new ConfigurationStore mechanism) #2311, #2338
* [BUGFIX] Fix issue causing incorrect identification of partially-implemented expectations as not abstract #2334
* [BUGFIX] DataContext with multiple DataSources no longer scans all configurations #2250


0.13.7
-----------------
* [BUGFIX] Fix Local variable 'temp_table_schema_name' might be referenced before assignment bug in sqlalchemy_dataset.py #2302
* [MAINTENANCE] Ensure compatibility with new pip resolver v20.3+ #2256
* [ENHANCEMENT] Improvements in the how-to guide, run_diagnostics method in Expectation base class and Expectation templates to support the new rapid "dev loop" of community-contributed Expectations. #2296
* [ENHANCEMENT] Improvements in the output of Expectations tests to make it more legible. #2296
* [DOCS] Clarification of the instructions for using conda in the "Setting Up Your Dev Environment" doc. #2306


0.13.6
-----------------
* [ENHANCEMENT] Skip checks when great_expectations package did not change #2287
* [ENHANCEMENT] A how-to guide, run_diagnostics method in Expectation base class and Expectation templates to support the new rapid "dev loop" of community-contributed Expectations. #2222
* [BUGFIX] Fix Local variable 'query_schema' might be referenced before assignment bug in sqlalchemy_dataset.py #2286 (Thanks @alessandrolacorte!)
* [BUGFIX] Use correct schema to fetch table and column metadata #2284 (Thanks @armaandhull!)
* [BUGFIX] Updated sqlalchemy_dataset to convert numeric metrics to json_serializable up front, avoiding an issue where expectations on data immediately fail due to the conversion to/from json. #2207


0.13.5
-----------------
* [FEATURE] Add MicrosoftTeamsNotificationAction (Thanks @Antoninj!)
* [FEATURE] New ``contrib`` package #2264
* [ENHANCEMENT] Data docs can now be built skipping the index page using the python API #2224
* [ENHANCEMENT] Speed up new suite creation flow when connecting to Databases. Issue #1670 (Thanks @armaandhull!)
* [ENHANCEMENT] Serialize PySpark DataFrame by converting to dictionary #2237
* [BUGFIX] Mask passwords in DataContext.list_datasources(). Issue #2184
* [BUGFIX] Skip escaping substitution variables in escape_all_config_variables #2243. Issue #2196 (Thanks @
varundunga!)
* [BUGFIX] Pandas extension guessing #2239 (Thanks @sbrugman!)
* [BUGFIX] Replace runtime batch_data DataFrame with string #2240
* [BUGFIX] Update Notebook Render Tests to Reflect Updated Python Packages #2262
* [DOCS] Updated the code of conduct to mention events #2278
* [DOCS] Update the diagram for batch metadata #2161
* [DOCS] Update metrics.rst #2257
* [MAINTENANCE] Different versions of Pandas react differently to corrupt XLS files. #2230
* [MAINTENANCE] remove the obsolete TODO comments #2229 (Thanks @beyondacm!)
* [MAINTENANCE] Update run_id to airflow_run_id for clarity. #2233


0.13.4
-----------------
* [FEATURE] Implement expect_column_values_to_not_match_regex_list in Spark (Thanks @mikaylaedwards!)
* [ENHANCEMENT] Improve support for quantile calculations in Snowflake
* [ENHANCEMENT] DataDocs show values of Evaluation Parameters #2165. Issue #2010
* [ENHANCEMENT] Work on requirements.txt #2052 (Thanks @shapiroj18!)
* [ENHANCEMENT] expect_table_row_count_to_equal_other_table #2133
* [ENHANCEMENT] Improved support for quantile calculations in Snowflake #2176
* [ENHANCEMENT] DataDocs show values of Evaluation Parameters #2165
* [BUGFIX] Add pagination to TupleS3StoreBackend.list_keys() #2169. Issue #2164
* [BUGFIX] Fixed black conflict, upgraded black, made import optional #2183
* [BUGFIX] Made improvements for the treatment of decimals for database backends for lossy conversion #2207
* [BUGFIX] Pass manually_initialize_store_backend_id to database store backends to mirror functionality of other backends. Issue #2181
* [BUGFIX] Make glob_directive more permissive in ConfiguredAssetFilesystemDataConnector #2197. Issue #2193
* [DOCS] Added link to Youtube video on in-code contexts #2177
* [DOCS] Docstrings for DataConnector and associated classes #2172
* [DOCS] Custom expectations improvement #2179
* [DOCS] Add a conda example to creating virtualenvs #2189
* [DOCS] Fix Airflow logo URL #2198 (Thanks @floscha!)
* [DOCS] Update explore_expectations_in_a_notebook.rst #2174
* [DOCS] Change to DOCS that describe Evaluation Parameters #2209
* [MAINTENANCE] Removed mentions of show_cta_footer and added deprecation notes in usage stats #2190. Issue #2120

0.13.3
-----------------
* [ENHANCEMENT] Updated the BigQuery Integration to create a view instead of a table (thanks @alessandrolacorte!) #2082.
* [ENHANCEMENT] Allow  database store backend to support specification of schema in credentials file
* [ENHANCEMENT] Add support for connection_string and url in configuring DatabaseStoreBackend, bringing parity to other SQL-based objects. In the rare case of user code that instantiates a DatabaseStoreBackend without using the Great Expectations config architecture, users should ensure they are providing kwargs to init, because the init signature order has changed.
* [ENHANCEMENT] Improved exception handling in the Slack notifications rendering logic
* [ENHANCEMENT] Uniform configuration support for both 0.13 and 0.12 versions of the Datasource class
* [ENHANCEMENT] A single `DataContext.get_batch()` method supports both 0.13 and 0.12 style call arguments
* [ENHANCEMENT] Initializing DataContext in-code is now available in both 0.13 and 0.12 versions
* [BUGFIX] Fixed a bug in the error printing logic in several exception handling blocks in the Data Docs rendering. This will make it easier for users to submit error messages in case of an error in rendering.
* [DOCS] Miscellaneous doc improvements
* [DOCS] Update cloud composer workflow to use GCSStoreBackendDefaults

0.13.2
-----------------
* [ENHANCEMENT] Support avro format in Spark datasource (thanks @ryanaustincarlson!) #2122
* [ENHANCEMENT] Made improvements to the backend for expect_column_quantile_values_to_be_between #2127
* [ENHANCEMENT] Robust Representation in Configuration of Both Legacy and New Datasource
* [ENHANCEMENT] Continuing 0.13 clean-up and improvements
* [BUGFIX] Fix spark configuration not getting passed to the SparkSession builder (thanks @EricSteg!) #2124
* [BUGFIX] Misc bugfixes and improvements to code & documentation for new in-code data context API #2118
* [BUGFIX] When Introspecting a database, sql_data_connector will ignore view_names that are also system_tables
* [BUGFIX] Made improvements for code & documentation for in-code data context
* [BUGFIX] Fixed bug where TSQL mean on `int` columns returned incorrect result
* [DOCS] Updated explanation for ConfiguredAssetDataConnector and InferredAssetDataConnector
* [DOCS] General 0.13 docs improvements

0.13.1
-----------------
* [ENHANCEMENT] Improved data docs performance by ~30x for large projects and ~4x for smaller projects by changing instantiation of Jinja environment #2100
* [ENHANCEMENT] Allow  database store backend to support specification of schema in credentials file #2058 (thanks @GTLangseth!)
* [ENHANCEMENT] More detailed information in Datasource.self_check() diagnostic (concerning ExecutionEngine objects)
* [ENHANCEMENT] Improve UI for in-code data contexts #2068
* [ENHANCEMENT] Add a store_backend_id property to StoreBackend #2030, #2075
* [ENHANCEMENT] Use an existing expectation_store.store_backend_id to initialize an in-code DataContext #2046, #2075
* [BUGFIX] Corrected handling of boto3_options by PandasExecutionEngine
* [BUGFIX] New Expectation via CLI / SQL Query no longer throws TypeError
* [BUGFIX] Implement validator.default_expectations_arguments
* [DOCS] Fix doc create and editing expectations #2105 (thanks @Lee-W!)
* [DOCS] Updated documentation on 0.13 classes
* [DOCS] Fixed a typo in the HOWTO guide for adding a self-managed Spark datasource
* [DOCS] Updated documentation for new UI for in-code data contexts

0.13.0
-----------------
* INTRODUCING THE NEW MODULAR EXPECTATIONS API (Experimental): this release introduces a new way to create expectation logic in its own class, making it much easier to author and share expectations. ``Expectation`` and ``MetricProvider`` classes now work together to validate data and consolidate logic for all backends by function. See the how-to guides in our documentation for more information on how to use the new API.
* INTRODUCING THE NEW DATASOURCE API (Experimental): this release introduces a new way to connect to datasources providing much richer guarantees for discovering ("inferring") data assets and partitions. The new API replaces "BatchKwargs" and "BatchKwargsGenerators" with BatchDefinition and BatchSpec objects built from DataConnector classes. You can read about the new API in our docs.
* The Core Concepts section of our documentation has been updated with descriptions of the classes and concepts used in the new API; we will continue to update that section and welcome questions and improvements.
* BREAKING: Data Docs rendering is now handled in the new Modular Expectations, which means that any custom expectation rendering needs to be migrated to the new API to function in version 0.13.0.
* BREAKING: **Renamed** Datasource to LegacyDatasource and introduced the new Datasource class. Because most installations rely on one PandasDatasource, SqlAlchemyDatasource, or SparkDFDatasource, most users will not be affected. However, if you have implemented highly customized Datasource class inheriting from the base class, you may need to update your inheritance.
* BREAKING: The new Modular Expectations API will begin removing the ``parse_strings_as_datetimes`` and ``allow_cross_type_comparisons`` flags in expectations. Expectation Suites that use the flags will need to be updated to use the new Modular Expectations. In general, simply removing the flag will produce correct behavior; if you still want the exact same semantics, you should ensure your raw data already has typed datetime objects.
* **NOTE:** Both the new Datasource API and the new Modular Expectations API are *experimental* and will change somewhat during the next several point releases. We are extremely excited for your feedback while we iterate rapidly, and continue to welcome new community contributions.

0.12.10
-----------------
* [BUGFIX] Update requirements.txt for ruamel.yaml to >=0.16 - #2048 (thanks @mmetzger!)
* [BUGFIX] Added option to return scalar instead of list from query store #2060
* [BUGFIX] Add missing markdown_content_block_container #2063
* [BUGFIX] Fixed a divided by zero error for checkpoints on empty expectation suites #2064
* [BUGFIX] Updated sort to correctly return partial unexpected results when expect_column_values_to_be_of_type has more than one unexpected type #2074
* [BUGFIX] Resolve Data Docs resource identifier issues to speed up UpdateDataDocs action #2078
* [DOCS] Updated contribution changelog location #2051 (thanks @shapiroj18!)
* [DOCS] Adding Airflow operator and Astrononomer deploy guides #2070
* [DOCS] Missing image link to bigquery logo #2071 (thanks @nelsonauner!)

0.12.9
-----------------
* [BUGFIX] Fixed the import of s3fs to use the optional import pattern - issue #2053
* [DOCS] Updated the title styling and added a Discuss comment article for the OpsgenieAlertAction how-to guide

0.12.8
-----------------
* [FEATURE] Add OpsgenieAlertAction #2012 (thanks @miike!)
* [FEATURE] Add S3SubdirReaderBatchKwargsGenerator #2001 (thanks @noklam)
* [ENHANCEMENT] Snowflake uses temp tables by default while still allowing transient tables
* [ENHANCEMENT] Enabled use of lowercase table and column names in GE with the `use_quoted_name` key in batch_kwargs #2023
* [BUGFIX] Basic suite builder profiler (suite scaffold) now skips excluded expectations #2037
* [BUGFIX] Off-by-one error in linking to static images #2036 (thanks @NimaVaziri!)
* [BUGFIX] Improve handling of pandas NA type issue #2029 PR #2039 (thanks @isichei!)
* [DOCS] Update Virtual Environment Example #2027 (thanks @shapiroj18!)
* [DOCS] Update implemented_expectations.rst (thanks @jdimatteo!)
* [DOCS] Update how_to_configure_a_pandas_s3_datasource.rst #2042 (thanks @CarstenFrommhold!)

0.12.7
-----------------
* [ENHANCEMENT] CLI supports s3a:// or gs:// paths for Pandas Datasources (issue #2006)
* [ENHANCEMENT] Escape $ characters in configuration, support multiple substitutions (#2005 & #2015)
* [ENHANCEMENT] Implement Skip prompt flag on datasource profile cli (#1881 Thanks @thcidale0808!)
* [BUGFIX] Fixed bug where slack messages cause stacktrace when data docs pages have issue
* [DOCS] How to use docker images (#1797)
* [DOCS] Remove incorrect doc line from PagerdutyAlertAction (Thanks @niallrees!)
* [MAINTENANCE] Update broken link (Thanks @noklam!)
* [MAINTENANCE] Fix path for how-to guide (Thanks @gauthamzz!)

0.12.6
-----------------
* [BUGFIX] replace black in requirements.txt

0.12.5
-----------------
* [ENHANCEMENT] Implement expect_column_values_to_be_json_parseable in spark (Thanks @mikaylaedwards!)
* [ENHANCEMENT] Fix boto3 options passing into datasource correctly (Thanks @noklam!)
* [ENHANCEMENT] Add .pkl to list of recognized extensions (Thanks @KPLauritzen!)
* [BUGFIX] Query batch kwargs support for Athena backend (issue 1964)
* [BUGFIX] Skip config substitution if key is "password" (issue 1927)
* [BUGFIX] fix site_names functionality and add site_names param to get_docs_sites_urls (issue 1991)
* [BUGFIX] Always render expectation suites in data docs unless passing a specific ExpectationSuiteIdentifier in resource_identifiers (issue 1944)
* [BUGFIX] remove black from requirements.txt
* [BUGFIX] docs build cli: fix --yes argument (Thanks @varunbpatil!)
* [DOCS] Update docstring for SubdirReaderBatchKwargsGenerator (Thanks @KPLauritzen!)
* [DOCS] Fix broken link in README.md (Thanks @eyaltrabelsi!)
* [DOCS] Clarifications on several docs (Thanks all!!)

0.12.4
-----------------
* [FEATURE] Add PagerdutyAlertAction (Thanks @NiallRees!)
* [FEATURE] enable using Minio for S3 backend (Thanks @noklam!)
* [ENHANCEMENT] Add SqlAlchemy support for expect_compound_columns_to_be_unique (Thanks @jhweaver!)
* [ENHANCEMENT] Add Spark support for expect_compound_columns_to_be_unique (Thanks @tscottcoombes1!)
* [ENHANCEMENT] Save expectation suites with datetimes in evaluation parameters (Thanks @mbakunze!)
* [ENHANCEMENT] Show data asset name in Slack message (Thanks @haydarai!)
* [ENHANCEMENT] Enhance data doc to show data asset name in overview block (Thanks @noklam!)
* [ENHANCEMENT] Clean up checkpoint output
* [BUGFIX] Change default prefix for TupleStoreBackend (issue 1907)
* [BUGFIX] Duplicate s3 approach for GCS for building object keys
* [BUGFIX] import NotebookConfig (Thanks @cclauss!)
* [BUGFIX] Improve links (Thanks @sbrugman!)
* [MAINTENANCE] Unpin black in requirements (Thanks @jtilly!)
* [MAINTENANCE] remove test case name special characters

0.12.3
-----------------
* [ENHANCEMENT] Add expect_compound_columns_to_be_unique and clarify multicolumn uniqueness
* [ENHANCEMENT] Add expectation expect_table_columns_to_match_set
* [ENHANCEMENT] Checkpoint run command now prints out details on each validation #1437
* [ENHANCEMENT] Slack notifications can now display links to GCS-hosted DataDocs sites
* [ENHANCEMENT] Public base URL can be configured for Data Docs sites
* [ENHANCEMENT] SuiteEditNotebookRenderer.add_header class now allows usage of env variables in jinja templates (thanks @mbakunze)!
* [ENHANCEMENT] Display table for Cramer's Phi expectation in Data Docs (thanks @mlondschien)!
* [BUGFIX] Explicitly convert keys to tuples when removing from TupleS3StoreBackend (thanks @balexander)!
* [BUGFIX] Use more-specific s3.meta.client.exceptions with dealing with boto resource api (thanks @lcorneliussen)!
* [BUGFIX] Links to Amazon S3 are compatible with virtual host-style access and path-style access
* [DOCS] How to Instantiate a Data Context on a Databricks Spark Cluster
* [DOCS] Update to Deploying Great Expectations with Google Cloud Composer
* [MAINTENANCE] Update moto dependency to include cryptography (see #spulec/moto/3290)

0.12.2
-----------------
* [ENHANCEMENT] Update schema for anonymized expectation types to avoid large key domain
* [ENHANCEMENT] BaseProfiler type mapping expanded to include more pandas and numpy dtypes
* [BUGFIX] Allow for pandas reader option inference with parquet and Excel (thanks @dlachasse)!
* [BUGFIX] Fix bug where running checkpoint fails if GCS data docs site has a prefix (thanks @sergii-tsymbal-exa)!
* [BUGFIX] Fix bug in deleting datasource config from config file (thanks @rxmeez)!
* [BUGFIX] clarify inclusiveness of min/max values in string rendering
* [BUGFIX] Building data docs no longer crashes when a data asset name is an integer #1913
* [DOCS] Add notes on transient table creation to Snowflake guide (thanks @verhey)!
* [DOCS] Fixed several broken links and glossary organization (thanks @JavierMonton and @sbrugman)!
* [DOCS] Deploying Great Expectations with Google Cloud Composer (Hosted Airflow)

0.12.1
-----------------
* [FEATURE] Add ``expect_column_pair_cramers_phi_value_to_be_less_than`` expectation to ``PandasDatasource`` to check for the independence of two columns by computing their Cramers Phi (thanks @mlondschien)!
* [FEATURE] add support for ``expect_column_pair_values_to_be_in_set`` to ``Spark`` (thanks @mikaylaedwards)!
* [FEATURE] Add new expectation:`` expect_multicolumn_sum_to_equal`` for ``pandas` and ``Spark`` (thanks @chipmyersjr)!
* [ENHANCEMENT] Update isort, pre-commit & pre-commit hooks, start more linting (thanks @dandandan)!
* [ENHANCEMENT] Bundle shaded marshmallow==3.7.1 to avoid dependency conflicts on GCP Composer
* [ENHANCEMENT] Improve row_condition support in aggregate expectations
* [BUGFIX] SuiteEditNotebookRenderer no longer break GCS and S3 data paths
* [BUGFIX] Fix bug preventing the use of get_available_partition_ids in s3 generator
* [BUGFIX] SuiteEditNotebookRenderer no longer break GCS and S3 data paths
* [BUGFIX] TupleGCSStoreBackend: remove duplicate prefix for urls (thanks @azban)!
* [BUGFIX] Fix `TypeError: unhashable type` error in Data Docs rendering

0.12.0
-----------------
* [BREAKING] This release includes a breaking change that *only* affects users who directly call `add_expectation`, `remove_expectation`, or `find_expectations`. (Most users do not use these APIs but add Expectations by stating them directly on Datasets). Those methods have been updated to take an ExpectationConfiguration object and `match_type` object. The change provides more flexibility in determining which expectations should be modified and allows us provide substantially improved support for two major features that we have frequently heard requested: conditional Expectations and more flexible multi-column custom expectations. See :ref:`expectation_suite_operations` and :ref:`migrating_versions` for more information.
* [FEATURE] Add support for conditional expectations using pandas execution engine (#1217 HUGE thanks @arsenii!)
* [FEATURE] ValidationActions can now consume and return "payload", which can be used to share information across ValidationActions
* [FEATURE] Add support for nested columns in the PySpark expectations (thanks @bramelfrink)!
* [FEATURE] add support for `expect_column_values_to_be_increasing` to `Spark` (thanks @mikaylaedwards)!
* [FEATURE] add support for `expect_column_values_to_be_decreasing` to `Spark` (thanks @mikaylaedwards)!
* [FEATURE] Slack Messages sent as ValidationActions now have link to DataDocs, if available.
* [FEATURE] Expectations now define “domain,” “success,” and “runtime” kwargs to allow them to determine expectation equivalence for updating expectations. Fixes column pair expectation update logic.
* [ENHANCEMENT] Add a `skip_and_clean_missing` flag to `DefaultSiteIndexBuilder.build` (default True). If True, when an index page is being built and an existing HTML page does not have corresponding source data (i.e. an expectation suite or validation result was removed from source store), the HTML page is automatically deleted and will not appear in the index. This ensures that the expectations store and validations store are the source of truth for Data Docs.
* [ENHANCEMENT] Include datetime and bool column types in descriptive documentation results
* [ENHANCEMENT] Improve data docs page breadcrumbs to have clearer run information
* [ENHANCEMENT] Data Docs Validation Results only shows unexpected value counts if all unexpected values are available
* [ENHANCEMENT] Convert GE version key from great_expectations.__version__ to great_expectations_version (thanks, @cwerner!) (#1606)
* [ENHANCEMENT] Add support in JSON Schema profiler for combining schema with anyOf key and creating nullability expectations
* [BUGFIX] Add guard for checking Redshift Dialect in match_like_pattern expectation
* [BUGFIX] Fix content_block build failure for dictionary content - (thanks @jliew!) #1722
* [BUGFIX] Fix bug that was preventing env var substitution in `config_variables.yml` when not at the top level
* [BUGFIX] Fix issue where expect_column_values_to_be_in_type_list did not work with positional type_list argument in SqlAlchemyDataset or SparkDFDataset
* [BUGFIX] Fixes a bug that was causing exceptions to occur if user had a Data Docs config excluding a particular site section
* [DOCS] Add how-to guides for configuring MySQL and MSSQL Datasources
* [DOCS] Add information about issue tags to contributing docs
* [DEPRECATION] Deprecate demo suite behavior in `suite new`

0.11.9
-----------------
* [FEATURE] New Dataset Support: Microsoft SQL Server
* [FEATURE] Render expectation validation results to markdown
* [FEATURE] Add --assume-yes/--yes/-y option to cli docs build command (thanks @feluelle)
* [FEATURE] Add SSO and SSH key pair authentication for Snowflake (thanks @dmateusp)
* [FEATURE] Add pattern-matching expectations that use the Standard SQL "LIKE" operator: "expect_column_values_to_match_like_pattern", "expect_column_values_to_not_match_like_pattern", "expect_column_values_to_match_like_pattern_list", and "expect_column_values_to_not_match_like_pattern_list"
* [ENHANCEMENT] Make Data Docs rendering of profiling results more flexible by deprecating the reliance on validation results having the specific run_name of "profiling"
* [ENHANCEMENT] Use green checkmark in Slack msgs instead of tada
* [ENHANCEMENT] log class instantiation errors for better debugging
* [BUGFIX] usage_statistics decorator now handles 'dry_run' flag
* [BUGFIX] Add spark_context to DatasourceConfigSchema (#1713) (thanks @Dandandan)
* [BUGFIX] Handle case when unexpected_count list element is str
* [DOCS] Deploying Data Docs
* [DOCS] New how-to guide: How to instantiate a Data Context on an EMR Spark cluster
* [DOCS] Managed Spark DF Documentation #1729 (thanks @mgorsk1)
* [DOCS] Typos and clarifications (thanks @dechoma @sbrugman @rexboyce)

0.11.8
-----------------
* [FEATURE] Customizable "Suite Edit" generated notebooks
* [ENHANCEMENT] Add support and docs for loading evaluation parameter from SQL database
* [ENHANCEMENT] Fixed some typos/grammar and a broken link in the suite_scaffold_notebook_renderer
* [ENHANCEMENT] allow updates to DatabaseStoreBackend keys by default, requiring `allow_update=False` to disallow
* [ENHANCEMENT] Improve support for prefixes declared in TupleS3StoreBackend that include reserved characters
* [BUGFIX] Fix issue where allow_updates was set for StoreBackend that did not support it
* [BUGFIX] Fix issue where GlobReaderBatchKwargsGenerator failed with relative base_directory
* [BUGFIX] Adding explicit requirement for "importlib-metadata" (needed for Python versions prior to Python 3.8).
* [MAINTENANCE] Install GitHub Dependabot
* [BUGFIX] Fix missing importlib for python 3.8 #1651

0.11.7
-----------------
* [ENHANCEMENT] Improve CLI error handling.
* [ENHANCEMENT] Do not register signal handlers if not running in main thread
* [ENHANCEMENT] store_backend (S3 and GCS) now throws InvalidKeyError if file does not exist at expected location
* [BUGFIX] ProfilerTypeMapping uses lists instead of sets to prevent serialization errors when saving suites created by JsonSchemaProfiler
* [DOCS] Update suite scaffold how-to
* [DOCS] Docs/how to define expectations that span multiple tables
* [DOCS] how to metadata stores validation on s3

0.11.6
-----------------
* [FEATURE] Auto-install Python DB packages.  If the required packages for a DB library are not installed, GE will offer the user to install them, without exiting CLI
* [FEATURE] Add new expectation expect_table_row_count_to_equal_other_table for SqlAlchemyDataset
* [FEATURE] A profiler that builds suites from JSONSchema files
* [ENHANCEMENT] Add ``.feather`` file support to PandasDatasource
* [ENHANCEMENT] Use ``colorama init`` to support terminal color on Windows
* [ENHANCEMENT] Update how_to_trigger_slack_notifications_as_a_validation_action.rst
* [ENHANCEMENT] Added note for config_version in great_expectations.yml
* [ENHANCEMENT] Implement "column_quantiles" for MySQL (via a compound SQLAlchemy query, since MySQL does not support "percentile_disc")
* [BUGFIX] "data_asset.validate" events with "data_asset_name" key in the batch kwargs were failing schema validation
* [BUGFIX] database_store_backend does not support storing Expectations in DB
* [BUGFIX] instantiation of ExpectationSuite always adds GE version metadata to prevent datadocs from crashing
* [BUGFIX] Fix all tests having to do with missing data source libraries
* [DOCS] will/docs/how_to/Store Expectations on Google Cloud Store

0.11.5
-----------------
* [FEATURE] Add support for expect_column_values_to_match_regex_list exception for Spark backend
* [ENHANCEMENT] Added 3 new usage stats events: "cli.new_ds_choice", "data_context.add_datasource", and "datasource.sqlalchemy.connect"
* [ENHANCEMENT] Support platform_specific_separator flag for TupleS3StoreBackend prefix
* [ENHANCEMENT] Allow environment substitution in config_variables.yml
* [BUGFIX] fixed issue where calling head() on a SqlAlchemyDataset would fail if the underlying table is empty
* [BUGFIX] fixed bug in rounding of mostly argument to nullity expectations produced by the BasicSuiteBuilderProfiler
* [DOCS] New How-to guide: How to add a Validation Operator (+ updated in Validation Operator doc strings)

0.11.4
-----------------
* [BUGIFX] Fixed an error that crashed the CLI when called in an environment with neither SQLAlchemy nor google.auth installed

0.11.3
-----------------
* [ENHANCEMENT] Removed the misleading scary "Site doesn't exist or is inaccessible" message that the CLI displayed before building Data Docs for the first time.
* [ENHANCEMENT] Catch sqlalchemy.exc.ArgumentError and google.auth.exceptions.GoogleAuthError in SqlAlchemyDatasource __init__ and re-raise them as DatasourceInitializationError - this allows the CLI to execute its retry logic when users provide a malformed SQLAlchemy URL or attempt to connect to a BigQuery project without having proper authentication.
* [BUGFIX] Fixed issue where the URL of the Glossary of Expectations article in the auto-generated suite edit notebook was wrong (out of date) (#1557).
* [BUGFIX] Use renderer_type to set paths in jinja templates instead of utm_medium since utm_medium is optional
* [ENHANCEMENT] Bring in custom_views_directory in DefaultJinjaView to enable custom jinja templates stored in plugins dir
* [BUGFIX] fixed glossary links in walkthrough modal, README, CTA button, scaffold notebook
* [BUGFIX] Improved TupleGCSStoreBackend configurability (#1398 #1399)
* [BUGFIX] Data Docs: switch bootstrap-table-filter-control.min.js to CDN
* [ENHANCEMENT] BasicSuiteBuilderProfiler now rounds mostly values for readability
* [DOCS] Add AutoAPI as the primary source for API Reference docs.

0.11.2
-----------------
* [FEATURE] Add support for expect_volumn_values_to_match_json_schema exception for Spark backend (thanks @chipmyersjr!)
* [ENHANCEMENT] Add formatted __repr__ for ValidationOperatorResult
* [ENHANCEMENT] add option to suppress logging when getting expectation suite
* [BUGFIX] Fix object name construction when calling SqlAlchemyDataset.head (thanks @mascah!)
* [BUGFIX] Fixed bug where evaluation parameters used in arithmetic expressions would not be identified as upstream dependencies.
* [BUGFIX] Fix issue where DatabaseStoreBackend threw IntegrityError when storing same metric twice
* [FEATURE] Added new cli upgrade helper to help facilitate upgrading projects to be compatible with GE 0.11.
  See :ref:`upgrading_to_0.11` for more info.
* [BUGFIX] Fixed bug preventing GCS Data Docs sites to cleaned
* [BUGFIX] Correct doc link in checkpoint yml
* [BUGFIX] Fixed issue where CLI checkpoint list truncated names (#1518)
* [BUGFIX] Fix S3 Batch Kwargs Generator incorrect migration to new build_batch_kwargs API
* [BUGFIX] Fix missing images in data docs walkthrough modal
* [BUGFIX] Fix bug in checkpoints that was causing incorrect run_time to be set
* [BUGFIX] Fix issue where data docs could remove trailing zeros from values when low precision was requested

0.11.1
-----------------
* [BUGFIX] Fixed bug that was caused by comparison between timezone aware and non-aware datetimes
* [DOCS] Updated docs with info on typed run ids and validation operator results
* [BUGFIX] Update call-to-action buttons on index page with correct URLs

0.11.0
-----------------
* [BREAKING] ``run_id`` is now typed using the new ``RunIdentifier`` class, which consists of a ``run_time`` and
  ``run_name``. Existing projects that have Expectation Suite Validation Results must be migrated.
  See :ref:`upgrading_to_0.11` for instructions.
* [BREAKING] ``ValidationMetric`` and ``ValidationMetricIdentifier`` objects now have a ``data_asset_name`` attribute.
  Existing projects with evaluation parameter stores that have database backends must be migrated.
  See :ref:`upgrading_to_0.11` for instructions.
* [BREAKING] ``ValidationOperator.run`` now returns an instance of new type, ``ValidationOperatorResult`` (instead of a
  dictionary). If your code uses output from Validation Operators, it must be updated.
* Major update to the styling and organization of documentation! Watch for more content and reorganization as we continue to improve the documentation experience with Great Expectations.
* [FEATURE] Data Docs: redesigned index page with paginated/sortable/searchable/filterable tables
* [FEATURE] Data Docs: searchable tables on Expectation Suite Validation Result pages
* ``data_asset_name`` is now added to batch_kwargs by batch_kwargs_generators (if available) and surfaced in Data Docs
* Renamed all ``generator_asset`` parameters to ``data_asset_name``
* Updated the dateutil dependency
* Added experimental QueryStore
* Removed deprecated cli tap command
* Added of 0.11 upgrade helper
* Corrected Scaffold maturity language in notebook to Experimental
* Updated the installation/configuration documentation for Snowflake users
* [ENHANCEMENT] Improved error messages for misconfigured checkpoints.
* [BUGFIX] Fixed bug that could cause some substituted variables in DataContext config to be saved to `great_expectations.yml`

0.10.12
-----------------
* [DOCS] Improved help for CLI `checkpoint` command
* [BUGFIX] BasicSuiteBuilderProfiler could include extra expectations when only some expectations were selected (#1422)
* [FEATURE] add support for `expect_multicolumn_values_to_be_unique` and `expect_column_pair_values_A_to_be_greater_than_B`
  to `Spark`. Thanks @WilliamWsyHK!
* [ENHANCEMENT] Allow a dictionary of variables can be passed to the DataContext constructor to allow override
  config variables at runtime. Thanks @balexander!
* [FEATURE] add support for `expect_column_pair_values_A_to_be_greater_than_B` to `Spark`.
* [BUGFIX] Remove SQLAlchemy typehints to avoid requiring library (thanks @mzjp2)!
* [BUGFIX] Fix issue where quantile boundaries could not be set to zero. Thanks @kokes!

0.10.11
-----------------
* Bugfix: build_data_docs list_keys for GCS returns keys and when empty a more user friendly message
* ENHANCEMENT: Enable Redshift Quantile Profiling


0.10.10
-----------------
* Removed out-of-date Airflow integration examples. This repo provides a comprehensive example of Airflow integration: `#GE Airflow Example <https://github.com/superconductive/ge_tutorials>`_
* Bugfix suite scaffold notebook now has correct suite name in first markdown cell.
* Bugfix: fixed an example in the custom expectations documentation article - "result" key was missing in the returned dictionary
* Data Docs Bugfix: template string substitution is now done using .safe_substitute(), to handle cases where string templates
  or substitution params have extraneous $ signs. Also added logic to handle templates where intended output has groupings of 2 or more $ signs
* Docs fix: fix in yml for example action_list_operator for metrics
* GE is now auto-linted using Black

-----------------

* DataContext.get_docs_sites_urls now raises error if non-existent site_name is specified
* Bugfix for the CLI command `docs build` ignoring the --site_name argument (#1378)
* Bugfix and refactor for `datasource delete` CLI command (#1386) @mzjp2
* Instantiate datasources and validate config only when datasource is used (#1374) @mzjp2
* suite delete changed from an optional argument to a required one
* bugfix for uploading objects to GCP #1393
* added a new usage stats event for the case when a data context is created through CLI
* tuplefilestore backend, expectationstore backend remove_key bugs fixed
* no url is returned on empty data_docs site
* return url for resource only if key exists
* Test added for the period special char case
* updated checkpoint module to not require sqlalchemy
* added BigQuery as an option in the list of databases in the CLI
* added special cases for handling BigQuery - table names are already qualified with schema name, so we must make sure that we do not prepend the schema name twice
* changed the prompt for the name of the temp table in BigQuery in the CLI to hint that a fully qualified name (project.dataset.table) should be provided
* Bugfix for: expect_column_quantile_values_to_be_between expectation throws an "unexpected keyword WITHIN" on BigQuery (#1391)

0.10.8
-----------------
* added support for overriding the default jupyter command via a GE_JUPYTER_CMD environment variable (#1347) @nehiljain
* Bugfix for checkpoint missing template (#1379)

0.10.7
-----------------
* crud delete suite bug fix

0.10.6
-----------------

* Checkpoints: a new feature to ease deployment of suites into your pipelines
  - DataContext.list_checkpoints() returns a list of checkpoint names found in the project
  - DataContext.get_checkpoint() returns a validated dictionary loaded from yml
  - new cli commands

    - `checkpoint new`
    - `checkpoint list`
    - `checkpoint run`
    - `checkpoint script`

* marked cli `tap` commands as deprecating on next release
* marked cli `validation-operator run` command as deprecating
* internal improvements in the cli code
* Improve UpdateDataDocsAction docs

0.10.5
-----------------

* improvements to ge.read_json tests
* tidy up the changelog

  - Fix bullet list spacing issues
  - Fix 0.10. formatting
  - Drop roadmap_and_changelog.rst and move changelog.rst to the top level of the table of contents
* DataContext.run_validation_operator() now raises a DataContextError if:
  - no batches are passed
  - batches are of the the wrong type
  - no matching validation operator is found in the project
* Clarified scaffolding language in scaffold notebook
* DataContext.create() adds an additional directory: `checkpoints`
* Marked tap command for deprecation in next major release

0.10.4
-----------------
* consolidated error handling in CLI DataContext loading
* new cli command `suite scaffold` to speed up creation of suites
* new cli command `suite demo` that creates an example suite
* Update bigquery.rst `#1330 <https://github.com/great-expectations/great_expectations/issues/1330>`_
* Fix datetime reference in create_expectations.rst `#1321 <https://github.com/great-expectations/great_expectations/issues/1321>`_ Thanks @jschendel !
* Update issue templates
* CLI command experimental decorator
* Update style_guide.rst
* Add pull request template
* Use pickle to generate hash for dataframes with unhashable objects. `#1315 <https://github.com/great-expectations/great_expectations/issues/1315>`_ Thanks @shahinism !
* Unpin pytest

0.10.3
-----------------
* Use pickle to generate hash for dataframes with unhashable objects.

0.10.2
-----------------
* renamed NotebookRenderer to SuiteEditNotebookRenderer
* SuiteEditNotebookRenderer now lints using black
* New SuiteScaffoldNotebookRenderer renderer to expedite suite creation
* removed autopep8 dependency
* bugfix: extra backslash in S3 urls if store was configured without a prefix `#1314 <https://github.com/great-expectations/great_expectations/issues/1314>`_

0.10.1
-----------------
* removing bootstrap scrollspy on table of contents `#1282 <https://github.com/great-expectations/great_expectations/issues/1282>`_
* Silently tolerate connection timeout during usage stats reporting

0.10.0
-----------------
* (BREAKING) Clarified API language: renamed all ``generator`` parameters and methods to the more correct ``batch_kwargs_generator`` language. Existing projects may require simple migration steps. See :ref:`Upgrading to 0.10.x <upgrading_to_0.10.x>` for instructions.
* Adds anonymized usage statistics to Great Expectations. See this article for details: :ref:`Usage Statistics`.
* CLI: improve look/consistency of ``docs list``, ``suite list``, and ``datasource list`` output; add ``store list`` and ``validation-operator list`` commands.
* New SuiteBuilderProfiler that facilitates faster suite generation by allowing columns to be profiled
* Added two convenience methods to ExpectationSuite: get_table_expectations & get_column_expectations
* Added optional profiler_configuration to DataContext.profile() and DataAsset.profile()
* Added list_available_expectation_types() to DataAsset

0.9.11
-----------------
* Add evaluation parameters support in WarningAndFailureExpectationSuitesValidationOperator `#1284 <https://github.com/great-expectations/great_expectations/issues/1284>`_ thanks `@balexander <https://github.com/balexander>`_
* Fix compatibility with MS SQL Server. `#1269 <https://github.com/great-expectations/great_expectations/issues/1269>`_ thanks `@kepiej <https://github.com/kepiej>`_
* Bug fixes for query_generator `#1292 <https://github.com/great-expectations/great_expectations/issues/1292>`_ thanks `@ian-whitestone <https://github.com/ian-whitestone>`_

0.9.10
-----------------
* Data Docs: improve configurability of site_section_builders
* TupleFilesystemStoreBackend now ignore `.ipynb_checkpoints` directories `#1203 <https://github.com/great-expectations/great_expectations/issues/1203>`_
* bugfix for Data Docs links encoding on S3 `#1235 <https://github.com/great-expectations/great_expectations/issues/1235>`_

0.9.9
-----------------
* Allow evaluation parameters support in run_validation_operator
* Add log_level parameter to jupyter_ux.setup_notebook_logging.
* Add experimental display_profiled_column_evrs_as_section and display_column_evrs_as_section methods, with a minor (nonbreaking) refactor to create a new _render_for_jupyter method.
* Allow selection of site in UpdateDataDocsAction with new arg target_site_names in great_expectations.yml
* Fix issue with regular expression support in BigQuery (#1244)

0.9.8
-----------------
* Allow basic operations in evaluation parameters, with or without evaluation parameters.
* When unexpected exceptions occur (e.g., during data docs rendering), the user will see detailed error messages, providing information about the specific issue as well as the stack trace.
* Remove the "project new" option from the command line (since it is not implemented; users can only run "init" to create a new project).
* Update type detection for bigquery based on driver changes in pybigquery driver 0.4.14. Added a warning for users who are running an older pybigquery driver
* added execution tests to the NotebookRenderer to mitigate codegen risks
* Add option "persist", true by default, for SparkDFDataset to persist the DataFrame it is passed. This addresses #1133 in a deeper way (thanks @tejsvirai for the robust debugging support and reproduction on spark).

  * Disabling this option should *only* be done if the user has *already* externally persisted the DataFrame, or if the dataset is too large to persist but *computations are guaranteed to be stable across jobs*.

* Enable passing dataset kwargs through datasource via dataset_options batch_kwarg.
* Fix AttributeError when validating expectations from a JSON file
* Data Docs: fix bug that was causing erratic scrolling behavior when table of contents contains many columns
* Data Docs: add ability to hide how-to buttons and related content in Data Docs

0.9.7
-----------------
* Update marshmallow dependency to >3. NOTE: as of this release, you MUST use marshamllow >3.0, which REQUIRES python 3. (`#1187 <https://github.com/great-expectations/great_expectations/issues/1187>`_) @jcampbell

  * Schema checking is now stricter for expectation suites, and data_asset_name must not be present as a top-level key in expectation suite json. It is safe to remove.
  * Similarly, datasource configuration must now adhere strictly to the required schema, including having any required credentials stored in the "credentials" dictionary.

* New beta CLI command: `tap new` that generates an executable python file to expedite deployments. (`#1193 <https://github.com/great-expectations/great_expectations/issues/1193>`_) @Aylr
* bugfix in TableBatchKwargsGenerator docs
* Added feature maturity in README (`#1203 <https://github.com/great-expectations/great_expectations/issues/1203>`_) @kyleaton
* Fix failing test that should skip if postgresql not running (`#1199 <https://github.com/great-expectations/great_expectations/issues/1199>`_) @cicdw


0.9.6
-----------------
* validate result dict when instantiating an ExpectationValidationResult (`#1133 <https://github.com/great-expectations/great_expectations/issues/1133>`_)
* DataDocs: Expectation Suite name on Validation Result pages now link to Expectation Suite page
* `great_expectations init`: cli now asks user if csv has header when adding a Spark Datasource with csv file
* Improve support for using GCP Storage Bucket as a Data Docs Site backend (thanks @hammadzz)
* fix notebook renderer handling for expectations with no column kwarg and table not in their name (`#1194 <https://github.com/great-expectations/great_expectations/issues/1194>`_)


0.9.5
-----------------
* Fixed unexpected behavior with suite edit, data docs and jupyter
* pytest pinned to 5.3.5


0.9.4
-----------------
* Update CLI `init` flow to support snowflake transient tables
* Use filename for default expectation suite name in CLI `init`
* Tables created by SqlAlchemyDataset use a shorter name with 8 hex characters of randomness instead of a full uuid
* Better error message when config substitution variable is missing
* removed an unused directory in the GE folder
* removed obsolete config error handling
* Docs typo fixes
* Jupyter notebook improvements
* `great_expectations init` improvements
* Simpler messaging in validation notebooks
* replaced hacky loop with suite list call in notebooks
* CLI suite new now supports `--empty` flag that generates an empty suite and opens a notebook
* add error handling to `init` flow for cases where user tries using a broken file


0.9.3
-----------------
* Add support for transient table creation in snowflake (#1012)
* Improve path support in TupleStoreBackend for better cross-platform compatibility
* New features on `ExpectationSuite`

  - ``add_citation()``
  - ``get_citations()``

* `SampleExpectationsDatasetProfiler` now leaves a citation containing the original batch kwargs
* `great_expectations suite edit` now uses batch_kwargs from citations if they exist
* Bugfix :: suite edit notebooks no longer blow away the existing suite while loading a batch of data
* More robust and tested logic in `suite edit`
* DataDocs: bugfixes and improvements for smaller viewports
* Bugfix :: fix for bug that crashes SampleExpectationsDatasetProfiler if unexpected_percent is of type decimal.Decimal (`#1109 <https://github.com/great-expectations/great_expectations/issues/1109>`_)


0.9.2
-----------------
* Fixes #1095
* Added a `list_expectation_suites` function to `data_context`, and a corresponding CLI function - `suite list`.
* CI no longer enforces legacy python tests.

0.9.1
------
* Bugfix for dynamic "How to Edit This Expectation Suite" command in DataDocs

0.9.0
-----------------

Version 0.9.0 is a major update to Great Expectations! The DataContext has continued to evolve into a powerful tool
for ensuring that Expectation Suites can properly represent the way users think about their data, and upgrading will
make it much easier to store and share expectation suites, and to build data docs that support your whole team.
You’ll get awesome new features including improvements to data docs look and the ability to choose and store metrics
for building flexible data quality dashboards.

The changes for version 0.9.0 fall into several broad areas:

1. Onboarding

Release 0.9.0 of Great Expectations makes it much easier to get started with the project. The `init` flow has grown
to support a much wider array of use cases and to use more natural language rather than introducing
GreatExpectations concepts earlier. You can more easily configure different backends and datasources, take advantage
of guided walkthroughs to find and profile data, and share project configurations with colleagues.

If you have already completed the `init` flow using a previous version of Great Expectations, you do not need to
rerun the command. However, **there are some small changes to your configuration that will be required**. See
:ref:`migrating_versions` for details.

2. CLI Command Improvements

With this release we have introduced a consistent naming pattern for accessing subcommands based on the noun (a
Great Expectations object like `suite` or `docs`) and verb (an action like `edit` or `new`). The new user experience
will allow us to more naturally organize access to CLI tools as new functionality is added.

3. Expectation Suite Naming and Namespace Changes

Defining shared expectation suites and validating data from different sources is much easier in this release. The
DataContext, which manages storage and configuration of expectations, validations, profiling, and data docs, no
longer requires that expectation suites live in a datasource-specific “namespace.” Instead, you should name suites
with the logical name corresponding to your data, making it easy to share them or validate against different data
sources. For example, the expectation suite "npi" for National Provider Identifier data can now be shared across
teams who access the same logical data in local systems using Pandas, on a distributed Spark cluster, or via a
relational database.

Batch Kwargs, or instructions for a datasource to build a batch of data, are similarly freed from a required
namespace, and you can more easily integrate Great Expectations into workflows where you do not need to use a
BatchKwargsGenerator (usually because you have a batch of data ready to validate, such as in a table or a known
directory).

The most noticeable impact of this API change is in the complete removal of the DataAssetIdentifier class. For
example, the `create_expectation_suite` and `get_batch` methods now no longer require a data_asset_name parameter,
relying only on the expectation_suite_name and batch_kwargs to do their job. Similarly, there is no more asset name
normalization required. See the upgrade guide for more information.

4. Metrics and Evaluation Parameter Stores

Metrics have received much more love in this release of Great Expectations! We've improved the system for declaring
evaluation parameters that support dependencies between different expectation suites, so you can easily identify a
particular field in the result of one expectation to use as the input into another. And the MetricsStore is now much
more flexible, supporting a new ValidationAction that makes it possible to select metrics from a validation result
to be saved in a database where they can power a dashboard.

5. Internal Type Changes and Improvements

Finally, in this release, we have done a lot of work under the hood to make things more robust, including updating
all of the internal objects to be more strongly typed. That change, while largely invisible to end users, paves the
way for some really exciting opportunities for extending Great Expectations as we build a bigger community around
the project.


We are really excited about this release, and encourage you to upgrade right away to take advantage of the more
flexible naming and simpler API for creating, accessing, and sharing your expectations. As always feel free to join
us on Slack for questions you don't see addressed!


0.8.9__develop
-----------------


0.8.8
-----------------
* Add support for allow_relative_error to expect_column_quantile_values_to_be_between, allowing Redshift users access
  to this expectation
* Add support for checking backend type information for datetime columns using expect_column_min_to_be_between and
  expect_column_max_to_be_between

0.8.7
-----------------
* Add support for expect_column_values_to_be_of_type for BigQuery backend (#940)
* Add image CDN for community usage stats
* Documentation improvements and fixes

0.8.6
-----------------
* Raise informative error if config variables are declared but unavailable
* Update ExpectationsStore defaults to be consistent across all FixedLengthTupleStoreBackend objects
* Add support for setting spark_options via SparkDFDatasource
* Include tail_weights by default when using build_continuous_partition_object
* Fix Redshift quantiles computation and type detection
* Allow boto3 options to be configured (#887)

0.8.5
-----------------
* BREAKING CHANGE: move all reader options from the top-level batch_kwargs object to a sub-dictionary called
  "reader_options" for SparkDFDatasource and PandasDatasource. This means it is no longer possible to specify
  supplemental reader-specific options at the top-level of `get_batch`,  `yield_batch_kwargs` or `build_batch_kwargs`
  calls, and instead, you must explicitly specify that they are reader_options, e.g. by a call such as:
  `context.yield_batch_kwargs(data_asset_name, reader_options={'encoding': 'utf-8'})`.
* BREAKING CHANGE: move all query_params from the top-level batch_kwargs object to a sub-dictionary called
  "query_params" for SqlAlchemyDatasource. This means it is no longer possible to specify supplemental query_params at
  the top-level of `get_batch`,  `yield_batch_kwargs` or `build_batch_kwargs`
  calls, and instead, you must explicitly specify that they are query_params, e.g. by a call such as:
  `context.yield_batch_kwargs(data_asset_name, query_params={'schema': 'foo'})`.
* Add support for filtering validation result suites and validation result pages to show only failed expectations in
  generated documentation
* Add support for limit parameter to batch_kwargs for all datasources: Pandas, SqlAlchemy, and SparkDF; add support
  to generators to support building batch_kwargs with limits specified.
* Include raw_query and query_params in query_generator batch_kwargs
* Rename generator keyword arguments from data_asset_name to generator_asset to avoid ambiguity with normalized names
* Consistently migrate timestamp from batch_kwargs to batch_id
* Include batch_id in validation results
* Fix issue where batch_id was not included in some generated datasets
* Fix rendering issue with expect_table_columns_to_match_ordered_list expectation
* Add support for GCP, including BigQuery and GCS
* Add support to S3 generator for retrieving directories by specifying the `directory_assets` configuration
* Fix warning regarding implicit class_name during init flow
* Expose build_generator API publicly on datasources
* Allow configuration of known extensions and return more informative message when SubdirReaderBatchKwargsGenerator cannot find
  relevant files.
* Add support for allow_relative_error on internal dataset quantile functions, and add support for
  build_continuous_partition_object in Redshift
* Fix truncated scroll bars in value_counts graphs


0.8.4.post0
----------------
* Correct a packaging issue resulting in missing notebooks in tarball release; update docs to reflect new notebook
  locations.


0.8.4
-----------------
* Improved the tutorials that walk new users through the process of creating expectations and validating data
* Changed the flow of the init command - now it creates the scaffolding of the project and adds a datasource. After
  that users can choose their path.
* Added a component with links to useful tutorials to the index page of the Data Docs website
* Improved the UX of adding a SQL datasource in the CLI - now the CLI asks for specific credentials for Postgres,
  MySQL, Redshift and Snowflake, allows continuing debugging in the config file and has better error messages
* Added batch_kwargs information to DataDocs validation results
* Fix an issue affecting file stores on Windows


0.8.3
-----------------
* Fix a bug in data-docs' rendering of mostly parameter
* Correct wording for expect_column_proportion_of_unique_values_to_be_between
* Set charset and meta tags to avoid unicode decode error in some browser/backend configurations
* Improve formatting of empirical histograms in validation result data docs
* Add support for using environment variables in `config_variables_file_path`
* Documentation improvements and corrections


0.8.2.post0
------------
* Correct a packaging issue resulting in missing css files in tarball release


0.8.2
-----------------
* Add easier support for customizing data-docs css
* Use higher precision for rendering 'mostly' parameter in data-docs; add more consistent locale-based
  formatting in data-docs
* Fix an issue causing visual overlap of large numbers of validation results in build-docs index
* Documentation fixes (thanks @DanielOliver!) and improvements
* Minor CLI wording fixes
* Improved handling of MySql temporary tables
* Improved detection of older config versions


0.8.1
-----------------
* Fix an issue where version was reported as '0+unknown'


0.8.0
-----------------

Version 0.8.0 is a significant update to Great Expectations, with many improvements focused on configurability
and usability.  See the :ref:`migrating_versions` guide for more details on specific changes, which include
several breaking changes to configs and APIs.

Highlights include:

1. Validation Operators and Actions. Validation operators make it easy to integrate GE into a variety of pipeline runners. They
   offer one-line integration that emphasizes configurability. See the :ref:`validation_operators_and_actions`
   feature guide for more information.

   - The DataContext `get_batch` method no longer treats `expectation_suite_name` or `batch_kwargs` as optional; they
     must be explicitly specified.
   - The top-level GE validate method allows more options for specifying the specific data_asset class to use.

2. First-class support for plugins in a DataContext, with several features that make it easier to configure and
   maintain DataContexts across common deployment patterns.

   - **Environments**: A DataContext can now manage :ref:`environment_and_secrets` more easily thanks to more dynamic and
     flexible variable substitution.
   - **Stores**: A new internal abstraction for DataContexts, :ref:`Stores <reference__core_concepts__data_context__stores>`, make extending GE easier by
     consolidating logic for reading and writing resources from a database, local, or cloud storage.
   - **Types**: Utilities configured in a DataContext are now referenced using `class_name` and `module_name` throughout
     the DataContext configuration, making it easier to extend or supplement pre-built resources. For now, the "type"
     parameter is still supported but expect it to be removed in a future release.

3. Partitioners: Batch Kwargs are clarified and enhanced to help easily reference well-known chunks of data using a
   partition_id. Batch ID and Batch Fingerprint help round out support for enhanced metadata around data
   assets that GE validates. See :ref:`Batch Identifiers <reference__core_concepts__batch_parameters>` for more information. The `GlobReaderBatchKwargsGenerator`,
   `QueryBatchKwargsGenerator`, `S3GlobReaderBatchKwargsGenerator`, `SubdirReaderBatchKwargsGenerator`, and `TableBatchKwargsGenerator` all support partition_id for
   easily accessing data assets.

4. Other Improvements:

   - We're beginning a long process of some under-the-covers refactors designed to make GE more maintainable as we
     begin adding additional features.
   - Restructured documentation: our docs have a new structure and have been reorganized to provide space for more
     easily adding and accessing reference material. Stay tuned for additional detail.
   - The command build-documentation has been renamed build-docs and now by
     default opens the Data Docs in the users' browser.

v0.7.11
-----------------
* Fix an issue where head() lost the column name for SqlAlchemyDataset objects with a single column
* Fix logic for the 'auto' bin selection of `build_continuous_partition_object`
* Add missing jinja2 dependency
* Fix an issue with inconsistent availability of strict_min and strict_max options on expect_column_values_to_be_between
* Fix an issue where expectation suite evaluation_parameters could be overridden by values during validate operation


v0.7.10
-----------------
* Fix an issue in generated documentation where the Home button failed to return to the index
* Add S3 Generator to module docs and improve module docs formatting
* Add support for views to QueryBatchKwargsGenerator
* Add success/failure icons to index page
* Return to uniform histogram creation during profiling to avoid large partitions for internal performance reasons


v0.7.9
-----------------
* Add an S3 generator, which will introspect a configured bucket and generate batch_kwargs from identified objects
* Add support to PandasDatasource and SparkDFDatasource for reading directly from S3
* Enhance the Site Index page in documentation so that validation results are sorted and display the newest items first
  when using the default run-id scheme
* Add a new utility method, `build_continuous_partition_object` which will build partition objects using the dataset
  API and so supports any GE backend.
* Fix an issue where columns with spaces in their names caused failures in some SqlAlchemyDataset and SparkDFDataset
  expectations
* Fix an issue where generated queries including null checks failed on MSSQL (#695)
* Fix an issue where evaluation parameters passed in as a set instead of a list could cause JSON serialization problems
  for the result object (#699)


v0.7.8
-----------------
* BREAKING: slack webhook URL now must be in the profiles.yml file (treat as a secret)
* Profiler improvements:

  - Display candidate profiling data assets in alphabetical order
  - Add columns to the expectation_suite meta during profiling to support human-readable description information

* Improve handling of optional dependencies during CLI init
* Improve documentation for create_expectations notebook
* Fix several anachronistic documentation and docstring phrases (#659, #660, #668, #681; #thanks @StevenMMortimer)
* Fix data docs rendering issues:

  - documentation rendering failure from unrecognized profiled column type (#679; thanks @dinedal))
  - PY2 failure on encountering unicode (#676)


0.7.7
-----------------
* Standardize the way that plugin module loading works. DataContext will begin to use the new-style class and plugin
  identification moving forward; yml configs should specify class_name and module_name (with module_name optional for
  GE types). For now, it is possible to use the "type" parameter in configuration (as before).
* Add support for custom data_asset_type to all datasources
* Add support for strict_min and strict_max to inequality-based expectations to allow strict inequality checks
  (thanks @RoyalTS!)
* Add support for reader_method = "delta" to SparkDFDatasource
* Fix databricks generator (thanks @sspitz3!)
* Improve performance of DataContext loading by moving optional import
* Fix several memory and performance issues in SparkDFDataset.

  - Use only distinct value count instead of bringing values to driver
  - Migrate away from UDF for set membership, nullity, and regex expectations

* Fix several UI issues in the data_documentation

  - Move prescriptive dataset expectations to Overview section
  - Fix broken link on Home breadcrumb
  - Scroll follows navigation properly
  - Improved flow for long items in value_set
  - Improved testing for ValidationRenderer
  - Clarify dependencies introduced in documentation sites
  - Improve testing and documentation for site_builder, including run_id filter
  - Fix missing header in Index page and cut-off tooltip
  - Add run_id to path for validation files


0.7.6
-----------------
* New Validation Renderer! Supports turning validation results into HTML and displays differences between the expected
  and the observed attributes of a dataset.
* Data Documentation sites are now fully configurable; a data context can be configured to generate multiple
  sites built with different GE objects to support a variety of data documentation use cases. See data documentation
  guide for more detail.
* CLI now has a new top-level command, `build-documentation` that can support rendering documentation for specified
  sites and even named data assets in a specific site.
* Introduced DotDict and LooselyTypedDotDict classes that allow to enforce typing of dictionaries.
* Bug fixes: improved internal logic of rendering data documentation, slack notification, and CLI profile command when
  datasource argument was not provided.

0.7.5
-----------------
* Fix missing requirement for pypandoc brought in from markdown support for notes rendering.

0.7.4
-----------------
* Fix numerous rendering bugs and formatting issues for rendering documentation.
* Add support for pandas extension dtypes in pandas backend of expect_column_values_to_be_of_type and
  expect_column_values_to_be_in_type_list and fix bug affecting some dtype-based checks.
* Add datetime and boolean column-type detection in BasicDatasetProfiler.
* Improve BasicDatasetProfiler performance by disabling interactive evaluation when output of expectation is not
  immediately used for determining next expectations in profile.
* Add support for rendering expectation_suite and expectation_level notes from meta in docs.
* Fix minor formatting issue in readthedocs documentation.

0.7.3
-----------------
* BREAKING: Harmonize expect_column_values_to_be_of_type and expect_column_values_to_be_in_type_list semantics in
  Pandas with other backends, including support for None type and type_list parameters to support profiling.
  *These type expectations now rely exclusively on native python or numpy type names.*
* Add configurable support for Custom DataAsset modules to DataContext
* Improve support for setting and inheriting custom data_asset_type names
* Add tooltips with expectations backing data elements to rendered documentation
* Allow better selective disabling of tests (thanks @RoyalITS)
* Fix documentation build errors causing missing code blocks on readthedocs
* Update the parameter naming system in DataContext to reflect data_asset_name *and* expectation_suite_name
* Change scary warning about discarding expectations to be clearer, less scary, and only in log
* Improve profiler support for boolean types, value_counts, and type detection
* Allow user to specify data_assets to profile via CLI
* Support CLI rendering of expectation_suite and EVR-based documentation

0.7.2
-----------------
* Improved error detection and handling in CLI "add datasource" feature
* Fixes in rendering of profiling results (descriptive renderer of validation results)
* Query Generator of SQLAlchemy datasource adds tables in non-default schemas to the data asset namespace
* Added convenience methods to display HTML renderers of sections in Jupyter notebooks
* Implemented prescriptive rendering of expectations for most expectation types

0.7.1
------------

* Added documentation/tutorials/videos for onboarding and new profiling and documentation features
* Added prescriptive documentation built from expectation suites
* Improved index, layout, and navigation of data context HTML documentation site
* Bug fix: non-Python files were not included in the package
* Improved the rendering logic to gracefully deal with failed expectations
* Improved the basic dataset profiler to be more resilient
* Implement expect_column_values_to_be_of_type, expect_column_values_to_be_in_type_list for SparkDFDataset
* Updated CLI with a new documentation command and improved profile and render commands
* Expectation suites and validation results within a data context are saved in a more readable form (with indentation)
* Improved compatibility between SparkDatasource and InMemoryGenerator
* Optimization for Pandas column type checking
* Optimization for Spark duplicate value expectation (thanks @orenovadia!)
* Default run_id format no longer includes ":" and specifies UTC time
* Other internal improvements and bug fixes


0.7.0
------------

Version 0.7 of Great Expectations is HUGE. It introduces several major new features
and a large number of improvements, including breaking API changes.

The core vocabulary of expectations remains consistent. Upgrading to
the new version of GE will primarily require changes to code that
uses data contexts; existing expectation suites will require only changes
to top-level names.

 * Major update of Data Contexts. Data Contexts now offer significantly \
   more support for building and maintaining expectation suites and \
   interacting with existing pipeline systems, including providing a namespace for objects.\
   They can handle integrating, registering, and storing validation results, and
   provide a namespace for data assets, making **batches** first-class citizens in GE.
   Read more: :ref:`data_context` or :py:mod:`great_expectations.data_context`

 * Major refactor of autoinspect. Autoinspect is now built around a module
   called "profile" which provides a class-based structure for building
   expectation suites. There is no longer a default  "autoinspect_func" --
   calling autoinspect requires explicitly passing the desired profiler. See :ref:`profiling`

 * New "Compile to Docs" feature produces beautiful documentation from expectations and expectation
   validation reports, helping keep teams on the same page.

 * Name clarifications: we've stopped using the overloaded terms "expectations
   config" and "config" and instead use "expectation suite" to refer to a
   collection (or suite!) of expectations that can be used for validating a
   data asset.

   - Expectation Suites include several top level keys that are useful \
     for organizing content in a data context: data_asset_name, \
     expectation_suite_name, and data_asset_type. When a data_asset is \
     validated, those keys will be placed in the `meta` key of the \
     validation result.

 * Major enhancement to the CLI tool including `init`, `render` and more flexibility with `validate`

 * Added helper notebooks to make it easy to get started. Each notebook acts as a combination of \
   tutorial and code scaffolding, to help you quickly learn best practices by applying them to \
   your own data.

 * Relaxed constraints on expectation parameter values, making it possible to declare many column
   aggregate expectations in a way that is always "vacuously" true, such as
   ``expect_column_values_to_be_between`` ``None`` and ``None``. This makes it possible to progressively
   tighten expectations while using them as the basis for profiling results and documentation.

  * Enabled caching on dataset objects by default.

 * Bugfixes and improvements:

   * New expectations:

     * expect_column_quantile_values_to_be_between
     * expect_column_distinct_values_to_be_in_set

   * Added support for ``head`` method on all current backends, returning a PandasDataset
   * More implemented expectations for SparkDF Dataset with optimizations

     * expect_column_values_to_be_between
     * expect_column_median_to_be_between
     * expect_column_value_lengths_to_be_between

   * Optimized histogram fetching for SqlalchemyDataset and SparkDFDataset
   * Added cross-platform internal partition method, paving path for improved profiling
   * Fixed bug with outputstrftime not being honored in PandasDataset
   * Fixed series naming for column value counts
   * Standardized naming for expect_column_values_to_be_of_type
   * Standardized and made explicit use of sample normalization in stdev calculation
   * Added from_dataset helper
   * Internal testing improvements
   * Documentation reorganization and improvements
   * Introduce custom exceptions for more detailed error logs

0.6.1
------------
* Re-add testing (and support) for py2
* NOTE: Support for SqlAlchemyDataset and SparkDFDataset is enabled via optional install \
  (e.g. ``pip install great_expectations[sqlalchemy]`` or ``pip install great_expectations[spark]``)

0.6.0
------------
* Add support for SparkDFDataset and caching (HUGE work from @cselig)
* Migrate distributional expectations to new testing framework
* Add support for two new expectations: expect_column_distinct_values_to_contain_set
  and expect_column_distinct_values_to_equal_set (thanks @RoyalTS)
* FUTURE BREAKING CHANGE: The new cache mechanism for Datasets, \
  when enabled, causes GE to assume that dataset does not change between evaluation of individual expectations. \
  We anticipate this will become the future default behavior.
* BREAKING CHANGE: Drop official support pandas < 0.22

0.5.1
---------------
* **Fix** issue where no result_format available for expect_column_values_to_be_null caused error
* Use vectorized computation in pandas (#443, #445; thanks @RoyalTS)


0.5.0
----------------
* Restructured class hierarchy to have a more generic DataAsset parent that maintains expectation logic separate \
  from the tabular organization of Dataset expectations
* Added new FileDataAsset and associated expectations (#416 thanks @anhollis)
* Added support for date/datetime type columns in some SQLAlchemy expectations (#413)
* Added support for a multicolumn expectation, expect multicolumn values to be unique (#408)
* **Optimization**: You can now disable `partial_unexpected_counts` by setting the `partial_unexpected_count` value to \
  0 in the result_format argument, and we do not compute it when it would not be returned. (#431, thanks @eugmandel)
* **Fix**: Correct error in unexpected_percent computations for sqlalchemy when unexpected values exceed limit (#424)
* **Fix**: Pass meta object to expectation result (#415, thanks @jseeman)
* Add support for multicolumn expectations, with `expect_multicolumn_values_to_be_unique` as an example (#406)
* Add dataset class to from_pandas to simplify using custom datasets (#404, thanks @jtilly)
* Add schema support for sqlalchemy data context (#410, thanks @rahulj51)
* Minor documentation, warning, and testing improvements (thanks @zdog).


0.4.5
----------------
* Add a new autoinspect API and remove default expectations.
* Improve details for expect_table_columns_to_match_ordered_list (#379, thanks @rlshuhart)
* Linting fixes (thanks @elsander)
* Add support for dataset_class in from_pandas (thanks @jtilly)
* Improve redshift compatibility by correcting faulty isnull operator (thanks @avanderm)
* Adjust partitions to use tail_weight to improve JSON compatibility and
  support special cases of KL Divergence (thanks @anhollis)
* Enable custom_sql datasets for databases with multiple schemas, by
  adding a fallback for column reflection (#387, thanks @elsander)
* Remove `IF NOT EXISTS` check for custom sql temporary tables, for
  Redshift compatibility (#372, thanks @elsander)
* Allow users to pass args/kwargs for engine creation in
  SqlAlchemyDataContext (#369, thanks @elsander)
* Add support for custom schema in SqlAlchemyDataset (#370, thanks @elsander)
* Use getfullargspec to avoid deprecation warnings.
* Add expect_column_values_to_be_unique to SqlAlchemyDataset
* **Fix** map expectations for categorical columns (thanks @eugmandel)
* Improve internal testing suite (thanks @anhollis and @ccnobbli)
* Consistently use value_set instead of mixing value_set and values_set (thanks @njsmith8)

0.4.4
----------------
* Improve CLI help and set CLI return value to the number of unmet expectations
* Add error handling for empty columns to SqlAlchemyDataset, and associated tests
* **Fix** broken support for older pandas versions (#346)
* **Fix** pandas deepcopy issue (#342)

0.4.3
-------
* Improve type lists in expect_column_type_to_be[_in_list] (thanks @smontanaro and @ccnobbli)
* Update cli to use entry_points for conda compatibility, and add version option to cli
* Remove extraneous development dependency to airflow
* Address SQlAlchemy warnings in median computation
* Improve glossary in documentation
* Add 'statistics' section to validation report with overall validation results (thanks @sotte)
* Add support for parameterized expectations
* Improve support for custom expectations with better error messages (thanks @syk0saje)
* Implement expect_column_value_lenghts_to_[be_between|equal] for SQAlchemy (thanks @ccnobbli)
* **Fix** PandasDataset subclasses to inherit child class

0.4.2
-------
* **Fix** bugs in expect_column_values_to_[not]_be_null: computing unexpected value percentages and handling all-null (thanks @ccnobbli)
* Support mysql use of Decimal type (thanks @bouke-nederstigt)
* Add new expectation expect_column_values_to_not_match_regex_list.

  * Change behavior of expect_column_values_to_match_regex_list to use python re.findall in PandasDataset, relaxing \
    matching of individuals expressions to allow matches anywhere in the string.

* **Fix** documentation errors and other small errors (thanks @roblim, @ccnobbli)

0.4.1
-------
* Correct inclusion of new data_context module in source distribution

0.4.0
-------
* Initial implementation of data context API and SqlAlchemyDataset including implementations of the following \
  expectations:

  * expect_column_to_exist
  * expect_table_row_count_to_be
  * expect_table_row_count_to_be_between
  * expect_column_values_to_not_be_null
  * expect_column_values_to_be_null
  * expect_column_values_to_be_in_set
  * expect_column_values_to_be_between
  * expect_column_mean_to_be
  * expect_column_min_to_be
  * expect_column_max_to_be
  * expect_column_sum_to_be
  * expect_column_unique_value_count_to_be_between
  * expect_column_proportion_of_unique_values_to_be_between

* Major refactor of output_format to new result_format parameter. See docs for full details:

  * exception_list and related uses of the term exception have been renamed to unexpected
  * Output formats are explicitly hierarchical now, with BOOLEAN_ONLY < BASIC < SUMMARY < COMPLETE. \
    All *column_aggregate_expectation* expectations now return element count and related information included at the \
    BASIC level or higher.

* New expectation available for parameterized distributions--\
  expect_column_parameterized_distribution_ks_test_p_value_to_be_greater_than (what a name! :) -- (thanks @ccnobbli)
* ge.from_pandas() utility (thanks @schrockn)
* Pandas operations on a PandasDataset now return another PandasDataset (thanks @dlwhite5)
* expect_column_to_exist now takes a column_index parameter to specify column order (thanks @louispotok)
* Top-level validate option (ge.validate())
* ge.read_json() helper (thanks @rjurney)
* Behind-the-scenes improvements to testing framework to ensure parity across data contexts.
* Documentation improvements, bug-fixes, and internal api improvements

0.3.2
-------
* Include requirements file in source dist to support conda

0.3.1
--------
* **Fix** infinite recursion error when building custom expectations
* Catch dateutil parsing overflow errors

0.2
-----
* Distributional expectations and associated helpers are improved and renamed to be more clear regarding the tests they apply
* Expectation decorators have been refactored significantly to streamline implementing expectations and support custom expectations
* API and examples for custom expectations are available
* New output formats are available for all expectations
* Significant improvements to test suite and compatibility
