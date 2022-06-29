import os
import argparse
import io

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-src', required=True, type=str)
    parser.add_argument('-ref', required=True, type=str)
    
    args = parser.parse_args()

    path2src = args.src
    path2ref = args.ref

    # path2src = '/home/zakaria.abbou/PycharmProjects/pythonProject_LC_python3.7/pairs_to_XML/test.tok.src'
    # path2ref = '/home/zakaria.abbou/PycharmProjects/pythonProject_LC_python3.7/pairs_to_XML/test.tok.ref'

    lstSrc = []
    with io.open(path2src, encoding='utf8') as fread:
        for line in fread:
            lstSrc.append(line)

    lstRef = []
    with io.open(path2ref, encoding='utf8') as fread:
        for line in fread:
            lstRef.append(line)

    with io.open(path2src + '.sgm', 'w', encoding='utf8') as fwrite:
        fwrite.write(u'<srcset setid="demokr-vn" srclang="kr">\n')
        fwrite.write(u'<doc docid="demo1" genre="news" origlang="kr">\n')
        fwrite.write(u'<p>\n')
        for i, line in enumerate(lstSrc):
            _str = u'<seg id="'
            _str += str(i+1)
            _str += u'"> '
            _str += line.strip()
            _str += u'</seg>\n'
            fwrite.write(_str)
        fwrite.write(u'</p>\n')
        fwrite.write(u'</doc>\n')
        fwrite.write(u'</srcset>')
        fwrite.flush()

    with io.open(path2ref + '.sgm', 'w', encoding='utf8') as fwrite:
        fwrite.write(u'<refset setid="demokr-vn" srclang="vn">\n')
        fwrite.write(u'<doc docid="demo1" genre="news" origlang="kr" sysid="ref">\n')
        fwrite.write(u'<p>\n')
        for i, line in enumerate(lstRef):
            _str = u'<seg id="'
            _str += str(i+1)
            _str += u'"> '
            _str += line.strip()
            _str += u'</seg>\n'
            fwrite.write(_str)
        fwrite.write(u'</p>\n')
        fwrite.write(u'</doc>\n')
        fwrite.write(u'</refset>')
        fwrite.flush()

if __name__ == '__main__':
    main()