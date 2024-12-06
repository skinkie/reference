[
  {
    "block": "at",
    "scripts": [
        {"script": "clean_tmp", "args": "%%dir%%"},
        {"script": "netex_to_db.py", "args": "--log=%%log%% ./aux_test_input/at-test.zip %%dir%%/netex-import.duckdb"},
        {"script": "epip_db_to_db.py", "args": "--log=%%log%% %%dir%%/netex-import.duckdb %%dir%%/netex-database.duckdb"},
        {"script": "epip_db_to_xml.py", "args": "--log=%%log%% %%dir%%/netex-import.duckdb %%dir%%/netex-database.duckdb %%dir%%/%%block%%-netex.xml"},
        {"script": "aux_assertions.py", "args": "--log=%%log%% ./aux_test_input/at-assertions.txt %%dir%%/%%block%%-netex.xml"},
        {"script": "aux_netex_stats.py", "args": "--log=%%log%% %%dir%%/%%block%%-netex.xml"},
        {"script": "netex_to_db.py", "args": "--log=%%log%% %%dir%%/%%block%%-netex.xml %%dir%%/netex-database.duckdb"},
        {"script": "netex_db_to_gtfs.py", "args": "--log=%%log%% %%dir%%/netex-database.duckdb %%dir%%/%%block%%-gtfs.zip"},
        {"script": "aux_gtfs_check.py", "args": "--log=%%log%% %%dir%%/%%block%%-gtfs.zip"},
        {"script": "gtfs_show_map.py", "args": "--log=%%log%% --limitation 100 %%dir%%/%%block%%-gtfs.zip %%dir%%/%%block%%-map.html"}
        ]
  },
    {
    "block": "at1",
    "scripts": [
        {"script": "clean_tmp", "args": "%%dir%%"},
        {"script": "netex_to_db.py", "args": "--log=%%log%% ./aux_test_input/20240918-2247_netex_vmobil_2024.zip %%dir%%/netex-import.duckdb"},
        {"script": "epip_db_to_db.py", "args": "--log=%%log%% %%dir%%/netex-import.duckdb %%dir%%/netex-database.duckdb"},
        {"script": "epip_db_to_xml.py", "args": "--log=%%log%% %%dir%%/netex-import.duckdb %%dir%%/netex-database.duckdb %%dir%%/%%block%%-netex.xml"},
        {"script": "aux_assertions.py", "args": "--log=%%log%% ./aux_test_input/at-assertions.txt %%dir%%/%%block%%-netex.xml"},
        {"script": "aux_netex_stats.py", "args": "--log=%%log%% %%dir%%/%%block%%-netex.xml"},
        {"script": "netex_to_db.py", "args": "--log=%%log%% %%dir%%/%%block%%-netex.xml %%dir%%/netex-database.duckdb"},
        {"script": "netex_db_to_gtfs.py", "args": "--log=%%log%% %%dir%%/netex-database.duckdb %%dir%%/%%block%%-gtfs.zip"},
        {"script": "aux_gtfs_check.py", "args": "--log=%%log%% %%dir%%/%%block%%-gtfs.zip"},
        {"script": "gtfs_show_map.py", "args": "--log=%%log%% --limitation 100 %%dir%%/%%block%%-gtfs.zip %%dir%%/%%block%%-map.html"}
        ]
  },
    {
    "block": "trenitalia",
    "scripts": [
        {"script": "clean_tmp", "args": "%%dir%%"},
        {"script": "netex_to_db.py", "args": "--log=%%log%% ./aux_test_input/trenitalia.zip %%dir%%/netex-import.duckdb"},
        {"script": "epip_db_to_db.py", "args": "--log=%%log%% %%dir%%/netex-import.duckdb %%dir%%/netex-database.duckdb"},
        {"script": "epip_db_to_xml.py", "args": "--log=%%log%% %%dir%%/netex-import.duckdb %%dir%%/netex-database.duckdb %%dir%%/%%block%%-netex.xml"},
        {"script": "aux_assertions.py", "args": "--log=%%log%% ./aux_test_input/general-netex-assertions.txt %%dir%%/%%block%%-netex.xml"},
        {"script": "aux_netex_stats.py", "args": "--log=%%log%% %%dir%%/%%block%%-netex.xml"},
        {"script": "netex_to_db.py", "args": "--log=%%log%% %%dir%%/%%block%%-netex.xml %%dir%%/netex-database.duckdb"},
        {"script": "netex_db_to_gtfs.py", "args": "--log=%%log%% %%dir%%/netex-database.duckdb %%dir%%/%%block%%-gtfs.zip"},
        {"script": "gtfs_show_map.py", "args": "--log=%%log%% --limitation 100 %%dir%%/%%block%%-gtfs.zip %%dir%%/%%block%%-map.html"}
        ]
  },
    {
    "block": "soleanetex",
    "url": "https://transport.data.gouv.fr/datasets/fr-200052264-t0014-0000-1",
    "scripts": [
        {"script": "clean_tmp", "args": "%%dir%%"},
        {"script": "netex_to_db.py", "args": "--log=%%log%% ./aux_test_input/fluo-grand-est-sitram-netex.zip %%dir%%/netex-import.duckdb"},
        {"script": "epip_db_to_db.py", "args": "--log=%%log%% %%dir%%/netex-import.duckdb %%dir%%/netex-database.duckdb"},
        {"script": "epip_db_to_xml.py", "args": "--log=%%log%% %%dir%%/netex-import.duckdb %%dir%%/netex-database.duckdb %%dir%%/%%block%%-netex.xml"},
        {"script": "aux_assertions.py", "args": "--log=%%log%% ./aux_test_input/general-netex-assertions.txt %%dir%%/%%block%%-netex.xml"},
        {"script": "aux_netex_stats.py", "args": "--log=%%log%% %%dir%%/%%block%%-netex.xml"},
        {"script": "netex_to_db.py", "args": "--log=%%log%% %%dir%%/%%block%%-netex.xml %%dir%%/netex-database.duckdb"},
        {"script": "netex_db_to_gtfs.py", "args": "--log=%%log%% %%dir%%/netex-database.duckdb %%dir%%/%%block%%-gtfs.zip"},
        {"script": "gtfs_show_map.py", "args": "--log=%%log%% --limitation 100 %%dir%%/%%block%%-gtfs.zip %%dir%%/%%block%%-map.html"}
        ]
  },
     {
    "block": "soleanetex1",
    "url": "https://transport.data.gouv.fr/datasets/fr-200052264-t0014-0000-1",
    "scripts": [
        {"script": "clean_tmp", "args": "%%dir%%"},
        {"script": "netex_to_db.py", "args": "--log=%%log%% ./aux_test_input/fluo-grand-est-sitram-netex.zip %%dir%%/netex-import.duckdb"},
        {"script": "netex_db_to_gtfs.py", "args": "--log=%%log%% %%dir%%/netex-import.duckdb %%dir%%/%%block%%-gtfs.zip"},
        {"script": "aux_gtfs_check.py", "args": "--log=%%log%% %%dir%%/%%block%%-gtfs.zip"},
        {"script": "gtfs_show_map.py", "args": "--log=%%log%% --limitation 100 %%dir%%/%%block%%-gtfs.zip %%dir%%/%%block%%-map.html"}
        ]
  },
    {
    "block": "it2",
    "scripts": [
        {"script": "clean_tmp", "args": "%%dir%%"},
        {"script": "netex_to_db.py", "args": "--log=%%log%%./aux_test_input/it1.zip %%dir%%/netex-import.duckdb"},
        {"script": "epip_db_to_db.py", "args": "--log=%%log%% %%dir%%/netex-import.duckdb %%dir%%/netex-database.duckdb"},
        {"script": "epip_db_to_xml.py", "args": "--log=%%log%% %%dir%%/netex-import.duckdb %%dir%%/netex-database.duckdb %%dir%%/%%block%%-netex.xml"},
        {"script": "aux_assertions.py", "args": "--log=%%log%% ./aux_test_input/it-netex-assertions.txt %%dir%%/%%block%%-netex.xml"},
        {"script": "aux_netex_stats.py", "args": "--log=%%log%% %%dir%%/%%block%%-netex.xml"},
        {"script": "netex_to_db.py", "args": "--log=%%log%% %%dir%%/%%block%%-netex.xml %%dir%%/netex-database.duckdb"},
        {"script": "netex_db_to_gtfs.py", "args": "--log=%%log%% %%dir%%/netex-database.duckdb %%dir%%/%%block%%-gtfs.zip"},
        {"script": "gtfs_show_map.py", "args": "--log=%%log%% %%dir%%/%%block%%-gtfs.zip %%dir%%/%%block%%-map.html"}
        ]
  },
    {
    "block": "it3",
    "scripts": [
        {"script": "clean_tmp", "args": "%%dir%%"},
        {"script": "netex_to_db.py", "args": "--log=%%log%% ./aux_test_input/it-itc4-net_151.xml.gz %%dir%%/netex-import.duckdb"},
        {"script": "epip_db_to_db.py", "args": "--log=%%log%% %%dir%%/netex-import.duckdb %%dir%%/netex-database.duckdb"},
        {"script": "epip_db_to_xml.py", "args": "--log=%%log%% %%dir%%/netex-import.duckdb %%dir%%/netex-database.duckdb %%dir%%/%%block%%-netex.xml"},
        {"script": "aux_assertions.py", "args": "--log=%%log%% ./aux_test_input/it-netex-assertions.txt %%dir%%/%%block%%-netex.xml"},
        {"script": "aux_netex_stats.py", "args": "--log=%%log%% %%dir%%/%%block%%-netex.xml"},
        {"script": "netex_to_db.py", "args": "--log=%%log%% %%dir%%/%%block%%-netex.xml %%dir%%/netex-database.duckdb"},
        {"script": "netex_db_to_gtfs.py", "args": "--log=%%log%% %%dir%%/netex-database.duckdb %%dir%%/%%block%%-gtfs.zip"},
        {"script": "gtfs_show_map.py", "args": "--log=%%log%% %%dir%%/%%block%%-gtfs.zip %%dir%%/%%block%%-map.html"}
        ]
  },
      {
    "block": "milano",
    "scripts": [
        {"script": "clean_tmp", "args": "%%dir%%"},
        {"script": "netex_to_db.py", "args": "--log=%%log%% ./aux_test_input/milano.gz %%dir%%/netex-import.duckdb"},
        {"script": "epip_db_to_db.py", "args": "--log=%%log%% %%dir%%/netex-import.duckdb %%dir%%/netex-database.duckdb"},
        {"script": "epip_db_to_xml.py", "args": "--log=%%log%% %%dir%%/netex-import.duckdb %%dir%%/netex-database.duckdb %%dir%%/%%block%%-netex.xml"},
        {"script": "aux_assertions.py", "args": "--log=%%log%% ./aux_test_input/general-netex-assertions.txt %%dir%%/%%block%%-netex.xml"},
        {"script": "aux_netex_stats.py", "args": "--log=%%log%% %%dir%%/%%block%%-netex.xml"},
        {"script": "netex_to_db.py", "args": "--log=%%log%% %%dir%%/%%block%%-netex.xml %%dir%%/netex-database.duckdb"},
        {"script": "netex_db_to_gtfs.py", "args": "--log=%%log%% %%dir%%/netex-database.duckdb %%dir%%/%%block%%-gtfs.zip"},
        {"script": "gtfs_show_map.py", "args": "--log=%%log%% %%dir%%/%%block%%-gtfs.zip %%dir%%/%%block%%-map.html"}
        ]
  },
      {
    "block": "trenord",
    "scripts": [
        {"script": "clean_tmp", "args": "%%dir%%"},
        {"script": "netex_to_db.py", "args": "--log=%%log%% ./aux_test_input/it-itc4-trenord_336.xml %%dir%%/netex-import.duckdb"},
        {"script": "epip_db_to_db.py", "args": "--log=%%log%% %%dir%%/netex-import.duckdb %%dir%%/netex-database.duckdb"},
        {"script": "epip_db_to_xml.py", "args": "--log=%%log%% %%dir%%/netex-import.duckdb %%dir%%/netex-database.duckdb %%dir%%/%%block%%-netex.xml"},
        {"script": "aux_assertions.py", "args": "--log=%%log%% ./aux_test_input/trenord-netex-assertions.txt %%dir%%/%%block%%-netex.xml"},
        {"script": "aux_netex_stats.py", "args": "--log=%%log%% %%dir%%/%%block%%-netex.xml"},
        {"script": "netex_to_db.py", "args": "--log=%%log%% %%dir%%/%%block%%-netex.xml %%dir%%/netex-database.duckdb"},
        {"script": "netex_db_to_gtfs.py", "args": "--log=%%log%% %%dir%%/netex-database.duckdb %%dir%%/%%block%%-gtfs.zip"},
        {"script": "gtfs_show_map.py", "args": "--log=%%log%% %%dir%%/%%block%%-gtfs.zip %%dir%%/%%block%%-map.html"}
        ]
  },
  {
    "block": "sncf",
    "scripts": [
        {"script": "clean_tmp", "args": "%%dir%%"},
        {"script": "netex_to_db.py", "args": "--log=%%log%% ./aux_test_input/sncf-test.zip %%dir%%/netex-import.duckdb"},
        {"script": "epip_db_to_db.py", "args": "--log=%%log%% %%dir%%/netex-import.duckdb %%dir%%/netex-database.duckdb"},
        {"script": "epip_db_to_xml.py", "args": "--log=%%log%% %%dir%%/netex-import.duckdb %%dir%%/netex-database.duckdb %%dir%%/%%block%%-netex.xml"},
        {"script": "aux_assertions.py", "args": "--log=%%log%% ./aux_test_input/sncf-assertions.txt %%dir%%/%%block%%-netex.xml"},
        {"script": "aux_netex_stats.py", "args": "--log=%%log%% %%dir%%/%%block%%-netex.xml"},
        {"script": "netex_to_db.py", "args": "--log=%%log%% %%dir%%/%%block%%-netex.xml %%dir%%/netex-database.duckdb"},
        {"script": "netex_db_to_gtfs.py", "args": "--log=%%log%% %%dir%%/netex-database.duckdb %%dir%%/%%block%%-gtfs.zip"},
        {"script": "gtfs_show_map.py", "args": "--log=%%log%% %%dir%%/%%block%%-gtfs.zip %%dir%%/%%block%%-map.html"}
        ]
  },
 {
    "block": "sncf2",
    "scripts": [
        {"script": "clean_tmp", "args": "%%dir%%"},
        {"script": "netex_to_db.py", "args": "--log=%%log%% ./aux_test_input/export-intercites-netex-last.zip %%dir%%/netex-import.duckdb"},
        {"script": "epip_db_to_db.py", "args": "--log=%%log%% %%dir%%/netex-import.duckdb %%dir%%/netex-database.duckdb"},
        {"script": "epip_db_to_xml.py", "args": "--log=%%log%% %%dir%%/netex-import.duckdb %%dir%%/netex-database.duckdb %%dir%%/%%block%%-netex.xml"},
        {"script": "aux_assertions.py", "args": "--log=%%log%% ./aux_test_input/sncf-assertions.txt %%dir%%/%%block%%-netex.xml"},
        {"script": "aux_netex_stats.py", "args": "--log=%%log%% %%dir%%/%%block%%-netex.xml"},
        {"script": "netex_to_db.py", "args": "--log=%%log%% %%dir%%/%%block%%-netex.xml %%dir%%/netex-database.duckdb"},
        {"script": "netex_db_to_gtfs.py", "args": "--log=%%log%% %%dir%%/netex-database.duckdb %%dir%%/%%block%%-gtfs.zip"},
        {"script": "gtfs_show_map.py", "args": "--log=%%log%% %%dir%%/%%block%%-gtfs.zip %%dir%%/%%block%%-map.html"}
        ]
  },
 {
    "block": "sncf2a",
    "scripts": [
        {"script": "clean_tmp", "args": "%%dir%%"},
        {"script": "netex_to_db.py", "args": "--log=%%log%% ./aux_test_input/export-intercites-netex-last.zip %%dir%%/netex-import.duckdb"},
        {"script": "netex_db_to_gtfs.py", "args": "--log=%%log%% %%dir%%/netex-import.duckdb %%dir%%/%%block%%-gtfs.zip"},
        {"script": "gtfs_show_map.py", "args": "--log=%%log%% %%dir%%/%%block%%-gtfs.zip %%dir%%/%%block%%-map.html"}
        ]
  },
 {
    "block": "bolzano",
    "scripts": [
        {"script": "clean_tmp", "args": "%%dir%%"},
        {"script": "netex_to_db.py", "args": "--log=%%log%% %%dir%%/netex-export1.xml %%dir%%/netex-import.duckdb"},
        {"script": "netex_db_to_gtfs.py", "args": "--log=%%log%% %%dir%%/netex-import.duckdb %%dir%%/%%block%%-gtfs.zip"},
        {"script": "gtfs_show_map.py", "args": "--log=%%log%% %%dir%%/%%block%%-gtfs.zip %%dir%%/%%block%%-map.html"}
        ]
  },
    {
    "block": "swiss",
    "scripts": [
        {"script": "clean_tmp", "args": "%%dir%%"},
        {"script": "swiss_to_db.py", "args": "--log=%%log%% ./aux_test_input/swiss.zip %%dir%%/swiss-import.duckdb"},
        {"script": "epip_db_to_db.py", "args": "--log=%%log%% %%dir%%/swiss-import.duckdb %%dir%%/netex-database.duckdb"},
        {"script": "epip_db_to_xml.py", "args": "--log=%%log%% %%dir%%/swiss-import.duckdb %%dir%%/netex-database.duckdb %%dir%%/%%block%%-netex.xml"},
        {"script": "aux_assertions.py", "args": "--log=%%log%% ./aux_test_input/swiss-assertions.txt %%dir%%/%%block%%-netex.xml"},
        {"script": "aux_netex_stats.py", "args": "--log=%%log%% %%dir%%/%%block%%-netex.xml"},
        {"script": "netex_to_db.py", "args": "--log=%%log%% %%dir%%/%%block%%-netex.xml %%dir%%/netex-database.duckdb"},
        {"script": "netex_db_to_gtfs.py", "args": "--log=%%log%% %%dir%%/netex-database.duckdb %%dir%%/%%block%%-gtfs.zip"},
        {"script": "aux_gtfs_check.py", "args": "--log=%%log%% %%dir%%/%%block%%-gtfs.zip"},
        {"script": "gtfs_show_map.py", "args": "--log=%%log%% %%dir%%/%%block%%-gtfs.zip %%dir%%/%%block%%-map.html"}
        ]
  },
    {
    "block": "thonongtfs",
    "url":"https://transport.data.gouv.fr/datasets/thonon-agglomeration-donnees-gtfs",
    "description":"Thonon school buses",
    "scripts": [
        {"script": "clean_tmp", "args": "%%dir%%"},
        {"script": "gtfs_import_to_db.py", "args": "--log=%%log%% ./aux_test_input/thonon_gtfs.zip %%dir%%/gtfs-import.duckdb"},
        {"script": "gtfs_convert_to_db.py", "args": "--log=%%log%% %%dir%%/gtfs-import.duckdb %%dir%%/netex-import.duckdb"},
        {"script": "epip_db_to_db.py", "args": "--log=%%log%% %%dir%%/netex-import.duckdb %%dir%%/netex-database.duckdb"},
        {"script": "epip_db_to_xml.py", "args": "--log=%%log%% %%dir%%/netex-import.duckdb %%dir%%/netex-database.duckdb %%dir%%/%%block%%-netex.xml"},
        {"script": "aux_assertions.py", "args": "--log=%%log%% ./aux_test_input/general-netex-assertions.txt %%dir%%/%%block%%-netex.xml"},
        {"script": "aux_netex_stats.py", "args": "--log=%%log%% %%dir%%/%%block%%-netex.xml"},
        {"script": "netex_to_db.py", "args": "--log=%%log%% %%dir%%/%%block%%-netex.xml %%dir%%/netex-database.duckdb"},
        {"script": "netex_db_to_gtfs.py", "args": "--log=%%log%% %%dir%%/netex-database.duckdb %%dir%%/%%block%%-gtfs.zip"},
        {"script": "aux_gtfs_check.py", "args": "--log=%%log%% %%dir%%/%%block%%-gtfs.zip"},
        {"script": "gtfs_show_map.py", "args": "--log=%%log%% %%dir%%/%%block%%-gtfs.zip %%dir%%/%%block%%_gtfs-map.html"}
        ]
  },
     {
    "block": "swiss3",
    "scripts": [
        {"script": "clean_tmp", "args": "%%dir%%"},
        {"script": "swiss_to_db.py", "args": "--log=%%log%% ./aux_test_input/swiss3.zip %%dir%%/swiss-import.duckdb"},
        {"script": "epip_db_to_db.py", "args": "--log=%%log%% %%dir%%/swiss-import.duckdb %%dir%%/netex-database.duckdb"},
        {"script": "epip_db_to_xml.py", "args": "--log=%%log%% %%dir%%/swiss-import.duckdb %%dir%%/netex-database.duckdb %%dir%%/%%block%%-netex.xml"},
        {"script": "aux_assertions.py", "args": "--log=%%log%% ./aux_test_input/swiss-assertions.txt %%dir%%/%%block%%-netex.xml"},
        {"script": "aux_netex_stats.py", "args": "--log=%%log%% %%dir%%/%%block%%-netex.xml"},
        {"script": "netex_to_db.py", "args": "--log=%%log%% %%dir%%/%%block%%-netex.xml %%dir%%/netex-database.duckdb"},
        {"script": "related_explorer.py", "args": "--log=%%log%% %%dir%%/netex-database.duckdb ServiceJourney random %%dir%%/sj.xml"},
        {"script": "netex_db_to_gtfs.py", "args": "--log=%%log%% %%dir%%/netex-database.duckdb %%dir%%/%%block%%-gtfs.zip"},
        {"script": "aux_gtfs_check.py", "args": "--log=%%log%% %%dir%%/%%block%%-gtfs.zip"},
        {"script": "gtfs_show_map.py", "args": "--log=%%log%% %%dir%%/%%block%%-gtfs.zip %%dir%%/%%block%%-map.html"}
        ]
  }
  ,
     {
    "block": "swiss4",
    "scripts": [
        {"script": "clean_tmp", "args": "%%dir%%"},
        {"script": "swiss_to_db.py", "args": "--log=%%log%% d:/swiss4.zip %%dir%%/swiss-import.duckdb"},
        {"script": "epip_db_to_db.py", "args": "--log=%%log%% %%dir%%/swiss-import.duckdb %%dir%%/netex-database.duckdb"},
        {"script": "epip_db_to_xml.py", "args": "--log=%%log%% %%dir%%/swiss-import.duckdb %%dir%%/netex-database.duckdb %%dir%%/%%block%%-netex.xml"},
        {"script": "aux_assertions.py", "args": "--log=%%log%% ./aux_test_input/swiss-assertions.txt %%dir%%/%%block%%-netex.xml"},
        {"script": "aux_netex_stats.py", "args": "--log=%%log%% %%dir%%/%%block%%-netex.xml"},
        {"script": "netex_to_db.py", "args": "--log=%%log%% %%dir%%/%%block%%-netex.xml %%dir%%/netex2-database.duckdb"},
        {"script": "related_explorer.py", "args": "%%dir%%/netex2-database.duckdb ServiceJourney random %%dir%%/sj.xml"},
        {"script": "related_explorer.py", "args": "%%dir%%/netex2-database.duckdb Line random %%dir%%/line.xml"},
        {"script": "related_explorer.py", "args": "%%dir%%/netex2-database.duckdb ServiceJourney random %%dir%%/sj1.xml"},
        {"script": "related_explorer.py", "args": "%%dir%%/netex2-database.duckdb ServiceJourney random %%dir%%/sj2.xml"},
        {"script": "#netex_db_to_gtfs.py", "args": "--log=%%log%% %%dir%%/netex-database.duckdb %%dir%%/%%block%%-gtfs.zip"},
        {"script": "#aux_gtfs_check.py", "args": "--log=%%log%% %%dir%%/%%block%%-gtfs.zip"},
        {"script": "#gtfs_show_map.py", "args": "--log=%%log%% %%dir%%/%%block%%-gtfs.zip %%dir%%/%%block%%-map.html"}
        ]
  }
  ,
     {
    "block": "swissmikro",
    "scripts": [
        {"script": "clean_tmp", "args": "%%dir%%"},
        {"script": "gtfs_import_to_db.py", "args": "./aux_test_input/swiss_mikro.zip %%dir%%/gtfs-import.duckdb --log=%%log%% "},
        {"script": "gtfs_convert_to_db.py", "args": "--log=%%log%% %%dir%%/gtfs-import.duckdb %%dir%%/netex-import.duckdb"},
        {"script": "epip_db_to_db.py", "args": "--log=%%log%% %%dir%%/netex-import.duckdb %%dir%%/netex-database.duckdb"},
        {"script": "epip_db_to_xml.py", "args": "--log=%%log%% %%dir%%/netex-import.duckdb %%dir%%/netex-database.duckdb %%dir%%/%%block%%-netex.xml"},
        {"script": "aux_netex_stats.py", "args": "--log=%%log%% %%dir%%/%%block%%-netex.xml"},
        {"script": "netex_to_db.py", "args": "--log=%%log%% %%dir%%/%%block%%-netex.xml %%dir%%/netex2-database.duckdb"},
        {"script": "related_explorer.py", "args": "%%dir%%/netex2-database.duckdb ServiceJourney random %%dir%%/sj.xml"},
        {"script": "related_explorer.py", "args": "%%dir%%/netex2-database.duckdb Line random %%dir%%/line.xml"},
        {"script": "related_explorer.py", "args": "%%dir%%/netex2-database.duckdb ServiceJourney random %%dir%%/sj1.xml"},
        {"script": "related_explorer.py", "args": "%%dir%%/netex2-database.duckdb ServiceJourney random %%dir%%/sj2.xml"}
        ]
  }
  ,
     {
    "block": "swiss4short",
    "scripts": [
        {"script": "clean_tmp", "args": "%%dir%%"},
        {"script": "swiss_to_db.py", "args": "--log=%%log%% d:/swiss4.zip %%dir%%/swiss-import.duckdb"},
        {"script": "netex_db_to_gtfs.py", "args": "--log=%%log%% %%dir%%/swiss-import.duckdb %%dir%%/%%block%%-gtfs.zip"},
        {"script": "aux_gtfs_check.py", "args": "--log=%%log%% %%dir%%/%%block%%-gtfs.zip"},
        {"script": "gtfs_show_map.py", "args": "--log=%%log%% %%dir%%/%%block%%-gtfs.zip %%dir%%/%%block%%-gtfs-map.html"}
        ]
    }
    ,
     {
    "block": "stav462",
    "url":"download from Roberto",
    "description":"STA file based on VDV 462 for testing",
    "scripts": [
        {"script": "clean_tmp", "args": "%%dir%%"},
        {"script": "netex_to_db.py", "args": "--log=%%log%% D:/conversion/GE16614_01_DIVA_apb_ALL_1_20240919165008.xml.zip %%dir%%/swiss-import.duckdb"},
        {"script": "epip_db_to_db.py", "args": "--log=%%log%% %%dir%%/swiss-import.duckdb %%dir%%/netex-database.duckdb"},
        {"script": "epip_db_to_xml.py", "args": "--log=%%log%% %%dir%%/swiss-import.duckdb %%dir%%/netex-database.duckdb %%dir%%/%%block%%-netex.xml"},
        {"script": "aux_assertions.py", "args": "--log=%%log%% ./aux_test_input/general-assertions.txt %%dir%%/%%block%%-netex.xml"},
        {"script": "aux_netex_stats.py", "args": "--log=%%log%% %%dir%%/%%block%%-netex.xml"},
        {"script": "netex_to_db.py", "args": "--log=%%log%% %%dir%%/%%block%%-netex.xml %%dir%%/netex-database.duckdb"},
        {"script": "related_explorer.py", "args": "--log=%%log%% %%dir%%/netex-database.duckdb ServiceJourney random %%dir%%/sj.xml"},
        {"script": "netex_db_to_gtfs.py", "args": "--log=%%log%% %%dir%%/netex-database.duckdb %%dir%%/%%block%%-gtfs.zip"},
        {"script": "aux_gtfs_check.py", "args": "--log=%%log%% %%dir%%/%%block%%-gtfs.zip"},
        {"script": "gtfs_show_map.py", "args": "--log=%%log%% %%dir%%/%%block%%-gtfs.zip %%dir%%/%%block%%-map.html"}
        ]
  }
  ,
     {
    "block": "it1",
    "scripts": [
        {"script": "clean_tmp", "args": "%%dir%%"},
        {"script": "netex_to_db.py", "args": "--log=%%log%% D:/it/it.zip %%dir%%/swiss-import.duckdb"},
        {"script": "epip_db_to_db.py", "args": "--log=%%log%% %%dir%%/swiss-import.duckdb %%dir%%/netex-database.duckdb"},
        {"script": "epip_db_to_xml.py", "args": "--log=%%log%% %%dir%%/swiss-import.duckdb %%dir%%/netex-database.duckdb %%dir%%/%%block%%-netex.xml"},
        {"script": "aux_assertions.py", "args": "--log=%%log%% ./aux_test_input/swiss-assertions.txt %%dir%%/%%block%%-netex.xml"},
        {"script": "aux_netex_stats.py", "args": "--log=%%log%% %%dir%%/%%block%%-netex.xml"},
        {"script": "netex_to_db.py", "args": "--log=%%log%% %%dir%%/%%block%%-netex.xml %%dir%%/netex-database.duckdb"},
        {"script": "related_explorer.py", "args": "--log=%%log%% %%dir%%/netex-database.duckdb ServiceJourney random %%dir%%/sj.xml"},
        {"script": "netex_db_to_gtfs.py", "args": "--log=%%log%% %%dir%%/netex-database.duckdb %%dir%%/%%block%%-gtfs.zip"},
        {"script": "aux_gtfs_check.py", "args": "--log=%%log%% %%dir%%/%%block%%-gtfs.zip"},
        {"script": "gtfs_show_map.py", "args": "--log=%%log%% %%dir%%/%%block%%-gtfs.zip %%dir%%/%%block%%-map.html"}
        ]
  }
  ,
     {
    "block": "thonon_collate",
    "scripts": [
        {"script": "clean_tmp", "args": "%%dir%%"},
        {"script": "aux_collator.py", "args": "--log=%%log%% ./aux_test_input/thonon_netex.zip %%dir%%/%%block%%-collated.xml"},
        {"script": "netex_to_db.py", "args": "--log=%%log%% %%dir%%/%%block%%-collated.xml %%dir%%/netex-import.duckdb"},
        {"script": "epip_db_to_db.py", "args": "%%dir%%/netex-import.duckdb %%dir%%/netex-database.duckdb"},
        {"script": "epip_db_to_xml.py", "args": "--log=%%log%% %%dir%%/netex-import.duckdb %%dir%%/netex-database.duckdb %%dir%%/%%block%%-netex.xml"},
        {"script": "clean_tmp", "args": "%%dir%%"},
        {"script": "netex_to_db.py", "args": "--log=%%log%% %%dir%%/%%block%%-netex.xml %%dir%%/netex-database.duckdb"},
        {"script": "netex_db_to_gtfs.py", "args": "--log=%%log%% %%dir%%/netex-database.duckdb %%dir%%/%%block%%-gtfs.zip"},
        {"script": "gtfs_show_map.py", "args": "--log=%%log%% %%dir%%/%%block%%-gtfs.zip %%dir%%/%%block%%-map.html"},
        {"script": "related_explorer.py", "args": "--log=%%log%% %%dir%%/netex-database.duckdb ServiceJourney random %%dir%%/%%block%%-netex.xml"}
        ]
  }
,
     {
    "block": "swisscollate",
    "scripts": [
        {"script": "aux_collator.py", "args": "./aux_test_input/swiss3.zip %%dir%%/%%block%%-collated.xml"},
        {"script": "#aux_deduplicate.py", "args": "%%dir%%/%%block%%-collated.xml %%dir%%/%%block%%-collated-dedup.xml %%dir%%/%%block%%-dupls.xlsx"},
        {"script": "aux_extract_one_servicejourney.py", "args": "%%dir%%/%%block%%-collated.xml %%dir%%/%%block%%-sy-1.xml"},
        {"script": "aux_extract_one_servicejourney.py", "args": "%%dir%%/%%block%%-collated.xml %%dir%%/%%block%%-sy-2.xml"}
        ]
  }

]
