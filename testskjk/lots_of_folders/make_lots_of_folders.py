import os,os.path,sys,argparse

def mkdirs(x):
    try: os.makedirs(x)
    except OSError: pass

def main(options):
    ni=50
    nj=20
    nk=10
    for i in range(ni):
        print i
        for j in range(nj):
            dname=os.path.join(options.dname,"%03d"%i,"%03d"%j)
            mkdirs(dname)
            for k in range(nk):
                fname=os.path.join(dname,"%03d.txt"%k)
                with open(fname,"wt") as f: f.write("%02X%02X%02X"%(i,j,k))

if __name__=="__main__":
    parser=argparse.ArgumentParser()

    parser.add_argument("dname",metavar="DIR",help="path to create lots of folders in")

    main(parser.parse_args(sys.argv[1:]))
    
