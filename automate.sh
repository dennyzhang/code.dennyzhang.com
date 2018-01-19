#!/usr/bin/env bash
working_dir=${1?}

function refresh_Link() {
    for f in $(find . -name README.org); do
        dirname=$(basename $(dirname $f))
        if ! grep "brain.dennyzhang.com.*$dirname" $f 1>/dev/null 2>&1; then
            echo "Update blog url for $f"
            sed -ie "s/http:\/\/brain.dennyzhang.com\/.*/http:\/\/brain.dennyzhang.com\/$dirname/g" $f
            rm -rf $dirname/README.orge
        fi

        if ! grep "tree\/master.*$dirname" $f 1>/dev/null 2>&1; then
            echo "Update GitHub url for $f"
            sed -ie "s/tree\/master\/.*/tree\/master\/$dirname][challenges-leetcode-interesting]]/g" $f
            rm -rf $dirname/README.orge
        fi

        if ! grep "leetcode.com.*$dirname" $f 1>/dev/null 2>&1; then
            echo "Update Leetcode url for $f"            
            sed -ie "s/https:\/\/leetcode.com\/problems\/.*/https:\/\/leetcode.com\/problems\/$dirname\/description][leetcode.com]]/g" $f
            rm -rf $dirname/README.orge
        fi
    done
}

cd $working_dir
refresh_Link