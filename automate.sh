#!/usr/bin/env bash
function my_test() {
   for f in $(find . -name README.org); do
        dirname=$(basename $(dirname $f))
        echo "Update for $f"
        sed -ie "s/designquestion/oodesign/g" $f
        rm -rf $dirname/README.orge
        #exit
   done
}

function refresh_link() {
    echo "refresh link"
    for f in $(ls -1t */README.org); do
        dirname=$(basename $(dirname $f))
        if ! grep "brain.dennyzhang.com.*$dirname" $f 1>/dev/null 2>&1; then
            echo "Update blog url for $f"
            sed -ie "s/Blog link: https:\/\/brain.dennyzhang.com\/.*/Blog link: https:\/\/brain.dennyzhang.com\/$dirname/g" $f
            rm -rf $dirname/README.orge
        fi

        if ! grep "tree\/master.*$dirname" $f 1>/dev/null 2>&1; then
            echo "Update GitHub url for $f"
            sed -ie "s/tree\/master\/.*/tree\/master\/$dirname][challenges-leetcode-interesting]]/g" $f
            rm -rf $dirname/README.orge
        fi

        if ! grep Lintcode.com $f 1>/dev/null 2>&1; then
            if ! grep "leetcode.com.*$dirname" $f 1>/dev/null 2>&1; then
                echo "Update Leetcode url for $f"            
                sed -ie "s/https:\/\/leetcode.com\/problems\/.*/https:\/\/leetcode.com\/problems\/$dirname\/description\/][leetcode.com]]/g" $f
                rm -rf $dirname/README.orge
            fi
        fi
    done
}

function refresh_md() {
    echo "Use emacs to refresh README.md"
    for f in $(ls -1t */README.org); do
        echo "Update $f"
        dirname=$(basename $(dirname $f))
        cd $dirname
        /Applications/Emacs.app/Contents/MacOS/Emacs-x86_64-10_9 --batch -l ../update_md.el
        cd ..
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
    refresh_md)
        refresh_md
        ;;
        *) 
        echo "no matched action. Supported: refresh_link|refresh_md"
        ;;
esac
