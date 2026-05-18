#!/bin/bash

PROJECT_DIR="$HOME/Projects/HEXA/projects/rema-protocol"

start_ema() {
    kitty \
        --class EMA_TERM \
        --title EMA_RUNTIME \
        bash -c "$PROJECT_DIR/scripts/start_ema.sh"
}

stop_ema() {
    pkill -f EMA_RUNTIME
}

status_ema() {
    if pgrep -f EMA_RUNTIME > /dev/null; then
        echo "EMA is ONLINE"
    else
        echo "EMA is OFFLINE"
    fi
}

case "$1" in
    ema)
        case "$2" in
            start)
                start_ema
                ;;
            stop)
                stop_ema
                ;;
            restart)
                stop_ema
                sleep 1
                start_ema
                ;;
            status)
                status_ema
                ;;
            *)
                echo "Usage: rema ema {start|stop|restart|status}"
                ;;
        esac
        ;;
    *)
        echo "Usage: rema ema {start|stop|restart|status}"
        ;;
esac