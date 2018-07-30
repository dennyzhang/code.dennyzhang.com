#!/usr/bin/env bash
function my_test() {
   for f in $(find . -name README.org); do
        dirname=$(basename $(dirname $f))
        echo "Update for $f"
        sed -ie "s/github.com\/DennyZhang\/challenges-leetcode-interesting\/tree\/master/github.com\/DennyZhang\/challenges-leetcode-interesting\/tree\/master\/problems/g" $f
        rm -rf $dirname/README.orge
        #exit
   done
}

function refresh_link() {
    echo "refresh link"
    cd problems
    for f in $(ls -1t */README.org); do
        dirname=$(basename $(dirname $f))
        if ! grep "Blog link: https:\/\/code.dennyzhang.com.*$dirname" $f 1>/dev/null 2>&1; then
            echo "Update blog url for $f"
            sed -ie "s/Blog link: https:\/\/code.dennyzhang.com\/.*/Blog link: https:\/\/code.dennyzhang.com\/$dirname/g" $f
            rm -rf $dirname/README.orge
        fi

        if ! grep "tree\/master.*$dirname" $f 1>/dev/null 2>&1; then
            echo "Update GitHub url for $f"
            sed -ie "s/tree\/master\/.*/tree\/master\/$dirname][challenges-leetcode-interesting]]/g" $f
            rm -rf $dirname/README.orge
        fi

        if ! grep -i lintcode.com $f 1>/dev/null 2>&1; then
            if ! grep "leetcode.com.*$dirname" $f 1>/dev/null 2>&1; then
                echo "Update Leetcode url for $f"            
                sed -ie "s/https:\/\/leetcode.com\/problems\/.*/https:\/\/leetcode.com\/problems\/$dirname\/description\/][leetcode.com]]/g" $f
                rm -rf $dirname/README.orge
            fi
        fi
    done
}

cd .

action=${1?}
case "$action" in 
    refresh_link)
        refresh_link
        ;;
    my_test)
        my_test
        ;;
        *) 
        echo "no matched action. Supported: refresh_link|my_test"
        ;;
esac
