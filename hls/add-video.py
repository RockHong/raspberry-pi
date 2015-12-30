# -*- coding: utf-8 -*-

import argparse
import os
import subprocess


template = '''
                <div class="col-sm-1">
                    <div class="video-sm hidden-xs" >
                        <video controls src="/{path}{outputdir}/prog_index.m3u8">
                        </video>
                        <p>
                        <a href="/{path}{outputdir}/prog_index.m3u8">{desc}</a>
                        <p>
                    </div>
                    <div class="video-xs visible-xs-block">
                        <!-- embed-responsive-4by3 embed-responsive-16by9 -->
                        <div class="embed-responsive embed-responsive-16by9">
                            <video controls class="embed-responsive-item" src="/{path}{outputdir}/prog_index.m3u8">
                            </video>
                        </div>
                        <p>
                            <a href="/{path}{outputdir}/prog_index.m3u8">{desc}</a>
                        </p>
                    </div>
                </div><!-- end: col -->'''


def mk_output_dir(args):
    dirname = ''
    if args.outdir is None:
        if is_ascii(args.src):
            dirname = args.src
        else:
            raise Exception('cannot determine output dir name.')
    else:
        dirname = args.outdir
        
    # remove suffix if have
    dirname = dirname[:dirname.find('.')]
    if not os.path.isdir(dirname):
        os.mkdir(dirname)
        
    return dirname
    

# http://stackoverflow.com/questions/196345/how-to-check-if-a-string-in-python-is-in-ascii 
def is_ascii(s):
    return all(ord(c) < 128 for c in s)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='video processor')
    parser.add_argument('--outdir', help='dir to store HLS segment files and play list')
    parser.add_argument('--host', default='http://192.168.0.169:8080/', help='host')
    parser.add_argument('--path', default='v/', help='path')
    parser.add_argument('--src', required=True, help='source video')
    parser.add_argument('--desc', help='video description')
    parser.add_argument('--htmlfile', help='html file to append')
    
    args = parser.parse_args()
    if args.desc is None:
        args.desc = args.src
    
    dirname = mk_output_dir(args)
    #subprocess.check_call(['mediafilesegmenter','-f', dirname,  '-b', '{host}{path}{outputdir}'.format(outputdir=dirname, host=args.host, path=args.path), args.src])
    print template.format(path=args.path, src=args.src, outputdir=dirname, desc=args.desc)





