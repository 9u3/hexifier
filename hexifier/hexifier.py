hexcol = {'00': '0', '01': '1', '02': '2', '03': '3', '04': '4', '05': '5', '06': '6', '07': '7', '08': '8', '09': '9', '0a': '10', '0b': '11', '0c': '12', '0d': '13', '0e': '14', '0f': '15', '10': '16', '11': '17', '12': '18', '13': '19', '14': '20', '15': '21', '16': '22', '17': '23', '18': '24', '19': '25', '1a': '26', '1b': '27', '1c': '28', '1d': '29', '1e': '30', '1f': '31', '20': '32', '21': '33', '22': '34', '23': '35', '24': '36', '25': '37', '26': '38', '27': '39', '28': '40', '29': '41', '2a': '42', '2b': '43', '2c': '44', '2d': '45', '2e': '46', '2f': '47', '30': '48', '31': '49', '32': '50', '33': '51', '34': '52', '35': '53', '36': '54', '37': '55', '38': '56', '39': '57', '3a': '58', '3b': '59', '3c': '60', '3d': '61', '3e': '62', '3f': '63', '40': '64', '41': '65', '42': '66', '43': '67', '44': '68', '45': '69', '46': '70', '47': '71', '48': '72', '49': '73', '4a': '74', '4b': '75', '4c': '76', '4d': '77', '4e': '78', '4f': '79', '50': '80', '51': '81', '52': '82', '53': '83', '54': '84', '55': '85', '56': '86', '57': '87', '58': '88', '59': '89', '5a': '90', '5b': '91', '5c': '92', '5d': '93', '5e': '94', '5f': '95', '60': '96', '61': '97', '62': '98', '63': '99', '64': '100', '65': '101', '66': '102', '67': '103', '68': '104', '69': '105', '6a': '106', '6b': '107', '6c': '108', '6d': '109', '6e': '110', '6f': '111', '70': '112', '71': '113', '72': '114', '73': '115', '74': '116', '75': '117', '76': '118', '77': '119', '78': '120', '79': '121', '7a': '122', '7b': '123', '7c': '124', '7d': '125', '7e': '126', '7f': '127', '80': '128', '81': '129', '82': '130', '83': '131', '84': '132', '85': '133', '86': '134', '87': '135', '88': '136', '89': '137', '8a': '138', '8b': '139', '8c': '140', '8d': '141', '8e': '142', '8f': '143', '90': '144', '91': '145', '92': '146', '93': '147', '94': '148', '95': '149', '96': '150', '97': '151', '98': '152', '99': '153', '9a': '154', '9b': '155', '9c': '156', '9d': '157', '9e': '158', '9f': '159', 'a0': '160', 'a1': '161', 'a2': '162', 'a3': '163', 'a4': '164', 'a5': '165', 'a6': '166', 'a7': '167', 'a8': '168', 'a9': '169', 'aa': '170', 'ab': '171', 'ac': '172', 'ad': '173', 'ae': '174', 'af': '175', 'b0': '176', 'b1': '177', 'b2': '178', 'b3': '179', 'b4': '180', 'b5': '181', 'b6': '182', 'b7': '183', 'b8': '184', 'b9': '185', 'ba': '186', 'bb': '187', 'bc': '188', 'bd': '189', 'be': '190', 'bf': '191', 'c0': '192', 'c1': '193', 'c2': '194', 'c3': '195', 'c4': '196', 'c5': '197', 'c6': '198', 'c7': '199', 'c8': '200', 'c9': '201', 'ca': '202', 'cb': '203', 'cc': '204', 'cd': '205', 'ce': '206', 'cf': '207', 'd0': '208', 'd1': '209', 'd2': '210', 'd3': '211', 'd4': '212', 'd5': '213', 'd6': '214', 'd7': '215', 'd8': '216', 'd9': '217', 'da': '218', 'db': '219', 'dc': '220', 'dd': '221', 'de': '222', 'df': '223', 'e0': '224', 'e1': '225', 'e2': '226', 'e3': '227', 'e4': '228', 'e5': '229', 'e6': '230', 'e7': '231', 'e8': '232', 'e9': '233', 'ea': '234', 'eb': '235', 'ec': '236', 'ed': '237', 'ee': '238', 'ef': '239', 'f0': '240', 'f1': '241', 'f2': '242', 'f3': '243', 'f4': '244', 'f5': '245', 'f6': '246', 'f7': '247', 'f8': '248', 'f9': '249', 'fa': '250', 'fb': '251', 'fc': '252', 'fd': '253', 'fe': '254', 'ff': '255'}

class hexifier:
    def __version__(self):
        return "1.03"
    def __hex_color__(self):
        return hexcol
    
    def rgbify(self, hx: str):
        hx = hx.lower()
        h = ""
        ret = []
        def rep(self, h, hxc):
            h += hexcol[hxc[:2]]
            hx = hxc.replace(hxc[:2], "", 1)
            return {"replaced": h, "hex": hx}
        h = rep(self, h, hx)
        ret.append(h["replaced"])
        h1 = rep(self, h["replaced"], h["hex"])
        ret.append(h1["replaced"].replace(h1["replaced"][:3], "", 1))
        h2 = rep(self, h1["replaced"], h1["hex"])
        ret.append(h2["replaced"].replace(h1["replaced"][:6], "", 1))
        return ", ".join(n for n in ret)
    
    def hexify(self, color: tuple):
        if type(color) != tuple:
            return f"Conversion Failed.\n'{color}' is not a tuple."
        elif len(color) > 3:
            return f"Conversion Failed.\nMore than 3 values"
        elif len(color) < 3:
            return f"Conversion Failed.\nLess than 3 values"
        else:
            hexres = ""
            try:
                for c in color:
                    c = int(c)
                    if c > 255:
                        raise Exception
                    elif c < 16:
                        s = "0"+f"{c:x}"
                        hexres += s
                    else:
                        hexres += f"{c:x}"
                return "#" + hexres.upper()
            except:
                return f"Conversion failed.\nOne or more values was above the 255 limit."
