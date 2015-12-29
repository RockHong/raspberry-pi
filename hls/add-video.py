# -*- coding: utf-8 -*-

import argparse
import os
import subprocess


template = '''
                <div class="col-sm-1">
                    <div class="video-sm hidden-xs" >
                        <video controls src="...">
                        </video>
                        <p>
                        <a href="/xxxx">In this webinar, you'll learn about the different methods for streaming video and how some of the advanced features of NGINX and NGINX Plus can be used to meet your video streaming needs</a>
                        <p>
                    </div>
                    <div class="video-xs visible-xs-block">
                        <!-- embed-responsive-4by3 embed-responsive-16by9 -->
                        <div class="embed-responsive embed-responsive-16by9">
                            <video controls class="embed-responsive-item" src="...">
                            </video>
                        </div>
                        <p>
                            <a href="/xxxx">In this webinar, you'll learn about the different methods for streaming video and how some of the advanced features of NGINX and NGINX Plus can be used to meet your video streaming needs</a>
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
    parser.add_argument('--baseurl', default='http://localhost:8080/v/', help='base url')
    parser.add_argument('--src', required=True, help='source video')
    parser.add_argument('--htmlfile', help='html file to append')
    
    args = parser.parse_args()
    
    dirname = mk_output_dir(args)
    subprocess.check_call(['mediafilesegmenter','-f {outputdir}  -b {baseurl}/{outputdir} {src}'.format(outputdir=dirname, baseurl=args.baseurl, src=args.src)])
    print template.format()




