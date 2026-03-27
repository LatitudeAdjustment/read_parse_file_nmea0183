# README.md

Claude-created program to read a file containing NMEA 0183 data and do initial,
very basic parsing.

## References

<https://en.wikipedia.org/wiki/NMEA_0183>

<https://actisense.com/wp-content/uploads/2020/01/NMEA-0183-Information-sheet-issue-4-1-1.pdf>

## Run Program

```bash
python read_parse_file_nmea0183.py ../serial_read_port_nmea0183/BU-353S4_Output_003.log
```

```bash
$ python read_parse_file_nmea0183.py ../serial_read_port_nmea0183/BU-353S4_Output_003.log
Sentence must start with '$': 'Listening on /dev/tty.usbserial-1110 at 4800 baud... (Ctrl+C to quit)'
None
Sentence must start with '$': '7973,W,1,05,4.2,13.4,M,-34.3,M,,0000*56'
None
{'talker': 'GP', 'sentence': 'RMC', 'fields': ['192039.000', 'A', '4104.4926', 'N', '07326.7962', 'W', '0.76', '172.06', '270326', '', '', 'A'], 'checksum': '7F', 'valid': True}
{'talker': 'GP', 'sentence': 'GGA', 'fields': ['192040.000', '4104.4929', 'N', '07326.7968', 'W', '1', '04', '5.3', '14.1', 'M', '-34.3', 'M', '', '0000'], 'checksum': '58', 'valid': True}
{'talker': 'GP', 'sentence': 'GSA', 'fields': ['M', '3', '06', '21', '22', '04', '', '', '', '', '', '', '', '', '7.7', '5.3', '5.6'], 'checksum': '3A', 'valid': True}
{'talker': 'GP', 'sentence': 'RMC', 'fields': ['192040.000', 'A', '4104.4929', 'N', '07326.7968', 'W', '1.07', '172.06', '270326', '', '', 'A'], 'checksum': '73', 'valid': True}
{'talker': 'GP', 'sentence': 'GGA', 'fields': ['192041.000', '4104.4931', 'N', '07326.7975', 'W', '1', '04', '5.3', '14.1', 'M', '-34.3', 'M', '', '0000'], 'checksum': '5C', 'valid': True}
{'talker': 'GP', 'sentence': 'GSA', 'fields': ['M', '3', '06', '21', '22', '04', '', '', '', '', '', '', '', '', '7.7', '5.3', '5.6'], 'checksum': '3A', 'valid': True}
{'talker': 'GP', 'sentence': 'RMC', 'fields': ['192041.000', 'A', '4104.4931', 'N', '07326.7975', 'W', '1.71', '229.53', '270326', '', '', 'A'], 'checksum': '7B', 'valid': True}
{'talker': 'GP', 'sentence': 'GGA', 'fields': ['192042.000', '4104.4932', 'N', '07326.7980', 'W', '1', '04', '5.3', '14.1', 'M', '-34.3', 'M', '', '0000'], 'checksum': '56', 'valid': True}
{'talker': 'GP', 'sentence': 'GSA', 'fields': ['M', '3', '06', '21', '22', '04', '', '', '', '', '', '', '', '', '7.7', '5.3', '5.6'], 'checksum': '3A', 'valid': True}
{'talker': 'GP', 'sentence': 'RMC', 'fields': ['192042.000', 'A', '4104.4932', 'N', '07326.7980', 'W', '1.83', '255.20', '270326', '', '', 'A'], 'checksum': '73', 'valid': True}
{'talker': 'GP', 'sentence': 'GGA', 'fields': ['192043.000', '4104.4934', 'N', '07326.7986', 'W', '0', '00', '', '14.1', 'M', '-34.3', 'M', '', '0000'], 'checksum': '7A', 'valid': True}
{'talker': 'GP', 'sentence': 'GSA', 'fields': ['M', '1', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''], 'checksum': '12', 'valid': True}
{'talker': 'GP', 'sentence': 'GSV', 'fields': ['3', '1', '12', '04', '14', '066', '14', '06', '69', '018', '07', '19', '63', '094', '10', '21', '27', '197', '19'], 'checksum': '7B', 'valid': True}
{'talker': 'GP', 'sentence': 'GSV', 'fields': ['3', '2', '12', '22', '17', '169', '20', '48', '15', '247', '', '17', '36', '110', '', '28', '24', '173', ''], 'checksum': '72', 'valid': True}
{'talker': 'GP', 'sentence': 'GSV', 'fields': ['3', '3', '12', '09', '18', '098', '', '25', '09', '322', '', '03', '06', '036', '', '23', '05', '147', ''], 'checksum': '70', 'valid': True}
{'talker': 'GP', 'sentence': 'RMC', 'fields': ['192043.000', 'V', '4104.4934', 'N', '07326.7986', 'W', '', '', '270326', '', '', 'N'], 'checksum': '60', 'valid': True}
{'talker': 'GP', 'sentence': 'GGA', 'fields': ['192044.000', '4104.4936', 'N', '07326.7992', 'W', '0', '00', '', '14.1', 'M', '-34.3', 'M', '', '0000'], 'checksum': '7A', 'valid': True}
{'talker': 'GP', 'sentence': 'GSA', 'fields': ['M', '1', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''], 'checksum': '12', 'valid': True}
{'talker': 'GP', 'sentence': 'RMC', 'fields': ['192044.000', 'V', '4104.4936', 'N', '07326.7992', 'W', '', '', '270326', '', '', 'N'], 'checksum': '60', 'valid': True}
{'talker': 'GP', 'sentence': 'GGA', 'fields': ['192045.000', '4104.4937', 'N', '07326.7998', 'W', '0', '00', '', '14.2', 'M', '-34.3', 'M', '', '0000'], 'checksum': '73', 'valid': True}
{'talker': 'GP', 'sentence': 'GSA', 'fields': ['M', '1', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''], 'checksum': '12', 'valid': True}
{'talker': 'GP', 'sentence': 'RMC', 'fields': ['192045.000', 'V', '4104.4937', 'N', '07326.7998', 'W', '', '', '270326', '', '', 'N'], 'checksum': '6A', 'valid': True}
{'talker': 'GP', 'sentence': 'GGA', 'fields': ['192046.000', '4104.4939', 'N', '07326.8005', 'W', '0', '00', '', '14.2', 'M', '-34.3', 'M', '', '0000'], 'checksum': '7C', 'valid': True}
{'talker': 'GP', 'sentence': 'GSA', 'fields': ['M', '1', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''], 'checksum': '12', 'valid': True}
{'talker': 'GP', 'sentence': 'RMC', 'fields': ['192046.000', 'V', '4104.4939', 'N', '07326.8005', 'W', '', '', '270326', '', '', 'N'], 'checksum': '65', 'valid': True}
{'talker': 'GP', 'sentence': 'GGA', 'fields': ['192047.000', '4104.4941', 'N', '07326.8011', 'W', '0', '00', '', '14.2', 'M', '-34.3', 'M', '', '0000'], 'checksum': '77', 'valid': True}
{'talker': 'GP', 'sentence': 'GSA', 'fields': ['M', '1', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''], 'checksum': '12', 'valid': True}
{'talker': 'GP', 'sentence': 'RMC', 'fields': ['192047.000', 'V', '4104.4941', 'N', '07326.8011', 'W', '', '', '270326', '', '', 'N'], 'checksum': '6E', 'valid': True}
{'talker': 'GP', 'sentence': 'GGA', 'fields': ['192048.000', '4104.4943', 'N', '07326.8017', 'W', '0', '00', '', '14.3', 'M', '-34.3', 'M', '', '0000'], 'checksum': '7D', 'valid': True}
{'talker': 'GP', 'sentence': 'GSA', 'fields': ['M', '1', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''], 'checksum': '12', 'valid': True}
{'talker': 'GP', 'sentence': 'GSV', 'fields': ['3', '1', '12', '04', '14', '066', '13', '06', '69', '018', '06', '19', '63', '094', '10', '21', '27', '197', '20'], 'checksum': '77', 'valid': True}
{'talker': 'GP', 'sentence': 'GSV', 'fields': ['3', '2', '12', '22', '17', '169', '20', '48', '15', '247', '', '17', '36', '110', '', '28', '24', '173', ''], 'checksum': '72', 'valid': True}
{'talker': 'GP', 'sentence': 'GSV', 'fields': ['3', '3', '12', '09', '18', '098', '', '25', '09', '322', '', '03', '06', '036', '', '23', '05', '147', ''], 'checksum': '70', 'valid': True}
{'talker': 'GP', 'sentence': 'RMC', 'fields': ['192048.000', 'V', '4104.4943', 'N', '07326.8017', 'W', '', '', '270326', '', '', 'N'], 'checksum': '65', 'valid': True}
{'talker': 'GP', 'sentence': 'GGA', 'fields': ['192049.000', '4104.4944', 'N', '07326.8024', 'W', '0', '00', '', '14.3', 'M', '-34.3', 'M', '', '0000'], 'checksum': '7B', 'valid': True}
{'talker': 'GP', 'sentence': 'GSA', 'fields': ['M', '1', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''], 'checksum': '12', 'valid': True}
Sentence must start with '$': ''
None
Sentence must start with '$': 'Stopped.'
None
```
