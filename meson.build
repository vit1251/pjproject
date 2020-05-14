project('pjproject', 'c', version: '2.10')

pjlib_inc = include_directories('pjlib/include')

# pjlib

pjlib_source = [
    'pjlib/src/pj/ioqueue_select.c',
    'pjlib/src/pj/file_access_unistd.c',
    'pjlib/src/pj/file_io_ansi.c',
    'pjlib/src/pj/os_core_unix.c',
    'pjlib/src/pj/os_error_unix.c',
    'pjlib/src/pj/os_time_unix.c',
    'pjlib/src/pj/os_timestamp_posix.c',
    'pjlib/src/pj/sock_qos_bsd.c',
    'pjlib/src/pj/guid_uuid.c',
    'pjlib/src/pj/addr_resolv_sock.c',
    'pjlib/src/pj/log_writer_stdout.c',
    'pjlib/src/pj/os_timestamp_common.c',
    'pjlib/src/pj/pool_policy_malloc.c',
    'pjlib/src/pj/sock_bsd.c',
    'pjlib/src/pj/sock_select.c',
    'pjlib/src/pj/activesock.c',
    'pjlib/src/pj/array.c',
    'pjlib/src/pj/config.c',
    'pjlib/src/pj/ctype.c',
    'pjlib/src/pj/errno.c',
    'pjlib/src/pj/except.c',
    'pjlib/src/pj/fifobuf.c',
    'pjlib/src/pj/guid.c',
    'pjlib/src/pj/hash.c',
    'pjlib/src/pj/ip_helper_generic.c',
    'pjlib/src/pj/list.c',
    'pjlib/src/pj/lock.c',
    'pjlib/src/pj/log.c',
    'pjlib/src/pj/os_time_common.c',
    'pjlib/src/pj/os_info.c',
    'pjlib/src/pj/pool.c',
    'pjlib/src/pj/pool_buf.c',
    'pjlib/src/pj/pool_caching.c',
    'pjlib/src/pj/pool_dbg.c',
    'pjlib/src/pj/rand.c',
    'pjlib/src/pj/rbtree.c',
    'pjlib/src/pj/sock_common.c',
    'pjlib/src/pj/sock_qos_common.c',
    'pjlib/src/pj/ssl_sock_common.c',
    'pjlib/src/pj/ssl_sock_ossl.c',
    'pjlib/src/pj/ssl_sock_gtls.c',
    'pjlib/src/pj/ssl_sock_dump.c',
    'pjlib/src/pj/ssl_sock_darwin.c',
    'pjlib/src/pj/string.c',
    'pjlib/src/pj/timer.c',
    'pjlib/src/pj/types.c',
]

pjlib = static_library('pjlib', pjlib_source,
        include_directories: [pjlib_inc],
        c_args: ['-Wall', '-DPJ_LINUX=1', '-O2', '-DPJ_IS_BIG_ENDIAN=0', '-DPJ_IS_LITTLE_ENDIAN=1'],
    )


# make -f /home/vsedyshev/Work/1111/pjproject/build/rules.mak APP=TEST app=pjlib-test ../bin/pjlib-test-x86_64-unknown-linux-gnu
# make[2]: Entering directory '/home/vsedyshev/Work/1111/pjproject/pjlib/build'
# mkdir -p output/pjlib-test-x86_64-unknown-linux-gnu/
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include \
# 	-o output/pjlib-test-x86_64-unknown-linux-gnu/main.o \
# 	../src/pjlib-test/main.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include \
# 	-o output/pjlib-test-x86_64-unknown-linux-gnu/activesock.o \
# 	../src/pjlib-test/activesock.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include \
# 	-o output/pjlib-test-x86_64-unknown-linux-gnu/atomic.o \
# 	../src/pjlib-test/atomic.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include \
# 	-o output/pjlib-test-x86_64-unknown-linux-gnu/echo_clt.o \
# 	../src/pjlib-test/echo_clt.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include \
# 	-o output/pjlib-test-x86_64-unknown-linux-gnu/errno.o \
# 	../src/pjlib-test/errno.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include \
# 	-o output/pjlib-test-x86_64-unknown-linux-gnu/exception.o \
# 	../src/pjlib-test/exception.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include \
# 	-o output/pjlib-test-x86_64-unknown-linux-gnu/fifobuf.o \
# 	../src/pjlib-test/fifobuf.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include \
# 	-o output/pjlib-test-x86_64-unknown-linux-gnu/file.o \
# 	../src/pjlib-test/file.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include \
# 	-o output/pjlib-test-x86_64-unknown-linux-gnu/hash_test.o \
# 	../src/pjlib-test/hash_test.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include \
# 	-o output/pjlib-test-x86_64-unknown-linux-gnu/ioq_perf.o \
# 	../src/pjlib-test/ioq_perf.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include \
# 	-o output/pjlib-test-x86_64-unknown-linux-gnu/ioq_udp.o \
# 	../src/pjlib-test/ioq_udp.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include \
# 	-o output/pjlib-test-x86_64-unknown-linux-gnu/ioq_unreg.o \
# 	../src/pjlib-test/ioq_unreg.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include \
# 	-o output/pjlib-test-x86_64-unknown-linux-gnu/ioq_tcp.o \
# 	../src/pjlib-test/ioq_tcp.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include \
# 	-o output/pjlib-test-x86_64-unknown-linux-gnu/list.o \
# 	../src/pjlib-test/list.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include \
# 	-o output/pjlib-test-x86_64-unknown-linux-gnu/mutex.o \
# 	../src/pjlib-test/mutex.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include \
# 	-o output/pjlib-test-x86_64-unknown-linux-gnu/os.o \
# 	../src/pjlib-test/os.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include \
# 	-o output/pjlib-test-x86_64-unknown-linux-gnu/pool.o \
# 	../src/pjlib-test/pool.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include \
# 	-o output/pjlib-test-x86_64-unknown-linux-gnu/pool_perf.o \
# 	../src/pjlib-test/pool_perf.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include \
# 	-o output/pjlib-test-x86_64-unknown-linux-gnu/rand.o \
# 	../src/pjlib-test/rand.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include \
# 	-o output/pjlib-test-x86_64-unknown-linux-gnu/rbtree.o \
# 	../src/pjlib-test/rbtree.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include \
# 	-o output/pjlib-test-x86_64-unknown-linux-gnu/select.o \
# 	../src/pjlib-test/select.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include \
# 	-o output/pjlib-test-x86_64-unknown-linux-gnu/sleep.o \
# 	../src/pjlib-test/sleep.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include \
# 	-o output/pjlib-test-x86_64-unknown-linux-gnu/sock.o \
# 	../src/pjlib-test/sock.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include \
# 	-o output/pjlib-test-x86_64-unknown-linux-gnu/sock_perf.o \
# 	../src/pjlib-test/sock_perf.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include \
# 	-o output/pjlib-test-x86_64-unknown-linux-gnu/ssl_sock.o \
# 	../src/pjlib-test/ssl_sock.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include \
# 	-o output/pjlib-test-x86_64-unknown-linux-gnu/string.o \
# 	../src/pjlib-test/string.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include \
# 	-o output/pjlib-test-x86_64-unknown-linux-gnu/test.o \
# 	../src/pjlib-test/test.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include \
# 	-o output/pjlib-test-x86_64-unknown-linux-gnu/thread.o \
# 	../src/pjlib-test/thread.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include \
# 	-o output/pjlib-test-x86_64-unknown-linux-gnu/timer.o \
# 	../src/pjlib-test/timer.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include \
# 	-o output/pjlib-test-x86_64-unknown-linux-gnu/timestamp.o \
# 	../src/pjlib-test/timestamp.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include \
# 	-o output/pjlib-test-x86_64-unknown-linux-gnu/udp_echo_srv_sync.o \
# 	../src/pjlib-test/udp_echo_srv_sync.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include \
# 	-o output/pjlib-test-x86_64-unknown-linux-gnu/udp_echo_srv_ioqueue.o \
# 	../src/pjlib-test/udp_echo_srv_ioqueue.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include \
# 	-o output/pjlib-test-x86_64-unknown-linux-gnu/util.o \
# 	../src/pjlib-test/util.c 
# if test ! -d ../bin; then mkdir -p ../bin; fi
# gcc -o ../bin/pjlib-test-x86_64-unknown-linux-gnu \
#      output/pjlib-test-x86_64-unknown-linux-gnu/main.o  output/pjlib-test-x86_64-unknown-linux-gnu/activesock.o  output/pjlib-test-x86_64-unknown-linux-gnu/atomic.o  output/pjlib-test-x86_64-unknown-linux-gnu/echo_clt.o  output/pjlib-test-x86_64-unknown-linux-gnu/errno.o  output/pjlib-test-x86_64-unknown-linux-gnu/exception.o  output/pjlib-test-x86_64-unknown-linux-gnu/fifobuf.o  output/pjlib-test-x86_64-unknown-linux-gnu/file.o  output/pjlib-test-x86_64-unknown-linux-gnu/hash_test.o  output/pjlib-test-x86_64-unknown-linux-gnu/ioq_perf.o  output/pjlib-test-x86_64-unknown-linux-gnu/ioq_udp.o  output/pjlib-test-x86_64-unknown-linux-gnu/ioq_unreg.o  output/pjlib-test-x86_64-unknown-linux-gnu/ioq_tcp.o  output/pjlib-test-x86_64-unknown-linux-gnu/list.o  output/pjlib-test-x86_64-unknown-linux-gnu/mutex.o  output/pjlib-test-x86_64-unknown-linux-gnu/os.o  output/pjlib-test-x86_64-unknown-linux-gnu/pool.o  output/pjlib-test-x86_64-unknown-linux-gnu/pool_perf.o  output/pjlib-test-x86_64-unknown-linux-gnu/rand.o  output/pjlib-test-x86_64-unknown-linux-gnu/rbtree.o  output/pjlib-test-x86_64-unknown-linux-gnu/select.o  output/pjlib-test-x86_64-unknown-linux-gnu/sleep.o  output/pjlib-test-x86_64-unknown-linux-gnu/sock.o  output/pjlib-test-x86_64-unknown-linux-gnu/sock_perf.o  output/pjlib-test-x86_64-unknown-linux-gnu/ssl_sock.o  output/pjlib-test-x86_64-unknown-linux-gnu/string.o  output/pjlib-test-x86_64-unknown-linux-gnu/test.o  output/pjlib-test-x86_64-unknown-linux-gnu/thread.o  output/pjlib-test-x86_64-unknown-linux-gnu/timer.o  output/pjlib-test-x86_64-unknown-linux-gnu/timestamp.o  output/pjlib-test-x86_64-unknown-linux-gnu/udp_echo_srv_sync.o  output/pjlib-test-x86_64-unknown-linux-gnu/udp_echo_srv_ioqueue.o  output/pjlib-test-x86_64-unknown-linux-gnu/util.o -lpj-x86_64-unknown-linux-gnu  -lssl -lcrypto -luuid -lm -lrt -lpthread  -lasound -lSDL2     -L/home/vsedyshev/Work/1111/pjproject/pjlib/lib -L/home/vsedyshev/Work/1111/pjproject/pjlib-util/lib -L/home/vsedyshev/Work/1111/pjproject/pjnath/lib -L/home/vsedyshev/Work/1111/pjproject/pjmedia/lib -L/home/vsedyshev/Work/1111/pjproject/pjsip/lib -L/home/vsedyshev/Work/1111/pjproject/third_party/lib -lSDL2     -lSDL2       
# make[2]: Leaving directory '/home/vsedyshev/Work/1111/pjproject/pjlib/build'
# make[1]: Leaving directory '/home/vsedyshev/Work/1111/pjproject/pjlib/build'
# make[1]: Entering directory '/home/vsedyshev/Work/1111/pjproject/pjlib-util/build'
# make -f /home/vsedyshev/Work/1111/pjproject/build/rules.mak APP=PJLIB_UTIL app=pjlib-util ../lib/libpjlib-util-x86_64-unknown-linux-gnu.a
# make[2]: Entering directory '/home/vsedyshev/Work/1111/pjproject/pjlib-util/build'
# mkdir -p output/pjlib-util-x86_64-unknown-linux-gnu/
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include -I../../pjlib/include \
# 	-o output/pjlib-util-x86_64-unknown-linux-gnu/base64.o \
# 	../src/pjlib-util/base64.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include -I../../pjlib/include \
# 	-o output/pjlib-util-x86_64-unknown-linux-gnu/cli.o \
# 	../src/pjlib-util/cli.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include -I../../pjlib/include \
# 	-o output/pjlib-util-x86_64-unknown-linux-gnu/cli_console.o \
# 	../src/pjlib-util/cli_console.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include -I../../pjlib/include \
# 	-o output/pjlib-util-x86_64-unknown-linux-gnu/cli_telnet.o \
# 	../src/pjlib-util/cli_telnet.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include -I../../pjlib/include \
# 	-o output/pjlib-util-x86_64-unknown-linux-gnu/crc32.o \
# 	../src/pjlib-util/crc32.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include -I../../pjlib/include \
# 	-o output/pjlib-util-x86_64-unknown-linux-gnu/errno.o \
# 	../src/pjlib-util/errno.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include -I../../pjlib/include \
# 	-o output/pjlib-util-x86_64-unknown-linux-gnu/dns.o \
# 	../src/pjlib-util/dns.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include -I../../pjlib/include \
# 	-o output/pjlib-util-x86_64-unknown-linux-gnu/dns_dump.o \
# 	../src/pjlib-util/dns_dump.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include -I../../pjlib/include \
# 	-o output/pjlib-util-x86_64-unknown-linux-gnu/dns_server.o \
# 	../src/pjlib-util/dns_server.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include -I../../pjlib/include \
# 	-o output/pjlib-util-x86_64-unknown-linux-gnu/getopt.o \
# 	../src/pjlib-util/getopt.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include -I../../pjlib/include \
# 	-o output/pjlib-util-x86_64-unknown-linux-gnu/hmac_md5.o \
# 	../src/pjlib-util/hmac_md5.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include -I../../pjlib/include \
# 	-o output/pjlib-util-x86_64-unknown-linux-gnu/hmac_sha1.o \
# 	../src/pjlib-util/hmac_sha1.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include -I../../pjlib/include \
# 	-o output/pjlib-util-x86_64-unknown-linux-gnu/http_client.o \
# 	../src/pjlib-util/http_client.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include -I../../pjlib/include \
# 	-o output/pjlib-util-x86_64-unknown-linux-gnu/json.o \
# 	../src/pjlib-util/json.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include -I../../pjlib/include \
# 	-o output/pjlib-util-x86_64-unknown-linux-gnu/md5.o \
# 	../src/pjlib-util/md5.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include -I../../pjlib/include \
# 	-o output/pjlib-util-x86_64-unknown-linux-gnu/pcap.o \
# 	../src/pjlib-util/pcap.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include -I../../pjlib/include \
# 	-o output/pjlib-util-x86_64-unknown-linux-gnu/resolver.o \
# 	../src/pjlib-util/resolver.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include -I../../pjlib/include \
# 	-o output/pjlib-util-x86_64-unknown-linux-gnu/scanner.o \
# 	../src/pjlib-util/scanner.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include -I../../pjlib/include \
# 	-o output/pjlib-util-x86_64-unknown-linux-gnu/sha1.o \
# 	../src/pjlib-util/sha1.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include -I../../pjlib/include \
# 	-o output/pjlib-util-x86_64-unknown-linux-gnu/srv_resolver.o \
# 	../src/pjlib-util/srv_resolver.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include -I../../pjlib/include \
# 	-o output/pjlib-util-x86_64-unknown-linux-gnu/string.o \
# 	../src/pjlib-util/string.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include -I../../pjlib/include \
# 	-o output/pjlib-util-x86_64-unknown-linux-gnu/stun_simple.o \
# 	../src/pjlib-util/stun_simple.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include -I../../pjlib/include \
# 	-o output/pjlib-util-x86_64-unknown-linux-gnu/stun_simple_client.o \
# 	../src/pjlib-util/stun_simple_client.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include -I../../pjlib/include \
# 	-o output/pjlib-util-x86_64-unknown-linux-gnu/xml.o \
# 	../src/pjlib-util/xml.c 
# if test ! -d ../lib; then mkdir -p ../lib; fi
# ar rv ../lib/libpjlib-util-x86_64-unknown-linux-gnu.a  output/pjlib-util-x86_64-unknown-linux-gnu/base64.o  output/pjlib-util-x86_64-unknown-linux-gnu/cli.o  output/pjlib-util-x86_64-unknown-linux-gnu/cli_console.o  output/pjlib-util-x86_64-unknown-linux-gnu/cli_telnet.o  output/pjlib-util-x86_64-unknown-linux-gnu/crc32.o  output/pjlib-util-x86_64-unknown-linux-gnu/errno.o  output/pjlib-util-x86_64-unknown-linux-gnu/dns.o  output/pjlib-util-x86_64-unknown-linux-gnu/dns_dump.o  output/pjlib-util-x86_64-unknown-linux-gnu/dns_server.o  output/pjlib-util-x86_64-unknown-linux-gnu/getopt.o  output/pjlib-util-x86_64-unknown-linux-gnu/hmac_md5.o  output/pjlib-util-x86_64-unknown-linux-gnu/hmac_sha1.o  output/pjlib-util-x86_64-unknown-linux-gnu/http_client.o  output/pjlib-util-x86_64-unknown-linux-gnu/json.o  output/pjlib-util-x86_64-unknown-linux-gnu/md5.o  output/pjlib-util-x86_64-unknown-linux-gnu/pcap.o  output/pjlib-util-x86_64-unknown-linux-gnu/resolver.o  output/pjlib-util-x86_64-unknown-linux-gnu/scanner.o  output/pjlib-util-x86_64-unknown-linux-gnu/sha1.o  output/pjlib-util-x86_64-unknown-linux-gnu/srv_resolver.o  output/pjlib-util-x86_64-unknown-linux-gnu/string.o  output/pjlib-util-x86_64-unknown-linux-gnu/stun_simple.o  output/pjlib-util-x86_64-unknown-linux-gnu/stun_simple_client.o  output/pjlib-util-x86_64-unknown-linux-gnu/xml.o
# r - output/pjlib-util-x86_64-unknown-linux-gnu/base64.o
# r - output/pjlib-util-x86_64-unknown-linux-gnu/cli.o
# r - output/pjlib-util-x86_64-unknown-linux-gnu/cli_console.o
# r - output/pjlib-util-x86_64-unknown-linux-gnu/cli_telnet.o
# r - output/pjlib-util-x86_64-unknown-linux-gnu/crc32.o
# r - output/pjlib-util-x86_64-unknown-linux-gnu/errno.o
# r - output/pjlib-util-x86_64-unknown-linux-gnu/dns.o
# r - output/pjlib-util-x86_64-unknown-linux-gnu/dns_dump.o
# r - output/pjlib-util-x86_64-unknown-linux-gnu/dns_server.o
# r - output/pjlib-util-x86_64-unknown-linux-gnu/getopt.o
# r - output/pjlib-util-x86_64-unknown-linux-gnu/hmac_md5.o
# r - output/pjlib-util-x86_64-unknown-linux-gnu/hmac_sha1.o
# r - output/pjlib-util-x86_64-unknown-linux-gnu/http_client.o
# r - output/pjlib-util-x86_64-unknown-linux-gnu/json.o
# r - output/pjlib-util-x86_64-unknown-linux-gnu/md5.o
# r - output/pjlib-util-x86_64-unknown-linux-gnu/pcap.o
# r - output/pjlib-util-x86_64-unknown-linux-gnu/resolver.o
# r - output/pjlib-util-x86_64-unknown-linux-gnu/scanner.o
# r - output/pjlib-util-x86_64-unknown-linux-gnu/sha1.o
# r - output/pjlib-util-x86_64-unknown-linux-gnu/srv_resolver.o
# r - output/pjlib-util-x86_64-unknown-linux-gnu/string.o
# r - output/pjlib-util-x86_64-unknown-linux-gnu/stun_simple.o
# r - output/pjlib-util-x86_64-unknown-linux-gnu/stun_simple_client.o
# r - output/pjlib-util-x86_64-unknown-linux-gnu/xml.o
# ranlib ../lib/libpjlib-util-x86_64-unknown-linux-gnu.a
# make[2]: Leaving directory '/home/vsedyshev/Work/1111/pjproject/pjlib-util/build'
# make -f /home/vsedyshev/Work/1111/pjproject/build/rules.mak APP=UTIL_TEST app=pjlib-util-test ../bin/pjlib-util-test-x86_64-unknown-linux-gnu
# make[2]: Entering directory '/home/vsedyshev/Work/1111/pjproject/pjlib-util/build'
# mkdir -p output/pjlib-util-test-x86_64-unknown-linux-gnu/
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include -I../../pjlib/include \
# 	-o output/pjlib-util-test-x86_64-unknown-linux-gnu/main.o \
# 	../src/pjlib-util-test/main.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include -I../../pjlib/include \
# 	-o output/pjlib-util-test-x86_64-unknown-linux-gnu/xml.o \
# 	../src/pjlib-util-test/xml.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include -I../../pjlib/include \
# 	-o output/pjlib-util-test-x86_64-unknown-linux-gnu/encryption.o \
# 	../src/pjlib-util-test/encryption.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include -I../../pjlib/include \
# 	-o output/pjlib-util-test-x86_64-unknown-linux-gnu/stun.o \
# 	../src/pjlib-util-test/stun.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include -I../../pjlib/include \
# 	-o output/pjlib-util-test-x86_64-unknown-linux-gnu/resolver_test.o \
# 	../src/pjlib-util-test/resolver_test.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include -I../../pjlib/include \
# 	-o output/pjlib-util-test-x86_64-unknown-linux-gnu/test.o \
# 	../src/pjlib-util-test/test.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include -I../../pjlib/include \
# 	-o output/pjlib-util-test-x86_64-unknown-linux-gnu/json_test.o \
# 	../src/pjlib-util-test/json_test.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include -I../../pjlib/include \
# 	-o output/pjlib-util-test-x86_64-unknown-linux-gnu/http_client.o \
# 	../src/pjlib-util-test/http_client.c 
# if test ! -d ../bin; then mkdir -p ../bin; fi
# gcc -o ../bin/pjlib-util-test-x86_64-unknown-linux-gnu \
#      output/pjlib-util-test-x86_64-unknown-linux-gnu/main.o  output/pjlib-util-test-x86_64-unknown-linux-gnu/xml.o  output/pjlib-util-test-x86_64-unknown-linux-gnu/encryption.o  output/pjlib-util-test-x86_64-unknown-linux-gnu/stun.o  output/pjlib-util-test-x86_64-unknown-linux-gnu/resolver_test.o  output/pjlib-util-test-x86_64-unknown-linux-gnu/test.o  output/pjlib-util-test-x86_64-unknown-linux-gnu/json_test.o  output/pjlib-util-test-x86_64-unknown-linux-gnu/http_client.o -lpjlib-util-x86_64-unknown-linux-gnu -lpj-x86_64-unknown-linux-gnu  -lssl -lcrypto -luuid -lm -lrt -lpthread  -lasound -lSDL2     -L/home/vsedyshev/Work/1111/pjproject/pjlib/lib -L/home/vsedyshev/Work/1111/pjproject/pjlib-util/lib -L/home/vsedyshev/Work/1111/pjproject/pjnath/lib -L/home/vsedyshev/Work/1111/pjproject/pjmedia/lib -L/home/vsedyshev/Work/1111/pjproject/pjsip/lib -L/home/vsedyshev/Work/1111/pjproject/third_party/lib -lSDL2     -lSDL2      
# make[2]: Leaving directory '/home/vsedyshev/Work/1111/pjproject/pjlib-util/build'
# make[1]: Leaving directory '/home/vsedyshev/Work/1111/pjproject/pjlib-util/build'
# make[1]: Entering directory '/home/vsedyshev/Work/1111/pjproject/pjnath/build'
# make -f /home/vsedyshev/Work/1111/pjproject/build/rules.mak APP=PJNATH app=pjnath ../lib/libpjnath-x86_64-unknown-linux-gnu.a
# make[2]: Entering directory '/home/vsedyshev/Work/1111/pjproject/pjnath/build'
# mkdir -p output/pjnath-x86_64-unknown-linux-gnu/
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include -I../../pjlib/include -I../../pjlib-util/include \
# 	-o output/pjnath-x86_64-unknown-linux-gnu/errno.o \
# 	../src/pjnath/errno.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include -I../../pjlib/include -I../../pjlib-util/include \
# 	-o output/pjnath-x86_64-unknown-linux-gnu/ice_session.o \
# 	../src/pjnath/ice_session.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include -I../../pjlib/include -I../../pjlib-util/include \
# 	-o output/pjnath-x86_64-unknown-linux-gnu/ice_strans.o \
# 	../src/pjnath/ice_strans.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include -I../../pjlib/include -I../../pjlib-util/include \
# 	-o output/pjnath-x86_64-unknown-linux-gnu/nat_detect.o \
# 	../src/pjnath/nat_detect.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include -I../../pjlib/include -I../../pjlib-util/include \
# 	-o output/pjnath-x86_64-unknown-linux-gnu/stun_auth.o \
# 	../src/pjnath/stun_auth.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include -I../../pjlib/include -I../../pjlib-util/include \
# 	-o output/pjnath-x86_64-unknown-linux-gnu/stun_msg.o \
# 	../src/pjnath/stun_msg.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include -I../../pjlib/include -I../../pjlib-util/include \
# 	-o output/pjnath-x86_64-unknown-linux-gnu/stun_msg_dump.o \
# 	../src/pjnath/stun_msg_dump.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include -I../../pjlib/include -I../../pjlib-util/include \
# 	-o output/pjnath-x86_64-unknown-linux-gnu/stun_session.o \
# 	../src/pjnath/stun_session.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include -I../../pjlib/include -I../../pjlib-util/include \
# 	-o output/pjnath-x86_64-unknown-linux-gnu/stun_sock.o \
# 	../src/pjnath/stun_sock.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include -I../../pjlib/include -I../../pjlib-util/include \
# 	-o output/pjnath-x86_64-unknown-linux-gnu/stun_transaction.o \
# 	../src/pjnath/stun_transaction.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include -I../../pjlib/include -I../../pjlib-util/include \
# 	-o output/pjnath-x86_64-unknown-linux-gnu/turn_session.o \
# 	../src/pjnath/turn_session.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include -I../../pjlib/include -I../../pjlib-util/include \
# 	-o output/pjnath-x86_64-unknown-linux-gnu/turn_sock.o \
# 	../src/pjnath/turn_sock.c 
# if test ! -d ../lib; then mkdir -p ../lib; fi
# ar rv ../lib/libpjnath-x86_64-unknown-linux-gnu.a  output/pjnath-x86_64-unknown-linux-gnu/errno.o  output/pjnath-x86_64-unknown-linux-gnu/ice_session.o  output/pjnath-x86_64-unknown-linux-gnu/ice_strans.o  output/pjnath-x86_64-unknown-linux-gnu/nat_detect.o  output/pjnath-x86_64-unknown-linux-gnu/stun_auth.o  output/pjnath-x86_64-unknown-linux-gnu/stun_msg.o  output/pjnath-x86_64-unknown-linux-gnu/stun_msg_dump.o  output/pjnath-x86_64-unknown-linux-gnu/stun_session.o  output/pjnath-x86_64-unknown-linux-gnu/stun_sock.o  output/pjnath-x86_64-unknown-linux-gnu/stun_transaction.o  output/pjnath-x86_64-unknown-linux-gnu/turn_session.o  output/pjnath-x86_64-unknown-linux-gnu/turn_sock.o
# r - output/pjnath-x86_64-unknown-linux-gnu/errno.o
# r - output/pjnath-x86_64-unknown-linux-gnu/ice_session.o
# r - output/pjnath-x86_64-unknown-linux-gnu/ice_strans.o
# r - output/pjnath-x86_64-unknown-linux-gnu/nat_detect.o
# r - output/pjnath-x86_64-unknown-linux-gnu/stun_auth.o
# r - output/pjnath-x86_64-unknown-linux-gnu/stun_msg.o
# r - output/pjnath-x86_64-unknown-linux-gnu/stun_msg_dump.o
# r - output/pjnath-x86_64-unknown-linux-gnu/stun_session.o
# r - output/pjnath-x86_64-unknown-linux-gnu/stun_sock.o
# r - output/pjnath-x86_64-unknown-linux-gnu/stun_transaction.o
# r - output/pjnath-x86_64-unknown-linux-gnu/turn_session.o
# r - output/pjnath-x86_64-unknown-linux-gnu/turn_sock.o
# ranlib ../lib/libpjnath-x86_64-unknown-linux-gnu.a
# make[2]: Leaving directory '/home/vsedyshev/Work/1111/pjproject/pjnath/build'
# make -f /home/vsedyshev/Work/1111/pjproject/build/rules.mak APP=PJNATH_TEST app=pjnath-test ../bin/pjnath-test-x86_64-unknown-linux-gnu
# make[2]: Entering directory '/home/vsedyshev/Work/1111/pjproject/pjnath/build'
# mkdir -p output/pjnath-test-x86_64-unknown-linux-gnu/
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include -I../../pjlib/include -I../../pjlib-util/include \
# 	-o output/pjnath-test-x86_64-unknown-linux-gnu/main.o \
# 	../src/pjnath-test/main.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include -I../../pjlib/include -I../../pjlib-util/include \
# 	-o output/pjnath-test-x86_64-unknown-linux-gnu/ice_test.o \
# 	../src/pjnath-test/ice_test.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include -I../../pjlib/include -I../../pjlib-util/include \
# 	-o output/pjnath-test-x86_64-unknown-linux-gnu/stun.o \
# 	../src/pjnath-test/stun.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include -I../../pjlib/include -I../../pjlib-util/include \
# 	-o output/pjnath-test-x86_64-unknown-linux-gnu/sess_auth.o \
# 	../src/pjnath-test/sess_auth.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include -I../../pjlib/include -I../../pjlib-util/include \
# 	-o output/pjnath-test-x86_64-unknown-linux-gnu/server.o \
# 	../src/pjnath-test/server.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include -I../../pjlib/include -I../../pjlib-util/include \
# 	-o output/pjnath-test-x86_64-unknown-linux-gnu/concur_test.o \
# 	../src/pjnath-test/concur_test.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include -I../../pjlib/include -I../../pjlib-util/include \
# 	-o output/pjnath-test-x86_64-unknown-linux-gnu/stun_sock_test.o \
# 	../src/pjnath-test/stun_sock_test.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include -I../../pjlib/include -I../../pjlib-util/include \
# 	-o output/pjnath-test-x86_64-unknown-linux-gnu/turn_sock_test.o \
# 	../src/pjnath-test/turn_sock_test.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include -I../../pjlib/include -I../../pjlib-util/include \
# 	-o output/pjnath-test-x86_64-unknown-linux-gnu/test.o \
# 	../src/pjnath-test/test.c 
# if test ! -d ../bin; then mkdir -p ../bin; fi
# gcc -o ../bin/pjnath-test-x86_64-unknown-linux-gnu \
#      output/pjnath-test-x86_64-unknown-linux-gnu/main.o  output/pjnath-test-x86_64-unknown-linux-gnu/ice_test.o  output/pjnath-test-x86_64-unknown-linux-gnu/stun.o  output/pjnath-test-x86_64-unknown-linux-gnu/sess_auth.o  output/pjnath-test-x86_64-unknown-linux-gnu/server.o  output/pjnath-test-x86_64-unknown-linux-gnu/concur_test.o  output/pjnath-test-x86_64-unknown-linux-gnu/stun_sock_test.o  output/pjnath-test-x86_64-unknown-linux-gnu/turn_sock_test.o  output/pjnath-test-x86_64-unknown-linux-gnu/test.o -lpjnath-x86_64-unknown-linux-gnu -lpjlib-util-x86_64-unknown-linux-gnu -lpj-x86_64-unknown-linux-gnu  -lssl -lcrypto -luuid -lm -lrt -lpthread  -lasound -lSDL2     -L/home/vsedyshev/Work/1111/pjproject/pjlib/lib -L/home/vsedyshev/Work/1111/pjproject/pjlib-util/lib -L/home/vsedyshev/Work/1111/pjproject/pjnath/lib -L/home/vsedyshev/Work/1111/pjproject/pjmedia/lib -L/home/vsedyshev/Work/1111/pjproject/pjsip/lib -L/home/vsedyshev/Work/1111/pjproject/third_party/lib -lSDL2     -lSDL2       
# make[2]: Leaving directory '/home/vsedyshev/Work/1111/pjproject/pjnath/build'
# make -f /home/vsedyshev/Work/1111/pjproject/build/rules.mak APP=PJTURN_CLIENT app=pjturn-client ../bin/pjturn-client-x86_64-unknown-linux-gnu
# make[2]: Entering directory '/home/vsedyshev/Work/1111/pjproject/pjnath/build'
# mkdir -p output/pjturn-client-x86_64-unknown-linux-gnu/
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include -I../../pjlib/include -I../../pjlib-util/include \
# 	-o output/pjturn-client-x86_64-unknown-linux-gnu/client_main.o \
# 	../src/pjturn-client/client_main.c 
# if test ! -d ../bin; then mkdir -p ../bin; fi
# gcc -o ../bin/pjturn-client-x86_64-unknown-linux-gnu \
#      output/pjturn-client-x86_64-unknown-linux-gnu/client_main.o -lpjnath-x86_64-unknown-linux-gnu -lpjlib-util-x86_64-unknown-linux-gnu -lpj-x86_64-unknown-linux-gnu  -lssl -lcrypto -luuid -lm -lrt -lpthread  -lasound -lSDL2     -L/home/vsedyshev/Work/1111/pjproject/pjlib/lib -L/home/vsedyshev/Work/1111/pjproject/pjlib-util/lib -L/home/vsedyshev/Work/1111/pjproject/pjnath/lib -L/home/vsedyshev/Work/1111/pjproject/pjmedia/lib -L/home/vsedyshev/Work/1111/pjproject/pjsip/lib -L/home/vsedyshev/Work/1111/pjproject/third_party/lib -lSDL2     -lSDL2       
# make[2]: Leaving directory '/home/vsedyshev/Work/1111/pjproject/pjnath/build'
# make -f /home/vsedyshev/Work/1111/pjproject/build/rules.mak APP=PJTURN_SRV app=pjturn-srv ../bin/pjturn-srv-x86_64-unknown-linux-gnu
# make[2]: Entering directory '/home/vsedyshev/Work/1111/pjproject/pjnath/build'
# mkdir -p output/pjturn-srv-x86_64-unknown-linux-gnu/
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include -I../../pjlib/include -I../../pjlib-util/include \
# 	-o output/pjturn-srv-x86_64-unknown-linux-gnu/allocation.o \
# 	../src/pjturn-srv/allocation.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include -I../../pjlib/include -I../../pjlib-util/include \
# 	-o output/pjturn-srv-x86_64-unknown-linux-gnu/auth.o \
# 	../src/pjturn-srv/auth.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include -I../../pjlib/include -I../../pjlib-util/include \
# 	-o output/pjturn-srv-x86_64-unknown-linux-gnu/listener_udp.o \
# 	../src/pjturn-srv/listener_udp.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include -I../../pjlib/include -I../../pjlib-util/include \
# 	-o output/pjturn-srv-x86_64-unknown-linux-gnu/listener_tcp.o \
# 	../src/pjturn-srv/listener_tcp.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include -I../../pjlib/include -I../../pjlib-util/include \
# 	-o output/pjturn-srv-x86_64-unknown-linux-gnu/server.o \
# 	../src/pjturn-srv/server.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include -I../../pjlib/include -I../../pjlib-util/include \
# 	-o output/pjturn-srv-x86_64-unknown-linux-gnu/main.o \
# 	../src/pjturn-srv/main.c 
# if test ! -d ../bin; then mkdir -p ../bin; fi
# gcc -o ../bin/pjturn-srv-x86_64-unknown-linux-gnu \
#      output/pjturn-srv-x86_64-unknown-linux-gnu/allocation.o  output/pjturn-srv-x86_64-unknown-linux-gnu/auth.o  output/pjturn-srv-x86_64-unknown-linux-gnu/listener_udp.o  output/pjturn-srv-x86_64-unknown-linux-gnu/listener_tcp.o  output/pjturn-srv-x86_64-unknown-linux-gnu/server.o  output/pjturn-srv-x86_64-unknown-linux-gnu/main.o -lpjnath-x86_64-unknown-linux-gnu -lpjlib-util-x86_64-unknown-linux-gnu -lpj-x86_64-unknown-linux-gnu  -lssl -lcrypto -luuid -lm -lrt -lpthread  -lasound -lSDL2     -L/home/vsedyshev/Work/1111/pjproject/pjlib/lib -L/home/vsedyshev/Work/1111/pjproject/pjlib-util/lib -L/home/vsedyshev/Work/1111/pjproject/pjnath/lib -L/home/vsedyshev/Work/1111/pjproject/pjmedia/lib -L/home/vsedyshev/Work/1111/pjproject/pjsip/lib -L/home/vsedyshev/Work/1111/pjproject/third_party/lib -lSDL2     -lSDL2       
# make[2]: Leaving directory '/home/vsedyshev/Work/1111/pjproject/pjnath/build'
# make[1]: Leaving directory '/home/vsedyshev/Work/1111/pjproject/pjnath/build'
# make[1]: Entering directory '/home/vsedyshev/Work/1111/pjproject/third_party/build'
# for dir in  gsm ilbc speex g7221 srtp resample yuv webrtc; do \
# 	if make  -C $dir all; then \
# 	    true; \
# 	else \
# 	    exit 1; \
# 	fi; \
# done
# make[2]: Entering directory '/home/vsedyshev/Work/1111/pjproject/third_party/build/gsm'
# make -f /home/vsedyshev/Work/1111/pjproject/build/rules.mak APP=GSM_CODEC app=libgsmcodec ../../lib/libgsmcodec-x86_64-unknown-linux-gnu.a
# make[3]: Entering directory '/home/vsedyshev/Work/1111/pjproject/third_party/build/gsm'
# mkdir -p output/libgsmcodec-x86_64-unknown-linux-gnu/
# gcc -c -DSASR -DWAV49 -DNeedFunctionPrototypes=1 -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I. -I../../gsm/inc -I../../../pjlib/include \
# 	-o output/libgsmcodec-x86_64-unknown-linux-gnu/add.o \
# 	../../gsm/src/add.c 
# gcc -c -DSASR -DWAV49 -DNeedFunctionPrototypes=1 -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I. -I../../gsm/inc -I../../../pjlib/include \
# 	-o output/libgsmcodec-x86_64-unknown-linux-gnu/code.o \
# 	../../gsm/src/code.c 
# gcc -c -DSASR -DWAV49 -DNeedFunctionPrototypes=1 -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I. -I../../gsm/inc -I../../../pjlib/include \
# 	-o output/libgsmcodec-x86_64-unknown-linux-gnu/decode.o \
# 	../../gsm/src/decode.c 
# gcc -c -DSASR -DWAV49 -DNeedFunctionPrototypes=1 -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I. -I../../gsm/inc -I../../../pjlib/include \
# 	-o output/libgsmcodec-x86_64-unknown-linux-gnu/gsm_create.o \
# 	../../gsm/src/gsm_create.c 
# gcc -c -DSASR -DWAV49 -DNeedFunctionPrototypes=1 -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I. -I../../gsm/inc -I../../../pjlib/include \
# 	-o output/libgsmcodec-x86_64-unknown-linux-gnu/gsm_decode.o \
# 	../../gsm/src/gsm_decode.c 
# gcc -c -DSASR -DWAV49 -DNeedFunctionPrototypes=1 -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I. -I../../gsm/inc -I../../../pjlib/include \
# 	-o output/libgsmcodec-x86_64-unknown-linux-gnu/gsm_destroy.o \
# 	../../gsm/src/gsm_destroy.c 
# gcc -c -DSASR -DWAV49 -DNeedFunctionPrototypes=1 -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I. -I../../gsm/inc -I../../../pjlib/include \
# 	-o output/libgsmcodec-x86_64-unknown-linux-gnu/gsm_encode.o \
# 	../../gsm/src/gsm_encode.c 
# gcc -c -DSASR -DWAV49 -DNeedFunctionPrototypes=1 -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I. -I../../gsm/inc -I../../../pjlib/include \
# 	-o output/libgsmcodec-x86_64-unknown-linux-gnu/gsm_explode.o \
# 	../../gsm/src/gsm_explode.c 
# gcc -c -DSASR -DWAV49 -DNeedFunctionPrototypes=1 -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I. -I../../gsm/inc -I../../../pjlib/include \
# 	-o output/libgsmcodec-x86_64-unknown-linux-gnu/gsm_implode.o \
# 	../../gsm/src/gsm_implode.c 
# gcc -c -DSASR -DWAV49 -DNeedFunctionPrototypes=1 -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I. -I../../gsm/inc -I../../../pjlib/include \
# 	-o output/libgsmcodec-x86_64-unknown-linux-gnu/gsm_option.o \
# 	../../gsm/src/gsm_option.c 
# gcc -c -DSASR -DWAV49 -DNeedFunctionPrototypes=1 -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I. -I../../gsm/inc -I../../../pjlib/include \
# 	-o output/libgsmcodec-x86_64-unknown-linux-gnu/long_term.o \
# 	../../gsm/src/long_term.c 
# gcc -c -DSASR -DWAV49 -DNeedFunctionPrototypes=1 -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I. -I../../gsm/inc -I../../../pjlib/include \
# 	-o output/libgsmcodec-x86_64-unknown-linux-gnu/lpc.o \
# 	../../gsm/src/lpc.c 
# gcc -c -DSASR -DWAV49 -DNeedFunctionPrototypes=1 -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I. -I../../gsm/inc -I../../../pjlib/include \
# 	-o output/libgsmcodec-x86_64-unknown-linux-gnu/preprocess.o \
# 	../../gsm/src/preprocess.c 
# gcc -c -DSASR -DWAV49 -DNeedFunctionPrototypes=1 -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I. -I../../gsm/inc -I../../../pjlib/include \
# 	-o output/libgsmcodec-x86_64-unknown-linux-gnu/rpe.o \
# 	../../gsm/src/rpe.c 
# gcc -c -DSASR -DWAV49 -DNeedFunctionPrototypes=1 -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I. -I../../gsm/inc -I../../../pjlib/include \
# 	-o output/libgsmcodec-x86_64-unknown-linux-gnu/short_term.o \
# 	../../gsm/src/short_term.c 
# gcc -c -DSASR -DWAV49 -DNeedFunctionPrototypes=1 -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I. -I../../gsm/inc -I../../../pjlib/include \
# 	-o output/libgsmcodec-x86_64-unknown-linux-gnu/table.o \
# 	../../gsm/src/table.c 
# if test ! -d ../../lib; then mkdir -p ../../lib; fi
# ar rv ../../lib/libgsmcodec-x86_64-unknown-linux-gnu.a  output/libgsmcodec-x86_64-unknown-linux-gnu/add.o  output/libgsmcodec-x86_64-unknown-linux-gnu/code.o  output/libgsmcodec-x86_64-unknown-linux-gnu/decode.o  output/libgsmcodec-x86_64-unknown-linux-gnu/gsm_create.o  output/libgsmcodec-x86_64-unknown-linux-gnu/gsm_decode.o  output/libgsmcodec-x86_64-unknown-linux-gnu/gsm_destroy.o  output/libgsmcodec-x86_64-unknown-linux-gnu/gsm_encode.o  output/libgsmcodec-x86_64-unknown-linux-gnu/gsm_explode.o  output/libgsmcodec-x86_64-unknown-linux-gnu/gsm_implode.o  output/libgsmcodec-x86_64-unknown-linux-gnu/gsm_option.o  output/libgsmcodec-x86_64-unknown-linux-gnu/long_term.o  output/libgsmcodec-x86_64-unknown-linux-gnu/lpc.o  output/libgsmcodec-x86_64-unknown-linux-gnu/preprocess.o  output/libgsmcodec-x86_64-unknown-linux-gnu/rpe.o  output/libgsmcodec-x86_64-unknown-linux-gnu/short_term.o  output/libgsmcodec-x86_64-unknown-linux-gnu/table.o
# r - output/libgsmcodec-x86_64-unknown-linux-gnu/add.o
# r - output/libgsmcodec-x86_64-unknown-linux-gnu/code.o
# r - output/libgsmcodec-x86_64-unknown-linux-gnu/decode.o
# r - output/libgsmcodec-x86_64-unknown-linux-gnu/gsm_create.o
# r - output/libgsmcodec-x86_64-unknown-linux-gnu/gsm_decode.o
# r - output/libgsmcodec-x86_64-unknown-linux-gnu/gsm_destroy.o
# r - output/libgsmcodec-x86_64-unknown-linux-gnu/gsm_encode.o
# r - output/libgsmcodec-x86_64-unknown-linux-gnu/gsm_explode.o
# r - output/libgsmcodec-x86_64-unknown-linux-gnu/gsm_implode.o
# r - output/libgsmcodec-x86_64-unknown-linux-gnu/gsm_option.o
# r - output/libgsmcodec-x86_64-unknown-linux-gnu/long_term.o
# r - output/libgsmcodec-x86_64-unknown-linux-gnu/lpc.o
# r - output/libgsmcodec-x86_64-unknown-linux-gnu/preprocess.o
# r - output/libgsmcodec-x86_64-unknown-linux-gnu/rpe.o
# r - output/libgsmcodec-x86_64-unknown-linux-gnu/short_term.o
# r - output/libgsmcodec-x86_64-unknown-linux-gnu/table.o
# ranlib ../../lib/libgsmcodec-x86_64-unknown-linux-gnu.a
# make[3]: Leaving directory '/home/vsedyshev/Work/1111/pjproject/third_party/build/gsm'
# make[2]: Leaving directory '/home/vsedyshev/Work/1111/pjproject/third_party/build/gsm'
# make[2]: Entering directory '/home/vsedyshev/Work/1111/pjproject/third_party/build/ilbc'
# make -f /home/vsedyshev/Work/1111/pjproject/build/rules.mak APP=ILBC app=libilbccodec ../../lib/libilbccodec-x86_64-unknown-linux-gnu.a
# make[3]: Entering directory '/home/vsedyshev/Work/1111/pjproject/third_party/build/ilbc'
# mkdir -p output/libilbccodec-x86_64-unknown-linux-gnu/
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I. -I../../ilbc -I../../../pjlib/include \
# 	-o output/libilbccodec-x86_64-unknown-linux-gnu/FrameClassify.o \
# 	../../ilbc/FrameClassify.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I. -I../../ilbc -I../../../pjlib/include \
# 	-o output/libilbccodec-x86_64-unknown-linux-gnu/LPCdecode.o \
# 	../../ilbc/LPCdecode.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I. -I../../ilbc -I../../../pjlib/include \
# 	-o output/libilbccodec-x86_64-unknown-linux-gnu/LPCencode.o \
# 	../../ilbc/LPCencode.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I. -I../../ilbc -I../../../pjlib/include \
# 	-o output/libilbccodec-x86_64-unknown-linux-gnu/StateConstructW.o \
# 	../../ilbc/StateConstructW.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I. -I../../ilbc -I../../../pjlib/include \
# 	-o output/libilbccodec-x86_64-unknown-linux-gnu/StateSearchW.o \
# 	../../ilbc/StateSearchW.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I. -I../../ilbc -I../../../pjlib/include \
# 	-o output/libilbccodec-x86_64-unknown-linux-gnu/anaFilter.o \
# 	../../ilbc/anaFilter.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I. -I../../ilbc -I../../../pjlib/include \
# 	-o output/libilbccodec-x86_64-unknown-linux-gnu/constants.o \
# 	../../ilbc/constants.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I. -I../../ilbc -I../../../pjlib/include \
# 	-o output/libilbccodec-x86_64-unknown-linux-gnu/createCB.o \
# 	../../ilbc/createCB.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I. -I../../ilbc -I../../../pjlib/include \
# 	-o output/libilbccodec-x86_64-unknown-linux-gnu/doCPLC.o \
# 	../../ilbc/doCPLC.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I. -I../../ilbc -I../../../pjlib/include \
# 	-o output/libilbccodec-x86_64-unknown-linux-gnu/enhancer.o \
# 	../../ilbc/enhancer.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I. -I../../ilbc -I../../../pjlib/include \
# 	-o output/libilbccodec-x86_64-unknown-linux-gnu/filter.o \
# 	../../ilbc/filter.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I. -I../../ilbc -I../../../pjlib/include \
# 	-o output/libilbccodec-x86_64-unknown-linux-gnu/gainquant.o \
# 	../../ilbc/gainquant.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I. -I../../ilbc -I../../../pjlib/include \
# 	-o output/libilbccodec-x86_64-unknown-linux-gnu/getCBvec.o \
# 	../../ilbc/getCBvec.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I. -I../../ilbc -I../../../pjlib/include \
# 	-o output/libilbccodec-x86_64-unknown-linux-gnu/helpfun.o \
# 	../../ilbc/helpfun.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I. -I../../ilbc -I../../../pjlib/include \
# 	-o output/libilbccodec-x86_64-unknown-linux-gnu/hpInput.o \
# 	../../ilbc/hpInput.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I. -I../../ilbc -I../../../pjlib/include \
# 	-o output/libilbccodec-x86_64-unknown-linux-gnu/hpOutput.o \
# 	../../ilbc/hpOutput.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I. -I../../ilbc -I../../../pjlib/include \
# 	-o output/libilbccodec-x86_64-unknown-linux-gnu/iCBConstruct.o \
# 	../../ilbc/iCBConstruct.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I. -I../../ilbc -I../../../pjlib/include \
# 	-o output/libilbccodec-x86_64-unknown-linux-gnu/iCBSearch.o \
# 	../../ilbc/iCBSearch.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I. -I../../ilbc -I../../../pjlib/include \
# 	-o output/libilbccodec-x86_64-unknown-linux-gnu/iLBC_decode.o \
# 	../../ilbc/iLBC_decode.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I. -I../../ilbc -I../../../pjlib/include \
# 	-o output/libilbccodec-x86_64-unknown-linux-gnu/iLBC_encode.o \
# 	../../ilbc/iLBC_encode.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I. -I../../ilbc -I../../../pjlib/include \
# 	-o output/libilbccodec-x86_64-unknown-linux-gnu/lsf.o \
# 	../../ilbc/lsf.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I. -I../../ilbc -I../../../pjlib/include \
# 	-o output/libilbccodec-x86_64-unknown-linux-gnu/packing.o \
# 	../../ilbc/packing.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I. -I../../ilbc -I../../../pjlib/include \
# 	-o output/libilbccodec-x86_64-unknown-linux-gnu/syntFilter.o \
# 	../../ilbc/syntFilter.c 
# if test ! -d ../../lib; then mkdir -p ../../lib; fi
# ar rv ../../lib/libilbccodec-x86_64-unknown-linux-gnu.a  output/libilbccodec-x86_64-unknown-linux-gnu/FrameClassify.o  output/libilbccodec-x86_64-unknown-linux-gnu/LPCdecode.o  output/libilbccodec-x86_64-unknown-linux-gnu/LPCencode.o  output/libilbccodec-x86_64-unknown-linux-gnu/StateConstructW.o  output/libilbccodec-x86_64-unknown-linux-gnu/StateSearchW.o  output/libilbccodec-x86_64-unknown-linux-gnu/anaFilter.o  output/libilbccodec-x86_64-unknown-linux-gnu/constants.o  output/libilbccodec-x86_64-unknown-linux-gnu/createCB.o  output/libilbccodec-x86_64-unknown-linux-gnu/doCPLC.o  output/libilbccodec-x86_64-unknown-linux-gnu/enhancer.o  output/libilbccodec-x86_64-unknown-linux-gnu/filter.o  output/libilbccodec-x86_64-unknown-linux-gnu/gainquant.o  output/libilbccodec-x86_64-unknown-linux-gnu/getCBvec.o  output/libilbccodec-x86_64-unknown-linux-gnu/helpfun.o  output/libilbccodec-x86_64-unknown-linux-gnu/hpInput.o  output/libilbccodec-x86_64-unknown-linux-gnu/hpOutput.o  output/libilbccodec-x86_64-unknown-linux-gnu/iCBConstruct.o  output/libilbccodec-x86_64-unknown-linux-gnu/iCBSearch.o  output/libilbccodec-x86_64-unknown-linux-gnu/iLBC_decode.o  output/libilbccodec-x86_64-unknown-linux-gnu/iLBC_encode.o  output/libilbccodec-x86_64-unknown-linux-gnu/lsf.o  output/libilbccodec-x86_64-unknown-linux-gnu/packing.o  output/libilbccodec-x86_64-unknown-linux-gnu/syntFilter.o
# r - output/libilbccodec-x86_64-unknown-linux-gnu/FrameClassify.o
# r - output/libilbccodec-x86_64-unknown-linux-gnu/LPCdecode.o
# r - output/libilbccodec-x86_64-unknown-linux-gnu/LPCencode.o
# r - output/libilbccodec-x86_64-unknown-linux-gnu/StateConstructW.o
# r - output/libilbccodec-x86_64-unknown-linux-gnu/StateSearchW.o
# r - output/libilbccodec-x86_64-unknown-linux-gnu/anaFilter.o
# r - output/libilbccodec-x86_64-unknown-linux-gnu/constants.o
# r - output/libilbccodec-x86_64-unknown-linux-gnu/createCB.o
# r - output/libilbccodec-x86_64-unknown-linux-gnu/doCPLC.o
# r - output/libilbccodec-x86_64-unknown-linux-gnu/enhancer.o
# r - output/libilbccodec-x86_64-unknown-linux-gnu/filter.o
# r - output/libilbccodec-x86_64-unknown-linux-gnu/gainquant.o
# r - output/libilbccodec-x86_64-unknown-linux-gnu/getCBvec.o
# r - output/libilbccodec-x86_64-unknown-linux-gnu/helpfun.o
# r - output/libilbccodec-x86_64-unknown-linux-gnu/hpInput.o
# r - output/libilbccodec-x86_64-unknown-linux-gnu/hpOutput.o
# r - output/libilbccodec-x86_64-unknown-linux-gnu/iCBConstruct.o
# r - output/libilbccodec-x86_64-unknown-linux-gnu/iCBSearch.o
# r - output/libilbccodec-x86_64-unknown-linux-gnu/iLBC_decode.o
# r - output/libilbccodec-x86_64-unknown-linux-gnu/iLBC_encode.o
# r - output/libilbccodec-x86_64-unknown-linux-gnu/lsf.o
# r - output/libilbccodec-x86_64-unknown-linux-gnu/packing.o
# r - output/libilbccodec-x86_64-unknown-linux-gnu/syntFilter.o
# ranlib ../../lib/libilbccodec-x86_64-unknown-linux-gnu.a
# make[3]: Leaving directory '/home/vsedyshev/Work/1111/pjproject/third_party/build/ilbc'
# make[2]: Leaving directory '/home/vsedyshev/Work/1111/pjproject/third_party/build/ilbc'
# make[2]: Entering directory '/home/vsedyshev/Work/1111/pjproject/third_party/build/speex'
# make -f /home/vsedyshev/Work/1111/pjproject/build/rules.mak APP=SPEEX app=libspeex ../../lib/libspeex-x86_64-unknown-linux-gnu.a
# make[3]: Entering directory '/home/vsedyshev/Work/1111/pjproject/third_party/build/speex'
# mkdir -p output/libspeex-x86_64-unknown-linux-gnu/
# gcc -c -DHAVE_CONFIG_H -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I. -I../../speex/include -I../../speex/libspeex -I../../../pjlib/include \
# 	-o output/libspeex-x86_64-unknown-linux-gnu/bits.o \
# 	../../speex/libspeex/bits.c 
# gcc -c -DHAVE_CONFIG_H -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I. -I../../speex/include -I../../speex/libspeex -I../../../pjlib/include \
# 	-o output/libspeex-x86_64-unknown-linux-gnu/cb_search.o \
# 	../../speex/libspeex/cb_search.c 
# gcc -c -DHAVE_CONFIG_H -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I. -I../../speex/include -I../../speex/libspeex -I../../../pjlib/include \
# 	-o output/libspeex-x86_64-unknown-linux-gnu/exc_10_16_table.o \
# 	../../speex/libspeex/exc_10_16_table.c 
# gcc -c -DHAVE_CONFIG_H -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I. -I../../speex/include -I../../speex/libspeex -I../../../pjlib/include \
# 	-o output/libspeex-x86_64-unknown-linux-gnu/exc_10_32_table.o \
# 	../../speex/libspeex/exc_10_32_table.c 
# gcc -c -DHAVE_CONFIG_H -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I. -I../../speex/include -I../../speex/libspeex -I../../../pjlib/include \
# 	-o output/libspeex-x86_64-unknown-linux-gnu/exc_20_32_table.o \
# 	../../speex/libspeex/exc_20_32_table.c 
# gcc -c -DHAVE_CONFIG_H -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I. -I../../speex/include -I../../speex/libspeex -I../../../pjlib/include \
# 	-o output/libspeex-x86_64-unknown-linux-gnu/exc_5_256_table.o \
# 	../../speex/libspeex/exc_5_256_table.c 
# gcc -c -DHAVE_CONFIG_H -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I. -I../../speex/include -I../../speex/libspeex -I../../../pjlib/include \
# 	-o output/libspeex-x86_64-unknown-linux-gnu/exc_5_64_table.o \
# 	../../speex/libspeex/exc_5_64_table.c 
# gcc -c -DHAVE_CONFIG_H -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I. -I../../speex/include -I../../speex/libspeex -I../../../pjlib/include \
# 	-o output/libspeex-x86_64-unknown-linux-gnu/exc_8_128_table.o \
# 	../../speex/libspeex/exc_8_128_table.c 
# gcc -c -DHAVE_CONFIG_H -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I. -I../../speex/include -I../../speex/libspeex -I../../../pjlib/include \
# 	-o output/libspeex-x86_64-unknown-linux-gnu/fftwrap.o \
# 	../../speex/libspeex/fftwrap.c 
# gcc -c -DHAVE_CONFIG_H -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I. -I../../speex/include -I../../speex/libspeex -I../../../pjlib/include \
# 	-o output/libspeex-x86_64-unknown-linux-gnu/filterbank.o \
# 	../../speex/libspeex/filterbank.c 
# gcc -c -DHAVE_CONFIG_H -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I. -I../../speex/include -I../../speex/libspeex -I../../../pjlib/include \
# 	-o output/libspeex-x86_64-unknown-linux-gnu/filters.o \
# 	../../speex/libspeex/filters.c 
# gcc -c -DHAVE_CONFIG_H -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I. -I../../speex/include -I../../speex/libspeex -I../../../pjlib/include \
# 	-o output/libspeex-x86_64-unknown-linux-gnu/gain_table.o \
# 	../../speex/libspeex/gain_table.c 
# gcc -c -DHAVE_CONFIG_H -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I. -I../../speex/include -I../../speex/libspeex -I../../../pjlib/include \
# 	-o output/libspeex-x86_64-unknown-linux-gnu/gain_table_lbr.o \
# 	../../speex/libspeex/gain_table_lbr.c 
# gcc -c -DHAVE_CONFIG_H -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I. -I../../speex/include -I../../speex/libspeex -I../../../pjlib/include \
# 	-o output/libspeex-x86_64-unknown-linux-gnu/hexc_10_32_table.o \
# 	../../speex/libspeex/hexc_10_32_table.c 
# gcc -c -DHAVE_CONFIG_H -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I. -I../../speex/include -I../../speex/libspeex -I../../../pjlib/include \
# 	-o output/libspeex-x86_64-unknown-linux-gnu/hexc_table.o \
# 	../../speex/libspeex/hexc_table.c 
# gcc -c -DHAVE_CONFIG_H -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I. -I../../speex/include -I../../speex/libspeex -I../../../pjlib/include \
# 	-o output/libspeex-x86_64-unknown-linux-gnu/high_lsp_tables.o \
# 	../../speex/libspeex/high_lsp_tables.c 
# gcc -c -DHAVE_CONFIG_H -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I. -I../../speex/include -I../../speex/libspeex -I../../../pjlib/include \
# 	-o output/libspeex-x86_64-unknown-linux-gnu/kiss_fft.o \
# 	../../speex/libspeex/kiss_fft.c 
# gcc -c -DHAVE_CONFIG_H -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I. -I../../speex/include -I../../speex/libspeex -I../../../pjlib/include \
# 	-o output/libspeex-x86_64-unknown-linux-gnu/kiss_fftr.o \
# 	../../speex/libspeex/kiss_fftr.c 
# gcc -c -DHAVE_CONFIG_H -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I. -I../../speex/include -I../../speex/libspeex -I../../../pjlib/include \
# 	-o output/libspeex-x86_64-unknown-linux-gnu/lpc.o \
# 	../../speex/libspeex/lpc.c 
# gcc -c -DHAVE_CONFIG_H -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I. -I../../speex/include -I../../speex/libspeex -I../../../pjlib/include \
# 	-o output/libspeex-x86_64-unknown-linux-gnu/lsp.o \
# 	../../speex/libspeex/lsp.c 
# gcc -c -DHAVE_CONFIG_H -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I. -I../../speex/include -I../../speex/libspeex -I../../../pjlib/include \
# 	-o output/libspeex-x86_64-unknown-linux-gnu/lsp_tables_nb.o \
# 	../../speex/libspeex/lsp_tables_nb.c 
# gcc -c -DHAVE_CONFIG_H -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I. -I../../speex/include -I../../speex/libspeex -I../../../pjlib/include \
# 	-o output/libspeex-x86_64-unknown-linux-gnu/ltp.o \
# 	../../speex/libspeex/ltp.c 
# gcc -c -DHAVE_CONFIG_H -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I. -I../../speex/include -I../../speex/libspeex -I../../../pjlib/include \
# 	-o output/libspeex-x86_64-unknown-linux-gnu/mdf.o \
# 	../../speex/libspeex/mdf.c 
# gcc -c -DHAVE_CONFIG_H -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I. -I../../speex/include -I../../speex/libspeex -I../../../pjlib/include \
# 	-o output/libspeex-x86_64-unknown-linux-gnu/modes.o \
# 	../../speex/libspeex/modes.c 
# gcc -c -DHAVE_CONFIG_H -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I. -I../../speex/include -I../../speex/libspeex -I../../../pjlib/include \
# 	-o output/libspeex-x86_64-unknown-linux-gnu/modes_wb.o \
# 	../../speex/libspeex/modes_wb.c 
# gcc -c -DHAVE_CONFIG_H -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I. -I../../speex/include -I../../speex/libspeex -I../../../pjlib/include \
# 	-o output/libspeex-x86_64-unknown-linux-gnu/nb_celp.o \
# 	../../speex/libspeex/nb_celp.c 
# gcc -c -DHAVE_CONFIG_H -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I. -I../../speex/include -I../../speex/libspeex -I../../../pjlib/include \
# 	-o output/libspeex-x86_64-unknown-linux-gnu/preprocess.o \
# 	../../speex/libspeex/preprocess.c 
# gcc -c -DHAVE_CONFIG_H -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I. -I../../speex/include -I../../speex/libspeex -I../../../pjlib/include \
# 	-o output/libspeex-x86_64-unknown-linux-gnu/quant_lsp.o \
# 	../../speex/libspeex/quant_lsp.c 
# gcc -c -DHAVE_CONFIG_H -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I. -I../../speex/include -I../../speex/libspeex -I../../../pjlib/include \
# 	-o output/libspeex-x86_64-unknown-linux-gnu/resample.o \
# 	../../speex/libspeex/resample.c 
# gcc -c -DHAVE_CONFIG_H -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I. -I../../speex/include -I../../speex/libspeex -I../../../pjlib/include \
# 	-o output/libspeex-x86_64-unknown-linux-gnu/sb_celp.o \
# 	../../speex/libspeex/sb_celp.c 
# gcc -c -DHAVE_CONFIG_H -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I. -I../../speex/include -I../../speex/libspeex -I../../../pjlib/include \
# 	-o output/libspeex-x86_64-unknown-linux-gnu/smallft.o \
# 	../../speex/libspeex/smallft.c 
# gcc -c -DHAVE_CONFIG_H -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I. -I../../speex/include -I../../speex/libspeex -I../../../pjlib/include \
# 	-o output/libspeex-x86_64-unknown-linux-gnu/speex.o \
# 	../../speex/libspeex/speex.c 
# gcc -c -DHAVE_CONFIG_H -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I. -I../../speex/include -I../../speex/libspeex -I../../../pjlib/include \
# 	-o output/libspeex-x86_64-unknown-linux-gnu/speex_callbacks.o \
# 	../../speex/libspeex/speex_callbacks.c 
# gcc -c -DHAVE_CONFIG_H -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I. -I../../speex/include -I../../speex/libspeex -I../../../pjlib/include \
# 	-o output/libspeex-x86_64-unknown-linux-gnu/speex_header.o \
# 	../../speex/libspeex/speex_header.c 
# gcc -c -DHAVE_CONFIG_H -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I. -I../../speex/include -I../../speex/libspeex -I../../../pjlib/include \
# 	-o output/libspeex-x86_64-unknown-linux-gnu/scal.o \
# 	../../speex/libspeex/scal.c 
# gcc -c -DHAVE_CONFIG_H -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I. -I../../speex/include -I../../speex/libspeex -I../../../pjlib/include \
# 	-o output/libspeex-x86_64-unknown-linux-gnu/stereo.o \
# 	../../speex/libspeex/stereo.c 
# gcc -c -DHAVE_CONFIG_H -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I. -I../../speex/include -I../../speex/libspeex -I../../../pjlib/include \
# 	-o output/libspeex-x86_64-unknown-linux-gnu/vbr.o \
# 	../../speex/libspeex/vbr.c 
# gcc -c -DHAVE_CONFIG_H -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I. -I../../speex/include -I../../speex/libspeex -I../../../pjlib/include \
# 	-o output/libspeex-x86_64-unknown-linux-gnu/vq.o \
# 	../../speex/libspeex/vq.c 
# gcc -c -DHAVE_CONFIG_H -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I. -I../../speex/include -I../../speex/libspeex -I../../../pjlib/include \
# 	-o output/libspeex-x86_64-unknown-linux-gnu/window.o \
# 	../../speex/libspeex/window.c 
# if test ! -d ../../lib; then mkdir -p ../../lib; fi
# ar rv ../../lib/libspeex-x86_64-unknown-linux-gnu.a  output/libspeex-x86_64-unknown-linux-gnu/bits.o  output/libspeex-x86_64-unknown-linux-gnu/cb_search.o  output/libspeex-x86_64-unknown-linux-gnu/exc_10_16_table.o  output/libspeex-x86_64-unknown-linux-gnu/exc_10_32_table.o  output/libspeex-x86_64-unknown-linux-gnu/exc_20_32_table.o  output/libspeex-x86_64-unknown-linux-gnu/exc_5_256_table.o  output/libspeex-x86_64-unknown-linux-gnu/exc_5_64_table.o  output/libspeex-x86_64-unknown-linux-gnu/exc_8_128_table.o  output/libspeex-x86_64-unknown-linux-gnu/fftwrap.o  output/libspeex-x86_64-unknown-linux-gnu/filterbank.o  output/libspeex-x86_64-unknown-linux-gnu/filters.o  output/libspeex-x86_64-unknown-linux-gnu/gain_table.o  output/libspeex-x86_64-unknown-linux-gnu/gain_table_lbr.o  output/libspeex-x86_64-unknown-linux-gnu/hexc_10_32_table.o  output/libspeex-x86_64-unknown-linux-gnu/hexc_table.o  output/libspeex-x86_64-unknown-linux-gnu/high_lsp_tables.o  output/libspeex-x86_64-unknown-linux-gnu/kiss_fft.o  output/libspeex-x86_64-unknown-linux-gnu/kiss_fftr.o  output/libspeex-x86_64-unknown-linux-gnu/lpc.o  output/libspeex-x86_64-unknown-linux-gnu/lsp.o  output/libspeex-x86_64-unknown-linux-gnu/lsp_tables_nb.o  output/libspeex-x86_64-unknown-linux-gnu/ltp.o  output/libspeex-x86_64-unknown-linux-gnu/mdf.o  output/libspeex-x86_64-unknown-linux-gnu/modes.o  output/libspeex-x86_64-unknown-linux-gnu/modes_wb.o  output/libspeex-x86_64-unknown-linux-gnu/nb_celp.o  output/libspeex-x86_64-unknown-linux-gnu/preprocess.o  output/libspeex-x86_64-unknown-linux-gnu/quant_lsp.o  output/libspeex-x86_64-unknown-linux-gnu/resample.o  output/libspeex-x86_64-unknown-linux-gnu/sb_celp.o  output/libspeex-x86_64-unknown-linux-gnu/smallft.o  output/libspeex-x86_64-unknown-linux-gnu/speex.o  output/libspeex-x86_64-unknown-linux-gnu/speex_callbacks.o  output/libspeex-x86_64-unknown-linux-gnu/speex_header.o  output/libspeex-x86_64-unknown-linux-gnu/scal.o  output/libspeex-x86_64-unknown-linux-gnu/stereo.o  output/libspeex-x86_64-unknown-linux-gnu/vbr.o  output/libspeex-x86_64-unknown-linux-gnu/vq.o  output/libspeex-x86_64-unknown-linux-gnu/window.o
# r - output/libspeex-x86_64-unknown-linux-gnu/bits.o
# r - output/libspeex-x86_64-unknown-linux-gnu/cb_search.o
# r - output/libspeex-x86_64-unknown-linux-gnu/exc_10_16_table.o
# r - output/libspeex-x86_64-unknown-linux-gnu/exc_10_32_table.o
# r - output/libspeex-x86_64-unknown-linux-gnu/exc_20_32_table.o
# r - output/libspeex-x86_64-unknown-linux-gnu/exc_5_256_table.o
# r - output/libspeex-x86_64-unknown-linux-gnu/exc_5_64_table.o
# r - output/libspeex-x86_64-unknown-linux-gnu/exc_8_128_table.o
# r - output/libspeex-x86_64-unknown-linux-gnu/fftwrap.o
# r - output/libspeex-x86_64-unknown-linux-gnu/filterbank.o
# r - output/libspeex-x86_64-unknown-linux-gnu/filters.o
# r - output/libspeex-x86_64-unknown-linux-gnu/gain_table.o
# r - output/libspeex-x86_64-unknown-linux-gnu/gain_table_lbr.o
# r - output/libspeex-x86_64-unknown-linux-gnu/hexc_10_32_table.o
# r - output/libspeex-x86_64-unknown-linux-gnu/hexc_table.o
# r - output/libspeex-x86_64-unknown-linux-gnu/high_lsp_tables.o
# r - output/libspeex-x86_64-unknown-linux-gnu/kiss_fft.o
# r - output/libspeex-x86_64-unknown-linux-gnu/kiss_fftr.o
# r - output/libspeex-x86_64-unknown-linux-gnu/lpc.o
# r - output/libspeex-x86_64-unknown-linux-gnu/lsp.o
# r - output/libspeex-x86_64-unknown-linux-gnu/lsp_tables_nb.o
# r - output/libspeex-x86_64-unknown-linux-gnu/ltp.o
# r - output/libspeex-x86_64-unknown-linux-gnu/mdf.o
# r - output/libspeex-x86_64-unknown-linux-gnu/modes.o
# r - output/libspeex-x86_64-unknown-linux-gnu/modes_wb.o
# r - output/libspeex-x86_64-unknown-linux-gnu/nb_celp.o
# r - output/libspeex-x86_64-unknown-linux-gnu/preprocess.o
# r - output/libspeex-x86_64-unknown-linux-gnu/quant_lsp.o
# r - output/libspeex-x86_64-unknown-linux-gnu/resample.o
# r - output/libspeex-x86_64-unknown-linux-gnu/sb_celp.o
# r - output/libspeex-x86_64-unknown-linux-gnu/smallft.o
# r - output/libspeex-x86_64-unknown-linux-gnu/speex.o
# r - output/libspeex-x86_64-unknown-linux-gnu/speex_callbacks.o
# r - output/libspeex-x86_64-unknown-linux-gnu/speex_header.o
# r - output/libspeex-x86_64-unknown-linux-gnu/scal.o
# r - output/libspeex-x86_64-unknown-linux-gnu/stereo.o
# r - output/libspeex-x86_64-unknown-linux-gnu/vbr.o
# r - output/libspeex-x86_64-unknown-linux-gnu/vq.o
# r - output/libspeex-x86_64-unknown-linux-gnu/window.o
# ranlib ../../lib/libspeex-x86_64-unknown-linux-gnu.a
# make[3]: Leaving directory '/home/vsedyshev/Work/1111/pjproject/third_party/build/speex'
# make[2]: Leaving directory '/home/vsedyshev/Work/1111/pjproject/third_party/build/speex'
# make[2]: Entering directory '/home/vsedyshev/Work/1111/pjproject/third_party/build/g7221'
# make -f /home/vsedyshev/Work/1111/pjproject/build/rules.mak APP=G7221_CODEC app=libg7221codec ../../lib/libg7221codec-x86_64-unknown-linux-gnu.a
# make[3]: Entering directory '/home/vsedyshev/Work/1111/pjproject/third_party/build/g7221'
# mkdir -p output/libg7221codec-x86_64-unknown-linux-gnu/common/
# mkdir -p output/libg7221codec-x86_64-unknown-linux-gnu/decode/
# mkdir -p output/libg7221codec-x86_64-unknown-linux-gnu/encode/
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../.. -I../../g7221/common -I../../g7221/common/stl-files -I../../../pjlib/include \
# 	-o output/libg7221codec-x86_64-unknown-linux-gnu/common/common.o \
# 	../../g7221/common/common.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../.. -I../../g7221/common -I../../g7221/common/stl-files -I../../../pjlib/include \
# 	-o output/libg7221codec-x86_64-unknown-linux-gnu/common/huff_tab.o \
# 	../../g7221/common/huff_tab.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../.. -I../../g7221/common -I../../g7221/common/stl-files -I../../../pjlib/include \
# 	-o output/libg7221codec-x86_64-unknown-linux-gnu/common/tables.o \
# 	../../g7221/common/tables.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../.. -I../../g7221/common -I../../g7221/common/stl-files -I../../../pjlib/include \
# 	-o output/libg7221codec-x86_64-unknown-linux-gnu/common/basic_op.o \
# 	../../g7221/common/basic_op.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../.. -I../../g7221/common -I../../g7221/common/stl-files -I../../../pjlib/include \
# 	-o output/libg7221codec-x86_64-unknown-linux-gnu/decode/coef2sam.o \
# 	../../g7221/decode/coef2sam.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../.. -I../../g7221/common -I../../g7221/common/stl-files -I../../../pjlib/include \
# 	-o output/libg7221codec-x86_64-unknown-linux-gnu/decode/dct4_s.o \
# 	../../g7221/decode/dct4_s.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../.. -I../../g7221/common -I../../g7221/common/stl-files -I../../../pjlib/include \
# 	-o output/libg7221codec-x86_64-unknown-linux-gnu/decode/decoder.o \
# 	../../g7221/decode/decoder.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../.. -I../../g7221/common -I../../g7221/common/stl-files -I../../../pjlib/include \
# 	-o output/libg7221codec-x86_64-unknown-linux-gnu/encode/dct4_a.o \
# 	../../g7221/encode/dct4_a.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../.. -I../../g7221/common -I../../g7221/common/stl-files -I../../../pjlib/include \
# 	-o output/libg7221codec-x86_64-unknown-linux-gnu/encode/sam2coef.o \
# 	../../g7221/encode/sam2coef.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../.. -I../../g7221/common -I../../g7221/common/stl-files -I../../../pjlib/include \
# 	-o output/libg7221codec-x86_64-unknown-linux-gnu/encode/encoder.o \
# 	../../g7221/encode/encoder.c 
# if test ! -d ../../lib; then mkdir -p ../../lib; fi
# ar rv ../../lib/libg7221codec-x86_64-unknown-linux-gnu.a  output/libg7221codec-x86_64-unknown-linux-gnu/common/common.o  output/libg7221codec-x86_64-unknown-linux-gnu/common/huff_tab.o  output/libg7221codec-x86_64-unknown-linux-gnu/common/tables.o  output/libg7221codec-x86_64-unknown-linux-gnu/common/basic_op.o  output/libg7221codec-x86_64-unknown-linux-gnu/decode/coef2sam.o  output/libg7221codec-x86_64-unknown-linux-gnu/decode/dct4_s.o  output/libg7221codec-x86_64-unknown-linux-gnu/decode/decoder.o  output/libg7221codec-x86_64-unknown-linux-gnu/encode/dct4_a.o  output/libg7221codec-x86_64-unknown-linux-gnu/encode/sam2coef.o  output/libg7221codec-x86_64-unknown-linux-gnu/encode/encoder.o
# r - output/libg7221codec-x86_64-unknown-linux-gnu/common/common.o
# r - output/libg7221codec-x86_64-unknown-linux-gnu/common/huff_tab.o
# r - output/libg7221codec-x86_64-unknown-linux-gnu/common/tables.o
# r - output/libg7221codec-x86_64-unknown-linux-gnu/common/basic_op.o
# r - output/libg7221codec-x86_64-unknown-linux-gnu/decode/coef2sam.o
# r - output/libg7221codec-x86_64-unknown-linux-gnu/decode/dct4_s.o
# r - output/libg7221codec-x86_64-unknown-linux-gnu/decode/decoder.o
# r - output/libg7221codec-x86_64-unknown-linux-gnu/encode/dct4_a.o
# r - output/libg7221codec-x86_64-unknown-linux-gnu/encode/sam2coef.o
# r - output/libg7221codec-x86_64-unknown-linux-gnu/encode/encoder.o
# ranlib ../../lib/libg7221codec-x86_64-unknown-linux-gnu.a
# make[3]: Leaving directory '/home/vsedyshev/Work/1111/pjproject/third_party/build/g7221'
# make[2]: Leaving directory '/home/vsedyshev/Work/1111/pjproject/third_party/build/g7221'
# make[2]: Entering directory '/home/vsedyshev/Work/1111/pjproject/third_party/build/srtp'
# make -f /home/vsedyshev/Work/1111/pjproject/build/rules.mak APP=SRTP app=libsrtp ../../lib/libsrtp-x86_64-unknown-linux-gnu.a
# make[3]: Entering directory '/home/vsedyshev/Work/1111/pjproject/third_party/build/srtp'
# mkdir -p output/libsrtp-x86_64-unknown-linux-gnu/crypto/cipher/
# mkdir -p output/libsrtp-x86_64-unknown-linux-gnu/crypto/hash/
# mkdir -p output/libsrtp-x86_64-unknown-linux-gnu/crypto/kernel/
# mkdir -p output/libsrtp-x86_64-unknown-linux-gnu/crypto/math/
# mkdir -p output/libsrtp-x86_64-unknown-linux-gnu/crypto/replay/
# mkdir -p output/libsrtp-x86_64-unknown-linux-gnu/pjlib/
# mkdir -p output/libsrtp-x86_64-unknown-linux-gnu/srtp/
# gcc -c -DHAVE_CONFIG_H -I. -I../../srtp/crypto/include -I../../srtp/include -I../../../pjlib/include -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1     -DOPENSSL \
# 	-o output/libsrtp-x86_64-unknown-linux-gnu/crypto/cipher/cipher.o \
# 	../../srtp/crypto/cipher/cipher.c 
# gcc -c -DHAVE_CONFIG_H -I. -I../../srtp/crypto/include -I../../srtp/include -I../../../pjlib/include -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1     -DOPENSSL \
# 	-o output/libsrtp-x86_64-unknown-linux-gnu/crypto/cipher/null_cipher.o \
# 	../../srtp/crypto/cipher/null_cipher.c 
# gcc -c -DHAVE_CONFIG_H -I. -I../../srtp/crypto/include -I../../srtp/include -I../../../pjlib/include -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1     -DOPENSSL \
# 	-o output/libsrtp-x86_64-unknown-linux-gnu/crypto/cipher/aes_icm_ossl.o \
# 	../../srtp/crypto/cipher/aes_icm_ossl.c 
# gcc -c -DHAVE_CONFIG_H -I. -I../../srtp/crypto/include -I../../srtp/include -I../../../pjlib/include -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1     -DOPENSSL \
# 	-o output/libsrtp-x86_64-unknown-linux-gnu/crypto/cipher/aes_gcm_ossl.o \
# 	../../srtp/crypto/cipher/aes_gcm_ossl.c 
# gcc -c -DHAVE_CONFIG_H -I. -I../../srtp/crypto/include -I../../srtp/include -I../../../pjlib/include -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1     -DOPENSSL \
# 	-o output/libsrtp-x86_64-unknown-linux-gnu/crypto/hash/null_auth.o \
# 	../../srtp/crypto/hash/null_auth.c 
# gcc -c -DHAVE_CONFIG_H -I. -I../../srtp/crypto/include -I../../srtp/include -I../../../pjlib/include -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1     -DOPENSSL \
# 	-o output/libsrtp-x86_64-unknown-linux-gnu/crypto/hash/auth.o \
# 	../../srtp/crypto/hash/auth.c 
# gcc -c -DHAVE_CONFIG_H -I. -I../../srtp/crypto/include -I../../srtp/include -I../../../pjlib/include -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1     -DOPENSSL \
# 	-o output/libsrtp-x86_64-unknown-linux-gnu/crypto/hash/hmac_ossl.o \
# 	../../srtp/crypto/hash/hmac_ossl.c 
# gcc -c -DHAVE_CONFIG_H -I. -I../../srtp/crypto/include -I../../srtp/include -I../../../pjlib/include -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1     -DOPENSSL \
# 	-o output/libsrtp-x86_64-unknown-linux-gnu/crypto/math/datatypes.o \
# 	../../srtp/crypto/math/datatypes.c 
# gcc -c -DHAVE_CONFIG_H -I. -I../../srtp/crypto/include -I../../srtp/include -I../../../pjlib/include -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1     -DOPENSSL \
# 	-o output/libsrtp-x86_64-unknown-linux-gnu/crypto/math/stat.o \
# 	../../srtp/crypto/math/stat.c 
# gcc -c -DHAVE_CONFIG_H -I. -I../../srtp/crypto/include -I../../srtp/include -I../../../pjlib/include -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1     -DOPENSSL \
# 	-o output/libsrtp-x86_64-unknown-linux-gnu/crypto/kernel/crypto_kernel.o \
# 	../../srtp/crypto/kernel/crypto_kernel.c 
# gcc -c -DHAVE_CONFIG_H -I. -I../../srtp/crypto/include -I../../srtp/include -I../../../pjlib/include -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1     -DOPENSSL \
# 	-o output/libsrtp-x86_64-unknown-linux-gnu/crypto/kernel/alloc.o \
# 	../../srtp/crypto/kernel/alloc.c 
# gcc -c -DHAVE_CONFIG_H -I. -I../../srtp/crypto/include -I../../srtp/include -I../../../pjlib/include -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1     -DOPENSSL \
# 	-o output/libsrtp-x86_64-unknown-linux-gnu/crypto/kernel/key.o \
# 	../../srtp/crypto/kernel/key.c 
# gcc -c -DHAVE_CONFIG_H -I. -I../../srtp/crypto/include -I../../srtp/include -I../../../pjlib/include -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1     -DOPENSSL \
# 	-o output/libsrtp-x86_64-unknown-linux-gnu/pjlib/srtp_err.o \
# 	../../srtp/pjlib/srtp_err.c 
# gcc -c -DHAVE_CONFIG_H -I. -I../../srtp/crypto/include -I../../srtp/include -I../../../pjlib/include -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1     -DOPENSSL \
# 	-o output/libsrtp-x86_64-unknown-linux-gnu/crypto/replay/rdb.o \
# 	../../srtp/crypto/replay/rdb.c 
# gcc -c -DHAVE_CONFIG_H -I. -I../../srtp/crypto/include -I../../srtp/include -I../../../pjlib/include -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1     -DOPENSSL \
# 	-o output/libsrtp-x86_64-unknown-linux-gnu/crypto/replay/rdbx.o \
# 	../../srtp/crypto/replay/rdbx.c 
# gcc -c -DHAVE_CONFIG_H -I. -I../../srtp/crypto/include -I../../srtp/include -I../../../pjlib/include -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1     -DOPENSSL \
# 	-o output/libsrtp-x86_64-unknown-linux-gnu/crypto/replay/ut_sim.o \
# 	../../srtp/crypto/replay/ut_sim.c 
# gcc -c -DHAVE_CONFIG_H -I. -I../../srtp/crypto/include -I../../srtp/include -I../../../pjlib/include -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1     -DOPENSSL \
# 	-o output/libsrtp-x86_64-unknown-linux-gnu/srtp/srtp.o \
# 	../../srtp/srtp/srtp.c 
# gcc -c -DHAVE_CONFIG_H -I. -I../../srtp/crypto/include -I../../srtp/include -I../../../pjlib/include -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1     -DOPENSSL \
# 	-o output/libsrtp-x86_64-unknown-linux-gnu/srtp/ekt.o \
# 	../../srtp/srtp/ekt.c 
# if test ! -d ../../lib; then mkdir -p ../../lib; fi
# ar rv ../../lib/libsrtp-x86_64-unknown-linux-gnu.a  output/libsrtp-x86_64-unknown-linux-gnu/crypto/cipher/cipher.o  output/libsrtp-x86_64-unknown-linux-gnu/crypto/cipher/null_cipher.o  output/libsrtp-x86_64-unknown-linux-gnu/crypto/cipher/aes_icm_ossl.o  output/libsrtp-x86_64-unknown-linux-gnu/crypto/cipher/aes_gcm_ossl.o  output/libsrtp-x86_64-unknown-linux-gnu/crypto/hash/null_auth.o  output/libsrtp-x86_64-unknown-linux-gnu/crypto/hash/auth.o  output/libsrtp-x86_64-unknown-linux-gnu/crypto/hash/hmac_ossl.o  output/libsrtp-x86_64-unknown-linux-gnu/crypto/math/datatypes.o  output/libsrtp-x86_64-unknown-linux-gnu/crypto/math/stat.o  output/libsrtp-x86_64-unknown-linux-gnu/crypto/kernel/crypto_kernel.o  output/libsrtp-x86_64-unknown-linux-gnu/crypto/kernel/alloc.o  output/libsrtp-x86_64-unknown-linux-gnu/crypto/kernel/key.o  output/libsrtp-x86_64-unknown-linux-gnu/pjlib/srtp_err.o  output/libsrtp-x86_64-unknown-linux-gnu/crypto/replay/rdb.o  output/libsrtp-x86_64-unknown-linux-gnu/crypto/replay/rdbx.o  output/libsrtp-x86_64-unknown-linux-gnu/crypto/replay/ut_sim.o  output/libsrtp-x86_64-unknown-linux-gnu/srtp/srtp.o  output/libsrtp-x86_64-unknown-linux-gnu/srtp/ekt.o
# r - output/libsrtp-x86_64-unknown-linux-gnu/crypto/cipher/cipher.o
# r - output/libsrtp-x86_64-unknown-linux-gnu/crypto/cipher/null_cipher.o
# r - output/libsrtp-x86_64-unknown-linux-gnu/crypto/cipher/aes_icm_ossl.o
# r - output/libsrtp-x86_64-unknown-linux-gnu/crypto/cipher/aes_gcm_ossl.o
# r - output/libsrtp-x86_64-unknown-linux-gnu/crypto/hash/null_auth.o
# r - output/libsrtp-x86_64-unknown-linux-gnu/crypto/hash/auth.o
# r - output/libsrtp-x86_64-unknown-linux-gnu/crypto/hash/hmac_ossl.o
# r - output/libsrtp-x86_64-unknown-linux-gnu/crypto/math/datatypes.o
# r - output/libsrtp-x86_64-unknown-linux-gnu/crypto/math/stat.o
# r - output/libsrtp-x86_64-unknown-linux-gnu/crypto/kernel/crypto_kernel.o
# r - output/libsrtp-x86_64-unknown-linux-gnu/crypto/kernel/alloc.o
# r - output/libsrtp-x86_64-unknown-linux-gnu/crypto/kernel/key.o
# r - output/libsrtp-x86_64-unknown-linux-gnu/pjlib/srtp_err.o
# r - output/libsrtp-x86_64-unknown-linux-gnu/crypto/replay/rdb.o
# r - output/libsrtp-x86_64-unknown-linux-gnu/crypto/replay/rdbx.o
# r - output/libsrtp-x86_64-unknown-linux-gnu/crypto/replay/ut_sim.o
# r - output/libsrtp-x86_64-unknown-linux-gnu/srtp/srtp.o
# r - output/libsrtp-x86_64-unknown-linux-gnu/srtp/ekt.o
# ranlib ../../lib/libsrtp-x86_64-unknown-linux-gnu.a
# make[3]: Leaving directory '/home/vsedyshev/Work/1111/pjproject/third_party/build/srtp'
# make[2]: Leaving directory '/home/vsedyshev/Work/1111/pjproject/third_party/build/srtp'
# make[2]: Entering directory '/home/vsedyshev/Work/1111/pjproject/third_party/build/resample'
# make -f /home/vsedyshev/Work/1111/pjproject/build/rules.mak APP=RESAMPLE app=libresample ../../lib/libresample-x86_64-unknown-linux-gnu.a
# make[3]: Entering directory '/home/vsedyshev/Work/1111/pjproject/third_party/build/resample'
# mkdir -p output/libresample-x86_64-unknown-linux-gnu/
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I. -I../../resample/include -I../../../pjlib/include \
# 	-o output/libresample-x86_64-unknown-linux-gnu/resamplesubs.o \
# 	../../resample/src/resamplesubs.c 
# if test ! -d ../../lib; then mkdir -p ../../lib; fi
# ar rv ../../lib/libresample-x86_64-unknown-linux-gnu.a  output/libresample-x86_64-unknown-linux-gnu/resamplesubs.o
# r - output/libresample-x86_64-unknown-linux-gnu/resamplesubs.o
# ranlib ../../lib/libresample-x86_64-unknown-linux-gnu.a
# make[3]: Leaving directory '/home/vsedyshev/Work/1111/pjproject/third_party/build/resample'
# make[2]: Leaving directory '/home/vsedyshev/Work/1111/pjproject/third_party/build/resample'
# make[2]: Entering directory '/home/vsedyshev/Work/1111/pjproject/third_party/build/yuv'
# make -f /home/vsedyshev/Work/1111/pjproject/build/rules.mak APP=YUV app=libyuv ../../lib/libyuv-x86_64-unknown-linux-gnu.a
# make[3]: Entering directory '/home/vsedyshev/Work/1111/pjproject/third_party/build/yuv'
# mkdir -p output/libyuv-x86_64-unknown-linux-gnu/
# g++ -c -fomit-frame-pointer  -DPJ_AUTOCONF=1 -g -O2    -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I. -I../../yuv/include -I../../../pjlib/include \
# 	-o output/libyuv-x86_64-unknown-linux-gnu/compare.o \
# 	../../yuv/source/compare.cc
# g++ -c -fomit-frame-pointer  -DPJ_AUTOCONF=1 -g -O2    -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I. -I../../yuv/include -I../../../pjlib/include \
# 	-o output/libyuv-x86_64-unknown-linux-gnu/compare_common.o \
# 	../../yuv/source/compare_common.cc
# g++ -c -fomit-frame-pointer  -DPJ_AUTOCONF=1 -g -O2    -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I. -I../../yuv/include -I../../../pjlib/include \
# 	-o output/libyuv-x86_64-unknown-linux-gnu/compare_gcc.o \
# 	../../yuv/source/compare_gcc.cc
# g++ -c -fomit-frame-pointer  -DPJ_AUTOCONF=1 -g -O2    -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I. -I../../yuv/include -I../../../pjlib/include \
# 	-o output/libyuv-x86_64-unknown-linux-gnu/compare_neon64.o \
# 	../../yuv/source/compare_neon64.cc
# g++ -c -fomit-frame-pointer  -DPJ_AUTOCONF=1 -g -O2    -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I. -I../../yuv/include -I../../../pjlib/include \
# 	-o output/libyuv-x86_64-unknown-linux-gnu/compare_neon.o \
# 	../../yuv/source/compare_neon.cc
# g++ -c -fomit-frame-pointer  -DPJ_AUTOCONF=1 -g -O2    -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I. -I../../yuv/include -I../../../pjlib/include \
# 	-o output/libyuv-x86_64-unknown-linux-gnu/compare_win.o \
# 	../../yuv/source/compare_win.cc
# g++ -c -fomit-frame-pointer  -DPJ_AUTOCONF=1 -g -O2    -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I. -I../../yuv/include -I../../../pjlib/include \
# 	-o output/libyuv-x86_64-unknown-linux-gnu/convert_argb.o \
# 	../../yuv/source/convert_argb.cc
# g++ -c -fomit-frame-pointer  -DPJ_AUTOCONF=1 -g -O2    -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I. -I../../yuv/include -I../../../pjlib/include \
# 	-o output/libyuv-x86_64-unknown-linux-gnu/convert.o \
# 	../../yuv/source/convert.cc
# g++ -c -fomit-frame-pointer  -DPJ_AUTOCONF=1 -g -O2    -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I. -I../../yuv/include -I../../../pjlib/include \
# 	-o output/libyuv-x86_64-unknown-linux-gnu/convert_from_argb.o \
# 	../../yuv/source/convert_from_argb.cc
# g++ -c -fomit-frame-pointer  -DPJ_AUTOCONF=1 -g -O2    -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I. -I../../yuv/include -I../../../pjlib/include \
# 	-o output/libyuv-x86_64-unknown-linux-gnu/convert_from.o \
# 	../../yuv/source/convert_from.cc
# g++ -c -fomit-frame-pointer  -DPJ_AUTOCONF=1 -g -O2    -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I. -I../../yuv/include -I../../../pjlib/include \
# 	-o output/libyuv-x86_64-unknown-linux-gnu/convert_jpeg.o \
# 	../../yuv/source/convert_jpeg.cc
# g++ -c -fomit-frame-pointer  -DPJ_AUTOCONF=1 -g -O2    -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I. -I../../yuv/include -I../../../pjlib/include \
# 	-o output/libyuv-x86_64-unknown-linux-gnu/convert_to_argb.o \
# 	../../yuv/source/convert_to_argb.cc
# g++ -c -fomit-frame-pointer  -DPJ_AUTOCONF=1 -g -O2    -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I. -I../../yuv/include -I../../../pjlib/include \
# 	-o output/libyuv-x86_64-unknown-linux-gnu/convert_to_i420.o \
# 	../../yuv/source/convert_to_i420.cc
# g++ -c -fomit-frame-pointer  -DPJ_AUTOCONF=1 -g -O2    -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I. -I../../yuv/include -I../../../pjlib/include \
# 	-o output/libyuv-x86_64-unknown-linux-gnu/cpu_id.o \
# 	../../yuv/source/cpu_id.cc
# g++ -c -fomit-frame-pointer  -DPJ_AUTOCONF=1 -g -O2    -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I. -I../../yuv/include -I../../../pjlib/include \
# 	-o output/libyuv-x86_64-unknown-linux-gnu/mjpeg_decoder.o \
# 	../../yuv/source/mjpeg_decoder.cc
# g++ -c -fomit-frame-pointer  -DPJ_AUTOCONF=1 -g -O2    -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I. -I../../yuv/include -I../../../pjlib/include \
# 	-o output/libyuv-x86_64-unknown-linux-gnu/mjpeg_validate.o \
# 	../../yuv/source/mjpeg_validate.cc
# g++ -c -fomit-frame-pointer  -DPJ_AUTOCONF=1 -g -O2    -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I. -I../../yuv/include -I../../../pjlib/include \
# 	-o output/libyuv-x86_64-unknown-linux-gnu/planar_functions.o \
# 	../../yuv/source/planar_functions.cc
# g++ -c -fomit-frame-pointer  -DPJ_AUTOCONF=1 -g -O2    -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I. -I../../yuv/include -I../../../pjlib/include \
# 	-o output/libyuv-x86_64-unknown-linux-gnu/rotate_any.o \
# 	../../yuv/source/rotate_any.cc
# g++ -c -fomit-frame-pointer  -DPJ_AUTOCONF=1 -g -O2    -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I. -I../../yuv/include -I../../../pjlib/include \
# 	-o output/libyuv-x86_64-unknown-linux-gnu/rotate_argb.o \
# 	../../yuv/source/rotate_argb.cc
# g++ -c -fomit-frame-pointer  -DPJ_AUTOCONF=1 -g -O2    -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I. -I../../yuv/include -I../../../pjlib/include \
# 	-o output/libyuv-x86_64-unknown-linux-gnu/rotate.o \
# 	../../yuv/source/rotate.cc
# g++ -c -fomit-frame-pointer  -DPJ_AUTOCONF=1 -g -O2    -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I. -I../../yuv/include -I../../../pjlib/include \
# 	-o output/libyuv-x86_64-unknown-linux-gnu/rotate_common.o \
# 	../../yuv/source/rotate_common.cc
# g++ -c -fomit-frame-pointer  -DPJ_AUTOCONF=1 -g -O2    -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I. -I../../yuv/include -I../../../pjlib/include \
# 	-o output/libyuv-x86_64-unknown-linux-gnu/rotate_gcc.o \
# 	../../yuv/source/rotate_gcc.cc
# g++ -c -fomit-frame-pointer  -DPJ_AUTOCONF=1 -g -O2    -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I. -I../../yuv/include -I../../../pjlib/include \
# 	-o output/libyuv-x86_64-unknown-linux-gnu/rotate_dspr2.o \
# 	../../yuv/source/rotate_dspr2.cc
# g++ -c -fomit-frame-pointer  -DPJ_AUTOCONF=1 -g -O2    -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I. -I../../yuv/include -I../../../pjlib/include \
# 	-o output/libyuv-x86_64-unknown-linux-gnu/rotate_neon64.o \
# 	../../yuv/source/rotate_neon64.cc
# g++ -c -fomit-frame-pointer  -DPJ_AUTOCONF=1 -g -O2    -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I. -I../../yuv/include -I../../../pjlib/include \
# 	-o output/libyuv-x86_64-unknown-linux-gnu/rotate_neon.o \
# 	../../yuv/source/rotate_neon.cc
# g++ -c -fomit-frame-pointer  -DPJ_AUTOCONF=1 -g -O2    -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I. -I../../yuv/include -I../../../pjlib/include \
# 	-o output/libyuv-x86_64-unknown-linux-gnu/rotate_win.o \
# 	../../yuv/source/rotate_win.cc
# g++ -c -fomit-frame-pointer  -DPJ_AUTOCONF=1 -g -O2    -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I. -I../../yuv/include -I../../../pjlib/include \
# 	-o output/libyuv-x86_64-unknown-linux-gnu/row_any.o \
# 	../../yuv/source/row_any.cc
# g++ -c -fomit-frame-pointer  -DPJ_AUTOCONF=1 -g -O2    -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I. -I../../yuv/include -I../../../pjlib/include \
# 	-o output/libyuv-x86_64-unknown-linux-gnu/row_common.o \
# 	../../yuv/source/row_common.cc
# g++ -c -fomit-frame-pointer  -DPJ_AUTOCONF=1 -g -O2    -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I. -I../../yuv/include -I../../../pjlib/include \
# 	-o output/libyuv-x86_64-unknown-linux-gnu/row_gcc.o \
# 	../../yuv/source/row_gcc.cc
# g++ -c -fomit-frame-pointer  -DPJ_AUTOCONF=1 -g -O2    -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I. -I../../yuv/include -I../../../pjlib/include \
# 	-o output/libyuv-x86_64-unknown-linux-gnu/row_dspr2.o \
# 	../../yuv/source/row_dspr2.cc
# g++ -c -fomit-frame-pointer  -DPJ_AUTOCONF=1 -g -O2    -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I. -I../../yuv/include -I../../../pjlib/include \
# 	-o output/libyuv-x86_64-unknown-linux-gnu/row_neon64.o \
# 	../../yuv/source/row_neon64.cc
# g++ -c -fomit-frame-pointer  -DPJ_AUTOCONF=1 -g -O2    -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I. -I../../yuv/include -I../../../pjlib/include \
# 	-o output/libyuv-x86_64-unknown-linux-gnu/row_neon.o \
# 	../../yuv/source/row_neon.cc
# g++ -c -fomit-frame-pointer  -DPJ_AUTOCONF=1 -g -O2    -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I. -I../../yuv/include -I../../../pjlib/include \
# 	-o output/libyuv-x86_64-unknown-linux-gnu/row_win.o \
# 	../../yuv/source/row_win.cc
# g++ -c -fomit-frame-pointer  -DPJ_AUTOCONF=1 -g -O2    -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I. -I../../yuv/include -I../../../pjlib/include \
# 	-o output/libyuv-x86_64-unknown-linux-gnu/scale_any.o \
# 	../../yuv/source/scale_any.cc
# g++ -c -fomit-frame-pointer  -DPJ_AUTOCONF=1 -g -O2    -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I. -I../../yuv/include -I../../../pjlib/include \
# 	-o output/libyuv-x86_64-unknown-linux-gnu/scale_argb.o \
# 	../../yuv/source/scale_argb.cc
# g++ -c -fomit-frame-pointer  -DPJ_AUTOCONF=1 -g -O2    -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I. -I../../yuv/include -I../../../pjlib/include \
# 	-o output/libyuv-x86_64-unknown-linux-gnu/scale.o \
# 	../../yuv/source/scale.cc
# g++ -c -fomit-frame-pointer  -DPJ_AUTOCONF=1 -g -O2    -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I. -I../../yuv/include -I../../../pjlib/include \
# 	-o output/libyuv-x86_64-unknown-linux-gnu/scale_common.o \
# 	../../yuv/source/scale_common.cc
# g++ -c -fomit-frame-pointer  -DPJ_AUTOCONF=1 -g -O2    -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I. -I../../yuv/include -I../../../pjlib/include \
# 	-o output/libyuv-x86_64-unknown-linux-gnu/scale_gcc.o \
# 	../../yuv/source/scale_gcc.cc
# g++ -c -fomit-frame-pointer  -DPJ_AUTOCONF=1 -g -O2    -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I. -I../../yuv/include -I../../../pjlib/include \
# 	-o output/libyuv-x86_64-unknown-linux-gnu/scale_dspr2.o \
# 	../../yuv/source/scale_dspr2.cc
# g++ -c -fomit-frame-pointer  -DPJ_AUTOCONF=1 -g -O2    -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I. -I../../yuv/include -I../../../pjlib/include \
# 	-o output/libyuv-x86_64-unknown-linux-gnu/scale_neon64.o \
# 	../../yuv/source/scale_neon64.cc
# g++ -c -fomit-frame-pointer  -DPJ_AUTOCONF=1 -g -O2    -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I. -I../../yuv/include -I../../../pjlib/include \
# 	-o output/libyuv-x86_64-unknown-linux-gnu/scale_neon.o \
# 	../../yuv/source/scale_neon.cc
# g++ -c -fomit-frame-pointer  -DPJ_AUTOCONF=1 -g -O2    -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I. -I../../yuv/include -I../../../pjlib/include \
# 	-o output/libyuv-x86_64-unknown-linux-gnu/scale_win.o \
# 	../../yuv/source/scale_win.cc
# g++ -c -fomit-frame-pointer  -DPJ_AUTOCONF=1 -g -O2    -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I. -I../../yuv/include -I../../../pjlib/include \
# 	-o output/libyuv-x86_64-unknown-linux-gnu/video_common.o \
# 	../../yuv/source/video_common.cc
# if test ! -d ../../lib; then mkdir -p ../../lib; fi
# ar rv ../../lib/libyuv-x86_64-unknown-linux-gnu.a  output/libyuv-x86_64-unknown-linux-gnu/compare.o  output/libyuv-x86_64-unknown-linux-gnu/compare_common.o  output/libyuv-x86_64-unknown-linux-gnu/compare_gcc.o  output/libyuv-x86_64-unknown-linux-gnu/compare_neon64.o  output/libyuv-x86_64-unknown-linux-gnu/compare_neon.o  output/libyuv-x86_64-unknown-linux-gnu/compare_win.o  output/libyuv-x86_64-unknown-linux-gnu/convert_argb.o  output/libyuv-x86_64-unknown-linux-gnu/convert.o  output/libyuv-x86_64-unknown-linux-gnu/convert_from_argb.o  output/libyuv-x86_64-unknown-linux-gnu/convert_from.o  output/libyuv-x86_64-unknown-linux-gnu/convert_jpeg.o  output/libyuv-x86_64-unknown-linux-gnu/convert_to_argb.o  output/libyuv-x86_64-unknown-linux-gnu/convert_to_i420.o  output/libyuv-x86_64-unknown-linux-gnu/cpu_id.o  output/libyuv-x86_64-unknown-linux-gnu/mjpeg_decoder.o  output/libyuv-x86_64-unknown-linux-gnu/mjpeg_validate.o  output/libyuv-x86_64-unknown-linux-gnu/planar_functions.o  output/libyuv-x86_64-unknown-linux-gnu/rotate_any.o  output/libyuv-x86_64-unknown-linux-gnu/rotate_argb.o  output/libyuv-x86_64-unknown-linux-gnu/rotate.o  output/libyuv-x86_64-unknown-linux-gnu/rotate_common.o  output/libyuv-x86_64-unknown-linux-gnu/rotate_gcc.o  output/libyuv-x86_64-unknown-linux-gnu/rotate_dspr2.o  output/libyuv-x86_64-unknown-linux-gnu/rotate_neon64.o  output/libyuv-x86_64-unknown-linux-gnu/rotate_neon.o  output/libyuv-x86_64-unknown-linux-gnu/rotate_win.o  output/libyuv-x86_64-unknown-linux-gnu/row_any.o  output/libyuv-x86_64-unknown-linux-gnu/row_common.o  output/libyuv-x86_64-unknown-linux-gnu/row_gcc.o  output/libyuv-x86_64-unknown-linux-gnu/row_dspr2.o  output/libyuv-x86_64-unknown-linux-gnu/row_neon64.o  output/libyuv-x86_64-unknown-linux-gnu/row_neon.o  output/libyuv-x86_64-unknown-linux-gnu/row_win.o  output/libyuv-x86_64-unknown-linux-gnu/scale_any.o  output/libyuv-x86_64-unknown-linux-gnu/scale_argb.o  output/libyuv-x86_64-unknown-linux-gnu/scale.o  output/libyuv-x86_64-unknown-linux-gnu/scale_common.o  output/libyuv-x86_64-unknown-linux-gnu/scale_gcc.o  output/libyuv-x86_64-unknown-linux-gnu/scale_dspr2.o  output/libyuv-x86_64-unknown-linux-gnu/scale_neon64.o  output/libyuv-x86_64-unknown-linux-gnu/scale_neon.o  output/libyuv-x86_64-unknown-linux-gnu/scale_win.o  output/libyuv-x86_64-unknown-linux-gnu/video_common.o
# r - output/libyuv-x86_64-unknown-linux-gnu/compare.o
# r - output/libyuv-x86_64-unknown-linux-gnu/compare_common.o
# r - output/libyuv-x86_64-unknown-linux-gnu/compare_gcc.o
# r - output/libyuv-x86_64-unknown-linux-gnu/compare_neon64.o
# r - output/libyuv-x86_64-unknown-linux-gnu/compare_neon.o
# r - output/libyuv-x86_64-unknown-linux-gnu/compare_win.o
# r - output/libyuv-x86_64-unknown-linux-gnu/convert_argb.o
# r - output/libyuv-x86_64-unknown-linux-gnu/convert.o
# r - output/libyuv-x86_64-unknown-linux-gnu/convert_from_argb.o
# r - output/libyuv-x86_64-unknown-linux-gnu/convert_from.o
# r - output/libyuv-x86_64-unknown-linux-gnu/convert_jpeg.o
# r - output/libyuv-x86_64-unknown-linux-gnu/convert_to_argb.o
# r - output/libyuv-x86_64-unknown-linux-gnu/convert_to_i420.o
# r - output/libyuv-x86_64-unknown-linux-gnu/cpu_id.o
# r - output/libyuv-x86_64-unknown-linux-gnu/mjpeg_decoder.o
# r - output/libyuv-x86_64-unknown-linux-gnu/mjpeg_validate.o
# r - output/libyuv-x86_64-unknown-linux-gnu/planar_functions.o
# r - output/libyuv-x86_64-unknown-linux-gnu/rotate_any.o
# r - output/libyuv-x86_64-unknown-linux-gnu/rotate_argb.o
# r - output/libyuv-x86_64-unknown-linux-gnu/rotate.o
# r - output/libyuv-x86_64-unknown-linux-gnu/rotate_common.o
# r - output/libyuv-x86_64-unknown-linux-gnu/rotate_gcc.o
# r - output/libyuv-x86_64-unknown-linux-gnu/rotate_dspr2.o
# r - output/libyuv-x86_64-unknown-linux-gnu/rotate_neon64.o
# r - output/libyuv-x86_64-unknown-linux-gnu/rotate_neon.o
# r - output/libyuv-x86_64-unknown-linux-gnu/rotate_win.o
# r - output/libyuv-x86_64-unknown-linux-gnu/row_any.o
# r - output/libyuv-x86_64-unknown-linux-gnu/row_common.o
# r - output/libyuv-x86_64-unknown-linux-gnu/row_gcc.o
# r - output/libyuv-x86_64-unknown-linux-gnu/row_dspr2.o
# r - output/libyuv-x86_64-unknown-linux-gnu/row_neon64.o
# r - output/libyuv-x86_64-unknown-linux-gnu/row_neon.o
# r - output/libyuv-x86_64-unknown-linux-gnu/row_win.o
# r - output/libyuv-x86_64-unknown-linux-gnu/scale_any.o
# r - output/libyuv-x86_64-unknown-linux-gnu/scale_argb.o
# r - output/libyuv-x86_64-unknown-linux-gnu/scale.o
# r - output/libyuv-x86_64-unknown-linux-gnu/scale_common.o
# r - output/libyuv-x86_64-unknown-linux-gnu/scale_gcc.o
# r - output/libyuv-x86_64-unknown-linux-gnu/scale_dspr2.o
# r - output/libyuv-x86_64-unknown-linux-gnu/scale_neon64.o
# r - output/libyuv-x86_64-unknown-linux-gnu/scale_neon.o
# r - output/libyuv-x86_64-unknown-linux-gnu/scale_win.o
# r - output/libyuv-x86_64-unknown-linux-gnu/video_common.o
# ranlib ../../lib/libyuv-x86_64-unknown-linux-gnu.a
# make[3]: Leaving directory '/home/vsedyshev/Work/1111/pjproject/third_party/build/yuv'
# make[2]: Leaving directory '/home/vsedyshev/Work/1111/pjproject/third_party/build/yuv'
# make[2]: Entering directory '/home/vsedyshev/Work/1111/pjproject/third_party/build/webrtc'
# make -f /home/vsedyshev/Work/1111/pjproject/build/rules.mak APP=WEBRTC app=libwebrtc ../../lib/libwebrtc-x86_64-unknown-linux-gnu.a
# make[3]: Entering directory '/home/vsedyshev/Work/1111/pjproject/third_party/build/webrtc'
# mkdir -p output/libwebrtc-x86_64-unknown-linux-gnu/common_audio/
# mkdir -p output/libwebrtc-x86_64-unknown-linux-gnu/common_audio/signal_processing/
# mkdir -p output/libwebrtc-x86_64-unknown-linux-gnu/modules/audio_processing/aec/
# mkdir -p output/libwebrtc-x86_64-unknown-linux-gnu/modules/audio_processing/aecm/
# mkdir -p output/libwebrtc-x86_64-unknown-linux-gnu/modules/audio_processing/ns/
# mkdir -p output/libwebrtc-x86_64-unknown-linux-gnu/modules/audio_processing/utility/
# mkdir -p output/libwebrtc-x86_64-unknown-linux-gnu/system_wrappers/source/
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I. -I../../webrtc/src -I../../../pjlib/include -fexceptions -DWEBRTC_POSIX=1  \
# 	-o output/libwebrtc-x86_64-unknown-linux-gnu/modules/audio_processing/aec/aec_core.o \
# 	../../webrtc/src/webrtc//modules/audio_processing/aec/aec_core.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I. -I../../webrtc/src -I../../../pjlib/include -fexceptions -DWEBRTC_POSIX=1  \
# 	-o output/libwebrtc-x86_64-unknown-linux-gnu/modules/audio_processing/aec/aec_rdft.o \
# 	../../webrtc/src/webrtc//modules/audio_processing/aec/aec_rdft.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I. -I../../webrtc/src -I../../../pjlib/include -fexceptions -DWEBRTC_POSIX=1  \
# 	-o output/libwebrtc-x86_64-unknown-linux-gnu/modules/audio_processing/aec/aec_resampler.o \
# 	../../webrtc/src/webrtc//modules/audio_processing/aec/aec_resampler.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I. -I../../webrtc/src -I../../../pjlib/include -fexceptions -DWEBRTC_POSIX=1  \
# 	-o output/libwebrtc-x86_64-unknown-linux-gnu/modules/audio_processing/aec/echo_cancellation.o \
# 	../../webrtc/src/webrtc//modules/audio_processing/aec/echo_cancellation.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I. -I../../webrtc/src -I../../../pjlib/include -fexceptions -DWEBRTC_POSIX=1  \
# 	-o output/libwebrtc-x86_64-unknown-linux-gnu/modules/audio_processing/aecm/aecm_core.o \
# 	../../webrtc/src/webrtc//modules/audio_processing/aecm/aecm_core.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I. -I../../webrtc/src -I../../../pjlib/include -fexceptions -DWEBRTC_POSIX=1  \
# 	-o output/libwebrtc-x86_64-unknown-linux-gnu/modules/audio_processing/aecm/echo_control_mobile.o \
# 	../../webrtc/src/webrtc//modules/audio_processing/aecm/echo_control_mobile.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I. -I../../webrtc/src -I../../../pjlib/include -fexceptions -DWEBRTC_POSIX=1  \
# 	-o output/libwebrtc-x86_64-unknown-linux-gnu/modules/audio_processing/ns/noise_suppression.o \
# 	../../webrtc/src/webrtc//modules/audio_processing/ns/noise_suppression.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I. -I../../webrtc/src -I../../../pjlib/include -fexceptions -DWEBRTC_POSIX=1  \
# 	-o output/libwebrtc-x86_64-unknown-linux-gnu/modules/audio_processing/ns/noise_suppression_x.o \
# 	../../webrtc/src/webrtc//modules/audio_processing/ns/noise_suppression_x.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I. -I../../webrtc/src -I../../../pjlib/include -fexceptions -DWEBRTC_POSIX=1  \
# 	-o output/libwebrtc-x86_64-unknown-linux-gnu/modules/audio_processing/ns/ns_core.o \
# 	../../webrtc/src/webrtc//modules/audio_processing/ns/ns_core.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I. -I../../webrtc/src -I../../../pjlib/include -fexceptions -DWEBRTC_POSIX=1  \
# 	-o output/libwebrtc-x86_64-unknown-linux-gnu/modules/audio_processing/ns/nsx_core.o \
# 	../../webrtc/src/webrtc//modules/audio_processing/ns/nsx_core.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I. -I../../webrtc/src -I../../../pjlib/include -fexceptions -DWEBRTC_POSIX=1  \
# 	-o output/libwebrtc-x86_64-unknown-linux-gnu/modules/audio_processing/utility/delay_estimator_wrapper.o \
# 	../../webrtc/src/webrtc//modules/audio_processing/utility/delay_estimator_wrapper.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I. -I../../webrtc/src -I../../../pjlib/include -fexceptions -DWEBRTC_POSIX=1  \
# 	-o output/libwebrtc-x86_64-unknown-linux-gnu/modules/audio_processing/utility/delay_estimator.o \
# 	../../webrtc/src/webrtc//modules/audio_processing/utility/delay_estimator.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I. -I../../webrtc/src -I../../../pjlib/include -fexceptions -DWEBRTC_POSIX=1  \
# 	-o output/libwebrtc-x86_64-unknown-linux-gnu/common_audio/fft4g.o \
# 	../../webrtc/src/webrtc//common_audio/fft4g.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I. -I../../webrtc/src -I../../../pjlib/include -fexceptions -DWEBRTC_POSIX=1  \
# 	-o output/libwebrtc-x86_64-unknown-linux-gnu/common_audio/ring_buffer.o \
# 	../../webrtc/src/webrtc//common_audio/ring_buffer.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I. -I../../webrtc/src -I../../../pjlib/include -fexceptions -DWEBRTC_POSIX=1  \
# 	-o output/libwebrtc-x86_64-unknown-linux-gnu/common_audio/signal_processing/complex_bit_reverse.o \
# 	../../webrtc/src/webrtc//common_audio/signal_processing/complex_bit_reverse.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I. -I../../webrtc/src -I../../../pjlib/include -fexceptions -DWEBRTC_POSIX=1  \
# 	-o output/libwebrtc-x86_64-unknown-linux-gnu/common_audio/signal_processing/complex_fft.o \
# 	../../webrtc/src/webrtc//common_audio/signal_processing/complex_fft.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I. -I../../webrtc/src -I../../../pjlib/include -fexceptions -DWEBRTC_POSIX=1  \
# 	-o output/libwebrtc-x86_64-unknown-linux-gnu/common_audio/signal_processing/copy_set_operations.o \
# 	../../webrtc/src/webrtc//common_audio/signal_processing/copy_set_operations.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I. -I../../webrtc/src -I../../../pjlib/include -fexceptions -DWEBRTC_POSIX=1  \
# 	-o output/libwebrtc-x86_64-unknown-linux-gnu/common_audio/signal_processing/cross_correlation.o \
# 	../../webrtc/src/webrtc//common_audio/signal_processing/cross_correlation.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I. -I../../webrtc/src -I../../../pjlib/include -fexceptions -DWEBRTC_POSIX=1  \
# 	-o output/libwebrtc-x86_64-unknown-linux-gnu/common_audio/signal_processing/division_operations.o \
# 	../../webrtc/src/webrtc//common_audio/signal_processing/division_operations.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I. -I../../webrtc/src -I../../../pjlib/include -fexceptions -DWEBRTC_POSIX=1  \
# 	-o output/libwebrtc-x86_64-unknown-linux-gnu/common_audio/signal_processing/downsample_fast.o \
# 	../../webrtc/src/webrtc//common_audio/signal_processing/downsample_fast.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I. -I../../webrtc/src -I../../../pjlib/include -fexceptions -DWEBRTC_POSIX=1  \
# 	-o output/libwebrtc-x86_64-unknown-linux-gnu/common_audio/signal_processing/energy.o \
# 	../../webrtc/src/webrtc//common_audio/signal_processing/energy.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I. -I../../webrtc/src -I../../../pjlib/include -fexceptions -DWEBRTC_POSIX=1  \
# 	-o output/libwebrtc-x86_64-unknown-linux-gnu/common_audio/signal_processing/get_scaling_square.o \
# 	../../webrtc/src/webrtc//common_audio/signal_processing/get_scaling_square.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I. -I../../webrtc/src -I../../../pjlib/include -fexceptions -DWEBRTC_POSIX=1  \
# 	-o output/libwebrtc-x86_64-unknown-linux-gnu/common_audio/signal_processing/min_max_operations.o \
# 	../../webrtc/src/webrtc//common_audio/signal_processing/min_max_operations.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I. -I../../webrtc/src -I../../../pjlib/include -fexceptions -DWEBRTC_POSIX=1  \
# 	-o output/libwebrtc-x86_64-unknown-linux-gnu/common_audio/signal_processing/randomization_functions.o \
# 	../../webrtc/src/webrtc//common_audio/signal_processing/randomization_functions.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I. -I../../webrtc/src -I../../../pjlib/include -fexceptions -DWEBRTC_POSIX=1  \
# 	-o output/libwebrtc-x86_64-unknown-linux-gnu/common_audio/signal_processing/real_fft.o \
# 	../../webrtc/src/webrtc//common_audio/signal_processing/real_fft.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I. -I../../webrtc/src -I../../../pjlib/include -fexceptions -DWEBRTC_POSIX=1  \
# 	-o output/libwebrtc-x86_64-unknown-linux-gnu/common_audio/signal_processing/spl_init.o \
# 	../../webrtc/src/webrtc//common_audio/signal_processing/spl_init.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I. -I../../webrtc/src -I../../../pjlib/include -fexceptions -DWEBRTC_POSIX=1  \
# 	-o output/libwebrtc-x86_64-unknown-linux-gnu/common_audio/signal_processing/spl_sqrt.o \
# 	../../webrtc/src/webrtc//common_audio/signal_processing/spl_sqrt.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I. -I../../webrtc/src -I../../../pjlib/include -fexceptions -DWEBRTC_POSIX=1  \
# 	-o output/libwebrtc-x86_64-unknown-linux-gnu/common_audio/signal_processing/spl_sqrt_floor.o \
# 	../../webrtc/src/webrtc//common_audio/signal_processing/spl_sqrt_floor.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I. -I../../webrtc/src -I../../../pjlib/include -fexceptions -DWEBRTC_POSIX=1  \
# 	-o output/libwebrtc-x86_64-unknown-linux-gnu/common_audio/signal_processing/vector_scaling_operations.o \
# 	../../webrtc/src/webrtc//common_audio/signal_processing/vector_scaling_operations.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I. -I../../webrtc/src -I../../../pjlib/include -fexceptions -DWEBRTC_POSIX=1  \
# 	-o output/libwebrtc-x86_64-unknown-linux-gnu/modules/audio_processing/aec/aec_core_sse2.o \
# 	../../webrtc/src/webrtc//modules/audio_processing/aec/aec_core_sse2.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I. -I../../webrtc/src -I../../../pjlib/include -fexceptions -DWEBRTC_POSIX=1  \
# 	-o output/libwebrtc-x86_64-unknown-linux-gnu/modules/audio_processing/aec/aec_rdft_sse2.o \
# 	../../webrtc/src/webrtc//modules/audio_processing/aec/aec_rdft_sse2.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I. -I../../webrtc/src -I../../../pjlib/include -fexceptions -DWEBRTC_POSIX=1  \
# 	-o output/libwebrtc-x86_64-unknown-linux-gnu/modules/audio_processing/aecm/aecm_core_c.o \
# 	../../webrtc/src/webrtc//modules/audio_processing/aecm/aecm_core_c.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I. -I../../webrtc/src -I../../../pjlib/include -fexceptions -DWEBRTC_POSIX=1  \
# 	-o output/libwebrtc-x86_64-unknown-linux-gnu/modules/audio_processing/ns/nsx_core_c.o \
# 	../../webrtc/src/webrtc//modules/audio_processing/ns/nsx_core_c.c 
# g++ -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I. -I../../webrtc/src -I../../../pjlib/include -fexceptions -DWEBRTC_POSIX=1  \
# 	-o output/libwebrtc-x86_64-unknown-linux-gnu/system_wrappers/source/cpu_features.o \
# 	../../webrtc/src/webrtc//system_wrappers/source/cpu_features.cc
# if test ! -d ../../lib; then mkdir -p ../../lib; fi
# ar rv ../../lib/libwebrtc-x86_64-unknown-linux-gnu.a  output/libwebrtc-x86_64-unknown-linux-gnu/modules/audio_processing/aec/aec_core.o  output/libwebrtc-x86_64-unknown-linux-gnu/modules/audio_processing/aec/aec_rdft.o  output/libwebrtc-x86_64-unknown-linux-gnu/modules/audio_processing/aec/aec_resampler.o  output/libwebrtc-x86_64-unknown-linux-gnu/modules/audio_processing/aec/echo_cancellation.o  output/libwebrtc-x86_64-unknown-linux-gnu/modules/audio_processing/aecm/aecm_core.o  output/libwebrtc-x86_64-unknown-linux-gnu/modules/audio_processing/aecm/echo_control_mobile.o  output/libwebrtc-x86_64-unknown-linux-gnu/modules/audio_processing/ns/noise_suppression.o  output/libwebrtc-x86_64-unknown-linux-gnu/modules/audio_processing/ns/noise_suppression_x.o  output/libwebrtc-x86_64-unknown-linux-gnu/modules/audio_processing/ns/ns_core.o  output/libwebrtc-x86_64-unknown-linux-gnu/modules/audio_processing/ns/nsx_core.o  output/libwebrtc-x86_64-unknown-linux-gnu/modules/audio_processing/utility/delay_estimator_wrapper.o  output/libwebrtc-x86_64-unknown-linux-gnu/modules/audio_processing/utility/delay_estimator.o  output/libwebrtc-x86_64-unknown-linux-gnu/common_audio/fft4g.o  output/libwebrtc-x86_64-unknown-linux-gnu/common_audio/ring_buffer.o  output/libwebrtc-x86_64-unknown-linux-gnu/common_audio/signal_processing/complex_bit_reverse.o  output/libwebrtc-x86_64-unknown-linux-gnu/common_audio/signal_processing/complex_fft.o  output/libwebrtc-x86_64-unknown-linux-gnu/common_audio/signal_processing/copy_set_operations.o  output/libwebrtc-x86_64-unknown-linux-gnu/common_audio/signal_processing/cross_correlation.o  output/libwebrtc-x86_64-unknown-linux-gnu/common_audio/signal_processing/division_operations.o  output/libwebrtc-x86_64-unknown-linux-gnu/common_audio/signal_processing/downsample_fast.o  output/libwebrtc-x86_64-unknown-linux-gnu/common_audio/signal_processing/energy.o  output/libwebrtc-x86_64-unknown-linux-gnu/common_audio/signal_processing/get_scaling_square.o  output/libwebrtc-x86_64-unknown-linux-gnu/common_audio/signal_processing/min_max_operations.o  output/libwebrtc-x86_64-unknown-linux-gnu/common_audio/signal_processing/randomization_functions.o  output/libwebrtc-x86_64-unknown-linux-gnu/common_audio/signal_processing/real_fft.o  output/libwebrtc-x86_64-unknown-linux-gnu/common_audio/signal_processing/spl_init.o  output/libwebrtc-x86_64-unknown-linux-gnu/common_audio/signal_processing/spl_sqrt.o  output/libwebrtc-x86_64-unknown-linux-gnu/common_audio/signal_processing/spl_sqrt_floor.o  output/libwebrtc-x86_64-unknown-linux-gnu/common_audio/signal_processing/vector_scaling_operations.o  output/libwebrtc-x86_64-unknown-linux-gnu/modules/audio_processing/aec/aec_core_sse2.o  output/libwebrtc-x86_64-unknown-linux-gnu/modules/audio_processing/aec/aec_rdft_sse2.o  output/libwebrtc-x86_64-unknown-linux-gnu/modules/audio_processing/aecm/aecm_core_c.o  output/libwebrtc-x86_64-unknown-linux-gnu/modules/audio_processing/ns/nsx_core_c.o  output/libwebrtc-x86_64-unknown-linux-gnu/system_wrappers/source/cpu_features.o
# r - output/libwebrtc-x86_64-unknown-linux-gnu/modules/audio_processing/aec/aec_core.o
# r - output/libwebrtc-x86_64-unknown-linux-gnu/modules/audio_processing/aec/aec_rdft.o
# r - output/libwebrtc-x86_64-unknown-linux-gnu/modules/audio_processing/aec/aec_resampler.o
# r - output/libwebrtc-x86_64-unknown-linux-gnu/modules/audio_processing/aec/echo_cancellation.o
# r - output/libwebrtc-x86_64-unknown-linux-gnu/modules/audio_processing/aecm/aecm_core.o
# r - output/libwebrtc-x86_64-unknown-linux-gnu/modules/audio_processing/aecm/echo_control_mobile.o
# r - output/libwebrtc-x86_64-unknown-linux-gnu/modules/audio_processing/ns/noise_suppression.o
# r - output/libwebrtc-x86_64-unknown-linux-gnu/modules/audio_processing/ns/noise_suppression_x.o
# r - output/libwebrtc-x86_64-unknown-linux-gnu/modules/audio_processing/ns/ns_core.o
# r - output/libwebrtc-x86_64-unknown-linux-gnu/modules/audio_processing/ns/nsx_core.o
# r - output/libwebrtc-x86_64-unknown-linux-gnu/modules/audio_processing/utility/delay_estimator_wrapper.o
# r - output/libwebrtc-x86_64-unknown-linux-gnu/modules/audio_processing/utility/delay_estimator.o
# r - output/libwebrtc-x86_64-unknown-linux-gnu/common_audio/fft4g.o
# r - output/libwebrtc-x86_64-unknown-linux-gnu/common_audio/ring_buffer.o
# r - output/libwebrtc-x86_64-unknown-linux-gnu/common_audio/signal_processing/complex_bit_reverse.o
# r - output/libwebrtc-x86_64-unknown-linux-gnu/common_audio/signal_processing/complex_fft.o
# r - output/libwebrtc-x86_64-unknown-linux-gnu/common_audio/signal_processing/copy_set_operations.o
# r - output/libwebrtc-x86_64-unknown-linux-gnu/common_audio/signal_processing/cross_correlation.o
# r - output/libwebrtc-x86_64-unknown-linux-gnu/common_audio/signal_processing/division_operations.o
# r - output/libwebrtc-x86_64-unknown-linux-gnu/common_audio/signal_processing/downsample_fast.o
# r - output/libwebrtc-x86_64-unknown-linux-gnu/common_audio/signal_processing/energy.o
# r - output/libwebrtc-x86_64-unknown-linux-gnu/common_audio/signal_processing/get_scaling_square.o
# r - output/libwebrtc-x86_64-unknown-linux-gnu/common_audio/signal_processing/min_max_operations.o
# r - output/libwebrtc-x86_64-unknown-linux-gnu/common_audio/signal_processing/randomization_functions.o
# r - output/libwebrtc-x86_64-unknown-linux-gnu/common_audio/signal_processing/real_fft.o
# r - output/libwebrtc-x86_64-unknown-linux-gnu/common_audio/signal_processing/spl_init.o
# r - output/libwebrtc-x86_64-unknown-linux-gnu/common_audio/signal_processing/spl_sqrt.o
# r - output/libwebrtc-x86_64-unknown-linux-gnu/common_audio/signal_processing/spl_sqrt_floor.o
# r - output/libwebrtc-x86_64-unknown-linux-gnu/common_audio/signal_processing/vector_scaling_operations.o
# r - output/libwebrtc-x86_64-unknown-linux-gnu/modules/audio_processing/aec/aec_core_sse2.o
# r - output/libwebrtc-x86_64-unknown-linux-gnu/modules/audio_processing/aec/aec_rdft_sse2.o
# r - output/libwebrtc-x86_64-unknown-linux-gnu/modules/audio_processing/aecm/aecm_core_c.o
# r - output/libwebrtc-x86_64-unknown-linux-gnu/modules/audio_processing/ns/nsx_core_c.o
# r - output/libwebrtc-x86_64-unknown-linux-gnu/system_wrappers/source/cpu_features.o
# ranlib ../../lib/libwebrtc-x86_64-unknown-linux-gnu.a
# make[3]: Leaving directory '/home/vsedyshev/Work/1111/pjproject/third_party/build/webrtc'
# make[2]: Leaving directory '/home/vsedyshev/Work/1111/pjproject/third_party/build/webrtc'
# make[1]: Leaving directory '/home/vsedyshev/Work/1111/pjproject/third_party/build'
# make[1]: Entering directory '/home/vsedyshev/Work/1111/pjproject/pjmedia/build'
# make -f /home/vsedyshev/Work/1111/pjproject/build/rules.mak APP=PJMEDIA app=pjmedia ../lib/libpjmedia-x86_64-unknown-linux-gnu.a
# make[2]: Entering directory '/home/vsedyshev/Work/1111/pjproject/pjmedia/build'
# mkdir -p output/pjmedia-x86_64-unknown-linux-gnu/
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1   -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1        -I/home/vsedyshev/Work/1111/pjproject/third_party/build/speex -I/home/vsedyshev/Work/1111/pjproject/third_party/speex/include -DPJMEDIA_HAS_OPENCORE_AMRNB_CODEC=0 -DPJMEDIA_HAS_OPENCORE_AMRWB_CODEC=0 -I/home/vsedyshev/Work/1111/pjproject/third_party/build/srtp -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/crypto/include -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/include -DPJMEDIA_RESAMPLE_IMP=PJMEDIA_RESAMPLE_LIBRESAMPLE -DPJMEDIA_HAS_LIBYUV=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/yuv/include -DPJMEDIA_HAS_WEBRTC_AEC=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/webrtc/src -DPJMEDIA_AUDIO_DEV_HAS_ALSA=1 -DPJMEDIA_AUDIO_DEV_HAS_PORTAUDIO=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjmedia/include -I../../pjnath/include -I../.. \
# 	-o output/pjmedia-x86_64-unknown-linux-gnu/echo_speex.o \
# 	../src/pjmedia/echo_speex.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1   -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1        -I/home/vsedyshev/Work/1111/pjproject/third_party/build/speex -I/home/vsedyshev/Work/1111/pjproject/third_party/speex/include -DPJMEDIA_HAS_OPENCORE_AMRNB_CODEC=0 -DPJMEDIA_HAS_OPENCORE_AMRWB_CODEC=0 -I/home/vsedyshev/Work/1111/pjproject/third_party/build/srtp -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/crypto/include -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/include -DPJMEDIA_RESAMPLE_IMP=PJMEDIA_RESAMPLE_LIBRESAMPLE -DPJMEDIA_HAS_LIBYUV=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/yuv/include -DPJMEDIA_HAS_WEBRTC_AEC=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/webrtc/src -DPJMEDIA_AUDIO_DEV_HAS_ALSA=1 -DPJMEDIA_AUDIO_DEV_HAS_PORTAUDIO=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjmedia/include -I../../pjnath/include -I../.. \
# 	-o output/pjmedia-x86_64-unknown-linux-gnu/alaw_ulaw.o \
# 	../src/pjmedia/alaw_ulaw.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1   -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1        -I/home/vsedyshev/Work/1111/pjproject/third_party/build/speex -I/home/vsedyshev/Work/1111/pjproject/third_party/speex/include -DPJMEDIA_HAS_OPENCORE_AMRNB_CODEC=0 -DPJMEDIA_HAS_OPENCORE_AMRWB_CODEC=0 -I/home/vsedyshev/Work/1111/pjproject/third_party/build/srtp -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/crypto/include -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/include -DPJMEDIA_RESAMPLE_IMP=PJMEDIA_RESAMPLE_LIBRESAMPLE -DPJMEDIA_HAS_LIBYUV=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/yuv/include -DPJMEDIA_HAS_WEBRTC_AEC=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/webrtc/src -DPJMEDIA_AUDIO_DEV_HAS_ALSA=1 -DPJMEDIA_AUDIO_DEV_HAS_PORTAUDIO=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjmedia/include -I../../pjnath/include -I../.. \
# 	-o output/pjmedia-x86_64-unknown-linux-gnu/alaw_ulaw_table.o \
# 	../src/pjmedia/alaw_ulaw_table.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1   -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1        -I/home/vsedyshev/Work/1111/pjproject/third_party/build/speex -I/home/vsedyshev/Work/1111/pjproject/third_party/speex/include -DPJMEDIA_HAS_OPENCORE_AMRNB_CODEC=0 -DPJMEDIA_HAS_OPENCORE_AMRWB_CODEC=0 -I/home/vsedyshev/Work/1111/pjproject/third_party/build/srtp -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/crypto/include -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/include -DPJMEDIA_RESAMPLE_IMP=PJMEDIA_RESAMPLE_LIBRESAMPLE -DPJMEDIA_HAS_LIBYUV=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/yuv/include -DPJMEDIA_HAS_WEBRTC_AEC=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/webrtc/src -DPJMEDIA_AUDIO_DEV_HAS_ALSA=1 -DPJMEDIA_AUDIO_DEV_HAS_PORTAUDIO=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjmedia/include -I../../pjnath/include -I../.. \
# 	-o output/pjmedia-x86_64-unknown-linux-gnu/avi_player.o \
# 	../src/pjmedia/avi_player.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1   -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1        -I/home/vsedyshev/Work/1111/pjproject/third_party/build/speex -I/home/vsedyshev/Work/1111/pjproject/third_party/speex/include -DPJMEDIA_HAS_OPENCORE_AMRNB_CODEC=0 -DPJMEDIA_HAS_OPENCORE_AMRWB_CODEC=0 -I/home/vsedyshev/Work/1111/pjproject/third_party/build/srtp -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/crypto/include -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/include -DPJMEDIA_RESAMPLE_IMP=PJMEDIA_RESAMPLE_LIBRESAMPLE -DPJMEDIA_HAS_LIBYUV=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/yuv/include -DPJMEDIA_HAS_WEBRTC_AEC=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/webrtc/src -DPJMEDIA_AUDIO_DEV_HAS_ALSA=1 -DPJMEDIA_AUDIO_DEV_HAS_PORTAUDIO=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjmedia/include -I../../pjnath/include -I../.. \
# 	-o output/pjmedia-x86_64-unknown-linux-gnu/bidirectional.o \
# 	../src/pjmedia/bidirectional.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1   -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1        -I/home/vsedyshev/Work/1111/pjproject/third_party/build/speex -I/home/vsedyshev/Work/1111/pjproject/third_party/speex/include -DPJMEDIA_HAS_OPENCORE_AMRNB_CODEC=0 -DPJMEDIA_HAS_OPENCORE_AMRWB_CODEC=0 -I/home/vsedyshev/Work/1111/pjproject/third_party/build/srtp -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/crypto/include -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/include -DPJMEDIA_RESAMPLE_IMP=PJMEDIA_RESAMPLE_LIBRESAMPLE -DPJMEDIA_HAS_LIBYUV=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/yuv/include -DPJMEDIA_HAS_WEBRTC_AEC=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/webrtc/src -DPJMEDIA_AUDIO_DEV_HAS_ALSA=1 -DPJMEDIA_AUDIO_DEV_HAS_PORTAUDIO=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjmedia/include -I../../pjnath/include -I../.. \
# 	-o output/pjmedia-x86_64-unknown-linux-gnu/clock_thread.o \
# 	../src/pjmedia/clock_thread.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1   -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1        -I/home/vsedyshev/Work/1111/pjproject/third_party/build/speex -I/home/vsedyshev/Work/1111/pjproject/third_party/speex/include -DPJMEDIA_HAS_OPENCORE_AMRNB_CODEC=0 -DPJMEDIA_HAS_OPENCORE_AMRWB_CODEC=0 -I/home/vsedyshev/Work/1111/pjproject/third_party/build/srtp -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/crypto/include -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/include -DPJMEDIA_RESAMPLE_IMP=PJMEDIA_RESAMPLE_LIBRESAMPLE -DPJMEDIA_HAS_LIBYUV=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/yuv/include -DPJMEDIA_HAS_WEBRTC_AEC=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/webrtc/src -DPJMEDIA_AUDIO_DEV_HAS_ALSA=1 -DPJMEDIA_AUDIO_DEV_HAS_PORTAUDIO=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjmedia/include -I../../pjnath/include -I../.. \
# 	-o output/pjmedia-x86_64-unknown-linux-gnu/codec.o \
# 	../src/pjmedia/codec.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1   -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1        -I/home/vsedyshev/Work/1111/pjproject/third_party/build/speex -I/home/vsedyshev/Work/1111/pjproject/third_party/speex/include -DPJMEDIA_HAS_OPENCORE_AMRNB_CODEC=0 -DPJMEDIA_HAS_OPENCORE_AMRWB_CODEC=0 -I/home/vsedyshev/Work/1111/pjproject/third_party/build/srtp -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/crypto/include -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/include -DPJMEDIA_RESAMPLE_IMP=PJMEDIA_RESAMPLE_LIBRESAMPLE -DPJMEDIA_HAS_LIBYUV=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/yuv/include -DPJMEDIA_HAS_WEBRTC_AEC=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/webrtc/src -DPJMEDIA_AUDIO_DEV_HAS_ALSA=1 -DPJMEDIA_AUDIO_DEV_HAS_PORTAUDIO=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjmedia/include -I../../pjnath/include -I../.. \
# 	-o output/pjmedia-x86_64-unknown-linux-gnu/conference.o \
# 	../src/pjmedia/conference.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1   -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1        -I/home/vsedyshev/Work/1111/pjproject/third_party/build/speex -I/home/vsedyshev/Work/1111/pjproject/third_party/speex/include -DPJMEDIA_HAS_OPENCORE_AMRNB_CODEC=0 -DPJMEDIA_HAS_OPENCORE_AMRWB_CODEC=0 -I/home/vsedyshev/Work/1111/pjproject/third_party/build/srtp -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/crypto/include -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/include -DPJMEDIA_RESAMPLE_IMP=PJMEDIA_RESAMPLE_LIBRESAMPLE -DPJMEDIA_HAS_LIBYUV=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/yuv/include -DPJMEDIA_HAS_WEBRTC_AEC=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/webrtc/src -DPJMEDIA_AUDIO_DEV_HAS_ALSA=1 -DPJMEDIA_AUDIO_DEV_HAS_PORTAUDIO=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjmedia/include -I../../pjnath/include -I../.. \
# 	-o output/pjmedia-x86_64-unknown-linux-gnu/conf_switch.o \
# 	../src/pjmedia/conf_switch.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1   -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1        -I/home/vsedyshev/Work/1111/pjproject/third_party/build/speex -I/home/vsedyshev/Work/1111/pjproject/third_party/speex/include -DPJMEDIA_HAS_OPENCORE_AMRNB_CODEC=0 -DPJMEDIA_HAS_OPENCORE_AMRWB_CODEC=0 -I/home/vsedyshev/Work/1111/pjproject/third_party/build/srtp -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/crypto/include -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/include -DPJMEDIA_RESAMPLE_IMP=PJMEDIA_RESAMPLE_LIBRESAMPLE -DPJMEDIA_HAS_LIBYUV=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/yuv/include -DPJMEDIA_HAS_WEBRTC_AEC=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/webrtc/src -DPJMEDIA_AUDIO_DEV_HAS_ALSA=1 -DPJMEDIA_AUDIO_DEV_HAS_PORTAUDIO=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjmedia/include -I../../pjnath/include -I../.. \
# 	-o output/pjmedia-x86_64-unknown-linux-gnu/converter.o \
# 	../src/pjmedia/converter.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1   -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1        -I/home/vsedyshev/Work/1111/pjproject/third_party/build/speex -I/home/vsedyshev/Work/1111/pjproject/third_party/speex/include -DPJMEDIA_HAS_OPENCORE_AMRNB_CODEC=0 -DPJMEDIA_HAS_OPENCORE_AMRWB_CODEC=0 -I/home/vsedyshev/Work/1111/pjproject/third_party/build/srtp -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/crypto/include -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/include -DPJMEDIA_RESAMPLE_IMP=PJMEDIA_RESAMPLE_LIBRESAMPLE -DPJMEDIA_HAS_LIBYUV=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/yuv/include -DPJMEDIA_HAS_WEBRTC_AEC=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/webrtc/src -DPJMEDIA_AUDIO_DEV_HAS_ALSA=1 -DPJMEDIA_AUDIO_DEV_HAS_PORTAUDIO=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjmedia/include -I../../pjnath/include -I../.. \
# 	-o output/pjmedia-x86_64-unknown-linux-gnu/converter_libswscale.o \
# 	../src/pjmedia/converter_libswscale.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1   -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1        -I/home/vsedyshev/Work/1111/pjproject/third_party/build/speex -I/home/vsedyshev/Work/1111/pjproject/third_party/speex/include -DPJMEDIA_HAS_OPENCORE_AMRNB_CODEC=0 -DPJMEDIA_HAS_OPENCORE_AMRWB_CODEC=0 -I/home/vsedyshev/Work/1111/pjproject/third_party/build/srtp -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/crypto/include -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/include -DPJMEDIA_RESAMPLE_IMP=PJMEDIA_RESAMPLE_LIBRESAMPLE -DPJMEDIA_HAS_LIBYUV=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/yuv/include -DPJMEDIA_HAS_WEBRTC_AEC=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/webrtc/src -DPJMEDIA_AUDIO_DEV_HAS_ALSA=1 -DPJMEDIA_AUDIO_DEV_HAS_PORTAUDIO=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjmedia/include -I../../pjnath/include -I../.. \
# 	-o output/pjmedia-x86_64-unknown-linux-gnu/converter_libyuv.o \
# 	../src/pjmedia/converter_libyuv.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1   -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1        -I/home/vsedyshev/Work/1111/pjproject/third_party/build/speex -I/home/vsedyshev/Work/1111/pjproject/third_party/speex/include -DPJMEDIA_HAS_OPENCORE_AMRNB_CODEC=0 -DPJMEDIA_HAS_OPENCORE_AMRWB_CODEC=0 -I/home/vsedyshev/Work/1111/pjproject/third_party/build/srtp -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/crypto/include -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/include -DPJMEDIA_RESAMPLE_IMP=PJMEDIA_RESAMPLE_LIBRESAMPLE -DPJMEDIA_HAS_LIBYUV=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/yuv/include -DPJMEDIA_HAS_WEBRTC_AEC=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/webrtc/src -DPJMEDIA_AUDIO_DEV_HAS_ALSA=1 -DPJMEDIA_AUDIO_DEV_HAS_PORTAUDIO=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjmedia/include -I../../pjnath/include -I../.. \
# 	-o output/pjmedia-x86_64-unknown-linux-gnu/delaybuf.o \
# 	../src/pjmedia/delaybuf.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1   -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1        -I/home/vsedyshev/Work/1111/pjproject/third_party/build/speex -I/home/vsedyshev/Work/1111/pjproject/third_party/speex/include -DPJMEDIA_HAS_OPENCORE_AMRNB_CODEC=0 -DPJMEDIA_HAS_OPENCORE_AMRWB_CODEC=0 -I/home/vsedyshev/Work/1111/pjproject/third_party/build/srtp -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/crypto/include -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/include -DPJMEDIA_RESAMPLE_IMP=PJMEDIA_RESAMPLE_LIBRESAMPLE -DPJMEDIA_HAS_LIBYUV=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/yuv/include -DPJMEDIA_HAS_WEBRTC_AEC=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/webrtc/src -DPJMEDIA_AUDIO_DEV_HAS_ALSA=1 -DPJMEDIA_AUDIO_DEV_HAS_PORTAUDIO=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjmedia/include -I../../pjnath/include -I../.. \
# 	-o output/pjmedia-x86_64-unknown-linux-gnu/echo_common.o \
# 	../src/pjmedia/echo_common.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1   -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1        -I/home/vsedyshev/Work/1111/pjproject/third_party/build/speex -I/home/vsedyshev/Work/1111/pjproject/third_party/speex/include -DPJMEDIA_HAS_OPENCORE_AMRNB_CODEC=0 -DPJMEDIA_HAS_OPENCORE_AMRWB_CODEC=0 -I/home/vsedyshev/Work/1111/pjproject/third_party/build/srtp -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/crypto/include -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/include -DPJMEDIA_RESAMPLE_IMP=PJMEDIA_RESAMPLE_LIBRESAMPLE -DPJMEDIA_HAS_LIBYUV=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/yuv/include -DPJMEDIA_HAS_WEBRTC_AEC=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/webrtc/src -DPJMEDIA_AUDIO_DEV_HAS_ALSA=1 -DPJMEDIA_AUDIO_DEV_HAS_PORTAUDIO=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjmedia/include -I../../pjnath/include -I../.. \
# 	-o output/pjmedia-x86_64-unknown-linux-gnu/echo_port.o \
# 	../src/pjmedia/echo_port.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1   -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1        -I/home/vsedyshev/Work/1111/pjproject/third_party/build/speex -I/home/vsedyshev/Work/1111/pjproject/third_party/speex/include -DPJMEDIA_HAS_OPENCORE_AMRNB_CODEC=0 -DPJMEDIA_HAS_OPENCORE_AMRWB_CODEC=0 -I/home/vsedyshev/Work/1111/pjproject/third_party/build/srtp -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/crypto/include -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/include -DPJMEDIA_RESAMPLE_IMP=PJMEDIA_RESAMPLE_LIBRESAMPLE -DPJMEDIA_HAS_LIBYUV=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/yuv/include -DPJMEDIA_HAS_WEBRTC_AEC=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/webrtc/src -DPJMEDIA_AUDIO_DEV_HAS_ALSA=1 -DPJMEDIA_AUDIO_DEV_HAS_PORTAUDIO=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjmedia/include -I../../pjnath/include -I../.. \
# 	-o output/pjmedia-x86_64-unknown-linux-gnu/echo_suppress.o \
# 	../src/pjmedia/echo_suppress.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1   -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1        -I/home/vsedyshev/Work/1111/pjproject/third_party/build/speex -I/home/vsedyshev/Work/1111/pjproject/third_party/speex/include -DPJMEDIA_HAS_OPENCORE_AMRNB_CODEC=0 -DPJMEDIA_HAS_OPENCORE_AMRWB_CODEC=0 -I/home/vsedyshev/Work/1111/pjproject/third_party/build/srtp -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/crypto/include -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/include -DPJMEDIA_RESAMPLE_IMP=PJMEDIA_RESAMPLE_LIBRESAMPLE -DPJMEDIA_HAS_LIBYUV=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/yuv/include -DPJMEDIA_HAS_WEBRTC_AEC=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/webrtc/src -DPJMEDIA_AUDIO_DEV_HAS_ALSA=1 -DPJMEDIA_AUDIO_DEV_HAS_PORTAUDIO=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjmedia/include -I../../pjnath/include -I../.. \
# 	-o output/pjmedia-x86_64-unknown-linux-gnu/echo_webrtc.o \
# 	../src/pjmedia/echo_webrtc.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1   -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1        -I/home/vsedyshev/Work/1111/pjproject/third_party/build/speex -I/home/vsedyshev/Work/1111/pjproject/third_party/speex/include -DPJMEDIA_HAS_OPENCORE_AMRNB_CODEC=0 -DPJMEDIA_HAS_OPENCORE_AMRWB_CODEC=0 -I/home/vsedyshev/Work/1111/pjproject/third_party/build/srtp -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/crypto/include -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/include -DPJMEDIA_RESAMPLE_IMP=PJMEDIA_RESAMPLE_LIBRESAMPLE -DPJMEDIA_HAS_LIBYUV=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/yuv/include -DPJMEDIA_HAS_WEBRTC_AEC=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/webrtc/src -DPJMEDIA_AUDIO_DEV_HAS_ALSA=1 -DPJMEDIA_AUDIO_DEV_HAS_PORTAUDIO=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjmedia/include -I../../pjnath/include -I../.. \
# 	-o output/pjmedia-x86_64-unknown-linux-gnu/endpoint.o \
# 	../src/pjmedia/endpoint.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1   -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1        -I/home/vsedyshev/Work/1111/pjproject/third_party/build/speex -I/home/vsedyshev/Work/1111/pjproject/third_party/speex/include -DPJMEDIA_HAS_OPENCORE_AMRNB_CODEC=0 -DPJMEDIA_HAS_OPENCORE_AMRWB_CODEC=0 -I/home/vsedyshev/Work/1111/pjproject/third_party/build/srtp -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/crypto/include -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/include -DPJMEDIA_RESAMPLE_IMP=PJMEDIA_RESAMPLE_LIBRESAMPLE -DPJMEDIA_HAS_LIBYUV=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/yuv/include -DPJMEDIA_HAS_WEBRTC_AEC=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/webrtc/src -DPJMEDIA_AUDIO_DEV_HAS_ALSA=1 -DPJMEDIA_AUDIO_DEV_HAS_PORTAUDIO=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjmedia/include -I../../pjnath/include -I../.. \
# 	-o output/pjmedia-x86_64-unknown-linux-gnu/errno.o \
# 	../src/pjmedia/errno.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1   -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1        -I/home/vsedyshev/Work/1111/pjproject/third_party/build/speex -I/home/vsedyshev/Work/1111/pjproject/third_party/speex/include -DPJMEDIA_HAS_OPENCORE_AMRNB_CODEC=0 -DPJMEDIA_HAS_OPENCORE_AMRWB_CODEC=0 -I/home/vsedyshev/Work/1111/pjproject/third_party/build/srtp -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/crypto/include -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/include -DPJMEDIA_RESAMPLE_IMP=PJMEDIA_RESAMPLE_LIBRESAMPLE -DPJMEDIA_HAS_LIBYUV=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/yuv/include -DPJMEDIA_HAS_WEBRTC_AEC=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/webrtc/src -DPJMEDIA_AUDIO_DEV_HAS_ALSA=1 -DPJMEDIA_AUDIO_DEV_HAS_PORTAUDIO=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjmedia/include -I../../pjnath/include -I../.. \
# 	-o output/pjmedia-x86_64-unknown-linux-gnu/event.o \
# 	../src/pjmedia/event.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1   -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1        -I/home/vsedyshev/Work/1111/pjproject/third_party/build/speex -I/home/vsedyshev/Work/1111/pjproject/third_party/speex/include -DPJMEDIA_HAS_OPENCORE_AMRNB_CODEC=0 -DPJMEDIA_HAS_OPENCORE_AMRWB_CODEC=0 -I/home/vsedyshev/Work/1111/pjproject/third_party/build/srtp -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/crypto/include -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/include -DPJMEDIA_RESAMPLE_IMP=PJMEDIA_RESAMPLE_LIBRESAMPLE -DPJMEDIA_HAS_LIBYUV=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/yuv/include -DPJMEDIA_HAS_WEBRTC_AEC=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/webrtc/src -DPJMEDIA_AUDIO_DEV_HAS_ALSA=1 -DPJMEDIA_AUDIO_DEV_HAS_PORTAUDIO=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjmedia/include -I../../pjnath/include -I../.. \
# 	-o output/pjmedia-x86_64-unknown-linux-gnu/format.o \
# 	../src/pjmedia/format.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1   -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1        -I/home/vsedyshev/Work/1111/pjproject/third_party/build/speex -I/home/vsedyshev/Work/1111/pjproject/third_party/speex/include -DPJMEDIA_HAS_OPENCORE_AMRNB_CODEC=0 -DPJMEDIA_HAS_OPENCORE_AMRWB_CODEC=0 -I/home/vsedyshev/Work/1111/pjproject/third_party/build/srtp -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/crypto/include -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/include -DPJMEDIA_RESAMPLE_IMP=PJMEDIA_RESAMPLE_LIBRESAMPLE -DPJMEDIA_HAS_LIBYUV=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/yuv/include -DPJMEDIA_HAS_WEBRTC_AEC=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/webrtc/src -DPJMEDIA_AUDIO_DEV_HAS_ALSA=1 -DPJMEDIA_AUDIO_DEV_HAS_PORTAUDIO=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjmedia/include -I../../pjnath/include -I../.. \
# 	-o output/pjmedia-x86_64-unknown-linux-gnu/ffmpeg_util.o \
# 	../src/pjmedia/ffmpeg_util.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1   -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1        -I/home/vsedyshev/Work/1111/pjproject/third_party/build/speex -I/home/vsedyshev/Work/1111/pjproject/third_party/speex/include -DPJMEDIA_HAS_OPENCORE_AMRNB_CODEC=0 -DPJMEDIA_HAS_OPENCORE_AMRWB_CODEC=0 -I/home/vsedyshev/Work/1111/pjproject/third_party/build/srtp -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/crypto/include -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/include -DPJMEDIA_RESAMPLE_IMP=PJMEDIA_RESAMPLE_LIBRESAMPLE -DPJMEDIA_HAS_LIBYUV=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/yuv/include -DPJMEDIA_HAS_WEBRTC_AEC=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/webrtc/src -DPJMEDIA_AUDIO_DEV_HAS_ALSA=1 -DPJMEDIA_AUDIO_DEV_HAS_PORTAUDIO=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjmedia/include -I../../pjnath/include -I../.. \
# 	-o output/pjmedia-x86_64-unknown-linux-gnu/g711.o \
# 	../src/pjmedia/g711.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1   -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1        -I/home/vsedyshev/Work/1111/pjproject/third_party/build/speex -I/home/vsedyshev/Work/1111/pjproject/third_party/speex/include -DPJMEDIA_HAS_OPENCORE_AMRNB_CODEC=0 -DPJMEDIA_HAS_OPENCORE_AMRWB_CODEC=0 -I/home/vsedyshev/Work/1111/pjproject/third_party/build/srtp -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/crypto/include -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/include -DPJMEDIA_RESAMPLE_IMP=PJMEDIA_RESAMPLE_LIBRESAMPLE -DPJMEDIA_HAS_LIBYUV=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/yuv/include -DPJMEDIA_HAS_WEBRTC_AEC=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/webrtc/src -DPJMEDIA_AUDIO_DEV_HAS_ALSA=1 -DPJMEDIA_AUDIO_DEV_HAS_PORTAUDIO=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjmedia/include -I../../pjnath/include -I../.. \
# 	-o output/pjmedia-x86_64-unknown-linux-gnu/jbuf.o \
# 	../src/pjmedia/jbuf.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1   -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1        -I/home/vsedyshev/Work/1111/pjproject/third_party/build/speex -I/home/vsedyshev/Work/1111/pjproject/third_party/speex/include -DPJMEDIA_HAS_OPENCORE_AMRNB_CODEC=0 -DPJMEDIA_HAS_OPENCORE_AMRWB_CODEC=0 -I/home/vsedyshev/Work/1111/pjproject/third_party/build/srtp -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/crypto/include -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/include -DPJMEDIA_RESAMPLE_IMP=PJMEDIA_RESAMPLE_LIBRESAMPLE -DPJMEDIA_HAS_LIBYUV=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/yuv/include -DPJMEDIA_HAS_WEBRTC_AEC=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/webrtc/src -DPJMEDIA_AUDIO_DEV_HAS_ALSA=1 -DPJMEDIA_AUDIO_DEV_HAS_PORTAUDIO=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjmedia/include -I../../pjnath/include -I../.. \
# 	-o output/pjmedia-x86_64-unknown-linux-gnu/master_port.o \
# 	../src/pjmedia/master_port.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1   -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1        -I/home/vsedyshev/Work/1111/pjproject/third_party/build/speex -I/home/vsedyshev/Work/1111/pjproject/third_party/speex/include -DPJMEDIA_HAS_OPENCORE_AMRNB_CODEC=0 -DPJMEDIA_HAS_OPENCORE_AMRWB_CODEC=0 -I/home/vsedyshev/Work/1111/pjproject/third_party/build/srtp -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/crypto/include -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/include -DPJMEDIA_RESAMPLE_IMP=PJMEDIA_RESAMPLE_LIBRESAMPLE -DPJMEDIA_HAS_LIBYUV=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/yuv/include -DPJMEDIA_HAS_WEBRTC_AEC=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/webrtc/src -DPJMEDIA_AUDIO_DEV_HAS_ALSA=1 -DPJMEDIA_AUDIO_DEV_HAS_PORTAUDIO=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjmedia/include -I../../pjnath/include -I../.. \
# 	-o output/pjmedia-x86_64-unknown-linux-gnu/mem_capture.o \
# 	../src/pjmedia/mem_capture.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1   -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1        -I/home/vsedyshev/Work/1111/pjproject/third_party/build/speex -I/home/vsedyshev/Work/1111/pjproject/third_party/speex/include -DPJMEDIA_HAS_OPENCORE_AMRNB_CODEC=0 -DPJMEDIA_HAS_OPENCORE_AMRWB_CODEC=0 -I/home/vsedyshev/Work/1111/pjproject/third_party/build/srtp -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/crypto/include -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/include -DPJMEDIA_RESAMPLE_IMP=PJMEDIA_RESAMPLE_LIBRESAMPLE -DPJMEDIA_HAS_LIBYUV=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/yuv/include -DPJMEDIA_HAS_WEBRTC_AEC=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/webrtc/src -DPJMEDIA_AUDIO_DEV_HAS_ALSA=1 -DPJMEDIA_AUDIO_DEV_HAS_PORTAUDIO=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjmedia/include -I../../pjnath/include -I../.. \
# 	-o output/pjmedia-x86_64-unknown-linux-gnu/mem_player.o \
# 	../src/pjmedia/mem_player.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1   -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1        -I/home/vsedyshev/Work/1111/pjproject/third_party/build/speex -I/home/vsedyshev/Work/1111/pjproject/third_party/speex/include -DPJMEDIA_HAS_OPENCORE_AMRNB_CODEC=0 -DPJMEDIA_HAS_OPENCORE_AMRWB_CODEC=0 -I/home/vsedyshev/Work/1111/pjproject/third_party/build/srtp -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/crypto/include -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/include -DPJMEDIA_RESAMPLE_IMP=PJMEDIA_RESAMPLE_LIBRESAMPLE -DPJMEDIA_HAS_LIBYUV=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/yuv/include -DPJMEDIA_HAS_WEBRTC_AEC=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/webrtc/src -DPJMEDIA_AUDIO_DEV_HAS_ALSA=1 -DPJMEDIA_AUDIO_DEV_HAS_PORTAUDIO=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjmedia/include -I../../pjnath/include -I../.. \
# 	-o output/pjmedia-x86_64-unknown-linux-gnu/null_port.o \
# 	../src/pjmedia/null_port.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1   -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1        -I/home/vsedyshev/Work/1111/pjproject/third_party/build/speex -I/home/vsedyshev/Work/1111/pjproject/third_party/speex/include -DPJMEDIA_HAS_OPENCORE_AMRNB_CODEC=0 -DPJMEDIA_HAS_OPENCORE_AMRWB_CODEC=0 -I/home/vsedyshev/Work/1111/pjproject/third_party/build/srtp -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/crypto/include -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/include -DPJMEDIA_RESAMPLE_IMP=PJMEDIA_RESAMPLE_LIBRESAMPLE -DPJMEDIA_HAS_LIBYUV=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/yuv/include -DPJMEDIA_HAS_WEBRTC_AEC=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/webrtc/src -DPJMEDIA_AUDIO_DEV_HAS_ALSA=1 -DPJMEDIA_AUDIO_DEV_HAS_PORTAUDIO=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjmedia/include -I../../pjnath/include -I../.. \
# 	-o output/pjmedia-x86_64-unknown-linux-gnu/plc_common.o \
# 	../src/pjmedia/plc_common.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1   -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1        -I/home/vsedyshev/Work/1111/pjproject/third_party/build/speex -I/home/vsedyshev/Work/1111/pjproject/third_party/speex/include -DPJMEDIA_HAS_OPENCORE_AMRNB_CODEC=0 -DPJMEDIA_HAS_OPENCORE_AMRWB_CODEC=0 -I/home/vsedyshev/Work/1111/pjproject/third_party/build/srtp -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/crypto/include -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/include -DPJMEDIA_RESAMPLE_IMP=PJMEDIA_RESAMPLE_LIBRESAMPLE -DPJMEDIA_HAS_LIBYUV=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/yuv/include -DPJMEDIA_HAS_WEBRTC_AEC=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/webrtc/src -DPJMEDIA_AUDIO_DEV_HAS_ALSA=1 -DPJMEDIA_AUDIO_DEV_HAS_PORTAUDIO=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjmedia/include -I../../pjnath/include -I../.. \
# 	-o output/pjmedia-x86_64-unknown-linux-gnu/port.o \
# 	../src/pjmedia/port.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1   -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1        -I/home/vsedyshev/Work/1111/pjproject/third_party/build/speex -I/home/vsedyshev/Work/1111/pjproject/third_party/speex/include -DPJMEDIA_HAS_OPENCORE_AMRNB_CODEC=0 -DPJMEDIA_HAS_OPENCORE_AMRWB_CODEC=0 -I/home/vsedyshev/Work/1111/pjproject/third_party/build/srtp -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/crypto/include -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/include -DPJMEDIA_RESAMPLE_IMP=PJMEDIA_RESAMPLE_LIBRESAMPLE -DPJMEDIA_HAS_LIBYUV=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/yuv/include -DPJMEDIA_HAS_WEBRTC_AEC=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/webrtc/src -DPJMEDIA_AUDIO_DEV_HAS_ALSA=1 -DPJMEDIA_AUDIO_DEV_HAS_PORTAUDIO=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjmedia/include -I../../pjnath/include -I../.. \
# 	-o output/pjmedia-x86_64-unknown-linux-gnu/splitcomb.o \
# 	../src/pjmedia/splitcomb.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1   -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1        -I/home/vsedyshev/Work/1111/pjproject/third_party/build/speex -I/home/vsedyshev/Work/1111/pjproject/third_party/speex/include -DPJMEDIA_HAS_OPENCORE_AMRNB_CODEC=0 -DPJMEDIA_HAS_OPENCORE_AMRWB_CODEC=0 -I/home/vsedyshev/Work/1111/pjproject/third_party/build/srtp -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/crypto/include -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/include -DPJMEDIA_RESAMPLE_IMP=PJMEDIA_RESAMPLE_LIBRESAMPLE -DPJMEDIA_HAS_LIBYUV=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/yuv/include -DPJMEDIA_HAS_WEBRTC_AEC=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/webrtc/src -DPJMEDIA_AUDIO_DEV_HAS_ALSA=1 -DPJMEDIA_AUDIO_DEV_HAS_PORTAUDIO=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjmedia/include -I../../pjnath/include -I../.. \
# 	-o output/pjmedia-x86_64-unknown-linux-gnu/resample_resample.o \
# 	../src/pjmedia/resample_resample.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1   -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1        -I/home/vsedyshev/Work/1111/pjproject/third_party/build/speex -I/home/vsedyshev/Work/1111/pjproject/third_party/speex/include -DPJMEDIA_HAS_OPENCORE_AMRNB_CODEC=0 -DPJMEDIA_HAS_OPENCORE_AMRWB_CODEC=0 -I/home/vsedyshev/Work/1111/pjproject/third_party/build/srtp -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/crypto/include -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/include -DPJMEDIA_RESAMPLE_IMP=PJMEDIA_RESAMPLE_LIBRESAMPLE -DPJMEDIA_HAS_LIBYUV=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/yuv/include -DPJMEDIA_HAS_WEBRTC_AEC=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/webrtc/src -DPJMEDIA_AUDIO_DEV_HAS_ALSA=1 -DPJMEDIA_AUDIO_DEV_HAS_PORTAUDIO=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjmedia/include -I../../pjnath/include -I../.. \
# 	-o output/pjmedia-x86_64-unknown-linux-gnu/resample_libsamplerate.o \
# 	../src/pjmedia/resample_libsamplerate.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1   -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1        -I/home/vsedyshev/Work/1111/pjproject/third_party/build/speex -I/home/vsedyshev/Work/1111/pjproject/third_party/speex/include -DPJMEDIA_HAS_OPENCORE_AMRNB_CODEC=0 -DPJMEDIA_HAS_OPENCORE_AMRWB_CODEC=0 -I/home/vsedyshev/Work/1111/pjproject/third_party/build/srtp -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/crypto/include -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/include -DPJMEDIA_RESAMPLE_IMP=PJMEDIA_RESAMPLE_LIBRESAMPLE -DPJMEDIA_HAS_LIBYUV=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/yuv/include -DPJMEDIA_HAS_WEBRTC_AEC=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/webrtc/src -DPJMEDIA_AUDIO_DEV_HAS_ALSA=1 -DPJMEDIA_AUDIO_DEV_HAS_PORTAUDIO=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjmedia/include -I../../pjnath/include -I../.. \
# 	-o output/pjmedia-x86_64-unknown-linux-gnu/resample_speex.o \
# 	../src/pjmedia/resample_speex.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1   -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1        -I/home/vsedyshev/Work/1111/pjproject/third_party/build/speex -I/home/vsedyshev/Work/1111/pjproject/third_party/speex/include -DPJMEDIA_HAS_OPENCORE_AMRNB_CODEC=0 -DPJMEDIA_HAS_OPENCORE_AMRWB_CODEC=0 -I/home/vsedyshev/Work/1111/pjproject/third_party/build/srtp -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/crypto/include -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/include -DPJMEDIA_RESAMPLE_IMP=PJMEDIA_RESAMPLE_LIBRESAMPLE -DPJMEDIA_HAS_LIBYUV=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/yuv/include -DPJMEDIA_HAS_WEBRTC_AEC=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/webrtc/src -DPJMEDIA_AUDIO_DEV_HAS_ALSA=1 -DPJMEDIA_AUDIO_DEV_HAS_PORTAUDIO=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjmedia/include -I../../pjnath/include -I../.. \
# 	-o output/pjmedia-x86_64-unknown-linux-gnu/resample_port.o \
# 	../src/pjmedia/resample_port.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1   -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1        -I/home/vsedyshev/Work/1111/pjproject/third_party/build/speex -I/home/vsedyshev/Work/1111/pjproject/third_party/speex/include -DPJMEDIA_HAS_OPENCORE_AMRNB_CODEC=0 -DPJMEDIA_HAS_OPENCORE_AMRWB_CODEC=0 -I/home/vsedyshev/Work/1111/pjproject/third_party/build/srtp -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/crypto/include -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/include -DPJMEDIA_RESAMPLE_IMP=PJMEDIA_RESAMPLE_LIBRESAMPLE -DPJMEDIA_HAS_LIBYUV=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/yuv/include -DPJMEDIA_HAS_WEBRTC_AEC=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/webrtc/src -DPJMEDIA_AUDIO_DEV_HAS_ALSA=1 -DPJMEDIA_AUDIO_DEV_HAS_PORTAUDIO=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjmedia/include -I../../pjnath/include -I../.. \
# 	-o output/pjmedia-x86_64-unknown-linux-gnu/rtcp.o \
# 	../src/pjmedia/rtcp.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1   -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1        -I/home/vsedyshev/Work/1111/pjproject/third_party/build/speex -I/home/vsedyshev/Work/1111/pjproject/third_party/speex/include -DPJMEDIA_HAS_OPENCORE_AMRNB_CODEC=0 -DPJMEDIA_HAS_OPENCORE_AMRWB_CODEC=0 -I/home/vsedyshev/Work/1111/pjproject/third_party/build/srtp -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/crypto/include -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/include -DPJMEDIA_RESAMPLE_IMP=PJMEDIA_RESAMPLE_LIBRESAMPLE -DPJMEDIA_HAS_LIBYUV=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/yuv/include -DPJMEDIA_HAS_WEBRTC_AEC=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/webrtc/src -DPJMEDIA_AUDIO_DEV_HAS_ALSA=1 -DPJMEDIA_AUDIO_DEV_HAS_PORTAUDIO=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjmedia/include -I../../pjnath/include -I../.. \
# 	-o output/pjmedia-x86_64-unknown-linux-gnu/rtcp_xr.o \
# 	../src/pjmedia/rtcp_xr.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1   -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1        -I/home/vsedyshev/Work/1111/pjproject/third_party/build/speex -I/home/vsedyshev/Work/1111/pjproject/third_party/speex/include -DPJMEDIA_HAS_OPENCORE_AMRNB_CODEC=0 -DPJMEDIA_HAS_OPENCORE_AMRWB_CODEC=0 -I/home/vsedyshev/Work/1111/pjproject/third_party/build/srtp -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/crypto/include -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/include -DPJMEDIA_RESAMPLE_IMP=PJMEDIA_RESAMPLE_LIBRESAMPLE -DPJMEDIA_HAS_LIBYUV=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/yuv/include -DPJMEDIA_HAS_WEBRTC_AEC=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/webrtc/src -DPJMEDIA_AUDIO_DEV_HAS_ALSA=1 -DPJMEDIA_AUDIO_DEV_HAS_PORTAUDIO=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjmedia/include -I../../pjnath/include -I../.. \
# 	-o output/pjmedia-x86_64-unknown-linux-gnu/rtcp_fb.o \
# 	../src/pjmedia/rtcp_fb.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1   -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1        -I/home/vsedyshev/Work/1111/pjproject/third_party/build/speex -I/home/vsedyshev/Work/1111/pjproject/third_party/speex/include -DPJMEDIA_HAS_OPENCORE_AMRNB_CODEC=0 -DPJMEDIA_HAS_OPENCORE_AMRWB_CODEC=0 -I/home/vsedyshev/Work/1111/pjproject/third_party/build/srtp -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/crypto/include -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/include -DPJMEDIA_RESAMPLE_IMP=PJMEDIA_RESAMPLE_LIBRESAMPLE -DPJMEDIA_HAS_LIBYUV=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/yuv/include -DPJMEDIA_HAS_WEBRTC_AEC=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/webrtc/src -DPJMEDIA_AUDIO_DEV_HAS_ALSA=1 -DPJMEDIA_AUDIO_DEV_HAS_PORTAUDIO=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjmedia/include -I../../pjnath/include -I../.. \
# 	-o output/pjmedia-x86_64-unknown-linux-gnu/rtp.o \
# 	../src/pjmedia/rtp.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1   -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1        -I/home/vsedyshev/Work/1111/pjproject/third_party/build/speex -I/home/vsedyshev/Work/1111/pjproject/third_party/speex/include -DPJMEDIA_HAS_OPENCORE_AMRNB_CODEC=0 -DPJMEDIA_HAS_OPENCORE_AMRWB_CODEC=0 -I/home/vsedyshev/Work/1111/pjproject/third_party/build/srtp -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/crypto/include -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/include -DPJMEDIA_RESAMPLE_IMP=PJMEDIA_RESAMPLE_LIBRESAMPLE -DPJMEDIA_HAS_LIBYUV=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/yuv/include -DPJMEDIA_HAS_WEBRTC_AEC=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/webrtc/src -DPJMEDIA_AUDIO_DEV_HAS_ALSA=1 -DPJMEDIA_AUDIO_DEV_HAS_PORTAUDIO=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjmedia/include -I../../pjnath/include -I../.. \
# 	-o output/pjmedia-x86_64-unknown-linux-gnu/sdp.o \
# 	../src/pjmedia/sdp.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1   -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1        -I/home/vsedyshev/Work/1111/pjproject/third_party/build/speex -I/home/vsedyshev/Work/1111/pjproject/third_party/speex/include -DPJMEDIA_HAS_OPENCORE_AMRNB_CODEC=0 -DPJMEDIA_HAS_OPENCORE_AMRWB_CODEC=0 -I/home/vsedyshev/Work/1111/pjproject/third_party/build/srtp -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/crypto/include -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/include -DPJMEDIA_RESAMPLE_IMP=PJMEDIA_RESAMPLE_LIBRESAMPLE -DPJMEDIA_HAS_LIBYUV=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/yuv/include -DPJMEDIA_HAS_WEBRTC_AEC=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/webrtc/src -DPJMEDIA_AUDIO_DEV_HAS_ALSA=1 -DPJMEDIA_AUDIO_DEV_HAS_PORTAUDIO=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjmedia/include -I../../pjnath/include -I../.. \
# 	-o output/pjmedia-x86_64-unknown-linux-gnu/sdp_cmp.o \
# 	../src/pjmedia/sdp_cmp.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1   -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1        -I/home/vsedyshev/Work/1111/pjproject/third_party/build/speex -I/home/vsedyshev/Work/1111/pjproject/third_party/speex/include -DPJMEDIA_HAS_OPENCORE_AMRNB_CODEC=0 -DPJMEDIA_HAS_OPENCORE_AMRWB_CODEC=0 -I/home/vsedyshev/Work/1111/pjproject/third_party/build/srtp -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/crypto/include -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/include -DPJMEDIA_RESAMPLE_IMP=PJMEDIA_RESAMPLE_LIBRESAMPLE -DPJMEDIA_HAS_LIBYUV=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/yuv/include -DPJMEDIA_HAS_WEBRTC_AEC=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/webrtc/src -DPJMEDIA_AUDIO_DEV_HAS_ALSA=1 -DPJMEDIA_AUDIO_DEV_HAS_PORTAUDIO=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjmedia/include -I../../pjnath/include -I../.. \
# 	-o output/pjmedia-x86_64-unknown-linux-gnu/sdp_neg.o \
# 	../src/pjmedia/sdp_neg.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1   -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1        -I/home/vsedyshev/Work/1111/pjproject/third_party/build/speex -I/home/vsedyshev/Work/1111/pjproject/third_party/speex/include -DPJMEDIA_HAS_OPENCORE_AMRNB_CODEC=0 -DPJMEDIA_HAS_OPENCORE_AMRWB_CODEC=0 -I/home/vsedyshev/Work/1111/pjproject/third_party/build/srtp -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/crypto/include -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/include -DPJMEDIA_RESAMPLE_IMP=PJMEDIA_RESAMPLE_LIBRESAMPLE -DPJMEDIA_HAS_LIBYUV=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/yuv/include -DPJMEDIA_HAS_WEBRTC_AEC=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/webrtc/src -DPJMEDIA_AUDIO_DEV_HAS_ALSA=1 -DPJMEDIA_AUDIO_DEV_HAS_PORTAUDIO=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjmedia/include -I../../pjnath/include -I../.. \
# 	-o output/pjmedia-x86_64-unknown-linux-gnu/session.o \
# 	../src/pjmedia/session.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1   -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1        -I/home/vsedyshev/Work/1111/pjproject/third_party/build/speex -I/home/vsedyshev/Work/1111/pjproject/third_party/speex/include -DPJMEDIA_HAS_OPENCORE_AMRNB_CODEC=0 -DPJMEDIA_HAS_OPENCORE_AMRWB_CODEC=0 -I/home/vsedyshev/Work/1111/pjproject/third_party/build/srtp -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/crypto/include -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/include -DPJMEDIA_RESAMPLE_IMP=PJMEDIA_RESAMPLE_LIBRESAMPLE -DPJMEDIA_HAS_LIBYUV=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/yuv/include -DPJMEDIA_HAS_WEBRTC_AEC=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/webrtc/src -DPJMEDIA_AUDIO_DEV_HAS_ALSA=1 -DPJMEDIA_AUDIO_DEV_HAS_PORTAUDIO=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjmedia/include -I../../pjnath/include -I../.. \
# 	-o output/pjmedia-x86_64-unknown-linux-gnu/silencedet.o \
# 	../src/pjmedia/silencedet.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1   -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1        -I/home/vsedyshev/Work/1111/pjproject/third_party/build/speex -I/home/vsedyshev/Work/1111/pjproject/third_party/speex/include -DPJMEDIA_HAS_OPENCORE_AMRNB_CODEC=0 -DPJMEDIA_HAS_OPENCORE_AMRWB_CODEC=0 -I/home/vsedyshev/Work/1111/pjproject/third_party/build/srtp -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/crypto/include -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/include -DPJMEDIA_RESAMPLE_IMP=PJMEDIA_RESAMPLE_LIBRESAMPLE -DPJMEDIA_HAS_LIBYUV=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/yuv/include -DPJMEDIA_HAS_WEBRTC_AEC=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/webrtc/src -DPJMEDIA_AUDIO_DEV_HAS_ALSA=1 -DPJMEDIA_AUDIO_DEV_HAS_PORTAUDIO=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjmedia/include -I../../pjnath/include -I../.. \
# 	-o output/pjmedia-x86_64-unknown-linux-gnu/sound_legacy.o \
# 	../src/pjmedia/sound_legacy.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1   -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1        -I/home/vsedyshev/Work/1111/pjproject/third_party/build/speex -I/home/vsedyshev/Work/1111/pjproject/third_party/speex/include -DPJMEDIA_HAS_OPENCORE_AMRNB_CODEC=0 -DPJMEDIA_HAS_OPENCORE_AMRWB_CODEC=0 -I/home/vsedyshev/Work/1111/pjproject/third_party/build/srtp -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/crypto/include -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/include -DPJMEDIA_RESAMPLE_IMP=PJMEDIA_RESAMPLE_LIBRESAMPLE -DPJMEDIA_HAS_LIBYUV=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/yuv/include -DPJMEDIA_HAS_WEBRTC_AEC=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/webrtc/src -DPJMEDIA_AUDIO_DEV_HAS_ALSA=1 -DPJMEDIA_AUDIO_DEV_HAS_PORTAUDIO=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjmedia/include -I../../pjnath/include -I../.. \
# 	-o output/pjmedia-x86_64-unknown-linux-gnu/sound_port.o \
# 	../src/pjmedia/sound_port.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1   -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1        -I/home/vsedyshev/Work/1111/pjproject/third_party/build/speex -I/home/vsedyshev/Work/1111/pjproject/third_party/speex/include -DPJMEDIA_HAS_OPENCORE_AMRNB_CODEC=0 -DPJMEDIA_HAS_OPENCORE_AMRWB_CODEC=0 -I/home/vsedyshev/Work/1111/pjproject/third_party/build/srtp -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/crypto/include -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/include -DPJMEDIA_RESAMPLE_IMP=PJMEDIA_RESAMPLE_LIBRESAMPLE -DPJMEDIA_HAS_LIBYUV=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/yuv/include -DPJMEDIA_HAS_WEBRTC_AEC=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/webrtc/src -DPJMEDIA_AUDIO_DEV_HAS_ALSA=1 -DPJMEDIA_AUDIO_DEV_HAS_PORTAUDIO=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjmedia/include -I../../pjnath/include -I../.. \
# 	-o output/pjmedia-x86_64-unknown-linux-gnu/stereo_port.o \
# 	../src/pjmedia/stereo_port.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1   -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1        -I/home/vsedyshev/Work/1111/pjproject/third_party/build/speex -I/home/vsedyshev/Work/1111/pjproject/third_party/speex/include -DPJMEDIA_HAS_OPENCORE_AMRNB_CODEC=0 -DPJMEDIA_HAS_OPENCORE_AMRWB_CODEC=0 -I/home/vsedyshev/Work/1111/pjproject/third_party/build/srtp -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/crypto/include -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/include -DPJMEDIA_RESAMPLE_IMP=PJMEDIA_RESAMPLE_LIBRESAMPLE -DPJMEDIA_HAS_LIBYUV=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/yuv/include -DPJMEDIA_HAS_WEBRTC_AEC=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/webrtc/src -DPJMEDIA_AUDIO_DEV_HAS_ALSA=1 -DPJMEDIA_AUDIO_DEV_HAS_PORTAUDIO=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjmedia/include -I../../pjnath/include -I../.. \
# 	-o output/pjmedia-x86_64-unknown-linux-gnu/stream_common.o \
# 	../src/pjmedia/stream_common.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1   -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1        -I/home/vsedyshev/Work/1111/pjproject/third_party/build/speex -I/home/vsedyshev/Work/1111/pjproject/third_party/speex/include -DPJMEDIA_HAS_OPENCORE_AMRNB_CODEC=0 -DPJMEDIA_HAS_OPENCORE_AMRWB_CODEC=0 -I/home/vsedyshev/Work/1111/pjproject/third_party/build/srtp -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/crypto/include -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/include -DPJMEDIA_RESAMPLE_IMP=PJMEDIA_RESAMPLE_LIBRESAMPLE -DPJMEDIA_HAS_LIBYUV=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/yuv/include -DPJMEDIA_HAS_WEBRTC_AEC=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/webrtc/src -DPJMEDIA_AUDIO_DEV_HAS_ALSA=1 -DPJMEDIA_AUDIO_DEV_HAS_PORTAUDIO=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjmedia/include -I../../pjnath/include -I../.. \
# 	-o output/pjmedia-x86_64-unknown-linux-gnu/stream.o \
# 	../src/pjmedia/stream.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1   -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1        -I/home/vsedyshev/Work/1111/pjproject/third_party/build/speex -I/home/vsedyshev/Work/1111/pjproject/third_party/speex/include -DPJMEDIA_HAS_OPENCORE_AMRNB_CODEC=0 -DPJMEDIA_HAS_OPENCORE_AMRWB_CODEC=0 -I/home/vsedyshev/Work/1111/pjproject/third_party/build/srtp -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/crypto/include -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/include -DPJMEDIA_RESAMPLE_IMP=PJMEDIA_RESAMPLE_LIBRESAMPLE -DPJMEDIA_HAS_LIBYUV=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/yuv/include -DPJMEDIA_HAS_WEBRTC_AEC=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/webrtc/src -DPJMEDIA_AUDIO_DEV_HAS_ALSA=1 -DPJMEDIA_AUDIO_DEV_HAS_PORTAUDIO=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjmedia/include -I../../pjnath/include -I../.. \
# 	-o output/pjmedia-x86_64-unknown-linux-gnu/stream_info.o \
# 	../src/pjmedia/stream_info.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1   -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1        -I/home/vsedyshev/Work/1111/pjproject/third_party/build/speex -I/home/vsedyshev/Work/1111/pjproject/third_party/speex/include -DPJMEDIA_HAS_OPENCORE_AMRNB_CODEC=0 -DPJMEDIA_HAS_OPENCORE_AMRWB_CODEC=0 -I/home/vsedyshev/Work/1111/pjproject/third_party/build/srtp -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/crypto/include -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/include -DPJMEDIA_RESAMPLE_IMP=PJMEDIA_RESAMPLE_LIBRESAMPLE -DPJMEDIA_HAS_LIBYUV=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/yuv/include -DPJMEDIA_HAS_WEBRTC_AEC=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/webrtc/src -DPJMEDIA_AUDIO_DEV_HAS_ALSA=1 -DPJMEDIA_AUDIO_DEV_HAS_PORTAUDIO=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjmedia/include -I../../pjnath/include -I../.. \
# 	-o output/pjmedia-x86_64-unknown-linux-gnu/tonegen.o \
# 	../src/pjmedia/tonegen.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1   -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1        -I/home/vsedyshev/Work/1111/pjproject/third_party/build/speex -I/home/vsedyshev/Work/1111/pjproject/third_party/speex/include -DPJMEDIA_HAS_OPENCORE_AMRNB_CODEC=0 -DPJMEDIA_HAS_OPENCORE_AMRWB_CODEC=0 -I/home/vsedyshev/Work/1111/pjproject/third_party/build/srtp -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/crypto/include -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/include -DPJMEDIA_RESAMPLE_IMP=PJMEDIA_RESAMPLE_LIBRESAMPLE -DPJMEDIA_HAS_LIBYUV=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/yuv/include -DPJMEDIA_HAS_WEBRTC_AEC=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/webrtc/src -DPJMEDIA_AUDIO_DEV_HAS_ALSA=1 -DPJMEDIA_AUDIO_DEV_HAS_PORTAUDIO=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjmedia/include -I../../pjnath/include -I../.. \
# 	-o output/pjmedia-x86_64-unknown-linux-gnu/transport_adapter_sample.o \
# 	../src/pjmedia/transport_adapter_sample.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1   -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1        -I/home/vsedyshev/Work/1111/pjproject/third_party/build/speex -I/home/vsedyshev/Work/1111/pjproject/third_party/speex/include -DPJMEDIA_HAS_OPENCORE_AMRNB_CODEC=0 -DPJMEDIA_HAS_OPENCORE_AMRWB_CODEC=0 -I/home/vsedyshev/Work/1111/pjproject/third_party/build/srtp -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/crypto/include -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/include -DPJMEDIA_RESAMPLE_IMP=PJMEDIA_RESAMPLE_LIBRESAMPLE -DPJMEDIA_HAS_LIBYUV=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/yuv/include -DPJMEDIA_HAS_WEBRTC_AEC=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/webrtc/src -DPJMEDIA_AUDIO_DEV_HAS_ALSA=1 -DPJMEDIA_AUDIO_DEV_HAS_PORTAUDIO=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjmedia/include -I../../pjnath/include -I../.. \
# 	-o output/pjmedia-x86_64-unknown-linux-gnu/transport_ice.o \
# 	../src/pjmedia/transport_ice.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1   -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1        -I/home/vsedyshev/Work/1111/pjproject/third_party/build/speex -I/home/vsedyshev/Work/1111/pjproject/third_party/speex/include -DPJMEDIA_HAS_OPENCORE_AMRNB_CODEC=0 -DPJMEDIA_HAS_OPENCORE_AMRWB_CODEC=0 -I/home/vsedyshev/Work/1111/pjproject/third_party/build/srtp -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/crypto/include -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/include -DPJMEDIA_RESAMPLE_IMP=PJMEDIA_RESAMPLE_LIBRESAMPLE -DPJMEDIA_HAS_LIBYUV=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/yuv/include -DPJMEDIA_HAS_WEBRTC_AEC=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/webrtc/src -DPJMEDIA_AUDIO_DEV_HAS_ALSA=1 -DPJMEDIA_AUDIO_DEV_HAS_PORTAUDIO=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjmedia/include -I../../pjnath/include -I../.. \
# 	-o output/pjmedia-x86_64-unknown-linux-gnu/transport_loop.o \
# 	../src/pjmedia/transport_loop.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1   -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1        -I/home/vsedyshev/Work/1111/pjproject/third_party/build/speex -I/home/vsedyshev/Work/1111/pjproject/third_party/speex/include -DPJMEDIA_HAS_OPENCORE_AMRNB_CODEC=0 -DPJMEDIA_HAS_OPENCORE_AMRWB_CODEC=0 -I/home/vsedyshev/Work/1111/pjproject/third_party/build/srtp -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/crypto/include -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/include -DPJMEDIA_RESAMPLE_IMP=PJMEDIA_RESAMPLE_LIBRESAMPLE -DPJMEDIA_HAS_LIBYUV=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/yuv/include -DPJMEDIA_HAS_WEBRTC_AEC=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/webrtc/src -DPJMEDIA_AUDIO_DEV_HAS_ALSA=1 -DPJMEDIA_AUDIO_DEV_HAS_PORTAUDIO=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjmedia/include -I../../pjnath/include -I../.. \
# 	-o output/pjmedia-x86_64-unknown-linux-gnu/transport_srtp.o \
# 	../src/pjmedia/transport_srtp.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1   -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1        -I/home/vsedyshev/Work/1111/pjproject/third_party/build/speex -I/home/vsedyshev/Work/1111/pjproject/third_party/speex/include -DPJMEDIA_HAS_OPENCORE_AMRNB_CODEC=0 -DPJMEDIA_HAS_OPENCORE_AMRWB_CODEC=0 -I/home/vsedyshev/Work/1111/pjproject/third_party/build/srtp -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/crypto/include -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/include -DPJMEDIA_RESAMPLE_IMP=PJMEDIA_RESAMPLE_LIBRESAMPLE -DPJMEDIA_HAS_LIBYUV=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/yuv/include -DPJMEDIA_HAS_WEBRTC_AEC=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/webrtc/src -DPJMEDIA_AUDIO_DEV_HAS_ALSA=1 -DPJMEDIA_AUDIO_DEV_HAS_PORTAUDIO=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjmedia/include -I../../pjnath/include -I../.. \
# 	-o output/pjmedia-x86_64-unknown-linux-gnu/transport_udp.o \
# 	../src/pjmedia/transport_udp.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1   -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1        -I/home/vsedyshev/Work/1111/pjproject/third_party/build/speex -I/home/vsedyshev/Work/1111/pjproject/third_party/speex/include -DPJMEDIA_HAS_OPENCORE_AMRNB_CODEC=0 -DPJMEDIA_HAS_OPENCORE_AMRWB_CODEC=0 -I/home/vsedyshev/Work/1111/pjproject/third_party/build/srtp -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/crypto/include -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/include -DPJMEDIA_RESAMPLE_IMP=PJMEDIA_RESAMPLE_LIBRESAMPLE -DPJMEDIA_HAS_LIBYUV=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/yuv/include -DPJMEDIA_HAS_WEBRTC_AEC=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/webrtc/src -DPJMEDIA_AUDIO_DEV_HAS_ALSA=1 -DPJMEDIA_AUDIO_DEV_HAS_PORTAUDIO=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjmedia/include -I../../pjnath/include -I../.. \
# 	-o output/pjmedia-x86_64-unknown-linux-gnu/types.o \
# 	../src/pjmedia/types.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1   -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1        -I/home/vsedyshev/Work/1111/pjproject/third_party/build/speex -I/home/vsedyshev/Work/1111/pjproject/third_party/speex/include -DPJMEDIA_HAS_OPENCORE_AMRNB_CODEC=0 -DPJMEDIA_HAS_OPENCORE_AMRWB_CODEC=0 -I/home/vsedyshev/Work/1111/pjproject/third_party/build/srtp -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/crypto/include -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/include -DPJMEDIA_RESAMPLE_IMP=PJMEDIA_RESAMPLE_LIBRESAMPLE -DPJMEDIA_HAS_LIBYUV=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/yuv/include -DPJMEDIA_HAS_WEBRTC_AEC=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/webrtc/src -DPJMEDIA_AUDIO_DEV_HAS_ALSA=1 -DPJMEDIA_AUDIO_DEV_HAS_PORTAUDIO=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjmedia/include -I../../pjnath/include -I../.. \
# 	-o output/pjmedia-x86_64-unknown-linux-gnu/vid_codec.o \
# 	../src/pjmedia/vid_codec.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1   -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1        -I/home/vsedyshev/Work/1111/pjproject/third_party/build/speex -I/home/vsedyshev/Work/1111/pjproject/third_party/speex/include -DPJMEDIA_HAS_OPENCORE_AMRNB_CODEC=0 -DPJMEDIA_HAS_OPENCORE_AMRWB_CODEC=0 -I/home/vsedyshev/Work/1111/pjproject/third_party/build/srtp -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/crypto/include -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/include -DPJMEDIA_RESAMPLE_IMP=PJMEDIA_RESAMPLE_LIBRESAMPLE -DPJMEDIA_HAS_LIBYUV=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/yuv/include -DPJMEDIA_HAS_WEBRTC_AEC=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/webrtc/src -DPJMEDIA_AUDIO_DEV_HAS_ALSA=1 -DPJMEDIA_AUDIO_DEV_HAS_PORTAUDIO=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjmedia/include -I../../pjnath/include -I../.. \
# 	-o output/pjmedia-x86_64-unknown-linux-gnu/vid_codec_util.o \
# 	../src/pjmedia/vid_codec_util.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1   -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1        -I/home/vsedyshev/Work/1111/pjproject/third_party/build/speex -I/home/vsedyshev/Work/1111/pjproject/third_party/speex/include -DPJMEDIA_HAS_OPENCORE_AMRNB_CODEC=0 -DPJMEDIA_HAS_OPENCORE_AMRWB_CODEC=0 -I/home/vsedyshev/Work/1111/pjproject/third_party/build/srtp -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/crypto/include -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/include -DPJMEDIA_RESAMPLE_IMP=PJMEDIA_RESAMPLE_LIBRESAMPLE -DPJMEDIA_HAS_LIBYUV=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/yuv/include -DPJMEDIA_HAS_WEBRTC_AEC=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/webrtc/src -DPJMEDIA_AUDIO_DEV_HAS_ALSA=1 -DPJMEDIA_AUDIO_DEV_HAS_PORTAUDIO=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjmedia/include -I../../pjnath/include -I../.. \
# 	-o output/pjmedia-x86_64-unknown-linux-gnu/vid_port.o \
# 	../src/pjmedia/vid_port.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1   -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1        -I/home/vsedyshev/Work/1111/pjproject/third_party/build/speex -I/home/vsedyshev/Work/1111/pjproject/third_party/speex/include -DPJMEDIA_HAS_OPENCORE_AMRNB_CODEC=0 -DPJMEDIA_HAS_OPENCORE_AMRWB_CODEC=0 -I/home/vsedyshev/Work/1111/pjproject/third_party/build/srtp -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/crypto/include -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/include -DPJMEDIA_RESAMPLE_IMP=PJMEDIA_RESAMPLE_LIBRESAMPLE -DPJMEDIA_HAS_LIBYUV=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/yuv/include -DPJMEDIA_HAS_WEBRTC_AEC=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/webrtc/src -DPJMEDIA_AUDIO_DEV_HAS_ALSA=1 -DPJMEDIA_AUDIO_DEV_HAS_PORTAUDIO=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjmedia/include -I../../pjnath/include -I../.. \
# 	-o output/pjmedia-x86_64-unknown-linux-gnu/vid_stream.o \
# 	../src/pjmedia/vid_stream.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1   -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1        -I/home/vsedyshev/Work/1111/pjproject/third_party/build/speex -I/home/vsedyshev/Work/1111/pjproject/third_party/speex/include -DPJMEDIA_HAS_OPENCORE_AMRNB_CODEC=0 -DPJMEDIA_HAS_OPENCORE_AMRWB_CODEC=0 -I/home/vsedyshev/Work/1111/pjproject/third_party/build/srtp -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/crypto/include -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/include -DPJMEDIA_RESAMPLE_IMP=PJMEDIA_RESAMPLE_LIBRESAMPLE -DPJMEDIA_HAS_LIBYUV=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/yuv/include -DPJMEDIA_HAS_WEBRTC_AEC=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/webrtc/src -DPJMEDIA_AUDIO_DEV_HAS_ALSA=1 -DPJMEDIA_AUDIO_DEV_HAS_PORTAUDIO=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjmedia/include -I../../pjnath/include -I../.. \
# 	-o output/pjmedia-x86_64-unknown-linux-gnu/vid_stream_info.o \
# 	../src/pjmedia/vid_stream_info.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1   -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1        -I/home/vsedyshev/Work/1111/pjproject/third_party/build/speex -I/home/vsedyshev/Work/1111/pjproject/third_party/speex/include -DPJMEDIA_HAS_OPENCORE_AMRNB_CODEC=0 -DPJMEDIA_HAS_OPENCORE_AMRWB_CODEC=0 -I/home/vsedyshev/Work/1111/pjproject/third_party/build/srtp -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/crypto/include -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/include -DPJMEDIA_RESAMPLE_IMP=PJMEDIA_RESAMPLE_LIBRESAMPLE -DPJMEDIA_HAS_LIBYUV=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/yuv/include -DPJMEDIA_HAS_WEBRTC_AEC=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/webrtc/src -DPJMEDIA_AUDIO_DEV_HAS_ALSA=1 -DPJMEDIA_AUDIO_DEV_HAS_PORTAUDIO=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjmedia/include -I../../pjnath/include -I../.. \
# 	-o output/pjmedia-x86_64-unknown-linux-gnu/vid_conf.o \
# 	../src/pjmedia/vid_conf.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1   -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1        -I/home/vsedyshev/Work/1111/pjproject/third_party/build/speex -I/home/vsedyshev/Work/1111/pjproject/third_party/speex/include -DPJMEDIA_HAS_OPENCORE_AMRNB_CODEC=0 -DPJMEDIA_HAS_OPENCORE_AMRWB_CODEC=0 -I/home/vsedyshev/Work/1111/pjproject/third_party/build/srtp -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/crypto/include -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/include -DPJMEDIA_RESAMPLE_IMP=PJMEDIA_RESAMPLE_LIBRESAMPLE -DPJMEDIA_HAS_LIBYUV=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/yuv/include -DPJMEDIA_HAS_WEBRTC_AEC=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/webrtc/src -DPJMEDIA_AUDIO_DEV_HAS_ALSA=1 -DPJMEDIA_AUDIO_DEV_HAS_PORTAUDIO=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjmedia/include -I../../pjnath/include -I../.. \
# 	-o output/pjmedia-x86_64-unknown-linux-gnu/wav_player.o \
# 	../src/pjmedia/wav_player.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1   -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1        -I/home/vsedyshev/Work/1111/pjproject/third_party/build/speex -I/home/vsedyshev/Work/1111/pjproject/third_party/speex/include -DPJMEDIA_HAS_OPENCORE_AMRNB_CODEC=0 -DPJMEDIA_HAS_OPENCORE_AMRWB_CODEC=0 -I/home/vsedyshev/Work/1111/pjproject/third_party/build/srtp -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/crypto/include -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/include -DPJMEDIA_RESAMPLE_IMP=PJMEDIA_RESAMPLE_LIBRESAMPLE -DPJMEDIA_HAS_LIBYUV=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/yuv/include -DPJMEDIA_HAS_WEBRTC_AEC=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/webrtc/src -DPJMEDIA_AUDIO_DEV_HAS_ALSA=1 -DPJMEDIA_AUDIO_DEV_HAS_PORTAUDIO=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjmedia/include -I../../pjnath/include -I../.. \
# 	-o output/pjmedia-x86_64-unknown-linux-gnu/wav_playlist.o \
# 	../src/pjmedia/wav_playlist.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1   -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1        -I/home/vsedyshev/Work/1111/pjproject/third_party/build/speex -I/home/vsedyshev/Work/1111/pjproject/third_party/speex/include -DPJMEDIA_HAS_OPENCORE_AMRNB_CODEC=0 -DPJMEDIA_HAS_OPENCORE_AMRWB_CODEC=0 -I/home/vsedyshev/Work/1111/pjproject/third_party/build/srtp -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/crypto/include -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/include -DPJMEDIA_RESAMPLE_IMP=PJMEDIA_RESAMPLE_LIBRESAMPLE -DPJMEDIA_HAS_LIBYUV=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/yuv/include -DPJMEDIA_HAS_WEBRTC_AEC=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/webrtc/src -DPJMEDIA_AUDIO_DEV_HAS_ALSA=1 -DPJMEDIA_AUDIO_DEV_HAS_PORTAUDIO=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjmedia/include -I../../pjnath/include -I../.. \
# 	-o output/pjmedia-x86_64-unknown-linux-gnu/wav_writer.o \
# 	../src/pjmedia/wav_writer.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1   -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1        -I/home/vsedyshev/Work/1111/pjproject/third_party/build/speex -I/home/vsedyshev/Work/1111/pjproject/third_party/speex/include -DPJMEDIA_HAS_OPENCORE_AMRNB_CODEC=0 -DPJMEDIA_HAS_OPENCORE_AMRWB_CODEC=0 -I/home/vsedyshev/Work/1111/pjproject/third_party/build/srtp -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/crypto/include -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/include -DPJMEDIA_RESAMPLE_IMP=PJMEDIA_RESAMPLE_LIBRESAMPLE -DPJMEDIA_HAS_LIBYUV=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/yuv/include -DPJMEDIA_HAS_WEBRTC_AEC=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/webrtc/src -DPJMEDIA_AUDIO_DEV_HAS_ALSA=1 -DPJMEDIA_AUDIO_DEV_HAS_PORTAUDIO=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjmedia/include -I../../pjnath/include -I../.. \
# 	-o output/pjmedia-x86_64-unknown-linux-gnu/wave.o \
# 	../src/pjmedia/wave.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1   -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1        -I/home/vsedyshev/Work/1111/pjproject/third_party/build/speex -I/home/vsedyshev/Work/1111/pjproject/third_party/speex/include -DPJMEDIA_HAS_OPENCORE_AMRNB_CODEC=0 -DPJMEDIA_HAS_OPENCORE_AMRWB_CODEC=0 -I/home/vsedyshev/Work/1111/pjproject/third_party/build/srtp -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/crypto/include -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/include -DPJMEDIA_RESAMPLE_IMP=PJMEDIA_RESAMPLE_LIBRESAMPLE -DPJMEDIA_HAS_LIBYUV=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/yuv/include -DPJMEDIA_HAS_WEBRTC_AEC=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/webrtc/src -DPJMEDIA_AUDIO_DEV_HAS_ALSA=1 -DPJMEDIA_AUDIO_DEV_HAS_PORTAUDIO=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjmedia/include -I../../pjnath/include -I../.. \
# 	-o output/pjmedia-x86_64-unknown-linux-gnu/wsola.o \
# 	../src/pjmedia/wsola.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1   -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1        -I/home/vsedyshev/Work/1111/pjproject/third_party/build/speex -I/home/vsedyshev/Work/1111/pjproject/third_party/speex/include -DPJMEDIA_HAS_OPENCORE_AMRNB_CODEC=0 -DPJMEDIA_HAS_OPENCORE_AMRWB_CODEC=0 -I/home/vsedyshev/Work/1111/pjproject/third_party/build/srtp -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/crypto/include -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/include -DPJMEDIA_RESAMPLE_IMP=PJMEDIA_RESAMPLE_LIBRESAMPLE -DPJMEDIA_HAS_LIBYUV=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/yuv/include -DPJMEDIA_HAS_WEBRTC_AEC=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/webrtc/src -DPJMEDIA_AUDIO_DEV_HAS_ALSA=1 -DPJMEDIA_AUDIO_DEV_HAS_PORTAUDIO=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjmedia/include -I../../pjnath/include -I../.. \
# 	-o output/pjmedia-x86_64-unknown-linux-gnu/audiodev.o \
# 	../src/pjmedia/audiodev.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1   -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1        -I/home/vsedyshev/Work/1111/pjproject/third_party/build/speex -I/home/vsedyshev/Work/1111/pjproject/third_party/speex/include -DPJMEDIA_HAS_OPENCORE_AMRNB_CODEC=0 -DPJMEDIA_HAS_OPENCORE_AMRWB_CODEC=0 -I/home/vsedyshev/Work/1111/pjproject/third_party/build/srtp -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/crypto/include -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/include -DPJMEDIA_RESAMPLE_IMP=PJMEDIA_RESAMPLE_LIBRESAMPLE -DPJMEDIA_HAS_LIBYUV=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/yuv/include -DPJMEDIA_HAS_WEBRTC_AEC=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/webrtc/src -DPJMEDIA_AUDIO_DEV_HAS_ALSA=1 -DPJMEDIA_AUDIO_DEV_HAS_PORTAUDIO=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjmedia/include -I../../pjnath/include -I../.. \
# 	-o output/pjmedia-x86_64-unknown-linux-gnu/videodev.o \
# 	../src/pjmedia/videodev.c 
# if test ! -d ../lib; then mkdir -p ../lib; fi
# ar rv ../lib/libpjmedia-x86_64-unknown-linux-gnu.a  output/pjmedia-x86_64-unknown-linux-gnu/echo_speex.o  output/pjmedia-x86_64-unknown-linux-gnu/alaw_ulaw.o  output/pjmedia-x86_64-unknown-linux-gnu/alaw_ulaw_table.o  output/pjmedia-x86_64-unknown-linux-gnu/avi_player.o  output/pjmedia-x86_64-unknown-linux-gnu/bidirectional.o  output/pjmedia-x86_64-unknown-linux-gnu/clock_thread.o  output/pjmedia-x86_64-unknown-linux-gnu/codec.o  output/pjmedia-x86_64-unknown-linux-gnu/conference.o  output/pjmedia-x86_64-unknown-linux-gnu/conf_switch.o  output/pjmedia-x86_64-unknown-linux-gnu/converter.o  output/pjmedia-x86_64-unknown-linux-gnu/converter_libswscale.o  output/pjmedia-x86_64-unknown-linux-gnu/converter_libyuv.o  output/pjmedia-x86_64-unknown-linux-gnu/delaybuf.o  output/pjmedia-x86_64-unknown-linux-gnu/echo_common.o  output/pjmedia-x86_64-unknown-linux-gnu/echo_port.o  output/pjmedia-x86_64-unknown-linux-gnu/echo_suppress.o  output/pjmedia-x86_64-unknown-linux-gnu/echo_webrtc.o  output/pjmedia-x86_64-unknown-linux-gnu/endpoint.o  output/pjmedia-x86_64-unknown-linux-gnu/errno.o  output/pjmedia-x86_64-unknown-linux-gnu/event.o  output/pjmedia-x86_64-unknown-linux-gnu/format.o  output/pjmedia-x86_64-unknown-linux-gnu/ffmpeg_util.o  output/pjmedia-x86_64-unknown-linux-gnu/g711.o  output/pjmedia-x86_64-unknown-linux-gnu/jbuf.o  output/pjmedia-x86_64-unknown-linux-gnu/master_port.o  output/pjmedia-x86_64-unknown-linux-gnu/mem_capture.o  output/pjmedia-x86_64-unknown-linux-gnu/mem_player.o  output/pjmedia-x86_64-unknown-linux-gnu/null_port.o  output/pjmedia-x86_64-unknown-linux-gnu/plc_common.o  output/pjmedia-x86_64-unknown-linux-gnu/port.o  output/pjmedia-x86_64-unknown-linux-gnu/splitcomb.o  output/pjmedia-x86_64-unknown-linux-gnu/resample_resample.o  output/pjmedia-x86_64-unknown-linux-gnu/resample_libsamplerate.o  output/pjmedia-x86_64-unknown-linux-gnu/resample_speex.o  output/pjmedia-x86_64-unknown-linux-gnu/resample_port.o  output/pjmedia-x86_64-unknown-linux-gnu/rtcp.o  output/pjmedia-x86_64-unknown-linux-gnu/rtcp_xr.o  output/pjmedia-x86_64-unknown-linux-gnu/rtcp_fb.o  output/pjmedia-x86_64-unknown-linux-gnu/rtp.o  output/pjmedia-x86_64-unknown-linux-gnu/sdp.o  output/pjmedia-x86_64-unknown-linux-gnu/sdp_cmp.o  output/pjmedia-x86_64-unknown-linux-gnu/sdp_neg.o  output/pjmedia-x86_64-unknown-linux-gnu/session.o  output/pjmedia-x86_64-unknown-linux-gnu/silencedet.o  output/pjmedia-x86_64-unknown-linux-gnu/sound_legacy.o  output/pjmedia-x86_64-unknown-linux-gnu/sound_port.o  output/pjmedia-x86_64-unknown-linux-gnu/stereo_port.o  output/pjmedia-x86_64-unknown-linux-gnu/stream_common.o  output/pjmedia-x86_64-unknown-linux-gnu/stream.o  output/pjmedia-x86_64-unknown-linux-gnu/stream_info.o  output/pjmedia-x86_64-unknown-linux-gnu/tonegen.o  output/pjmedia-x86_64-unknown-linux-gnu/transport_adapter_sample.o  output/pjmedia-x86_64-unknown-linux-gnu/transport_ice.o  output/pjmedia-x86_64-unknown-linux-gnu/transport_loop.o  output/pjmedia-x86_64-unknown-linux-gnu/transport_srtp.o  output/pjmedia-x86_64-unknown-linux-gnu/transport_udp.o  output/pjmedia-x86_64-unknown-linux-gnu/types.o  output/pjmedia-x86_64-unknown-linux-gnu/vid_codec.o  output/pjmedia-x86_64-unknown-linux-gnu/vid_codec_util.o  output/pjmedia-x86_64-unknown-linux-gnu/vid_port.o  output/pjmedia-x86_64-unknown-linux-gnu/vid_stream.o  output/pjmedia-x86_64-unknown-linux-gnu/vid_stream_info.o  output/pjmedia-x86_64-unknown-linux-gnu/vid_conf.o  output/pjmedia-x86_64-unknown-linux-gnu/wav_player.o  output/pjmedia-x86_64-unknown-linux-gnu/wav_playlist.o  output/pjmedia-x86_64-unknown-linux-gnu/wav_writer.o  output/pjmedia-x86_64-unknown-linux-gnu/wave.o  output/pjmedia-x86_64-unknown-linux-gnu/wsola.o  output/pjmedia-x86_64-unknown-linux-gnu/audiodev.o  output/pjmedia-x86_64-unknown-linux-gnu/videodev.o
# r - output/pjmedia-x86_64-unknown-linux-gnu/echo_speex.o
# r - output/pjmedia-x86_64-unknown-linux-gnu/alaw_ulaw.o
# r - output/pjmedia-x86_64-unknown-linux-gnu/alaw_ulaw_table.o
# r - output/pjmedia-x86_64-unknown-linux-gnu/avi_player.o
# r - output/pjmedia-x86_64-unknown-linux-gnu/bidirectional.o
# r - output/pjmedia-x86_64-unknown-linux-gnu/clock_thread.o
# r - output/pjmedia-x86_64-unknown-linux-gnu/codec.o
# r - output/pjmedia-x86_64-unknown-linux-gnu/conference.o
# r - output/pjmedia-x86_64-unknown-linux-gnu/conf_switch.o
# r - output/pjmedia-x86_64-unknown-linux-gnu/converter.o
# r - output/pjmedia-x86_64-unknown-linux-gnu/converter_libswscale.o
# r - output/pjmedia-x86_64-unknown-linux-gnu/converter_libyuv.o
# r - output/pjmedia-x86_64-unknown-linux-gnu/delaybuf.o
# r - output/pjmedia-x86_64-unknown-linux-gnu/echo_common.o
# r - output/pjmedia-x86_64-unknown-linux-gnu/echo_port.o
# r - output/pjmedia-x86_64-unknown-linux-gnu/echo_suppress.o
# r - output/pjmedia-x86_64-unknown-linux-gnu/echo_webrtc.o
# r - output/pjmedia-x86_64-unknown-linux-gnu/endpoint.o
# r - output/pjmedia-x86_64-unknown-linux-gnu/errno.o
# r - output/pjmedia-x86_64-unknown-linux-gnu/event.o
# r - output/pjmedia-x86_64-unknown-linux-gnu/format.o
# r - output/pjmedia-x86_64-unknown-linux-gnu/ffmpeg_util.o
# r - output/pjmedia-x86_64-unknown-linux-gnu/g711.o
# r - output/pjmedia-x86_64-unknown-linux-gnu/jbuf.o
# r - output/pjmedia-x86_64-unknown-linux-gnu/master_port.o
# r - output/pjmedia-x86_64-unknown-linux-gnu/mem_capture.o
# r - output/pjmedia-x86_64-unknown-linux-gnu/mem_player.o
# r - output/pjmedia-x86_64-unknown-linux-gnu/null_port.o
# r - output/pjmedia-x86_64-unknown-linux-gnu/plc_common.o
# r - output/pjmedia-x86_64-unknown-linux-gnu/port.o
# r - output/pjmedia-x86_64-unknown-linux-gnu/splitcomb.o
# r - output/pjmedia-x86_64-unknown-linux-gnu/resample_resample.o
# r - output/pjmedia-x86_64-unknown-linux-gnu/resample_libsamplerate.o
# r - output/pjmedia-x86_64-unknown-linux-gnu/resample_speex.o
# r - output/pjmedia-x86_64-unknown-linux-gnu/resample_port.o
# r - output/pjmedia-x86_64-unknown-linux-gnu/rtcp.o
# r - output/pjmedia-x86_64-unknown-linux-gnu/rtcp_xr.o
# r - output/pjmedia-x86_64-unknown-linux-gnu/rtcp_fb.o
# r - output/pjmedia-x86_64-unknown-linux-gnu/rtp.o
# r - output/pjmedia-x86_64-unknown-linux-gnu/sdp.o
# r - output/pjmedia-x86_64-unknown-linux-gnu/sdp_cmp.o
# r - output/pjmedia-x86_64-unknown-linux-gnu/sdp_neg.o
# r - output/pjmedia-x86_64-unknown-linux-gnu/session.o
# r - output/pjmedia-x86_64-unknown-linux-gnu/silencedet.o
# r - output/pjmedia-x86_64-unknown-linux-gnu/sound_legacy.o
# r - output/pjmedia-x86_64-unknown-linux-gnu/sound_port.o
# r - output/pjmedia-x86_64-unknown-linux-gnu/stereo_port.o
# r - output/pjmedia-x86_64-unknown-linux-gnu/stream_common.o
# r - output/pjmedia-x86_64-unknown-linux-gnu/stream.o
# r - output/pjmedia-x86_64-unknown-linux-gnu/stream_info.o
# r - output/pjmedia-x86_64-unknown-linux-gnu/tonegen.o
# r - output/pjmedia-x86_64-unknown-linux-gnu/transport_adapter_sample.o
# r - output/pjmedia-x86_64-unknown-linux-gnu/transport_ice.o
# r - output/pjmedia-x86_64-unknown-linux-gnu/transport_loop.o
# r - output/pjmedia-x86_64-unknown-linux-gnu/transport_srtp.o
# r - output/pjmedia-x86_64-unknown-linux-gnu/transport_udp.o
# r - output/pjmedia-x86_64-unknown-linux-gnu/types.o
# r - output/pjmedia-x86_64-unknown-linux-gnu/vid_codec.o
# r - output/pjmedia-x86_64-unknown-linux-gnu/vid_codec_util.o
# r - output/pjmedia-x86_64-unknown-linux-gnu/vid_port.o
# r - output/pjmedia-x86_64-unknown-linux-gnu/vid_stream.o
# r - output/pjmedia-x86_64-unknown-linux-gnu/vid_stream_info.o
# r - output/pjmedia-x86_64-unknown-linux-gnu/vid_conf.o
# r - output/pjmedia-x86_64-unknown-linux-gnu/wav_player.o
# r - output/pjmedia-x86_64-unknown-linux-gnu/wav_playlist.o
# r - output/pjmedia-x86_64-unknown-linux-gnu/wav_writer.o
# r - output/pjmedia-x86_64-unknown-linux-gnu/wave.o
# r - output/pjmedia-x86_64-unknown-linux-gnu/wsola.o
# r - output/pjmedia-x86_64-unknown-linux-gnu/audiodev.o
# r - output/pjmedia-x86_64-unknown-linux-gnu/videodev.o
# ranlib ../lib/libpjmedia-x86_64-unknown-linux-gnu.a
# make[2]: Leaving directory '/home/vsedyshev/Work/1111/pjproject/pjmedia/build'
# make -f /home/vsedyshev/Work/1111/pjproject/build/rules.mak APP=PJMEDIA_CODEC app=pjmedia-codec ../lib/libpjmedia-codec-x86_64-unknown-linux-gnu.a
# make[2]: Entering directory '/home/vsedyshev/Work/1111/pjproject/pjmedia/build'
# mkdir -p output/pjmedia-codec-x86_64-unknown-linux-gnu/
# mkdir -p output/pjmedia-codec-x86_64-unknown-linux-gnu/g722/
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1   -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1        -I/home/vsedyshev/Work/1111/pjproject/third_party/build/speex -I/home/vsedyshev/Work/1111/pjproject/third_party/speex/include -DPJMEDIA_HAS_OPENCORE_AMRNB_CODEC=0 -DPJMEDIA_HAS_OPENCORE_AMRWB_CODEC=0 -I/home/vsedyshev/Work/1111/pjproject/third_party/build/srtp -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/crypto/include -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/include -DPJMEDIA_RESAMPLE_IMP=PJMEDIA_RESAMPLE_LIBRESAMPLE -DPJMEDIA_HAS_LIBYUV=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/yuv/include -DPJMEDIA_HAS_WEBRTC_AEC=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/webrtc/src -DPJMEDIA_AUDIO_DEV_HAS_ALSA=1 -DPJMEDIA_AUDIO_DEV_HAS_PORTAUDIO=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjmedia/include -I../../pjnath/include -I../..     -I/home/vsedyshev/Work/1111/pjproject/third_party \
# 	-o output/pjmedia-codec-x86_64-unknown-linux-gnu/audio_codecs.o \
# 	../src/pjmedia-codec/audio_codecs.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1   -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1        -I/home/vsedyshev/Work/1111/pjproject/third_party/build/speex -I/home/vsedyshev/Work/1111/pjproject/third_party/speex/include -DPJMEDIA_HAS_OPENCORE_AMRNB_CODEC=0 -DPJMEDIA_HAS_OPENCORE_AMRWB_CODEC=0 -I/home/vsedyshev/Work/1111/pjproject/third_party/build/srtp -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/crypto/include -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/include -DPJMEDIA_RESAMPLE_IMP=PJMEDIA_RESAMPLE_LIBRESAMPLE -DPJMEDIA_HAS_LIBYUV=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/yuv/include -DPJMEDIA_HAS_WEBRTC_AEC=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/webrtc/src -DPJMEDIA_AUDIO_DEV_HAS_ALSA=1 -DPJMEDIA_AUDIO_DEV_HAS_PORTAUDIO=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjmedia/include -I../../pjnath/include -I../..     -I/home/vsedyshev/Work/1111/pjproject/third_party \
# 	-o output/pjmedia-codec-x86_64-unknown-linux-gnu/ffmpeg_vid_codecs.o \
# 	../src/pjmedia-codec/ffmpeg_vid_codecs.c 
# g++ -c  -DPJ_AUTOCONF=1 -g -O2    -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1   -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1        -I/home/vsedyshev/Work/1111/pjproject/third_party/build/speex -I/home/vsedyshev/Work/1111/pjproject/third_party/speex/include -DPJMEDIA_HAS_OPENCORE_AMRNB_CODEC=0 -DPJMEDIA_HAS_OPENCORE_AMRWB_CODEC=0 -I/home/vsedyshev/Work/1111/pjproject/third_party/build/srtp -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/crypto/include -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/include -DPJMEDIA_RESAMPLE_IMP=PJMEDIA_RESAMPLE_LIBRESAMPLE -DPJMEDIA_HAS_LIBYUV=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/yuv/include -DPJMEDIA_HAS_WEBRTC_AEC=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/webrtc/src -DPJMEDIA_AUDIO_DEV_HAS_ALSA=1 -DPJMEDIA_AUDIO_DEV_HAS_PORTAUDIO=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjmedia/include -I../../pjnath/include -I../..      -I/home/vsedyshev/Work/1111/pjproject/third_party \
# 	-o output/pjmedia-codec-x86_64-unknown-linux-gnu/openh264.o \
# 	../src/pjmedia-codec/openh264.cpp
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1   -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1        -I/home/vsedyshev/Work/1111/pjproject/third_party/build/speex -I/home/vsedyshev/Work/1111/pjproject/third_party/speex/include -DPJMEDIA_HAS_OPENCORE_AMRNB_CODEC=0 -DPJMEDIA_HAS_OPENCORE_AMRWB_CODEC=0 -I/home/vsedyshev/Work/1111/pjproject/third_party/build/srtp -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/crypto/include -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/include -DPJMEDIA_RESAMPLE_IMP=PJMEDIA_RESAMPLE_LIBRESAMPLE -DPJMEDIA_HAS_LIBYUV=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/yuv/include -DPJMEDIA_HAS_WEBRTC_AEC=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/webrtc/src -DPJMEDIA_AUDIO_DEV_HAS_ALSA=1 -DPJMEDIA_AUDIO_DEV_HAS_PORTAUDIO=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjmedia/include -I../../pjnath/include -I../..     -I/home/vsedyshev/Work/1111/pjproject/third_party \
# 	-o output/pjmedia-codec-x86_64-unknown-linux-gnu/h263_packetizer.o \
# 	../src/pjmedia-codec/h263_packetizer.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1   -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1        -I/home/vsedyshev/Work/1111/pjproject/third_party/build/speex -I/home/vsedyshev/Work/1111/pjproject/third_party/speex/include -DPJMEDIA_HAS_OPENCORE_AMRNB_CODEC=0 -DPJMEDIA_HAS_OPENCORE_AMRWB_CODEC=0 -I/home/vsedyshev/Work/1111/pjproject/third_party/build/srtp -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/crypto/include -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/include -DPJMEDIA_RESAMPLE_IMP=PJMEDIA_RESAMPLE_LIBRESAMPLE -DPJMEDIA_HAS_LIBYUV=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/yuv/include -DPJMEDIA_HAS_WEBRTC_AEC=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/webrtc/src -DPJMEDIA_AUDIO_DEV_HAS_ALSA=1 -DPJMEDIA_AUDIO_DEV_HAS_PORTAUDIO=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjmedia/include -I../../pjnath/include -I../..     -I/home/vsedyshev/Work/1111/pjproject/third_party \
# 	-o output/pjmedia-codec-x86_64-unknown-linux-gnu/h264_packetizer.o \
# 	../src/pjmedia-codec/h264_packetizer.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1   -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1        -I/home/vsedyshev/Work/1111/pjproject/third_party/build/speex -I/home/vsedyshev/Work/1111/pjproject/third_party/speex/include -DPJMEDIA_HAS_OPENCORE_AMRNB_CODEC=0 -DPJMEDIA_HAS_OPENCORE_AMRWB_CODEC=0 -I/home/vsedyshev/Work/1111/pjproject/third_party/build/srtp -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/crypto/include -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/include -DPJMEDIA_RESAMPLE_IMP=PJMEDIA_RESAMPLE_LIBRESAMPLE -DPJMEDIA_HAS_LIBYUV=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/yuv/include -DPJMEDIA_HAS_WEBRTC_AEC=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/webrtc/src -DPJMEDIA_AUDIO_DEV_HAS_ALSA=1 -DPJMEDIA_AUDIO_DEV_HAS_PORTAUDIO=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjmedia/include -I../../pjnath/include -I../..     -I/home/vsedyshev/Work/1111/pjproject/third_party \
# 	-o output/pjmedia-codec-x86_64-unknown-linux-gnu/ipp_codecs.o \
# 	../src/pjmedia-codec/ipp_codecs.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1   -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1        -I/home/vsedyshev/Work/1111/pjproject/third_party/build/speex -I/home/vsedyshev/Work/1111/pjproject/third_party/speex/include -DPJMEDIA_HAS_OPENCORE_AMRNB_CODEC=0 -DPJMEDIA_HAS_OPENCORE_AMRWB_CODEC=0 -I/home/vsedyshev/Work/1111/pjproject/third_party/build/srtp -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/crypto/include -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/include -DPJMEDIA_RESAMPLE_IMP=PJMEDIA_RESAMPLE_LIBRESAMPLE -DPJMEDIA_HAS_LIBYUV=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/yuv/include -DPJMEDIA_HAS_WEBRTC_AEC=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/webrtc/src -DPJMEDIA_AUDIO_DEV_HAS_ALSA=1 -DPJMEDIA_AUDIO_DEV_HAS_PORTAUDIO=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjmedia/include -I../../pjnath/include -I../..     -I/home/vsedyshev/Work/1111/pjproject/third_party \
# 	-o output/pjmedia-codec-x86_64-unknown-linux-gnu/silk.o \
# 	../src/pjmedia-codec/silk.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1   -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1        -I/home/vsedyshev/Work/1111/pjproject/third_party/build/speex -I/home/vsedyshev/Work/1111/pjproject/third_party/speex/include -DPJMEDIA_HAS_OPENCORE_AMRNB_CODEC=0 -DPJMEDIA_HAS_OPENCORE_AMRWB_CODEC=0 -I/home/vsedyshev/Work/1111/pjproject/third_party/build/srtp -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/crypto/include -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/include -DPJMEDIA_RESAMPLE_IMP=PJMEDIA_RESAMPLE_LIBRESAMPLE -DPJMEDIA_HAS_LIBYUV=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/yuv/include -DPJMEDIA_HAS_WEBRTC_AEC=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/webrtc/src -DPJMEDIA_AUDIO_DEV_HAS_ALSA=1 -DPJMEDIA_AUDIO_DEV_HAS_PORTAUDIO=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjmedia/include -I../../pjnath/include -I../..     -I/home/vsedyshev/Work/1111/pjproject/third_party \
# 	-o output/pjmedia-codec-x86_64-unknown-linux-gnu/opus.o \
# 	../src/pjmedia-codec/opus.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1   -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1        -I/home/vsedyshev/Work/1111/pjproject/third_party/build/speex -I/home/vsedyshev/Work/1111/pjproject/third_party/speex/include -DPJMEDIA_HAS_OPENCORE_AMRNB_CODEC=0 -DPJMEDIA_HAS_OPENCORE_AMRWB_CODEC=0 -I/home/vsedyshev/Work/1111/pjproject/third_party/build/srtp -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/crypto/include -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/include -DPJMEDIA_RESAMPLE_IMP=PJMEDIA_RESAMPLE_LIBRESAMPLE -DPJMEDIA_HAS_LIBYUV=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/yuv/include -DPJMEDIA_HAS_WEBRTC_AEC=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/webrtc/src -DPJMEDIA_AUDIO_DEV_HAS_ALSA=1 -DPJMEDIA_AUDIO_DEV_HAS_PORTAUDIO=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjmedia/include -I../../pjnath/include -I../..     -I/home/vsedyshev/Work/1111/pjproject/third_party \
# 	-o output/pjmedia-codec-x86_64-unknown-linux-gnu/l16.o \
# 	../src/pjmedia-codec/l16.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1   -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1        -I/home/vsedyshev/Work/1111/pjproject/third_party/build/speex -I/home/vsedyshev/Work/1111/pjproject/third_party/speex/include -DPJMEDIA_HAS_OPENCORE_AMRNB_CODEC=0 -DPJMEDIA_HAS_OPENCORE_AMRWB_CODEC=0 -I/home/vsedyshev/Work/1111/pjproject/third_party/build/srtp -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/crypto/include -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/include -DPJMEDIA_RESAMPLE_IMP=PJMEDIA_RESAMPLE_LIBRESAMPLE -DPJMEDIA_HAS_LIBYUV=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/yuv/include -DPJMEDIA_HAS_WEBRTC_AEC=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/webrtc/src -DPJMEDIA_AUDIO_DEV_HAS_ALSA=1 -DPJMEDIA_AUDIO_DEV_HAS_PORTAUDIO=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjmedia/include -I../../pjnath/include -I../..     -I/home/vsedyshev/Work/1111/pjproject/third_party \
# 	-o output/pjmedia-codec-x86_64-unknown-linux-gnu/gsm.o \
# 	../src/pjmedia-codec/gsm.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1   -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1        -I/home/vsedyshev/Work/1111/pjproject/third_party/build/speex -I/home/vsedyshev/Work/1111/pjproject/third_party/speex/include -DPJMEDIA_HAS_OPENCORE_AMRNB_CODEC=0 -DPJMEDIA_HAS_OPENCORE_AMRWB_CODEC=0 -I/home/vsedyshev/Work/1111/pjproject/third_party/build/srtp -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/crypto/include -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/include -DPJMEDIA_RESAMPLE_IMP=PJMEDIA_RESAMPLE_LIBRESAMPLE -DPJMEDIA_HAS_LIBYUV=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/yuv/include -DPJMEDIA_HAS_WEBRTC_AEC=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/webrtc/src -DPJMEDIA_AUDIO_DEV_HAS_ALSA=1 -DPJMEDIA_AUDIO_DEV_HAS_PORTAUDIO=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjmedia/include -I../../pjnath/include -I../..     -I/home/vsedyshev/Work/1111/pjproject/third_party \
# 	-o output/pjmedia-codec-x86_64-unknown-linux-gnu/speex_codec.o \
# 	../src/pjmedia-codec/speex_codec.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1   -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1        -I/home/vsedyshev/Work/1111/pjproject/third_party/build/speex -I/home/vsedyshev/Work/1111/pjproject/third_party/speex/include -DPJMEDIA_HAS_OPENCORE_AMRNB_CODEC=0 -DPJMEDIA_HAS_OPENCORE_AMRWB_CODEC=0 -I/home/vsedyshev/Work/1111/pjproject/third_party/build/srtp -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/crypto/include -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/include -DPJMEDIA_RESAMPLE_IMP=PJMEDIA_RESAMPLE_LIBRESAMPLE -DPJMEDIA_HAS_LIBYUV=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/yuv/include -DPJMEDIA_HAS_WEBRTC_AEC=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/webrtc/src -DPJMEDIA_AUDIO_DEV_HAS_ALSA=1 -DPJMEDIA_AUDIO_DEV_HAS_PORTAUDIO=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjmedia/include -I../../pjnath/include -I../..     -I/home/vsedyshev/Work/1111/pjproject/third_party \
# 	-o output/pjmedia-codec-x86_64-unknown-linux-gnu/ilbc.o \
# 	../src/pjmedia-codec/ilbc.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1   -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1        -I/home/vsedyshev/Work/1111/pjproject/third_party/build/speex -I/home/vsedyshev/Work/1111/pjproject/third_party/speex/include -DPJMEDIA_HAS_OPENCORE_AMRNB_CODEC=0 -DPJMEDIA_HAS_OPENCORE_AMRWB_CODEC=0 -I/home/vsedyshev/Work/1111/pjproject/third_party/build/srtp -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/crypto/include -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/include -DPJMEDIA_RESAMPLE_IMP=PJMEDIA_RESAMPLE_LIBRESAMPLE -DPJMEDIA_HAS_LIBYUV=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/yuv/include -DPJMEDIA_HAS_WEBRTC_AEC=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/webrtc/src -DPJMEDIA_AUDIO_DEV_HAS_ALSA=1 -DPJMEDIA_AUDIO_DEV_HAS_PORTAUDIO=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjmedia/include -I../../pjnath/include -I../..     -I/home/vsedyshev/Work/1111/pjproject/third_party \
# 	-o output/pjmedia-codec-x86_64-unknown-linux-gnu/g722.o \
# 	../src/pjmedia-codec/g722.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1   -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1        -I/home/vsedyshev/Work/1111/pjproject/third_party/build/speex -I/home/vsedyshev/Work/1111/pjproject/third_party/speex/include -DPJMEDIA_HAS_OPENCORE_AMRNB_CODEC=0 -DPJMEDIA_HAS_OPENCORE_AMRWB_CODEC=0 -I/home/vsedyshev/Work/1111/pjproject/third_party/build/srtp -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/crypto/include -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/include -DPJMEDIA_RESAMPLE_IMP=PJMEDIA_RESAMPLE_LIBRESAMPLE -DPJMEDIA_HAS_LIBYUV=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/yuv/include -DPJMEDIA_HAS_WEBRTC_AEC=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/webrtc/src -DPJMEDIA_AUDIO_DEV_HAS_ALSA=1 -DPJMEDIA_AUDIO_DEV_HAS_PORTAUDIO=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjmedia/include -I../../pjnath/include -I../..     -I/home/vsedyshev/Work/1111/pjproject/third_party \
# 	-o output/pjmedia-codec-x86_64-unknown-linux-gnu/g722/g722_enc.o \
# 	../src/pjmedia-codec/g722/g722_enc.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1   -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1        -I/home/vsedyshev/Work/1111/pjproject/third_party/build/speex -I/home/vsedyshev/Work/1111/pjproject/third_party/speex/include -DPJMEDIA_HAS_OPENCORE_AMRNB_CODEC=0 -DPJMEDIA_HAS_OPENCORE_AMRWB_CODEC=0 -I/home/vsedyshev/Work/1111/pjproject/third_party/build/srtp -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/crypto/include -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/include -DPJMEDIA_RESAMPLE_IMP=PJMEDIA_RESAMPLE_LIBRESAMPLE -DPJMEDIA_HAS_LIBYUV=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/yuv/include -DPJMEDIA_HAS_WEBRTC_AEC=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/webrtc/src -DPJMEDIA_AUDIO_DEV_HAS_ALSA=1 -DPJMEDIA_AUDIO_DEV_HAS_PORTAUDIO=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjmedia/include -I../../pjnath/include -I../..     -I/home/vsedyshev/Work/1111/pjproject/third_party \
# 	-o output/pjmedia-codec-x86_64-unknown-linux-gnu/g722/g722_dec.o \
# 	../src/pjmedia-codec/g722/g722_dec.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1   -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1        -I/home/vsedyshev/Work/1111/pjproject/third_party/build/speex -I/home/vsedyshev/Work/1111/pjproject/third_party/speex/include -DPJMEDIA_HAS_OPENCORE_AMRNB_CODEC=0 -DPJMEDIA_HAS_OPENCORE_AMRWB_CODEC=0 -I/home/vsedyshev/Work/1111/pjproject/third_party/build/srtp -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/crypto/include -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/include -DPJMEDIA_RESAMPLE_IMP=PJMEDIA_RESAMPLE_LIBRESAMPLE -DPJMEDIA_HAS_LIBYUV=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/yuv/include -DPJMEDIA_HAS_WEBRTC_AEC=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/webrtc/src -DPJMEDIA_AUDIO_DEV_HAS_ALSA=1 -DPJMEDIA_AUDIO_DEV_HAS_PORTAUDIO=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjmedia/include -I../../pjnath/include -I../..     -I/home/vsedyshev/Work/1111/pjproject/third_party \
# 	-o output/pjmedia-codec-x86_64-unknown-linux-gnu/g7221.o \
# 	../src/pjmedia-codec/g7221.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1   -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1        -I/home/vsedyshev/Work/1111/pjproject/third_party/build/speex -I/home/vsedyshev/Work/1111/pjproject/third_party/speex/include -DPJMEDIA_HAS_OPENCORE_AMRNB_CODEC=0 -DPJMEDIA_HAS_OPENCORE_AMRWB_CODEC=0 -I/home/vsedyshev/Work/1111/pjproject/third_party/build/srtp -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/crypto/include -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/include -DPJMEDIA_RESAMPLE_IMP=PJMEDIA_RESAMPLE_LIBRESAMPLE -DPJMEDIA_HAS_LIBYUV=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/yuv/include -DPJMEDIA_HAS_WEBRTC_AEC=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/webrtc/src -DPJMEDIA_AUDIO_DEV_HAS_ALSA=1 -DPJMEDIA_AUDIO_DEV_HAS_PORTAUDIO=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjmedia/include -I../../pjnath/include -I../..     -I/home/vsedyshev/Work/1111/pjproject/third_party \
# 	-o output/pjmedia-codec-x86_64-unknown-linux-gnu/g7221_sdp_match.o \
# 	../src/pjmedia-codec/g7221_sdp_match.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1   -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1        -I/home/vsedyshev/Work/1111/pjproject/third_party/build/speex -I/home/vsedyshev/Work/1111/pjproject/third_party/speex/include -DPJMEDIA_HAS_OPENCORE_AMRNB_CODEC=0 -DPJMEDIA_HAS_OPENCORE_AMRWB_CODEC=0 -I/home/vsedyshev/Work/1111/pjproject/third_party/build/srtp -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/crypto/include -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/include -DPJMEDIA_RESAMPLE_IMP=PJMEDIA_RESAMPLE_LIBRESAMPLE -DPJMEDIA_HAS_LIBYUV=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/yuv/include -DPJMEDIA_HAS_WEBRTC_AEC=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/webrtc/src -DPJMEDIA_AUDIO_DEV_HAS_ALSA=1 -DPJMEDIA_AUDIO_DEV_HAS_PORTAUDIO=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjmedia/include -I../../pjnath/include -I../..     -I/home/vsedyshev/Work/1111/pjproject/third_party \
# 	-o output/pjmedia-codec-x86_64-unknown-linux-gnu/amr_sdp_match.o \
# 	../src/pjmedia-codec/amr_sdp_match.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1   -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1        -I/home/vsedyshev/Work/1111/pjproject/third_party/build/speex -I/home/vsedyshev/Work/1111/pjproject/third_party/speex/include -DPJMEDIA_HAS_OPENCORE_AMRNB_CODEC=0 -DPJMEDIA_HAS_OPENCORE_AMRWB_CODEC=0 -I/home/vsedyshev/Work/1111/pjproject/third_party/build/srtp -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/crypto/include -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/include -DPJMEDIA_RESAMPLE_IMP=PJMEDIA_RESAMPLE_LIBRESAMPLE -DPJMEDIA_HAS_LIBYUV=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/yuv/include -DPJMEDIA_HAS_WEBRTC_AEC=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/webrtc/src -DPJMEDIA_AUDIO_DEV_HAS_ALSA=1 -DPJMEDIA_AUDIO_DEV_HAS_PORTAUDIO=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjmedia/include -I../../pjnath/include -I../..     -I/home/vsedyshev/Work/1111/pjproject/third_party \
# 	-o output/pjmedia-codec-x86_64-unknown-linux-gnu/passthrough.o \
# 	../src/pjmedia-codec/passthrough.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1   -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1        -I/home/vsedyshev/Work/1111/pjproject/third_party/build/speex -I/home/vsedyshev/Work/1111/pjproject/third_party/speex/include -DPJMEDIA_HAS_OPENCORE_AMRNB_CODEC=0 -DPJMEDIA_HAS_OPENCORE_AMRWB_CODEC=0 -I/home/vsedyshev/Work/1111/pjproject/third_party/build/srtp -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/crypto/include -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/include -DPJMEDIA_RESAMPLE_IMP=PJMEDIA_RESAMPLE_LIBRESAMPLE -DPJMEDIA_HAS_LIBYUV=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/yuv/include -DPJMEDIA_HAS_WEBRTC_AEC=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/webrtc/src -DPJMEDIA_AUDIO_DEV_HAS_ALSA=1 -DPJMEDIA_AUDIO_DEV_HAS_PORTAUDIO=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjmedia/include -I../../pjnath/include -I../..     -I/home/vsedyshev/Work/1111/pjproject/third_party \
# 	-o output/pjmedia-codec-x86_64-unknown-linux-gnu/vpx.o \
# 	../src/pjmedia-codec/vpx.c 
# if test ! -d ../lib; then mkdir -p ../lib; fi
# ar rv ../lib/libpjmedia-codec-x86_64-unknown-linux-gnu.a  output/pjmedia-codec-x86_64-unknown-linux-gnu/audio_codecs.o  output/pjmedia-codec-x86_64-unknown-linux-gnu/ffmpeg_vid_codecs.o  output/pjmedia-codec-x86_64-unknown-linux-gnu/openh264.o  output/pjmedia-codec-x86_64-unknown-linux-gnu/h263_packetizer.o  output/pjmedia-codec-x86_64-unknown-linux-gnu/h264_packetizer.o  output/pjmedia-codec-x86_64-unknown-linux-gnu/ipp_codecs.o  output/pjmedia-codec-x86_64-unknown-linux-gnu/silk.o  output/pjmedia-codec-x86_64-unknown-linux-gnu/opus.o  output/pjmedia-codec-x86_64-unknown-linux-gnu/l16.o  output/pjmedia-codec-x86_64-unknown-linux-gnu/gsm.o  output/pjmedia-codec-x86_64-unknown-linux-gnu/speex_codec.o  output/pjmedia-codec-x86_64-unknown-linux-gnu/ilbc.o  output/pjmedia-codec-x86_64-unknown-linux-gnu/g722.o  output/pjmedia-codec-x86_64-unknown-linux-gnu/g722/g722_enc.o  output/pjmedia-codec-x86_64-unknown-linux-gnu/g722/g722_dec.o  output/pjmedia-codec-x86_64-unknown-linux-gnu/g7221.o  output/pjmedia-codec-x86_64-unknown-linux-gnu/g7221_sdp_match.o  output/pjmedia-codec-x86_64-unknown-linux-gnu/amr_sdp_match.o  output/pjmedia-codec-x86_64-unknown-linux-gnu/passthrough.o  output/pjmedia-codec-x86_64-unknown-linux-gnu/vpx.o
# r - output/pjmedia-codec-x86_64-unknown-linux-gnu/audio_codecs.o
# r - output/pjmedia-codec-x86_64-unknown-linux-gnu/ffmpeg_vid_codecs.o
# r - output/pjmedia-codec-x86_64-unknown-linux-gnu/openh264.o
# r - output/pjmedia-codec-x86_64-unknown-linux-gnu/h263_packetizer.o
# r - output/pjmedia-codec-x86_64-unknown-linux-gnu/h264_packetizer.o
# r - output/pjmedia-codec-x86_64-unknown-linux-gnu/ipp_codecs.o
# r - output/pjmedia-codec-x86_64-unknown-linux-gnu/silk.o
# r - output/pjmedia-codec-x86_64-unknown-linux-gnu/opus.o
# r - output/pjmedia-codec-x86_64-unknown-linux-gnu/l16.o
# r - output/pjmedia-codec-x86_64-unknown-linux-gnu/gsm.o
# r - output/pjmedia-codec-x86_64-unknown-linux-gnu/speex_codec.o
# r - output/pjmedia-codec-x86_64-unknown-linux-gnu/ilbc.o
# r - output/pjmedia-codec-x86_64-unknown-linux-gnu/g722.o
# r - output/pjmedia-codec-x86_64-unknown-linux-gnu/g722/g722_enc.o
# r - output/pjmedia-codec-x86_64-unknown-linux-gnu/g722/g722_dec.o
# r - output/pjmedia-codec-x86_64-unknown-linux-gnu/g7221.o
# r - output/pjmedia-codec-x86_64-unknown-linux-gnu/g7221_sdp_match.o
# r - output/pjmedia-codec-x86_64-unknown-linux-gnu/amr_sdp_match.o
# r - output/pjmedia-codec-x86_64-unknown-linux-gnu/passthrough.o
# r - output/pjmedia-codec-x86_64-unknown-linux-gnu/vpx.o
# ranlib ../lib/libpjmedia-codec-x86_64-unknown-linux-gnu.a
# make[2]: Leaving directory '/home/vsedyshev/Work/1111/pjproject/pjmedia/build'
# make -f /home/vsedyshev/Work/1111/pjproject/build/rules.mak APP=PJMEDIA_VIDEODEV app=pjmedia-videodev ../lib/libpjmedia-videodev-x86_64-unknown-linux-gnu.a
# make[2]: Entering directory '/home/vsedyshev/Work/1111/pjproject/pjmedia/build'
# mkdir -p output/pjmedia-videodev-x86_64-unknown-linux-gnu/
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1   -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1        -I/home/vsedyshev/Work/1111/pjproject/third_party/build/speex -I/home/vsedyshev/Work/1111/pjproject/third_party/speex/include -DPJMEDIA_HAS_OPENCORE_AMRNB_CODEC=0 -DPJMEDIA_HAS_OPENCORE_AMRWB_CODEC=0 -I/home/vsedyshev/Work/1111/pjproject/third_party/build/srtp -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/crypto/include -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/include -DPJMEDIA_RESAMPLE_IMP=PJMEDIA_RESAMPLE_LIBRESAMPLE -DPJMEDIA_HAS_LIBYUV=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/yuv/include -DPJMEDIA_HAS_WEBRTC_AEC=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/webrtc/src -DPJMEDIA_AUDIO_DEV_HAS_ALSA=1 -DPJMEDIA_AUDIO_DEV_HAS_PORTAUDIO=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjmedia/include -I../../pjnath/include -I../.. \
# 	-o output/pjmedia-videodev-x86_64-unknown-linux-gnu/sdl_dev.o \
# 	../src/pjmedia-videodev/sdl_dev.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1   -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1        -I/home/vsedyshev/Work/1111/pjproject/third_party/build/speex -I/home/vsedyshev/Work/1111/pjproject/third_party/speex/include -DPJMEDIA_HAS_OPENCORE_AMRNB_CODEC=0 -DPJMEDIA_HAS_OPENCORE_AMRWB_CODEC=0 -I/home/vsedyshev/Work/1111/pjproject/third_party/build/srtp -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/crypto/include -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/include -DPJMEDIA_RESAMPLE_IMP=PJMEDIA_RESAMPLE_LIBRESAMPLE -DPJMEDIA_HAS_LIBYUV=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/yuv/include -DPJMEDIA_HAS_WEBRTC_AEC=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/webrtc/src -DPJMEDIA_AUDIO_DEV_HAS_ALSA=1 -DPJMEDIA_AUDIO_DEV_HAS_PORTAUDIO=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjmedia/include -I../../pjnath/include -I../.. \
# 	-o output/pjmedia-videodev-x86_64-unknown-linux-gnu/videodev.o \
# 	../src/pjmedia-videodev/videodev.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1   -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1        -I/home/vsedyshev/Work/1111/pjproject/third_party/build/speex -I/home/vsedyshev/Work/1111/pjproject/third_party/speex/include -DPJMEDIA_HAS_OPENCORE_AMRNB_CODEC=0 -DPJMEDIA_HAS_OPENCORE_AMRWB_CODEC=0 -I/home/vsedyshev/Work/1111/pjproject/third_party/build/srtp -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/crypto/include -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/include -DPJMEDIA_RESAMPLE_IMP=PJMEDIA_RESAMPLE_LIBRESAMPLE -DPJMEDIA_HAS_LIBYUV=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/yuv/include -DPJMEDIA_HAS_WEBRTC_AEC=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/webrtc/src -DPJMEDIA_AUDIO_DEV_HAS_ALSA=1 -DPJMEDIA_AUDIO_DEV_HAS_PORTAUDIO=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjmedia/include -I../../pjnath/include -I../.. \
# 	-o output/pjmedia-videodev-x86_64-unknown-linux-gnu/errno.o \
# 	../src/pjmedia-videodev/errno.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1   -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1        -I/home/vsedyshev/Work/1111/pjproject/third_party/build/speex -I/home/vsedyshev/Work/1111/pjproject/third_party/speex/include -DPJMEDIA_HAS_OPENCORE_AMRNB_CODEC=0 -DPJMEDIA_HAS_OPENCORE_AMRWB_CODEC=0 -I/home/vsedyshev/Work/1111/pjproject/third_party/build/srtp -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/crypto/include -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/include -DPJMEDIA_RESAMPLE_IMP=PJMEDIA_RESAMPLE_LIBRESAMPLE -DPJMEDIA_HAS_LIBYUV=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/yuv/include -DPJMEDIA_HAS_WEBRTC_AEC=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/webrtc/src -DPJMEDIA_AUDIO_DEV_HAS_ALSA=1 -DPJMEDIA_AUDIO_DEV_HAS_PORTAUDIO=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjmedia/include -I../../pjnath/include -I../.. \
# 	-o output/pjmedia-videodev-x86_64-unknown-linux-gnu/avi_dev.o \
# 	../src/pjmedia-videodev/avi_dev.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1   -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1        -I/home/vsedyshev/Work/1111/pjproject/third_party/build/speex -I/home/vsedyshev/Work/1111/pjproject/third_party/speex/include -DPJMEDIA_HAS_OPENCORE_AMRNB_CODEC=0 -DPJMEDIA_HAS_OPENCORE_AMRWB_CODEC=0 -I/home/vsedyshev/Work/1111/pjproject/third_party/build/srtp -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/crypto/include -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/include -DPJMEDIA_RESAMPLE_IMP=PJMEDIA_RESAMPLE_LIBRESAMPLE -DPJMEDIA_HAS_LIBYUV=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/yuv/include -DPJMEDIA_HAS_WEBRTC_AEC=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/webrtc/src -DPJMEDIA_AUDIO_DEV_HAS_ALSA=1 -DPJMEDIA_AUDIO_DEV_HAS_PORTAUDIO=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjmedia/include -I../../pjnath/include -I../.. \
# 	-o output/pjmedia-videodev-x86_64-unknown-linux-gnu/ffmpeg_dev.o \
# 	../src/pjmedia-videodev/ffmpeg_dev.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1   -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1        -I/home/vsedyshev/Work/1111/pjproject/third_party/build/speex -I/home/vsedyshev/Work/1111/pjproject/third_party/speex/include -DPJMEDIA_HAS_OPENCORE_AMRNB_CODEC=0 -DPJMEDIA_HAS_OPENCORE_AMRWB_CODEC=0 -I/home/vsedyshev/Work/1111/pjproject/third_party/build/srtp -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/crypto/include -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/include -DPJMEDIA_RESAMPLE_IMP=PJMEDIA_RESAMPLE_LIBRESAMPLE -DPJMEDIA_HAS_LIBYUV=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/yuv/include -DPJMEDIA_HAS_WEBRTC_AEC=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/webrtc/src -DPJMEDIA_AUDIO_DEV_HAS_ALSA=1 -DPJMEDIA_AUDIO_DEV_HAS_PORTAUDIO=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjmedia/include -I../../pjnath/include -I../.. \
# 	-o output/pjmedia-videodev-x86_64-unknown-linux-gnu/colorbar_dev.o \
# 	../src/pjmedia-videodev/colorbar_dev.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1   -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1        -I/home/vsedyshev/Work/1111/pjproject/third_party/build/speex -I/home/vsedyshev/Work/1111/pjproject/third_party/speex/include -DPJMEDIA_HAS_OPENCORE_AMRNB_CODEC=0 -DPJMEDIA_HAS_OPENCORE_AMRWB_CODEC=0 -I/home/vsedyshev/Work/1111/pjproject/third_party/build/srtp -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/crypto/include -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/include -DPJMEDIA_RESAMPLE_IMP=PJMEDIA_RESAMPLE_LIBRESAMPLE -DPJMEDIA_HAS_LIBYUV=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/yuv/include -DPJMEDIA_HAS_WEBRTC_AEC=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/webrtc/src -DPJMEDIA_AUDIO_DEV_HAS_ALSA=1 -DPJMEDIA_AUDIO_DEV_HAS_PORTAUDIO=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjmedia/include -I../../pjnath/include -I../.. \
# 	-o output/pjmedia-videodev-x86_64-unknown-linux-gnu/v4l2_dev.o \
# 	../src/pjmedia-videodev/v4l2_dev.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1   -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1        -I/home/vsedyshev/Work/1111/pjproject/third_party/build/speex -I/home/vsedyshev/Work/1111/pjproject/third_party/speex/include -DPJMEDIA_HAS_OPENCORE_AMRNB_CODEC=0 -DPJMEDIA_HAS_OPENCORE_AMRWB_CODEC=0 -I/home/vsedyshev/Work/1111/pjproject/third_party/build/srtp -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/crypto/include -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/include -DPJMEDIA_RESAMPLE_IMP=PJMEDIA_RESAMPLE_LIBRESAMPLE -DPJMEDIA_HAS_LIBYUV=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/yuv/include -DPJMEDIA_HAS_WEBRTC_AEC=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/webrtc/src -DPJMEDIA_AUDIO_DEV_HAS_ALSA=1 -DPJMEDIA_AUDIO_DEV_HAS_PORTAUDIO=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjmedia/include -I../../pjnath/include -I../.. \
# 	-o output/pjmedia-videodev-x86_64-unknown-linux-gnu/opengl_dev.o \
# 	../src/pjmedia-videodev/opengl_dev.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1   -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1        -I/home/vsedyshev/Work/1111/pjproject/third_party/build/speex -I/home/vsedyshev/Work/1111/pjproject/third_party/speex/include -DPJMEDIA_HAS_OPENCORE_AMRNB_CODEC=0 -DPJMEDIA_HAS_OPENCORE_AMRWB_CODEC=0 -I/home/vsedyshev/Work/1111/pjproject/third_party/build/srtp -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/crypto/include -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/include -DPJMEDIA_RESAMPLE_IMP=PJMEDIA_RESAMPLE_LIBRESAMPLE -DPJMEDIA_HAS_LIBYUV=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/yuv/include -DPJMEDIA_HAS_WEBRTC_AEC=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/webrtc/src -DPJMEDIA_AUDIO_DEV_HAS_ALSA=1 -DPJMEDIA_AUDIO_DEV_HAS_PORTAUDIO=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjmedia/include -I../../pjnath/include -I../.. \
# 	-o output/pjmedia-videodev-x86_64-unknown-linux-gnu/util.o \
# 	../src/pjmedia-videodev/util.c 
# if test ! -d ../lib; then mkdir -p ../lib; fi
# ar rv ../lib/libpjmedia-videodev-x86_64-unknown-linux-gnu.a  output/pjmedia-videodev-x86_64-unknown-linux-gnu/sdl_dev.o  output/pjmedia-videodev-x86_64-unknown-linux-gnu/videodev.o  output/pjmedia-videodev-x86_64-unknown-linux-gnu/errno.o  output/pjmedia-videodev-x86_64-unknown-linux-gnu/avi_dev.o  output/pjmedia-videodev-x86_64-unknown-linux-gnu/ffmpeg_dev.o  output/pjmedia-videodev-x86_64-unknown-linux-gnu/colorbar_dev.o  output/pjmedia-videodev-x86_64-unknown-linux-gnu/v4l2_dev.o  output/pjmedia-videodev-x86_64-unknown-linux-gnu/opengl_dev.o  output/pjmedia-videodev-x86_64-unknown-linux-gnu/util.o
# r - output/pjmedia-videodev-x86_64-unknown-linux-gnu/sdl_dev.o
# r - output/pjmedia-videodev-x86_64-unknown-linux-gnu/videodev.o
# r - output/pjmedia-videodev-x86_64-unknown-linux-gnu/errno.o
# r - output/pjmedia-videodev-x86_64-unknown-linux-gnu/avi_dev.o
# r - output/pjmedia-videodev-x86_64-unknown-linux-gnu/ffmpeg_dev.o
# r - output/pjmedia-videodev-x86_64-unknown-linux-gnu/colorbar_dev.o
# r - output/pjmedia-videodev-x86_64-unknown-linux-gnu/v4l2_dev.o
# r - output/pjmedia-videodev-x86_64-unknown-linux-gnu/opengl_dev.o
# r - output/pjmedia-videodev-x86_64-unknown-linux-gnu/util.o
# ranlib ../lib/libpjmedia-videodev-x86_64-unknown-linux-gnu.a
# make[2]: Leaving directory '/home/vsedyshev/Work/1111/pjproject/pjmedia/build'
# make -f /home/vsedyshev/Work/1111/pjproject/build/rules.mak APP=PJMEDIA_AUDIODEV app=pjmedia-audiodev ../lib/libpjmedia-audiodev-x86_64-unknown-linux-gnu.a
# make[2]: Entering directory '/home/vsedyshev/Work/1111/pjproject/pjmedia/build'
# mkdir -p output/pjmedia-audiodev-x86_64-unknown-linux-gnu/
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1   -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1        -I/home/vsedyshev/Work/1111/pjproject/third_party/build/speex -I/home/vsedyshev/Work/1111/pjproject/third_party/speex/include -DPJMEDIA_HAS_OPENCORE_AMRNB_CODEC=0 -DPJMEDIA_HAS_OPENCORE_AMRWB_CODEC=0 -I/home/vsedyshev/Work/1111/pjproject/third_party/build/srtp -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/crypto/include -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/include -DPJMEDIA_RESAMPLE_IMP=PJMEDIA_RESAMPLE_LIBRESAMPLE -DPJMEDIA_HAS_LIBYUV=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/yuv/include -DPJMEDIA_HAS_WEBRTC_AEC=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/webrtc/src -DPJMEDIA_AUDIO_DEV_HAS_ALSA=1 -DPJMEDIA_AUDIO_DEV_HAS_PORTAUDIO=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjmedia/include -I../../pjnath/include -I../.. \
# 	-o output/pjmedia-audiodev-x86_64-unknown-linux-gnu/audiodev.o \
# 	../src/pjmedia-audiodev/audiodev.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1   -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1        -I/home/vsedyshev/Work/1111/pjproject/third_party/build/speex -I/home/vsedyshev/Work/1111/pjproject/third_party/speex/include -DPJMEDIA_HAS_OPENCORE_AMRNB_CODEC=0 -DPJMEDIA_HAS_OPENCORE_AMRWB_CODEC=0 -I/home/vsedyshev/Work/1111/pjproject/third_party/build/srtp -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/crypto/include -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/include -DPJMEDIA_RESAMPLE_IMP=PJMEDIA_RESAMPLE_LIBRESAMPLE -DPJMEDIA_HAS_LIBYUV=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/yuv/include -DPJMEDIA_HAS_WEBRTC_AEC=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/webrtc/src -DPJMEDIA_AUDIO_DEV_HAS_ALSA=1 -DPJMEDIA_AUDIO_DEV_HAS_PORTAUDIO=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjmedia/include -I../../pjnath/include -I../.. \
# 	-o output/pjmedia-audiodev-x86_64-unknown-linux-gnu/audiotest.o \
# 	../src/pjmedia-audiodev/audiotest.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1   -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1        -I/home/vsedyshev/Work/1111/pjproject/third_party/build/speex -I/home/vsedyshev/Work/1111/pjproject/third_party/speex/include -DPJMEDIA_HAS_OPENCORE_AMRNB_CODEC=0 -DPJMEDIA_HAS_OPENCORE_AMRWB_CODEC=0 -I/home/vsedyshev/Work/1111/pjproject/third_party/build/srtp -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/crypto/include -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/include -DPJMEDIA_RESAMPLE_IMP=PJMEDIA_RESAMPLE_LIBRESAMPLE -DPJMEDIA_HAS_LIBYUV=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/yuv/include -DPJMEDIA_HAS_WEBRTC_AEC=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/webrtc/src -DPJMEDIA_AUDIO_DEV_HAS_ALSA=1 -DPJMEDIA_AUDIO_DEV_HAS_PORTAUDIO=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjmedia/include -I../../pjnath/include -I../.. \
# 	-o output/pjmedia-audiodev-x86_64-unknown-linux-gnu/errno.o \
# 	../src/pjmedia-audiodev/errno.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1   -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1        -I/home/vsedyshev/Work/1111/pjproject/third_party/build/speex -I/home/vsedyshev/Work/1111/pjproject/third_party/speex/include -DPJMEDIA_HAS_OPENCORE_AMRNB_CODEC=0 -DPJMEDIA_HAS_OPENCORE_AMRWB_CODEC=0 -I/home/vsedyshev/Work/1111/pjproject/third_party/build/srtp -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/crypto/include -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/include -DPJMEDIA_RESAMPLE_IMP=PJMEDIA_RESAMPLE_LIBRESAMPLE -DPJMEDIA_HAS_LIBYUV=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/yuv/include -DPJMEDIA_HAS_WEBRTC_AEC=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/webrtc/src -DPJMEDIA_AUDIO_DEV_HAS_ALSA=1 -DPJMEDIA_AUDIO_DEV_HAS_PORTAUDIO=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjmedia/include -I../../pjnath/include -I../.. \
# 	-o output/pjmedia-audiodev-x86_64-unknown-linux-gnu/legacy_dev.o \
# 	../src/pjmedia-audiodev/legacy_dev.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1   -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1        -I/home/vsedyshev/Work/1111/pjproject/third_party/build/speex -I/home/vsedyshev/Work/1111/pjproject/third_party/speex/include -DPJMEDIA_HAS_OPENCORE_AMRNB_CODEC=0 -DPJMEDIA_HAS_OPENCORE_AMRWB_CODEC=0 -I/home/vsedyshev/Work/1111/pjproject/third_party/build/srtp -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/crypto/include -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/include -DPJMEDIA_RESAMPLE_IMP=PJMEDIA_RESAMPLE_LIBRESAMPLE -DPJMEDIA_HAS_LIBYUV=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/yuv/include -DPJMEDIA_HAS_WEBRTC_AEC=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/webrtc/src -DPJMEDIA_AUDIO_DEV_HAS_ALSA=1 -DPJMEDIA_AUDIO_DEV_HAS_PORTAUDIO=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjmedia/include -I../../pjnath/include -I../.. \
# 	-o output/pjmedia-audiodev-x86_64-unknown-linux-gnu/null_dev.o \
# 	../src/pjmedia-audiodev/null_dev.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1   -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1        -I/home/vsedyshev/Work/1111/pjproject/third_party/build/speex -I/home/vsedyshev/Work/1111/pjproject/third_party/speex/include -DPJMEDIA_HAS_OPENCORE_AMRNB_CODEC=0 -DPJMEDIA_HAS_OPENCORE_AMRWB_CODEC=0 -I/home/vsedyshev/Work/1111/pjproject/third_party/build/srtp -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/crypto/include -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/include -DPJMEDIA_RESAMPLE_IMP=PJMEDIA_RESAMPLE_LIBRESAMPLE -DPJMEDIA_HAS_LIBYUV=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/yuv/include -DPJMEDIA_HAS_WEBRTC_AEC=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/webrtc/src -DPJMEDIA_AUDIO_DEV_HAS_ALSA=1 -DPJMEDIA_AUDIO_DEV_HAS_PORTAUDIO=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjmedia/include -I../../pjnath/include -I../.. \
# 	-o output/pjmedia-audiodev-x86_64-unknown-linux-gnu/pa_dev.o \
# 	../src/pjmedia-audiodev/pa_dev.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1   -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1        -I/home/vsedyshev/Work/1111/pjproject/third_party/build/speex -I/home/vsedyshev/Work/1111/pjproject/third_party/speex/include -DPJMEDIA_HAS_OPENCORE_AMRNB_CODEC=0 -DPJMEDIA_HAS_OPENCORE_AMRWB_CODEC=0 -I/home/vsedyshev/Work/1111/pjproject/third_party/build/srtp -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/crypto/include -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/include -DPJMEDIA_RESAMPLE_IMP=PJMEDIA_RESAMPLE_LIBRESAMPLE -DPJMEDIA_HAS_LIBYUV=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/yuv/include -DPJMEDIA_HAS_WEBRTC_AEC=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/webrtc/src -DPJMEDIA_AUDIO_DEV_HAS_ALSA=1 -DPJMEDIA_AUDIO_DEV_HAS_PORTAUDIO=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjmedia/include -I../../pjnath/include -I../.. \
# 	-o output/pjmedia-audiodev-x86_64-unknown-linux-gnu/wmme_dev.o \
# 	../src/pjmedia-audiodev/wmme_dev.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1   -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1        -I/home/vsedyshev/Work/1111/pjproject/third_party/build/speex -I/home/vsedyshev/Work/1111/pjproject/third_party/speex/include -DPJMEDIA_HAS_OPENCORE_AMRNB_CODEC=0 -DPJMEDIA_HAS_OPENCORE_AMRWB_CODEC=0 -I/home/vsedyshev/Work/1111/pjproject/third_party/build/srtp -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/crypto/include -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/include -DPJMEDIA_RESAMPLE_IMP=PJMEDIA_RESAMPLE_LIBRESAMPLE -DPJMEDIA_HAS_LIBYUV=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/yuv/include -DPJMEDIA_HAS_WEBRTC_AEC=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/webrtc/src -DPJMEDIA_AUDIO_DEV_HAS_ALSA=1 -DPJMEDIA_AUDIO_DEV_HAS_PORTAUDIO=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjmedia/include -I../../pjnath/include -I../.. \
# 	-o output/pjmedia-audiodev-x86_64-unknown-linux-gnu/alsa_dev.o \
# 	../src/pjmedia-audiodev/alsa_dev.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1   -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1        -I/home/vsedyshev/Work/1111/pjproject/third_party/build/speex -I/home/vsedyshev/Work/1111/pjproject/third_party/speex/include -DPJMEDIA_HAS_OPENCORE_AMRNB_CODEC=0 -DPJMEDIA_HAS_OPENCORE_AMRWB_CODEC=0 -I/home/vsedyshev/Work/1111/pjproject/third_party/build/srtp -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/crypto/include -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/include -DPJMEDIA_RESAMPLE_IMP=PJMEDIA_RESAMPLE_LIBRESAMPLE -DPJMEDIA_HAS_LIBYUV=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/yuv/include -DPJMEDIA_HAS_WEBRTC_AEC=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/webrtc/src -DPJMEDIA_AUDIO_DEV_HAS_ALSA=1 -DPJMEDIA_AUDIO_DEV_HAS_PORTAUDIO=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjmedia/include -I../../pjnath/include -I../.. \
# 	-o output/pjmedia-audiodev-x86_64-unknown-linux-gnu/bb10_dev.o \
# 	../src/pjmedia-audiodev/bb10_dev.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1   -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1        -I/home/vsedyshev/Work/1111/pjproject/third_party/build/speex -I/home/vsedyshev/Work/1111/pjproject/third_party/speex/include -DPJMEDIA_HAS_OPENCORE_AMRNB_CODEC=0 -DPJMEDIA_HAS_OPENCORE_AMRWB_CODEC=0 -I/home/vsedyshev/Work/1111/pjproject/third_party/build/srtp -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/crypto/include -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/include -DPJMEDIA_RESAMPLE_IMP=PJMEDIA_RESAMPLE_LIBRESAMPLE -DPJMEDIA_HAS_LIBYUV=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/yuv/include -DPJMEDIA_HAS_WEBRTC_AEC=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/webrtc/src -DPJMEDIA_AUDIO_DEV_HAS_ALSA=1 -DPJMEDIA_AUDIO_DEV_HAS_PORTAUDIO=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjmedia/include -I../../pjnath/include -I../.. \
# 	-o output/pjmedia-audiodev-x86_64-unknown-linux-gnu/bdimad_dev.o \
# 	../src/pjmedia-audiodev/bdimad_dev.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1   -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1        -I/home/vsedyshev/Work/1111/pjproject/third_party/build/speex -I/home/vsedyshev/Work/1111/pjproject/third_party/speex/include -DPJMEDIA_HAS_OPENCORE_AMRNB_CODEC=0 -DPJMEDIA_HAS_OPENCORE_AMRWB_CODEC=0 -I/home/vsedyshev/Work/1111/pjproject/third_party/build/srtp -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/crypto/include -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/include -DPJMEDIA_RESAMPLE_IMP=PJMEDIA_RESAMPLE_LIBRESAMPLE -DPJMEDIA_HAS_LIBYUV=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/yuv/include -DPJMEDIA_HAS_WEBRTC_AEC=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/webrtc/src -DPJMEDIA_AUDIO_DEV_HAS_ALSA=1 -DPJMEDIA_AUDIO_DEV_HAS_PORTAUDIO=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjmedia/include -I../../pjnath/include -I../.. \
# 	-o output/pjmedia-audiodev-x86_64-unknown-linux-gnu/android_jni_dev.o \
# 	../src/pjmedia-audiodev/android_jni_dev.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1   -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1        -I/home/vsedyshev/Work/1111/pjproject/third_party/build/speex -I/home/vsedyshev/Work/1111/pjproject/third_party/speex/include -DPJMEDIA_HAS_OPENCORE_AMRNB_CODEC=0 -DPJMEDIA_HAS_OPENCORE_AMRWB_CODEC=0 -I/home/vsedyshev/Work/1111/pjproject/third_party/build/srtp -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/crypto/include -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/include -DPJMEDIA_RESAMPLE_IMP=PJMEDIA_RESAMPLE_LIBRESAMPLE -DPJMEDIA_HAS_LIBYUV=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/yuv/include -DPJMEDIA_HAS_WEBRTC_AEC=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/webrtc/src -DPJMEDIA_AUDIO_DEV_HAS_ALSA=1 -DPJMEDIA_AUDIO_DEV_HAS_PORTAUDIO=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjmedia/include -I../../pjnath/include -I../.. \
# 	-o output/pjmedia-audiodev-x86_64-unknown-linux-gnu/opensl_dev.o \
# 	../src/pjmedia-audiodev/opensl_dev.c 
# if test ! -d ../lib; then mkdir -p ../lib; fi
# ar rv ../lib/libpjmedia-audiodev-x86_64-unknown-linux-gnu.a  output/pjmedia-audiodev-x86_64-unknown-linux-gnu/audiodev.o  output/pjmedia-audiodev-x86_64-unknown-linux-gnu/audiotest.o  output/pjmedia-audiodev-x86_64-unknown-linux-gnu/errno.o  output/pjmedia-audiodev-x86_64-unknown-linux-gnu/legacy_dev.o  output/pjmedia-audiodev-x86_64-unknown-linux-gnu/null_dev.o  output/pjmedia-audiodev-x86_64-unknown-linux-gnu/pa_dev.o  output/pjmedia-audiodev-x86_64-unknown-linux-gnu/wmme_dev.o  output/pjmedia-audiodev-x86_64-unknown-linux-gnu/alsa_dev.o  output/pjmedia-audiodev-x86_64-unknown-linux-gnu/bb10_dev.o  output/pjmedia-audiodev-x86_64-unknown-linux-gnu/bdimad_dev.o  output/pjmedia-audiodev-x86_64-unknown-linux-gnu/android_jni_dev.o  output/pjmedia-audiodev-x86_64-unknown-linux-gnu/opensl_dev.o
# r - output/pjmedia-audiodev-x86_64-unknown-linux-gnu/audiodev.o
# r - output/pjmedia-audiodev-x86_64-unknown-linux-gnu/audiotest.o
# r - output/pjmedia-audiodev-x86_64-unknown-linux-gnu/errno.o
# r - output/pjmedia-audiodev-x86_64-unknown-linux-gnu/legacy_dev.o
# r - output/pjmedia-audiodev-x86_64-unknown-linux-gnu/null_dev.o
# r - output/pjmedia-audiodev-x86_64-unknown-linux-gnu/pa_dev.o
# r - output/pjmedia-audiodev-x86_64-unknown-linux-gnu/wmme_dev.o
# r - output/pjmedia-audiodev-x86_64-unknown-linux-gnu/alsa_dev.o
# r - output/pjmedia-audiodev-x86_64-unknown-linux-gnu/bb10_dev.o
# r - output/pjmedia-audiodev-x86_64-unknown-linux-gnu/bdimad_dev.o
# r - output/pjmedia-audiodev-x86_64-unknown-linux-gnu/android_jni_dev.o
# r - output/pjmedia-audiodev-x86_64-unknown-linux-gnu/opensl_dev.o
# ranlib ../lib/libpjmedia-audiodev-x86_64-unknown-linux-gnu.a
# make[2]: Leaving directory '/home/vsedyshev/Work/1111/pjproject/pjmedia/build'
# make -f /home/vsedyshev/Work/1111/pjproject/build/rules.mak APP=PJSDP app=pjsdp ../lib/libpjsdp-x86_64-unknown-linux-gnu.a
# make[2]: Entering directory '/home/vsedyshev/Work/1111/pjproject/pjmedia/build'
# mkdir -p output/pjsdp-x86_64-unknown-linux-gnu/
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1   -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1        -I/home/vsedyshev/Work/1111/pjproject/third_party/build/speex -I/home/vsedyshev/Work/1111/pjproject/third_party/speex/include -DPJMEDIA_HAS_OPENCORE_AMRNB_CODEC=0 -DPJMEDIA_HAS_OPENCORE_AMRWB_CODEC=0 -I/home/vsedyshev/Work/1111/pjproject/third_party/build/srtp -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/crypto/include -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/include -DPJMEDIA_RESAMPLE_IMP=PJMEDIA_RESAMPLE_LIBRESAMPLE -DPJMEDIA_HAS_LIBYUV=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/yuv/include -DPJMEDIA_HAS_WEBRTC_AEC=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/webrtc/src -DPJMEDIA_AUDIO_DEV_HAS_ALSA=1 -DPJMEDIA_AUDIO_DEV_HAS_PORTAUDIO=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjmedia/include -I../../pjnath/include -I../.. \
# 	-o output/pjsdp-x86_64-unknown-linux-gnu/errno.o \
# 	../src/pjmedia/errno.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1   -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1        -I/home/vsedyshev/Work/1111/pjproject/third_party/build/speex -I/home/vsedyshev/Work/1111/pjproject/third_party/speex/include -DPJMEDIA_HAS_OPENCORE_AMRNB_CODEC=0 -DPJMEDIA_HAS_OPENCORE_AMRWB_CODEC=0 -I/home/vsedyshev/Work/1111/pjproject/third_party/build/srtp -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/crypto/include -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/include -DPJMEDIA_RESAMPLE_IMP=PJMEDIA_RESAMPLE_LIBRESAMPLE -DPJMEDIA_HAS_LIBYUV=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/yuv/include -DPJMEDIA_HAS_WEBRTC_AEC=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/webrtc/src -DPJMEDIA_AUDIO_DEV_HAS_ALSA=1 -DPJMEDIA_AUDIO_DEV_HAS_PORTAUDIO=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjmedia/include -I../../pjnath/include -I../.. \
# 	-o output/pjsdp-x86_64-unknown-linux-gnu/sdp.o \
# 	../src/pjmedia/sdp.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1   -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1        -I/home/vsedyshev/Work/1111/pjproject/third_party/build/speex -I/home/vsedyshev/Work/1111/pjproject/third_party/speex/include -DPJMEDIA_HAS_OPENCORE_AMRNB_CODEC=0 -DPJMEDIA_HAS_OPENCORE_AMRWB_CODEC=0 -I/home/vsedyshev/Work/1111/pjproject/third_party/build/srtp -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/crypto/include -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/include -DPJMEDIA_RESAMPLE_IMP=PJMEDIA_RESAMPLE_LIBRESAMPLE -DPJMEDIA_HAS_LIBYUV=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/yuv/include -DPJMEDIA_HAS_WEBRTC_AEC=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/webrtc/src -DPJMEDIA_AUDIO_DEV_HAS_ALSA=1 -DPJMEDIA_AUDIO_DEV_HAS_PORTAUDIO=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjmedia/include -I../../pjnath/include -I../.. \
# 	-o output/pjsdp-x86_64-unknown-linux-gnu/sdp_cmp.o \
# 	../src/pjmedia/sdp_cmp.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1   -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1        -I/home/vsedyshev/Work/1111/pjproject/third_party/build/speex -I/home/vsedyshev/Work/1111/pjproject/third_party/speex/include -DPJMEDIA_HAS_OPENCORE_AMRNB_CODEC=0 -DPJMEDIA_HAS_OPENCORE_AMRWB_CODEC=0 -I/home/vsedyshev/Work/1111/pjproject/third_party/build/srtp -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/crypto/include -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/include -DPJMEDIA_RESAMPLE_IMP=PJMEDIA_RESAMPLE_LIBRESAMPLE -DPJMEDIA_HAS_LIBYUV=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/yuv/include -DPJMEDIA_HAS_WEBRTC_AEC=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/webrtc/src -DPJMEDIA_AUDIO_DEV_HAS_ALSA=1 -DPJMEDIA_AUDIO_DEV_HAS_PORTAUDIO=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjmedia/include -I../../pjnath/include -I../.. \
# 	-o output/pjsdp-x86_64-unknown-linux-gnu/sdp_neg.o \
# 	../src/pjmedia/sdp_neg.c 
# if test ! -d ../lib; then mkdir -p ../lib; fi
# ar rv ../lib/libpjsdp-x86_64-unknown-linux-gnu.a  output/pjsdp-x86_64-unknown-linux-gnu/errno.o  output/pjsdp-x86_64-unknown-linux-gnu/sdp.o  output/pjsdp-x86_64-unknown-linux-gnu/sdp_cmp.o  output/pjsdp-x86_64-unknown-linux-gnu/sdp_neg.o
# r - output/pjsdp-x86_64-unknown-linux-gnu/errno.o
# r - output/pjsdp-x86_64-unknown-linux-gnu/sdp.o
# r - output/pjsdp-x86_64-unknown-linux-gnu/sdp_cmp.o
# r - output/pjsdp-x86_64-unknown-linux-gnu/sdp_neg.o
# ranlib ../lib/libpjsdp-x86_64-unknown-linux-gnu.a
# make[2]: Leaving directory '/home/vsedyshev/Work/1111/pjproject/pjmedia/build'
# make -f /home/vsedyshev/Work/1111/pjproject/build/rules.mak APP=PJMEDIA_TEST app=pjmedia-test ../bin/pjmedia-test-x86_64-unknown-linux-gnu
# make[2]: Entering directory '/home/vsedyshev/Work/1111/pjproject/pjmedia/build'
# mkdir -p output/pjmedia-test-x86_64-unknown-linux-gnu/
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1   -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1        -I/home/vsedyshev/Work/1111/pjproject/third_party/build/speex -I/home/vsedyshev/Work/1111/pjproject/third_party/speex/include -DPJMEDIA_HAS_OPENCORE_AMRNB_CODEC=0 -DPJMEDIA_HAS_OPENCORE_AMRWB_CODEC=0 -I/home/vsedyshev/Work/1111/pjproject/third_party/build/srtp -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/crypto/include -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/include -DPJMEDIA_RESAMPLE_IMP=PJMEDIA_RESAMPLE_LIBRESAMPLE -DPJMEDIA_HAS_LIBYUV=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/yuv/include -DPJMEDIA_HAS_WEBRTC_AEC=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/webrtc/src -DPJMEDIA_AUDIO_DEV_HAS_ALSA=1 -DPJMEDIA_AUDIO_DEV_HAS_PORTAUDIO=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjmedia/include -I../../pjnath/include -I../.. \
# 	-o output/pjmedia-test-x86_64-unknown-linux-gnu/codec_vectors.o \
# 	../src/test/codec_vectors.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1   -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1        -I/home/vsedyshev/Work/1111/pjproject/third_party/build/speex -I/home/vsedyshev/Work/1111/pjproject/third_party/speex/include -DPJMEDIA_HAS_OPENCORE_AMRNB_CODEC=0 -DPJMEDIA_HAS_OPENCORE_AMRWB_CODEC=0 -I/home/vsedyshev/Work/1111/pjproject/third_party/build/srtp -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/crypto/include -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/include -DPJMEDIA_RESAMPLE_IMP=PJMEDIA_RESAMPLE_LIBRESAMPLE -DPJMEDIA_HAS_LIBYUV=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/yuv/include -DPJMEDIA_HAS_WEBRTC_AEC=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/webrtc/src -DPJMEDIA_AUDIO_DEV_HAS_ALSA=1 -DPJMEDIA_AUDIO_DEV_HAS_PORTAUDIO=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjmedia/include -I../../pjnath/include -I../.. \
# 	-o output/pjmedia-test-x86_64-unknown-linux-gnu/jbuf_test.o \
# 	../src/test/jbuf_test.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1   -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1        -I/home/vsedyshev/Work/1111/pjproject/third_party/build/speex -I/home/vsedyshev/Work/1111/pjproject/third_party/speex/include -DPJMEDIA_HAS_OPENCORE_AMRNB_CODEC=0 -DPJMEDIA_HAS_OPENCORE_AMRWB_CODEC=0 -I/home/vsedyshev/Work/1111/pjproject/third_party/build/srtp -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/crypto/include -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/include -DPJMEDIA_RESAMPLE_IMP=PJMEDIA_RESAMPLE_LIBRESAMPLE -DPJMEDIA_HAS_LIBYUV=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/yuv/include -DPJMEDIA_HAS_WEBRTC_AEC=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/webrtc/src -DPJMEDIA_AUDIO_DEV_HAS_ALSA=1 -DPJMEDIA_AUDIO_DEV_HAS_PORTAUDIO=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjmedia/include -I../../pjnath/include -I../.. \
# 	-o output/pjmedia-test-x86_64-unknown-linux-gnu/main.o \
# 	../src/test/main.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1   -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1        -I/home/vsedyshev/Work/1111/pjproject/third_party/build/speex -I/home/vsedyshev/Work/1111/pjproject/third_party/speex/include -DPJMEDIA_HAS_OPENCORE_AMRNB_CODEC=0 -DPJMEDIA_HAS_OPENCORE_AMRWB_CODEC=0 -I/home/vsedyshev/Work/1111/pjproject/third_party/build/srtp -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/crypto/include -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/include -DPJMEDIA_RESAMPLE_IMP=PJMEDIA_RESAMPLE_LIBRESAMPLE -DPJMEDIA_HAS_LIBYUV=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/yuv/include -DPJMEDIA_HAS_WEBRTC_AEC=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/webrtc/src -DPJMEDIA_AUDIO_DEV_HAS_ALSA=1 -DPJMEDIA_AUDIO_DEV_HAS_PORTAUDIO=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjmedia/include -I../../pjnath/include -I../.. \
# 	-o output/pjmedia-test-x86_64-unknown-linux-gnu/mips_test.o \
# 	../src/test/mips_test.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1   -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1        -I/home/vsedyshev/Work/1111/pjproject/third_party/build/speex -I/home/vsedyshev/Work/1111/pjproject/third_party/speex/include -DPJMEDIA_HAS_OPENCORE_AMRNB_CODEC=0 -DPJMEDIA_HAS_OPENCORE_AMRWB_CODEC=0 -I/home/vsedyshev/Work/1111/pjproject/third_party/build/srtp -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/crypto/include -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/include -DPJMEDIA_RESAMPLE_IMP=PJMEDIA_RESAMPLE_LIBRESAMPLE -DPJMEDIA_HAS_LIBYUV=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/yuv/include -DPJMEDIA_HAS_WEBRTC_AEC=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/webrtc/src -DPJMEDIA_AUDIO_DEV_HAS_ALSA=1 -DPJMEDIA_AUDIO_DEV_HAS_PORTAUDIO=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjmedia/include -I../../pjnath/include -I../.. \
# 	-o output/pjmedia-test-x86_64-unknown-linux-gnu/vid_codec_test.o \
# 	../src/test/vid_codec_test.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1   -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1        -I/home/vsedyshev/Work/1111/pjproject/third_party/build/speex -I/home/vsedyshev/Work/1111/pjproject/third_party/speex/include -DPJMEDIA_HAS_OPENCORE_AMRNB_CODEC=0 -DPJMEDIA_HAS_OPENCORE_AMRWB_CODEC=0 -I/home/vsedyshev/Work/1111/pjproject/third_party/build/srtp -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/crypto/include -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/include -DPJMEDIA_RESAMPLE_IMP=PJMEDIA_RESAMPLE_LIBRESAMPLE -DPJMEDIA_HAS_LIBYUV=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/yuv/include -DPJMEDIA_HAS_WEBRTC_AEC=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/webrtc/src -DPJMEDIA_AUDIO_DEV_HAS_ALSA=1 -DPJMEDIA_AUDIO_DEV_HAS_PORTAUDIO=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjmedia/include -I../../pjnath/include -I../.. \
# 	-o output/pjmedia-test-x86_64-unknown-linux-gnu/vid_dev_test.o \
# 	../src/test/vid_dev_test.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1   -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1        -I/home/vsedyshev/Work/1111/pjproject/third_party/build/speex -I/home/vsedyshev/Work/1111/pjproject/third_party/speex/include -DPJMEDIA_HAS_OPENCORE_AMRNB_CODEC=0 -DPJMEDIA_HAS_OPENCORE_AMRWB_CODEC=0 -I/home/vsedyshev/Work/1111/pjproject/third_party/build/srtp -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/crypto/include -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/include -DPJMEDIA_RESAMPLE_IMP=PJMEDIA_RESAMPLE_LIBRESAMPLE -DPJMEDIA_HAS_LIBYUV=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/yuv/include -DPJMEDIA_HAS_WEBRTC_AEC=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/webrtc/src -DPJMEDIA_AUDIO_DEV_HAS_ALSA=1 -DPJMEDIA_AUDIO_DEV_HAS_PORTAUDIO=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjmedia/include -I../../pjnath/include -I../.. \
# 	-o output/pjmedia-test-x86_64-unknown-linux-gnu/vid_port_test.o \
# 	../src/test/vid_port_test.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1   -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1        -I/home/vsedyshev/Work/1111/pjproject/third_party/build/speex -I/home/vsedyshev/Work/1111/pjproject/third_party/speex/include -DPJMEDIA_HAS_OPENCORE_AMRNB_CODEC=0 -DPJMEDIA_HAS_OPENCORE_AMRWB_CODEC=0 -I/home/vsedyshev/Work/1111/pjproject/third_party/build/srtp -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/crypto/include -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/include -DPJMEDIA_RESAMPLE_IMP=PJMEDIA_RESAMPLE_LIBRESAMPLE -DPJMEDIA_HAS_LIBYUV=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/yuv/include -DPJMEDIA_HAS_WEBRTC_AEC=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/webrtc/src -DPJMEDIA_AUDIO_DEV_HAS_ALSA=1 -DPJMEDIA_AUDIO_DEV_HAS_PORTAUDIO=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjmedia/include -I../../pjnath/include -I../.. \
# 	-o output/pjmedia-test-x86_64-unknown-linux-gnu/rtp_test.o \
# 	../src/test/rtp_test.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1   -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1        -I/home/vsedyshev/Work/1111/pjproject/third_party/build/speex -I/home/vsedyshev/Work/1111/pjproject/third_party/speex/include -DPJMEDIA_HAS_OPENCORE_AMRNB_CODEC=0 -DPJMEDIA_HAS_OPENCORE_AMRWB_CODEC=0 -I/home/vsedyshev/Work/1111/pjproject/third_party/build/srtp -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/crypto/include -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/include -DPJMEDIA_RESAMPLE_IMP=PJMEDIA_RESAMPLE_LIBRESAMPLE -DPJMEDIA_HAS_LIBYUV=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/yuv/include -DPJMEDIA_HAS_WEBRTC_AEC=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/webrtc/src -DPJMEDIA_AUDIO_DEV_HAS_ALSA=1 -DPJMEDIA_AUDIO_DEV_HAS_PORTAUDIO=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjmedia/include -I../../pjnath/include -I../.. \
# 	-o output/pjmedia-test-x86_64-unknown-linux-gnu/test.o \
# 	../src/test/test.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1   -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1        -I/home/vsedyshev/Work/1111/pjproject/third_party/build/speex -I/home/vsedyshev/Work/1111/pjproject/third_party/speex/include -DPJMEDIA_HAS_OPENCORE_AMRNB_CODEC=0 -DPJMEDIA_HAS_OPENCORE_AMRWB_CODEC=0 -I/home/vsedyshev/Work/1111/pjproject/third_party/build/srtp -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/crypto/include -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/include -DPJMEDIA_RESAMPLE_IMP=PJMEDIA_RESAMPLE_LIBRESAMPLE -DPJMEDIA_HAS_LIBYUV=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/yuv/include -DPJMEDIA_HAS_WEBRTC_AEC=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/webrtc/src -DPJMEDIA_AUDIO_DEV_HAS_ALSA=1 -DPJMEDIA_AUDIO_DEV_HAS_PORTAUDIO=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjmedia/include -I../../pjnath/include -I../.. \
# 	-o output/pjmedia-test-x86_64-unknown-linux-gnu/sdp_neg_test.o \
# 	../src/test/sdp_neg_test.c 
# if test ! -d ../bin; then mkdir -p ../bin; fi
# gcc -o ../bin/pjmedia-test-x86_64-unknown-linux-gnu \
#      output/pjmedia-test-x86_64-unknown-linux-gnu/codec_vectors.o  output/pjmedia-test-x86_64-unknown-linux-gnu/jbuf_test.o  output/pjmedia-test-x86_64-unknown-linux-gnu/main.o  output/pjmedia-test-x86_64-unknown-linux-gnu/mips_test.o  output/pjmedia-test-x86_64-unknown-linux-gnu/vid_codec_test.o  output/pjmedia-test-x86_64-unknown-linux-gnu/vid_dev_test.o  output/pjmedia-test-x86_64-unknown-linux-gnu/vid_port_test.o  output/pjmedia-test-x86_64-unknown-linux-gnu/rtp_test.o  output/pjmedia-test-x86_64-unknown-linux-gnu/test.o  output/pjmedia-test-x86_64-unknown-linux-gnu/sdp_neg_test.o -lpjmedia-codec-x86_64-unknown-linux-gnu -lpjmedia-videodev-x86_64-unknown-linux-gnu -lpjmedia-audiodev-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjnath-x86_64-unknown-linux-gnu -lpjlib-util-x86_64-unknown-linux-gnu -lpj-x86_64-unknown-linux-gnu  -lsrtp-x86_64-unknown-linux-gnu -lresample-x86_64-unknown-linux-gnu -lgsmcodec-x86_64-unknown-linux-gnu -lspeex-x86_64-unknown-linux-gnu -lilbccodec-x86_64-unknown-linux-gnu -lg7221codec-x86_64-unknown-linux-gnu -lyuv-x86_64-unknown-linux-gnu -lwebrtc-x86_64-unknown-linux-gnu   -lssl -lcrypto -luuid -lm -lrt -lpthread  -lasound -lSDL2     -L/home/vsedyshev/Work/1111/pjproject/pjlib/lib -L/home/vsedyshev/Work/1111/pjproject/pjlib-util/lib -L/home/vsedyshev/Work/1111/pjproject/pjnath/lib -L/home/vsedyshev/Work/1111/pjproject/pjmedia/lib -L/home/vsedyshev/Work/1111/pjproject/pjsip/lib -L/home/vsedyshev/Work/1111/pjproject/third_party/lib -lSDL2     -lSDL2      -lSDL2     
# make[2]: Leaving directory '/home/vsedyshev/Work/1111/pjproject/pjmedia/build'
# make[1]: Leaving directory '/home/vsedyshev/Work/1111/pjproject/pjmedia/build'
# make[1]: Entering directory '/home/vsedyshev/Work/1111/pjproject/pjsip/build'
# make -f /home/vsedyshev/Work/1111/pjproject/build/rules.mak APP=PJSIP app=pjsip ../lib/libpjsip-x86_64-unknown-linux-gnu.a
# make[2]: Entering directory '/home/vsedyshev/Work/1111/pjproject/pjsip/build'
# mkdir -p output/pjsip-x86_64-unknown-linux-gnu/
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjnath/include -I../../pjmedia/include \
# 	-o output/pjsip-x86_64-unknown-linux-gnu/sip_config.o \
# 	../src/pjsip/sip_config.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjnath/include -I../../pjmedia/include \
# 	-o output/pjsip-x86_64-unknown-linux-gnu/sip_multipart.o \
# 	../src/pjsip/sip_multipart.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjnath/include -I../../pjmedia/include \
# 	-o output/pjsip-x86_64-unknown-linux-gnu/sip_errno.o \
# 	../src/pjsip/sip_errno.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjnath/include -I../../pjmedia/include \
# 	-o output/pjsip-x86_64-unknown-linux-gnu/sip_msg.o \
# 	../src/pjsip/sip_msg.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjnath/include -I../../pjmedia/include \
# 	-o output/pjsip-x86_64-unknown-linux-gnu/sip_parser.o \
# 	../src/pjsip/sip_parser.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjnath/include -I../../pjmedia/include \
# 	-o output/pjsip-x86_64-unknown-linux-gnu/sip_tel_uri.o \
# 	../src/pjsip/sip_tel_uri.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjnath/include -I../../pjmedia/include \
# 	-o output/pjsip-x86_64-unknown-linux-gnu/sip_uri.o \
# 	../src/pjsip/sip_uri.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjnath/include -I../../pjmedia/include \
# 	-o output/pjsip-x86_64-unknown-linux-gnu/sip_endpoint.o \
# 	../src/pjsip/sip_endpoint.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjnath/include -I../../pjmedia/include \
# 	-o output/pjsip-x86_64-unknown-linux-gnu/sip_util.o \
# 	../src/pjsip/sip_util.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjnath/include -I../../pjmedia/include \
# 	-o output/pjsip-x86_64-unknown-linux-gnu/sip_util_proxy.o \
# 	../src/pjsip/sip_util_proxy.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjnath/include -I../../pjmedia/include \
# 	-o output/pjsip-x86_64-unknown-linux-gnu/sip_resolve.o \
# 	../src/pjsip/sip_resolve.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjnath/include -I../../pjmedia/include \
# 	-o output/pjsip-x86_64-unknown-linux-gnu/sip_transport.o \
# 	../src/pjsip/sip_transport.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjnath/include -I../../pjmedia/include \
# 	-o output/pjsip-x86_64-unknown-linux-gnu/sip_transport_loop.o \
# 	../src/pjsip/sip_transport_loop.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjnath/include -I../../pjmedia/include \
# 	-o output/pjsip-x86_64-unknown-linux-gnu/sip_transport_udp.o \
# 	../src/pjsip/sip_transport_udp.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjnath/include -I../../pjmedia/include \
# 	-o output/pjsip-x86_64-unknown-linux-gnu/sip_transport_tcp.o \
# 	../src/pjsip/sip_transport_tcp.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjnath/include -I../../pjmedia/include \
# 	-o output/pjsip-x86_64-unknown-linux-gnu/sip_transport_tls.o \
# 	../src/pjsip/sip_transport_tls.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjnath/include -I../../pjmedia/include \
# 	-o output/pjsip-x86_64-unknown-linux-gnu/sip_auth_aka.o \
# 	../src/pjsip/sip_auth_aka.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjnath/include -I../../pjmedia/include \
# 	-o output/pjsip-x86_64-unknown-linux-gnu/sip_auth_client.o \
# 	../src/pjsip/sip_auth_client.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjnath/include -I../../pjmedia/include \
# 	-o output/pjsip-x86_64-unknown-linux-gnu/sip_auth_msg.o \
# 	../src/pjsip/sip_auth_msg.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjnath/include -I../../pjmedia/include \
# 	-o output/pjsip-x86_64-unknown-linux-gnu/sip_auth_parser.o \
# 	../src/pjsip/sip_auth_parser.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjnath/include -I../../pjmedia/include \
# 	-o output/pjsip-x86_64-unknown-linux-gnu/sip_auth_server.o \
# 	../src/pjsip/sip_auth_server.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjnath/include -I../../pjmedia/include \
# 	-o output/pjsip-x86_64-unknown-linux-gnu/sip_transaction.o \
# 	../src/pjsip/sip_transaction.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjnath/include -I../../pjmedia/include \
# 	-o output/pjsip-x86_64-unknown-linux-gnu/sip_util_statefull.o \
# 	../src/pjsip/sip_util_statefull.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjnath/include -I../../pjmedia/include \
# 	-o output/pjsip-x86_64-unknown-linux-gnu/sip_dialog.o \
# 	../src/pjsip/sip_dialog.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjnath/include -I../../pjmedia/include \
# 	-o output/pjsip-x86_64-unknown-linux-gnu/sip_ua_layer.o \
# 	../src/pjsip/sip_ua_layer.c 
# if test ! -d ../lib; then mkdir -p ../lib; fi
# ar rv ../lib/libpjsip-x86_64-unknown-linux-gnu.a  output/pjsip-x86_64-unknown-linux-gnu/sip_config.o  output/pjsip-x86_64-unknown-linux-gnu/sip_multipart.o  output/pjsip-x86_64-unknown-linux-gnu/sip_errno.o  output/pjsip-x86_64-unknown-linux-gnu/sip_msg.o  output/pjsip-x86_64-unknown-linux-gnu/sip_parser.o  output/pjsip-x86_64-unknown-linux-gnu/sip_tel_uri.o  output/pjsip-x86_64-unknown-linux-gnu/sip_uri.o  output/pjsip-x86_64-unknown-linux-gnu/sip_endpoint.o  output/pjsip-x86_64-unknown-linux-gnu/sip_util.o  output/pjsip-x86_64-unknown-linux-gnu/sip_util_proxy.o  output/pjsip-x86_64-unknown-linux-gnu/sip_resolve.o  output/pjsip-x86_64-unknown-linux-gnu/sip_transport.o  output/pjsip-x86_64-unknown-linux-gnu/sip_transport_loop.o  output/pjsip-x86_64-unknown-linux-gnu/sip_transport_udp.o  output/pjsip-x86_64-unknown-linux-gnu/sip_transport_tcp.o  output/pjsip-x86_64-unknown-linux-gnu/sip_transport_tls.o  output/pjsip-x86_64-unknown-linux-gnu/sip_auth_aka.o  output/pjsip-x86_64-unknown-linux-gnu/sip_auth_client.o  output/pjsip-x86_64-unknown-linux-gnu/sip_auth_msg.o  output/pjsip-x86_64-unknown-linux-gnu/sip_auth_parser.o  output/pjsip-x86_64-unknown-linux-gnu/sip_auth_server.o  output/pjsip-x86_64-unknown-linux-gnu/sip_transaction.o  output/pjsip-x86_64-unknown-linux-gnu/sip_util_statefull.o  output/pjsip-x86_64-unknown-linux-gnu/sip_dialog.o  output/pjsip-x86_64-unknown-linux-gnu/sip_ua_layer.o
# r - output/pjsip-x86_64-unknown-linux-gnu/sip_config.o
# r - output/pjsip-x86_64-unknown-linux-gnu/sip_multipart.o
# r - output/pjsip-x86_64-unknown-linux-gnu/sip_errno.o
# r - output/pjsip-x86_64-unknown-linux-gnu/sip_msg.o
# r - output/pjsip-x86_64-unknown-linux-gnu/sip_parser.o
# r - output/pjsip-x86_64-unknown-linux-gnu/sip_tel_uri.o
# r - output/pjsip-x86_64-unknown-linux-gnu/sip_uri.o
# r - output/pjsip-x86_64-unknown-linux-gnu/sip_endpoint.o
# r - output/pjsip-x86_64-unknown-linux-gnu/sip_util.o
# r - output/pjsip-x86_64-unknown-linux-gnu/sip_util_proxy.o
# r - output/pjsip-x86_64-unknown-linux-gnu/sip_resolve.o
# r - output/pjsip-x86_64-unknown-linux-gnu/sip_transport.o
# r - output/pjsip-x86_64-unknown-linux-gnu/sip_transport_loop.o
# r - output/pjsip-x86_64-unknown-linux-gnu/sip_transport_udp.o
# r - output/pjsip-x86_64-unknown-linux-gnu/sip_transport_tcp.o
# r - output/pjsip-x86_64-unknown-linux-gnu/sip_transport_tls.o
# r - output/pjsip-x86_64-unknown-linux-gnu/sip_auth_aka.o
# r - output/pjsip-x86_64-unknown-linux-gnu/sip_auth_client.o
# r - output/pjsip-x86_64-unknown-linux-gnu/sip_auth_msg.o
# r - output/pjsip-x86_64-unknown-linux-gnu/sip_auth_parser.o
# r - output/pjsip-x86_64-unknown-linux-gnu/sip_auth_server.o
# r - output/pjsip-x86_64-unknown-linux-gnu/sip_transaction.o
# r - output/pjsip-x86_64-unknown-linux-gnu/sip_util_statefull.o
# r - output/pjsip-x86_64-unknown-linux-gnu/sip_dialog.o
# r - output/pjsip-x86_64-unknown-linux-gnu/sip_ua_layer.o
# ranlib ../lib/libpjsip-x86_64-unknown-linux-gnu.a
# make[2]: Leaving directory '/home/vsedyshev/Work/1111/pjproject/pjsip/build'
# make -f /home/vsedyshev/Work/1111/pjproject/build/rules.mak APP=PJSIP_SIMPLE app=pjsip-simple ../lib/libpjsip-simple-x86_64-unknown-linux-gnu.a
# make[2]: Entering directory '/home/vsedyshev/Work/1111/pjproject/pjsip/build'
# mkdir -p output/pjsip-simple-x86_64-unknown-linux-gnu/
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjnath/include -I../../pjmedia/include \
# 	-o output/pjsip-simple-x86_64-unknown-linux-gnu/errno.o \
# 	../src/pjsip-simple/errno.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjnath/include -I../../pjmedia/include \
# 	-o output/pjsip-simple-x86_64-unknown-linux-gnu/evsub.o \
# 	../src/pjsip-simple/evsub.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjnath/include -I../../pjmedia/include \
# 	-o output/pjsip-simple-x86_64-unknown-linux-gnu/evsub_msg.o \
# 	../src/pjsip-simple/evsub_msg.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjnath/include -I../../pjmedia/include \
# 	-o output/pjsip-simple-x86_64-unknown-linux-gnu/iscomposing.o \
# 	../src/pjsip-simple/iscomposing.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjnath/include -I../../pjmedia/include \
# 	-o output/pjsip-simple-x86_64-unknown-linux-gnu/mwi.o \
# 	../src/pjsip-simple/mwi.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjnath/include -I../../pjmedia/include \
# 	-o output/pjsip-simple-x86_64-unknown-linux-gnu/pidf.o \
# 	../src/pjsip-simple/pidf.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjnath/include -I../../pjmedia/include \
# 	-o output/pjsip-simple-x86_64-unknown-linux-gnu/presence.o \
# 	../src/pjsip-simple/presence.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjnath/include -I../../pjmedia/include \
# 	-o output/pjsip-simple-x86_64-unknown-linux-gnu/presence_body.o \
# 	../src/pjsip-simple/presence_body.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjnath/include -I../../pjmedia/include \
# 	-o output/pjsip-simple-x86_64-unknown-linux-gnu/publishc.o \
# 	../src/pjsip-simple/publishc.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjnath/include -I../../pjmedia/include \
# 	-o output/pjsip-simple-x86_64-unknown-linux-gnu/rpid.o \
# 	../src/pjsip-simple/rpid.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjnath/include -I../../pjmedia/include \
# 	-o output/pjsip-simple-x86_64-unknown-linux-gnu/xpidf.o \
# 	../src/pjsip-simple/xpidf.c 
# if test ! -d ../lib; then mkdir -p ../lib; fi
# ar rv ../lib/libpjsip-simple-x86_64-unknown-linux-gnu.a  output/pjsip-simple-x86_64-unknown-linux-gnu/errno.o  output/pjsip-simple-x86_64-unknown-linux-gnu/evsub.o  output/pjsip-simple-x86_64-unknown-linux-gnu/evsub_msg.o  output/pjsip-simple-x86_64-unknown-linux-gnu/iscomposing.o  output/pjsip-simple-x86_64-unknown-linux-gnu/mwi.o  output/pjsip-simple-x86_64-unknown-linux-gnu/pidf.o  output/pjsip-simple-x86_64-unknown-linux-gnu/presence.o  output/pjsip-simple-x86_64-unknown-linux-gnu/presence_body.o  output/pjsip-simple-x86_64-unknown-linux-gnu/publishc.o  output/pjsip-simple-x86_64-unknown-linux-gnu/rpid.o  output/pjsip-simple-x86_64-unknown-linux-gnu/xpidf.o
# r - output/pjsip-simple-x86_64-unknown-linux-gnu/errno.o
# r - output/pjsip-simple-x86_64-unknown-linux-gnu/evsub.o
# r - output/pjsip-simple-x86_64-unknown-linux-gnu/evsub_msg.o
# r - output/pjsip-simple-x86_64-unknown-linux-gnu/iscomposing.o
# r - output/pjsip-simple-x86_64-unknown-linux-gnu/mwi.o
# r - output/pjsip-simple-x86_64-unknown-linux-gnu/pidf.o
# r - output/pjsip-simple-x86_64-unknown-linux-gnu/presence.o
# r - output/pjsip-simple-x86_64-unknown-linux-gnu/presence_body.o
# r - output/pjsip-simple-x86_64-unknown-linux-gnu/publishc.o
# r - output/pjsip-simple-x86_64-unknown-linux-gnu/rpid.o
# r - output/pjsip-simple-x86_64-unknown-linux-gnu/xpidf.o
# ranlib ../lib/libpjsip-simple-x86_64-unknown-linux-gnu.a
# make[2]: Leaving directory '/home/vsedyshev/Work/1111/pjproject/pjsip/build'
# make -f /home/vsedyshev/Work/1111/pjproject/build/rules.mak APP=PJSIP_UA app=pjsip-ua ../lib/libpjsip-ua-x86_64-unknown-linux-gnu.a
# make[2]: Entering directory '/home/vsedyshev/Work/1111/pjproject/pjsip/build'
# mkdir -p output/pjsip-ua-x86_64-unknown-linux-gnu/
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjnath/include -I../../pjmedia/include \
# 	-o output/pjsip-ua-x86_64-unknown-linux-gnu/sip_inv.o \
# 	../src/pjsip-ua/sip_inv.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjnath/include -I../../pjmedia/include \
# 	-o output/pjsip-ua-x86_64-unknown-linux-gnu/sip_reg.o \
# 	../src/pjsip-ua/sip_reg.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjnath/include -I../../pjmedia/include \
# 	-o output/pjsip-ua-x86_64-unknown-linux-gnu/sip_replaces.o \
# 	../src/pjsip-ua/sip_replaces.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjnath/include -I../../pjmedia/include \
# 	-o output/pjsip-ua-x86_64-unknown-linux-gnu/sip_xfer.o \
# 	../src/pjsip-ua/sip_xfer.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjnath/include -I../../pjmedia/include \
# 	-o output/pjsip-ua-x86_64-unknown-linux-gnu/sip_100rel.o \
# 	../src/pjsip-ua/sip_100rel.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjnath/include -I../../pjmedia/include \
# 	-o output/pjsip-ua-x86_64-unknown-linux-gnu/sip_timer.o \
# 	../src/pjsip-ua/sip_timer.c 
# if test ! -d ../lib; then mkdir -p ../lib; fi
# ar rv ../lib/libpjsip-ua-x86_64-unknown-linux-gnu.a  output/pjsip-ua-x86_64-unknown-linux-gnu/sip_inv.o  output/pjsip-ua-x86_64-unknown-linux-gnu/sip_reg.o  output/pjsip-ua-x86_64-unknown-linux-gnu/sip_replaces.o  output/pjsip-ua-x86_64-unknown-linux-gnu/sip_xfer.o  output/pjsip-ua-x86_64-unknown-linux-gnu/sip_100rel.o  output/pjsip-ua-x86_64-unknown-linux-gnu/sip_timer.o
# r - output/pjsip-ua-x86_64-unknown-linux-gnu/sip_inv.o
# r - output/pjsip-ua-x86_64-unknown-linux-gnu/sip_reg.o
# r - output/pjsip-ua-x86_64-unknown-linux-gnu/sip_replaces.o
# r - output/pjsip-ua-x86_64-unknown-linux-gnu/sip_xfer.o
# r - output/pjsip-ua-x86_64-unknown-linux-gnu/sip_100rel.o
# r - output/pjsip-ua-x86_64-unknown-linux-gnu/sip_timer.o
# ranlib ../lib/libpjsip-ua-x86_64-unknown-linux-gnu.a
# make[2]: Leaving directory '/home/vsedyshev/Work/1111/pjproject/pjsip/build'
# make -f /home/vsedyshev/Work/1111/pjproject/build/rules.mak APP=PJSUA_LIB app=pjsua-lib ../lib/libpjsua-x86_64-unknown-linux-gnu.a
# make[2]: Entering directory '/home/vsedyshev/Work/1111/pjproject/pjsip/build'
# mkdir -p output/pjsua-lib-x86_64-unknown-linux-gnu/
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjnath/include -I../../pjmedia/include -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       \
# 	-o output/pjsua-lib-x86_64-unknown-linux-gnu/pjsua_acc.o \
# 	../src/pjsua-lib/pjsua_acc.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjnath/include -I../../pjmedia/include -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       \
# 	-o output/pjsua-lib-x86_64-unknown-linux-gnu/pjsua_call.o \
# 	../src/pjsua-lib/pjsua_call.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjnath/include -I../../pjmedia/include -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       \
# 	-o output/pjsua-lib-x86_64-unknown-linux-gnu/pjsua_core.o \
# 	../src/pjsua-lib/pjsua_core.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjnath/include -I../../pjmedia/include -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       \
# 	-o output/pjsua-lib-x86_64-unknown-linux-gnu/pjsua_im.o \
# 	../src/pjsua-lib/pjsua_im.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjnath/include -I../../pjmedia/include -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       \
# 	-o output/pjsua-lib-x86_64-unknown-linux-gnu/pjsua_media.o \
# 	../src/pjsua-lib/pjsua_media.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjnath/include -I../../pjmedia/include -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       \
# 	-o output/pjsua-lib-x86_64-unknown-linux-gnu/pjsua_pres.o \
# 	../src/pjsua-lib/pjsua_pres.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjnath/include -I../../pjmedia/include -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       \
# 	-o output/pjsua-lib-x86_64-unknown-linux-gnu/pjsua_dump.o \
# 	../src/pjsua-lib/pjsua_dump.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjnath/include -I../../pjmedia/include -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       \
# 	-o output/pjsua-lib-x86_64-unknown-linux-gnu/pjsua_aud.o \
# 	../src/pjsua-lib/pjsua_aud.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjnath/include -I../../pjmedia/include -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       \
# 	-o output/pjsua-lib-x86_64-unknown-linux-gnu/pjsua_vid.o \
# 	../src/pjsua-lib/pjsua_vid.c 
# if test ! -d ../lib; then mkdir -p ../lib; fi
# ar rv ../lib/libpjsua-x86_64-unknown-linux-gnu.a  output/pjsua-lib-x86_64-unknown-linux-gnu/pjsua_acc.o  output/pjsua-lib-x86_64-unknown-linux-gnu/pjsua_call.o  output/pjsua-lib-x86_64-unknown-linux-gnu/pjsua_core.o  output/pjsua-lib-x86_64-unknown-linux-gnu/pjsua_im.o  output/pjsua-lib-x86_64-unknown-linux-gnu/pjsua_media.o  output/pjsua-lib-x86_64-unknown-linux-gnu/pjsua_pres.o  output/pjsua-lib-x86_64-unknown-linux-gnu/pjsua_dump.o  output/pjsua-lib-x86_64-unknown-linux-gnu/pjsua_aud.o  output/pjsua-lib-x86_64-unknown-linux-gnu/pjsua_vid.o
# r - output/pjsua-lib-x86_64-unknown-linux-gnu/pjsua_acc.o
# r - output/pjsua-lib-x86_64-unknown-linux-gnu/pjsua_call.o
# r - output/pjsua-lib-x86_64-unknown-linux-gnu/pjsua_core.o
# r - output/pjsua-lib-x86_64-unknown-linux-gnu/pjsua_im.o
# r - output/pjsua-lib-x86_64-unknown-linux-gnu/pjsua_media.o
# r - output/pjsua-lib-x86_64-unknown-linux-gnu/pjsua_pres.o
# r - output/pjsua-lib-x86_64-unknown-linux-gnu/pjsua_dump.o
# r - output/pjsua-lib-x86_64-unknown-linux-gnu/pjsua_aud.o
# r - output/pjsua-lib-x86_64-unknown-linux-gnu/pjsua_vid.o
# ranlib ../lib/libpjsua-x86_64-unknown-linux-gnu.a
# make[2]: Leaving directory '/home/vsedyshev/Work/1111/pjproject/pjsip/build'
# make -f /home/vsedyshev/Work/1111/pjproject/build/rules.mak APP=PJSUA2_LIB app=pjsua2-lib ../lib/libpjsua2-x86_64-unknown-linux-gnu.a
# make[2]: Entering directory '/home/vsedyshev/Work/1111/pjproject/pjsip/build'
# mkdir -p output/pjsua2-lib-x86_64-unknown-linux-gnu/
# g++ -c  -DPJ_AUTOCONF=1 -g -O2    -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjnath/include -I../../pjmedia/include -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjnath/include -I../../pjmedia/include -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       \
# 	-o output/pjsua2-lib-x86_64-unknown-linux-gnu/account.o \
# 	../src/pjsua2/account.cpp
# g++ -c  -DPJ_AUTOCONF=1 -g -O2    -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjnath/include -I../../pjmedia/include -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjnath/include -I../../pjmedia/include -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       \
# 	-o output/pjsua2-lib-x86_64-unknown-linux-gnu/endpoint.o \
# 	../src/pjsua2/endpoint.cpp
# g++ -c  -DPJ_AUTOCONF=1 -g -O2    -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjnath/include -I../../pjmedia/include -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjnath/include -I../../pjmedia/include -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       \
# 	-o output/pjsua2-lib-x86_64-unknown-linux-gnu/json.o \
# 	../src/pjsua2/json.cpp
# g++ -c  -DPJ_AUTOCONF=1 -g -O2    -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjnath/include -I../../pjmedia/include -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjnath/include -I../../pjmedia/include -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       \
# 	-o output/pjsua2-lib-x86_64-unknown-linux-gnu/persistent.o \
# 	../src/pjsua2/persistent.cpp
# g++ -c  -DPJ_AUTOCONF=1 -g -O2    -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjnath/include -I../../pjmedia/include -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjnath/include -I../../pjmedia/include -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       \
# 	-o output/pjsua2-lib-x86_64-unknown-linux-gnu/types.o \
# 	../src/pjsua2/types.cpp
# g++ -c  -DPJ_AUTOCONF=1 -g -O2    -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjnath/include -I../../pjmedia/include -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjnath/include -I../../pjmedia/include -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       \
# 	-o output/pjsua2-lib-x86_64-unknown-linux-gnu/siptypes.o \
# 	../src/pjsua2/siptypes.cpp
# g++ -c  -DPJ_AUTOCONF=1 -g -O2    -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjnath/include -I../../pjmedia/include -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjnath/include -I../../pjmedia/include -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       \
# 	-o output/pjsua2-lib-x86_64-unknown-linux-gnu/call.o \
# 	../src/pjsua2/call.cpp
# g++ -c  -DPJ_AUTOCONF=1 -g -O2    -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjnath/include -I../../pjmedia/include -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjnath/include -I../../pjmedia/include -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       \
# 	-o output/pjsua2-lib-x86_64-unknown-linux-gnu/presence.o \
# 	../src/pjsua2/presence.cpp
# g++ -c  -DPJ_AUTOCONF=1 -g -O2    -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjnath/include -I../../pjmedia/include -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjnath/include -I../../pjmedia/include -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       \
# 	-o output/pjsua2-lib-x86_64-unknown-linux-gnu/media.o \
# 	../src/pjsua2/media.cpp
# if test ! -d ../lib; then mkdir -p ../lib; fi
# ar rv ../lib/libpjsua2-x86_64-unknown-linux-gnu.a  output/pjsua2-lib-x86_64-unknown-linux-gnu/account.o  output/pjsua2-lib-x86_64-unknown-linux-gnu/endpoint.o  output/pjsua2-lib-x86_64-unknown-linux-gnu/json.o  output/pjsua2-lib-x86_64-unknown-linux-gnu/persistent.o  output/pjsua2-lib-x86_64-unknown-linux-gnu/types.o  output/pjsua2-lib-x86_64-unknown-linux-gnu/siptypes.o  output/pjsua2-lib-x86_64-unknown-linux-gnu/call.o  output/pjsua2-lib-x86_64-unknown-linux-gnu/presence.o  output/pjsua2-lib-x86_64-unknown-linux-gnu/media.o
# r - output/pjsua2-lib-x86_64-unknown-linux-gnu/account.o
# r - output/pjsua2-lib-x86_64-unknown-linux-gnu/endpoint.o
# r - output/pjsua2-lib-x86_64-unknown-linux-gnu/json.o
# r - output/pjsua2-lib-x86_64-unknown-linux-gnu/persistent.o
# r - output/pjsua2-lib-x86_64-unknown-linux-gnu/types.o
# r - output/pjsua2-lib-x86_64-unknown-linux-gnu/siptypes.o
# r - output/pjsua2-lib-x86_64-unknown-linux-gnu/call.o
# r - output/pjsua2-lib-x86_64-unknown-linux-gnu/presence.o
# r - output/pjsua2-lib-x86_64-unknown-linux-gnu/media.o
# ranlib ../lib/libpjsua2-x86_64-unknown-linux-gnu.a
# make[2]: Leaving directory '/home/vsedyshev/Work/1111/pjproject/pjsip/build'
# make -f /home/vsedyshev/Work/1111/pjproject/build/rules.mak APP=TEST app=pjsip-test ../bin/pjsip-test-x86_64-unknown-linux-gnu
# make[2]: Entering directory '/home/vsedyshev/Work/1111/pjproject/pjsip/build'
# mkdir -p output/pjsip-test-x86_64-unknown-linux-gnu/
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjnath/include -I../../pjmedia/include \
# 	-o output/pjsip-test-x86_64-unknown-linux-gnu/main.o \
# 	../src/test/main.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjnath/include -I../../pjmedia/include \
# 	-o output/pjsip-test-x86_64-unknown-linux-gnu/dlg_core_test.o \
# 	../src/test/dlg_core_test.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjnath/include -I../../pjmedia/include \
# 	-o output/pjsip-test-x86_64-unknown-linux-gnu/dns_test.o \
# 	../src/test/dns_test.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjnath/include -I../../pjmedia/include \
# 	-o output/pjsip-test-x86_64-unknown-linux-gnu/msg_err_test.o \
# 	../src/test/msg_err_test.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjnath/include -I../../pjmedia/include \
# 	-o output/pjsip-test-x86_64-unknown-linux-gnu/msg_logger.o \
# 	../src/test/msg_logger.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjnath/include -I../../pjmedia/include \
# 	-o output/pjsip-test-x86_64-unknown-linux-gnu/msg_test.o \
# 	../src/test/msg_test.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjnath/include -I../../pjmedia/include \
# 	-o output/pjsip-test-x86_64-unknown-linux-gnu/multipart_test.o \
# 	../src/test/multipart_test.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjnath/include -I../../pjmedia/include \
# 	-o output/pjsip-test-x86_64-unknown-linux-gnu/regc_test.o \
# 	../src/test/regc_test.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjnath/include -I../../pjmedia/include \
# 	-o output/pjsip-test-x86_64-unknown-linux-gnu/test.o \
# 	../src/test/test.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjnath/include -I../../pjmedia/include \
# 	-o output/pjsip-test-x86_64-unknown-linux-gnu/transport_loop_test.o \
# 	../src/test/transport_loop_test.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjnath/include -I../../pjmedia/include \
# 	-o output/pjsip-test-x86_64-unknown-linux-gnu/transport_tcp_test.o \
# 	../src/test/transport_tcp_test.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjnath/include -I../../pjmedia/include \
# 	-o output/pjsip-test-x86_64-unknown-linux-gnu/transport_test.o \
# 	../src/test/transport_test.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjnath/include -I../../pjmedia/include \
# 	-o output/pjsip-test-x86_64-unknown-linux-gnu/transport_udp_test.o \
# 	../src/test/transport_udp_test.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjnath/include -I../../pjmedia/include \
# 	-o output/pjsip-test-x86_64-unknown-linux-gnu/tsx_basic_test.o \
# 	../src/test/tsx_basic_test.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjnath/include -I../../pjmedia/include \
# 	-o output/pjsip-test-x86_64-unknown-linux-gnu/tsx_bench.o \
# 	../src/test/tsx_bench.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjnath/include -I../../pjmedia/include \
# 	-o output/pjsip-test-x86_64-unknown-linux-gnu/tsx_uac_test.o \
# 	../src/test/tsx_uac_test.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjnath/include -I../../pjmedia/include \
# 	-o output/pjsip-test-x86_64-unknown-linux-gnu/tsx_uas_test.o \
# 	../src/test/tsx_uas_test.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjnath/include -I../../pjmedia/include \
# 	-o output/pjsip-test-x86_64-unknown-linux-gnu/txdata_test.o \
# 	../src/test/txdata_test.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjnath/include -I../../pjmedia/include \
# 	-o output/pjsip-test-x86_64-unknown-linux-gnu/uri_test.o \
# 	../src/test/uri_test.c 
# gcc -c -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjnath/include -I../../pjmedia/include \
# 	-o output/pjsip-test-x86_64-unknown-linux-gnu/inv_offer_answer_test.o \
# 	../src/test/inv_offer_answer_test.c 
# if test ! -d ../bin; then mkdir -p ../bin; fi
# gcc -o ../bin/pjsip-test-x86_64-unknown-linux-gnu \
#      output/pjsip-test-x86_64-unknown-linux-gnu/main.o  output/pjsip-test-x86_64-unknown-linux-gnu/dlg_core_test.o  output/pjsip-test-x86_64-unknown-linux-gnu/dns_test.o  output/pjsip-test-x86_64-unknown-linux-gnu/msg_err_test.o  output/pjsip-test-x86_64-unknown-linux-gnu/msg_logger.o  output/pjsip-test-x86_64-unknown-linux-gnu/msg_test.o  output/pjsip-test-x86_64-unknown-linux-gnu/multipart_test.o  output/pjsip-test-x86_64-unknown-linux-gnu/regc_test.o  output/pjsip-test-x86_64-unknown-linux-gnu/test.o  output/pjsip-test-x86_64-unknown-linux-gnu/transport_loop_test.o  output/pjsip-test-x86_64-unknown-linux-gnu/transport_tcp_test.o  output/pjsip-test-x86_64-unknown-linux-gnu/transport_test.o  output/pjsip-test-x86_64-unknown-linux-gnu/transport_udp_test.o  output/pjsip-test-x86_64-unknown-linux-gnu/tsx_basic_test.o  output/pjsip-test-x86_64-unknown-linux-gnu/tsx_bench.o  output/pjsip-test-x86_64-unknown-linux-gnu/tsx_uac_test.o  output/pjsip-test-x86_64-unknown-linux-gnu/tsx_uas_test.o  output/pjsip-test-x86_64-unknown-linux-gnu/txdata_test.o  output/pjsip-test-x86_64-unknown-linux-gnu/uri_test.o  output/pjsip-test-x86_64-unknown-linux-gnu/inv_offer_answer_test.o -lpjsip-x86_64-unknown-linux-gnu -lpjsip-ua-x86_64-unknown-linux-gnu -lpjsip-simple-x86_64-unknown-linux-gnu  -lpjmedia-codec-x86_64-unknown-linux-gnu -lpjmedia-videodev-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjmedia-audiodev-x86_64-unknown-linux-gnu -lpjlib-util-x86_64-unknown-linux-gnu -lpjnath-x86_64-unknown-linux-gnu -lpj-x86_64-unknown-linux-gnu  -lsrtp-x86_64-unknown-linux-gnu -lresample-x86_64-unknown-linux-gnu -lgsmcodec-x86_64-unknown-linux-gnu -lspeex-x86_64-unknown-linux-gnu -lilbccodec-x86_64-unknown-linux-gnu -lg7221codec-x86_64-unknown-linux-gnu -lyuv-x86_64-unknown-linux-gnu -lwebrtc-x86_64-unknown-linux-gnu   -lssl -lcrypto -luuid -lm -lrt -lpthread  -lasound -lSDL2     -L/home/vsedyshev/Work/1111/pjproject/pjlib/lib -L/home/vsedyshev/Work/1111/pjproject/pjlib-util/lib -L/home/vsedyshev/Work/1111/pjproject/pjnath/lib -L/home/vsedyshev/Work/1111/pjproject/pjmedia/lib -L/home/vsedyshev/Work/1111/pjproject/pjsip/lib -L/home/vsedyshev/Work/1111/pjproject/third_party/lib -lSDL2     -lSDL2       
# make[2]: Leaving directory '/home/vsedyshev/Work/1111/pjproject/pjsip/build'
# make -f /home/vsedyshev/Work/1111/pjproject/build/rules.mak APP=PJSUA2_TEST app=pjsua2-test ../bin/pjsua2-test-x86_64-unknown-linux-gnu
# make[2]: Entering directory '/home/vsedyshev/Work/1111/pjproject/pjsip/build'
# mkdir -p output/pjsua2-test-x86_64-unknown-linux-gnu/
# g++ -c  -DPJ_AUTOCONF=1 -g -O2    -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjnath/include -I../../pjmedia/include -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjnath/include -I../../pjmedia/include -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1        \
# 	-o output/pjsua2-test-x86_64-unknown-linux-gnu/main.o \
# 	../src/pjsua2-test/main.cpp
# if test ! -d ../bin; then mkdir -p ../bin; fi
# gcc -o ../bin/pjsua2-test-x86_64-unknown-linux-gnu \
#      output/pjsua2-test-x86_64-unknown-linux-gnu/main.o -L/home/vsedyshev/Work/1111/pjproject/pjlib/lib -L/home/vsedyshev/Work/1111/pjproject/pjlib-util/lib -L/home/vsedyshev/Work/1111/pjproject/pjnath/lib -L/home/vsedyshev/Work/1111/pjproject/pjmedia/lib -L/home/vsedyshev/Work/1111/pjproject/pjsip/lib -L/home/vsedyshev/Work/1111/pjproject/third_party/lib -lSDL2     -lSDL2      -lpjsua2-x86_64-unknown-linux-gnu -lstdc++ -lpjsua-x86_64-unknown-linux-gnu -lpjsip-ua-x86_64-unknown-linux-gnu -lpjsip-simple-x86_64-unknown-linux-gnu -lpjsip-x86_64-unknown-linux-gnu -lpjmedia-codec-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjmedia-videodev-x86_64-unknown-linux-gnu -lpjmedia-audiodev-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjnath-x86_64-unknown-linux-gnu -lpjlib-util-x86_64-unknown-linux-gnu  -lsrtp-x86_64-unknown-linux-gnu -lresample-x86_64-unknown-linux-gnu -lgsmcodec-x86_64-unknown-linux-gnu -lspeex-x86_64-unknown-linux-gnu -lilbccodec-x86_64-unknown-linux-gnu -lg7221codec-x86_64-unknown-linux-gnu -lyuv-x86_64-unknown-linux-gnu -lwebrtc-x86_64-unknown-linux-gnu  -lpj-x86_64-unknown-linux-gnu -lssl -lcrypto -luuid -lm -lrt -lpthread  -lasound -lSDL2   
# make[2]: Leaving directory '/home/vsedyshev/Work/1111/pjproject/pjsip/build'
# make[1]: Leaving directory '/home/vsedyshev/Work/1111/pjproject/pjsip/build'
# make[1]: Entering directory '/home/vsedyshev/Work/1111/pjproject/pjsip-apps/build'
# make -f /home/vsedyshev/Work/1111/pjproject/build/rules.mak APP=PJSUA app=pjsua ../bin/pjsua-x86_64-unknown-linux-gnu
# make[2]: Entering directory '/home/vsedyshev/Work/1111/pjproject/pjsip-apps/build'
# mkdir -p output/pjsua-x86_64-unknown-linux-gnu/
# gcc -c -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1 -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -I/home/vsedyshev/Work/1111/pjproject/pjlib/include -I/home/vsedyshev/Work/1111/pjproject/pjlib-util/include -I/home/vsedyshev/Work/1111/pjproject/pjnath/include -I/home/vsedyshev/Work/1111/pjproject/pjmedia/include -I/home/vsedyshev/Work/1111/pjproject/pjsip/include  \
# 	-o output/pjsua-x86_64-unknown-linux-gnu/main.o \
# 	../src/pjsua/main.c 
# gcc -c -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1 -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -I/home/vsedyshev/Work/1111/pjproject/pjlib/include -I/home/vsedyshev/Work/1111/pjproject/pjlib-util/include -I/home/vsedyshev/Work/1111/pjproject/pjnath/include -I/home/vsedyshev/Work/1111/pjproject/pjmedia/include -I/home/vsedyshev/Work/1111/pjproject/pjsip/include  \
# 	-o output/pjsua-x86_64-unknown-linux-gnu/pjsua_app.o \
# 	../src/pjsua/pjsua_app.c 
# gcc -c -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1 -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -I/home/vsedyshev/Work/1111/pjproject/pjlib/include -I/home/vsedyshev/Work/1111/pjproject/pjlib-util/include -I/home/vsedyshev/Work/1111/pjproject/pjnath/include -I/home/vsedyshev/Work/1111/pjproject/pjmedia/include -I/home/vsedyshev/Work/1111/pjproject/pjsip/include  \
# 	-o output/pjsua-x86_64-unknown-linux-gnu/pjsua_app_cli.o \
# 	../src/pjsua/pjsua_app_cli.c 
# gcc -c -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1 -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -I/home/vsedyshev/Work/1111/pjproject/pjlib/include -I/home/vsedyshev/Work/1111/pjproject/pjlib-util/include -I/home/vsedyshev/Work/1111/pjproject/pjnath/include -I/home/vsedyshev/Work/1111/pjproject/pjmedia/include -I/home/vsedyshev/Work/1111/pjproject/pjsip/include  \
# 	-o output/pjsua-x86_64-unknown-linux-gnu/pjsua_app_common.o \
# 	../src/pjsua/pjsua_app_common.c 
# gcc -c -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1 -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -I/home/vsedyshev/Work/1111/pjproject/pjlib/include -I/home/vsedyshev/Work/1111/pjproject/pjlib-util/include -I/home/vsedyshev/Work/1111/pjproject/pjnath/include -I/home/vsedyshev/Work/1111/pjproject/pjmedia/include -I/home/vsedyshev/Work/1111/pjproject/pjsip/include  \
# 	-o output/pjsua-x86_64-unknown-linux-gnu/pjsua_app_config.o \
# 	../src/pjsua/pjsua_app_config.c 
# gcc -c -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1 -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -I/home/vsedyshev/Work/1111/pjproject/pjlib/include -I/home/vsedyshev/Work/1111/pjproject/pjlib-util/include -I/home/vsedyshev/Work/1111/pjproject/pjnath/include -I/home/vsedyshev/Work/1111/pjproject/pjmedia/include -I/home/vsedyshev/Work/1111/pjproject/pjsip/include  \
# 	-o output/pjsua-x86_64-unknown-linux-gnu/pjsua_app_legacy.o \
# 	../src/pjsua/pjsua_app_legacy.c 
# if test ! -d ../bin; then mkdir -p ../bin; fi
# gcc -o ../bin/pjsua-x86_64-unknown-linux-gnu \
#      output/pjsua-x86_64-unknown-linux-gnu/main.o  output/pjsua-x86_64-unknown-linux-gnu/pjsua_app.o  output/pjsua-x86_64-unknown-linux-gnu/pjsua_app_cli.o  output/pjsua-x86_64-unknown-linux-gnu/pjsua_app_common.o  output/pjsua-x86_64-unknown-linux-gnu/pjsua_app_config.o  output/pjsua-x86_64-unknown-linux-gnu/pjsua_app_legacy.o -L/home/vsedyshev/Work/1111/pjproject/pjlib/lib -L/home/vsedyshev/Work/1111/pjproject/pjlib-util/lib -L/home/vsedyshev/Work/1111/pjproject/pjnath/lib -L/home/vsedyshev/Work/1111/pjproject/pjmedia/lib -L/home/vsedyshev/Work/1111/pjproject/pjsip/lib -L/home/vsedyshev/Work/1111/pjproject/third_party/lib -lSDL2     -lSDL2      -lpjsua-x86_64-unknown-linux-gnu -lpjsip-ua-x86_64-unknown-linux-gnu -lpjsip-simple-x86_64-unknown-linux-gnu -lpjsip-x86_64-unknown-linux-gnu -lpjmedia-codec-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjmedia-videodev-x86_64-unknown-linux-gnu -lpjmedia-audiodev-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjnath-x86_64-unknown-linux-gnu -lpjlib-util-x86_64-unknown-linux-gnu  -lsrtp-x86_64-unknown-linux-gnu -lresample-x86_64-unknown-linux-gnu -lgsmcodec-x86_64-unknown-linux-gnu -lspeex-x86_64-unknown-linux-gnu -lilbccodec-x86_64-unknown-linux-gnu -lg7221codec-x86_64-unknown-linux-gnu -lyuv-x86_64-unknown-linux-gnu -lwebrtc-x86_64-unknown-linux-gnu  -lpj-x86_64-unknown-linux-gnu -lssl -lcrypto -luuid -lm -lrt -lpthread  -lasound -lSDL2   
# make[2]: Leaving directory '/home/vsedyshev/Work/1111/pjproject/pjsip-apps/build'
# make -f /home/vsedyshev/Work/1111/pjproject/build/rules.mak APP=PJSYSTEST app=pjsystest ../bin/pjsystest-x86_64-unknown-linux-gnu
# make[2]: Entering directory '/home/vsedyshev/Work/1111/pjproject/pjsip-apps/build'
# mkdir -p output/pjsystest-x86_64-unknown-linux-gnu/
# gcc -c -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1 -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -I/home/vsedyshev/Work/1111/pjproject/pjlib/include -I/home/vsedyshev/Work/1111/pjproject/pjlib-util/include -I/home/vsedyshev/Work/1111/pjproject/pjnath/include -I/home/vsedyshev/Work/1111/pjproject/pjmedia/include -I/home/vsedyshev/Work/1111/pjproject/pjsip/include  \
# 	-o output/pjsystest-x86_64-unknown-linux-gnu/systest.o \
# 	../src/pjsystest/systest.c 
# gcc -c -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1 -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -I/home/vsedyshev/Work/1111/pjproject/pjlib/include -I/home/vsedyshev/Work/1111/pjproject/pjlib-util/include -I/home/vsedyshev/Work/1111/pjproject/pjnath/include -I/home/vsedyshev/Work/1111/pjproject/pjmedia/include -I/home/vsedyshev/Work/1111/pjproject/pjsip/include  \
# 	-o output/pjsystest-x86_64-unknown-linux-gnu/main_console.o \
# 	../src/pjsystest/main_console.c 
# if test ! -d ../bin; then mkdir -p ../bin; fi
# gcc -o ../bin/pjsystest-x86_64-unknown-linux-gnu \
#      output/pjsystest-x86_64-unknown-linux-gnu/systest.o  output/pjsystest-x86_64-unknown-linux-gnu/main_console.o -L/home/vsedyshev/Work/1111/pjproject/pjlib/lib -L/home/vsedyshev/Work/1111/pjproject/pjlib-util/lib -L/home/vsedyshev/Work/1111/pjproject/pjnath/lib -L/home/vsedyshev/Work/1111/pjproject/pjmedia/lib -L/home/vsedyshev/Work/1111/pjproject/pjsip/lib -L/home/vsedyshev/Work/1111/pjproject/third_party/lib -lSDL2     -lSDL2      -lpjsua-x86_64-unknown-linux-gnu -lpjsip-ua-x86_64-unknown-linux-gnu -lpjsip-simple-x86_64-unknown-linux-gnu -lpjsip-x86_64-unknown-linux-gnu -lpjmedia-codec-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjmedia-videodev-x86_64-unknown-linux-gnu -lpjmedia-audiodev-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjnath-x86_64-unknown-linux-gnu -lpjlib-util-x86_64-unknown-linux-gnu  -lsrtp-x86_64-unknown-linux-gnu -lresample-x86_64-unknown-linux-gnu -lgsmcodec-x86_64-unknown-linux-gnu -lspeex-x86_64-unknown-linux-gnu -lilbccodec-x86_64-unknown-linux-gnu -lg7221codec-x86_64-unknown-linux-gnu -lyuv-x86_64-unknown-linux-gnu -lwebrtc-x86_64-unknown-linux-gnu  -lpj-x86_64-unknown-linux-gnu -lssl -lcrypto -luuid -lm -lrt -lpthread  -lasound -lSDL2   
# make[2]: Leaving directory '/home/vsedyshev/Work/1111/pjproject/pjsip-apps/build'
# make -f Samples.mak
# make[2]: Entering directory '/home/vsedyshev/Work/1111/pjproject/pjsip-apps/build'
# make --no-print-directory -f /home/vsedyshev/Work/1111/pjproject/build/rules.mak SAMPLE_SRCDIR=../src/samples SAMPLE_OBJS=auddemo.o SAMPLE_CFLAGS="-DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1 -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -I/home/vsedyshev/Work/1111/pjproject/pjlib/include -I/home/vsedyshev/Work/1111/pjproject/pjlib-util/include -I/home/vsedyshev/Work/1111/pjproject/pjnath/include -I/home/vsedyshev/Work/1111/pjproject/pjmedia/include -I/home/vsedyshev/Work/1111/pjproject/pjsip/include " SAMPLE_CXXFLAGS="-g -O2 -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1 -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -I/home/vsedyshev/Work/1111/pjproject/pjlib/include -I/home/vsedyshev/Work/1111/pjproject/pjlib-util/include -I/home/vsedyshev/Work/1111/pjproject/pjnath/include -I/home/vsedyshev/Work/1111/pjproject/pjmedia/include -I/home/vsedyshev/Work/1111/pjproject/pjsip/include " SAMPLE_LDFLAGS="-L/home/vsedyshev/Work/1111/pjproject/pjlib/lib -L/home/vsedyshev/Work/1111/pjproject/pjlib-util/lib -L/home/vsedyshev/Work/1111/pjproject/pjnath/lib -L/home/vsedyshev/Work/1111/pjproject/pjmedia/lib -L/home/vsedyshev/Work/1111/pjproject/pjsip/lib -L/home/vsedyshev/Work/1111/pjproject/third_party/lib -lSDL2     -lSDL2      -lpjsua-x86_64-unknown-linux-gnu -lpjsip-ua-x86_64-unknown-linux-gnu -lpjsip-simple-x86_64-unknown-linux-gnu -lpjsip-x86_64-unknown-linux-gnu -lpjmedia-codec-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjmedia-videodev-x86_64-unknown-linux-gnu -lpjmedia-audiodev-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjnath-x86_64-unknown-linux-gnu -lpjlib-util-x86_64-unknown-linux-gnu  -lsrtp-x86_64-unknown-linux-gnu -lresample-x86_64-unknown-linux-gnu -lgsmcodec-x86_64-unknown-linux-gnu -lspeex-x86_64-unknown-linux-gnu -lilbccodec-x86_64-unknown-linux-gnu -lg7221codec-x86_64-unknown-linux-gnu -lyuv-x86_64-unknown-linux-gnu -lwebrtc-x86_64-unknown-linux-gnu  -lpj-x86_64-unknown-linux-gnu -lssl -lcrypto -luuid -lm -lrt -lpthread  -lasound -lSDL2   " SAMPLE_EXE=auddemo APP=SAMPLE app=sample ../bin/samples/x86_64-unknown-linux-gnu/auddemo
# mkdir -p output/sample-x86_64-unknown-linux-gnu/
# gcc -c -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1 -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -I/home/vsedyshev/Work/1111/pjproject/pjlib/include -I/home/vsedyshev/Work/1111/pjproject/pjlib-util/include -I/home/vsedyshev/Work/1111/pjproject/pjnath/include -I/home/vsedyshev/Work/1111/pjproject/pjmedia/include -I/home/vsedyshev/Work/1111/pjproject/pjsip/include  \
# 	-o output/sample-x86_64-unknown-linux-gnu/auddemo.o \
# 	../src/samples/auddemo.c 
# if test ! -d ../bin/samples/x86_64-unknown-linux-gnu; then mkdir -p ../bin/samples/x86_64-unknown-linux-gnu; fi
# gcc -o ../bin/samples/x86_64-unknown-linux-gnu/auddemo \
#      output/sample-x86_64-unknown-linux-gnu/auddemo.o -L/home/vsedyshev/Work/1111/pjproject/pjlib/lib -L/home/vsedyshev/Work/1111/pjproject/pjlib-util/lib -L/home/vsedyshev/Work/1111/pjproject/pjnath/lib -L/home/vsedyshev/Work/1111/pjproject/pjmedia/lib -L/home/vsedyshev/Work/1111/pjproject/pjsip/lib -L/home/vsedyshev/Work/1111/pjproject/third_party/lib -lSDL2     -lSDL2      -lpjsua-x86_64-unknown-linux-gnu -lpjsip-ua-x86_64-unknown-linux-gnu -lpjsip-simple-x86_64-unknown-linux-gnu -lpjsip-x86_64-unknown-linux-gnu -lpjmedia-codec-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjmedia-videodev-x86_64-unknown-linux-gnu -lpjmedia-audiodev-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjnath-x86_64-unknown-linux-gnu -lpjlib-util-x86_64-unknown-linux-gnu  -lsrtp-x86_64-unknown-linux-gnu -lresample-x86_64-unknown-linux-gnu -lgsmcodec-x86_64-unknown-linux-gnu -lspeex-x86_64-unknown-linux-gnu -lilbccodec-x86_64-unknown-linux-gnu -lg7221codec-x86_64-unknown-linux-gnu -lyuv-x86_64-unknown-linux-gnu -lwebrtc-x86_64-unknown-linux-gnu  -lpj-x86_64-unknown-linux-gnu -lssl -lcrypto -luuid -lm -lrt -lpthread  -lasound -lSDL2   
# make --no-print-directory -f /home/vsedyshev/Work/1111/pjproject/build/rules.mak SAMPLE_SRCDIR=../src/samples SAMPLE_OBJS=aviplay.o SAMPLE_CFLAGS="-DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1 -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -I/home/vsedyshev/Work/1111/pjproject/pjlib/include -I/home/vsedyshev/Work/1111/pjproject/pjlib-util/include -I/home/vsedyshev/Work/1111/pjproject/pjnath/include -I/home/vsedyshev/Work/1111/pjproject/pjmedia/include -I/home/vsedyshev/Work/1111/pjproject/pjsip/include " SAMPLE_CXXFLAGS="-g -O2 -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1 -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -I/home/vsedyshev/Work/1111/pjproject/pjlib/include -I/home/vsedyshev/Work/1111/pjproject/pjlib-util/include -I/home/vsedyshev/Work/1111/pjproject/pjnath/include -I/home/vsedyshev/Work/1111/pjproject/pjmedia/include -I/home/vsedyshev/Work/1111/pjproject/pjsip/include " SAMPLE_LDFLAGS="-L/home/vsedyshev/Work/1111/pjproject/pjlib/lib -L/home/vsedyshev/Work/1111/pjproject/pjlib-util/lib -L/home/vsedyshev/Work/1111/pjproject/pjnath/lib -L/home/vsedyshev/Work/1111/pjproject/pjmedia/lib -L/home/vsedyshev/Work/1111/pjproject/pjsip/lib -L/home/vsedyshev/Work/1111/pjproject/third_party/lib -lSDL2     -lSDL2      -lpjsua-x86_64-unknown-linux-gnu -lpjsip-ua-x86_64-unknown-linux-gnu -lpjsip-simple-x86_64-unknown-linux-gnu -lpjsip-x86_64-unknown-linux-gnu -lpjmedia-codec-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjmedia-videodev-x86_64-unknown-linux-gnu -lpjmedia-audiodev-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjnath-x86_64-unknown-linux-gnu -lpjlib-util-x86_64-unknown-linux-gnu  -lsrtp-x86_64-unknown-linux-gnu -lresample-x86_64-unknown-linux-gnu -lgsmcodec-x86_64-unknown-linux-gnu -lspeex-x86_64-unknown-linux-gnu -lilbccodec-x86_64-unknown-linux-gnu -lg7221codec-x86_64-unknown-linux-gnu -lyuv-x86_64-unknown-linux-gnu -lwebrtc-x86_64-unknown-linux-gnu  -lpj-x86_64-unknown-linux-gnu -lssl -lcrypto -luuid -lm -lrt -lpthread  -lasound -lSDL2   " SAMPLE_EXE=aviplay APP=SAMPLE app=sample ../bin/samples/x86_64-unknown-linux-gnu/aviplay
# gcc -c -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1 -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -I/home/vsedyshev/Work/1111/pjproject/pjlib/include -I/home/vsedyshev/Work/1111/pjproject/pjlib-util/include -I/home/vsedyshev/Work/1111/pjproject/pjnath/include -I/home/vsedyshev/Work/1111/pjproject/pjmedia/include -I/home/vsedyshev/Work/1111/pjproject/pjsip/include  \
# 	-o output/sample-x86_64-unknown-linux-gnu/aviplay.o \
# 	../src/samples/aviplay.c 
# if test ! -d ../bin/samples/x86_64-unknown-linux-gnu; then mkdir -p ../bin/samples/x86_64-unknown-linux-gnu; fi
# gcc -o ../bin/samples/x86_64-unknown-linux-gnu/aviplay \
#      output/sample-x86_64-unknown-linux-gnu/aviplay.o -L/home/vsedyshev/Work/1111/pjproject/pjlib/lib -L/home/vsedyshev/Work/1111/pjproject/pjlib-util/lib -L/home/vsedyshev/Work/1111/pjproject/pjnath/lib -L/home/vsedyshev/Work/1111/pjproject/pjmedia/lib -L/home/vsedyshev/Work/1111/pjproject/pjsip/lib -L/home/vsedyshev/Work/1111/pjproject/third_party/lib -lSDL2     -lSDL2      -lpjsua-x86_64-unknown-linux-gnu -lpjsip-ua-x86_64-unknown-linux-gnu -lpjsip-simple-x86_64-unknown-linux-gnu -lpjsip-x86_64-unknown-linux-gnu -lpjmedia-codec-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjmedia-videodev-x86_64-unknown-linux-gnu -lpjmedia-audiodev-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjnath-x86_64-unknown-linux-gnu -lpjlib-util-x86_64-unknown-linux-gnu  -lsrtp-x86_64-unknown-linux-gnu -lresample-x86_64-unknown-linux-gnu -lgsmcodec-x86_64-unknown-linux-gnu -lspeex-x86_64-unknown-linux-gnu -lilbccodec-x86_64-unknown-linux-gnu -lg7221codec-x86_64-unknown-linux-gnu -lyuv-x86_64-unknown-linux-gnu -lwebrtc-x86_64-unknown-linux-gnu  -lpj-x86_64-unknown-linux-gnu -lssl -lcrypto -luuid -lm -lrt -lpthread  -lasound -lSDL2   
# make --no-print-directory -f /home/vsedyshev/Work/1111/pjproject/build/rules.mak SAMPLE_SRCDIR=../src/samples SAMPLE_OBJS=aectest.o SAMPLE_CFLAGS="-DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1 -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -I/home/vsedyshev/Work/1111/pjproject/pjlib/include -I/home/vsedyshev/Work/1111/pjproject/pjlib-util/include -I/home/vsedyshev/Work/1111/pjproject/pjnath/include -I/home/vsedyshev/Work/1111/pjproject/pjmedia/include -I/home/vsedyshev/Work/1111/pjproject/pjsip/include " SAMPLE_CXXFLAGS="-g -O2 -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1 -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -I/home/vsedyshev/Work/1111/pjproject/pjlib/include -I/home/vsedyshev/Work/1111/pjproject/pjlib-util/include -I/home/vsedyshev/Work/1111/pjproject/pjnath/include -I/home/vsedyshev/Work/1111/pjproject/pjmedia/include -I/home/vsedyshev/Work/1111/pjproject/pjsip/include " SAMPLE_LDFLAGS="-L/home/vsedyshev/Work/1111/pjproject/pjlib/lib -L/home/vsedyshev/Work/1111/pjproject/pjlib-util/lib -L/home/vsedyshev/Work/1111/pjproject/pjnath/lib -L/home/vsedyshev/Work/1111/pjproject/pjmedia/lib -L/home/vsedyshev/Work/1111/pjproject/pjsip/lib -L/home/vsedyshev/Work/1111/pjproject/third_party/lib -lSDL2     -lSDL2      -lpjsua-x86_64-unknown-linux-gnu -lpjsip-ua-x86_64-unknown-linux-gnu -lpjsip-simple-x86_64-unknown-linux-gnu -lpjsip-x86_64-unknown-linux-gnu -lpjmedia-codec-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjmedia-videodev-x86_64-unknown-linux-gnu -lpjmedia-audiodev-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjnath-x86_64-unknown-linux-gnu -lpjlib-util-x86_64-unknown-linux-gnu  -lsrtp-x86_64-unknown-linux-gnu -lresample-x86_64-unknown-linux-gnu -lgsmcodec-x86_64-unknown-linux-gnu -lspeex-x86_64-unknown-linux-gnu -lilbccodec-x86_64-unknown-linux-gnu -lg7221codec-x86_64-unknown-linux-gnu -lyuv-x86_64-unknown-linux-gnu -lwebrtc-x86_64-unknown-linux-gnu  -lpj-x86_64-unknown-linux-gnu -lssl -lcrypto -luuid -lm -lrt -lpthread  -lasound -lSDL2   " SAMPLE_EXE=aectest APP=SAMPLE app=sample ../bin/samples/x86_64-unknown-linux-gnu/aectest
# gcc -c -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1 -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -I/home/vsedyshev/Work/1111/pjproject/pjlib/include -I/home/vsedyshev/Work/1111/pjproject/pjlib-util/include -I/home/vsedyshev/Work/1111/pjproject/pjnath/include -I/home/vsedyshev/Work/1111/pjproject/pjmedia/include -I/home/vsedyshev/Work/1111/pjproject/pjsip/include  \
# 	-o output/sample-x86_64-unknown-linux-gnu/aectest.o \
# 	../src/samples/aectest.c 
# if test ! -d ../bin/samples/x86_64-unknown-linux-gnu; then mkdir -p ../bin/samples/x86_64-unknown-linux-gnu; fi
# gcc -o ../bin/samples/x86_64-unknown-linux-gnu/aectest \
#      output/sample-x86_64-unknown-linux-gnu/aectest.o -L/home/vsedyshev/Work/1111/pjproject/pjlib/lib -L/home/vsedyshev/Work/1111/pjproject/pjlib-util/lib -L/home/vsedyshev/Work/1111/pjproject/pjnath/lib -L/home/vsedyshev/Work/1111/pjproject/pjmedia/lib -L/home/vsedyshev/Work/1111/pjproject/pjsip/lib -L/home/vsedyshev/Work/1111/pjproject/third_party/lib -lSDL2     -lSDL2      -lpjsua-x86_64-unknown-linux-gnu -lpjsip-ua-x86_64-unknown-linux-gnu -lpjsip-simple-x86_64-unknown-linux-gnu -lpjsip-x86_64-unknown-linux-gnu -lpjmedia-codec-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjmedia-videodev-x86_64-unknown-linux-gnu -lpjmedia-audiodev-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjnath-x86_64-unknown-linux-gnu -lpjlib-util-x86_64-unknown-linux-gnu  -lsrtp-x86_64-unknown-linux-gnu -lresample-x86_64-unknown-linux-gnu -lgsmcodec-x86_64-unknown-linux-gnu -lspeex-x86_64-unknown-linux-gnu -lilbccodec-x86_64-unknown-linux-gnu -lg7221codec-x86_64-unknown-linux-gnu -lyuv-x86_64-unknown-linux-gnu -lwebrtc-x86_64-unknown-linux-gnu  -lpj-x86_64-unknown-linux-gnu -lssl -lcrypto -luuid -lm -lrt -lpthread  -lasound -lSDL2   
# make --no-print-directory -f /home/vsedyshev/Work/1111/pjproject/build/rules.mak SAMPLE_SRCDIR=../src/samples SAMPLE_OBJS=clidemo.o SAMPLE_CFLAGS="-DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1 -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -I/home/vsedyshev/Work/1111/pjproject/pjlib/include -I/home/vsedyshev/Work/1111/pjproject/pjlib-util/include -I/home/vsedyshev/Work/1111/pjproject/pjnath/include -I/home/vsedyshev/Work/1111/pjproject/pjmedia/include -I/home/vsedyshev/Work/1111/pjproject/pjsip/include " SAMPLE_CXXFLAGS="-g -O2 -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1 -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -I/home/vsedyshev/Work/1111/pjproject/pjlib/include -I/home/vsedyshev/Work/1111/pjproject/pjlib-util/include -I/home/vsedyshev/Work/1111/pjproject/pjnath/include -I/home/vsedyshev/Work/1111/pjproject/pjmedia/include -I/home/vsedyshev/Work/1111/pjproject/pjsip/include " SAMPLE_LDFLAGS="-L/home/vsedyshev/Work/1111/pjproject/pjlib/lib -L/home/vsedyshev/Work/1111/pjproject/pjlib-util/lib -L/home/vsedyshev/Work/1111/pjproject/pjnath/lib -L/home/vsedyshev/Work/1111/pjproject/pjmedia/lib -L/home/vsedyshev/Work/1111/pjproject/pjsip/lib -L/home/vsedyshev/Work/1111/pjproject/third_party/lib -lSDL2     -lSDL2      -lpjsua-x86_64-unknown-linux-gnu -lpjsip-ua-x86_64-unknown-linux-gnu -lpjsip-simple-x86_64-unknown-linux-gnu -lpjsip-x86_64-unknown-linux-gnu -lpjmedia-codec-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjmedia-videodev-x86_64-unknown-linux-gnu -lpjmedia-audiodev-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjnath-x86_64-unknown-linux-gnu -lpjlib-util-x86_64-unknown-linux-gnu  -lsrtp-x86_64-unknown-linux-gnu -lresample-x86_64-unknown-linux-gnu -lgsmcodec-x86_64-unknown-linux-gnu -lspeex-x86_64-unknown-linux-gnu -lilbccodec-x86_64-unknown-linux-gnu -lg7221codec-x86_64-unknown-linux-gnu -lyuv-x86_64-unknown-linux-gnu -lwebrtc-x86_64-unknown-linux-gnu  -lpj-x86_64-unknown-linux-gnu -lssl -lcrypto -luuid -lm -lrt -lpthread  -lasound -lSDL2   " SAMPLE_EXE=clidemo APP=SAMPLE app=sample ../bin/samples/x86_64-unknown-linux-gnu/clidemo
# gcc -c -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1 -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -I/home/vsedyshev/Work/1111/pjproject/pjlib/include -I/home/vsedyshev/Work/1111/pjproject/pjlib-util/include -I/home/vsedyshev/Work/1111/pjproject/pjnath/include -I/home/vsedyshev/Work/1111/pjproject/pjmedia/include -I/home/vsedyshev/Work/1111/pjproject/pjsip/include  \
# 	-o output/sample-x86_64-unknown-linux-gnu/clidemo.o \
# 	../src/samples/clidemo.c 
# if test ! -d ../bin/samples/x86_64-unknown-linux-gnu; then mkdir -p ../bin/samples/x86_64-unknown-linux-gnu; fi
# gcc -o ../bin/samples/x86_64-unknown-linux-gnu/clidemo \
#      output/sample-x86_64-unknown-linux-gnu/clidemo.o -L/home/vsedyshev/Work/1111/pjproject/pjlib/lib -L/home/vsedyshev/Work/1111/pjproject/pjlib-util/lib -L/home/vsedyshev/Work/1111/pjproject/pjnath/lib -L/home/vsedyshev/Work/1111/pjproject/pjmedia/lib -L/home/vsedyshev/Work/1111/pjproject/pjsip/lib -L/home/vsedyshev/Work/1111/pjproject/third_party/lib -lSDL2     -lSDL2      -lpjsua-x86_64-unknown-linux-gnu -lpjsip-ua-x86_64-unknown-linux-gnu -lpjsip-simple-x86_64-unknown-linux-gnu -lpjsip-x86_64-unknown-linux-gnu -lpjmedia-codec-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjmedia-videodev-x86_64-unknown-linux-gnu -lpjmedia-audiodev-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjnath-x86_64-unknown-linux-gnu -lpjlib-util-x86_64-unknown-linux-gnu  -lsrtp-x86_64-unknown-linux-gnu -lresample-x86_64-unknown-linux-gnu -lgsmcodec-x86_64-unknown-linux-gnu -lspeex-x86_64-unknown-linux-gnu -lilbccodec-x86_64-unknown-linux-gnu -lg7221codec-x86_64-unknown-linux-gnu -lyuv-x86_64-unknown-linux-gnu -lwebrtc-x86_64-unknown-linux-gnu  -lpj-x86_64-unknown-linux-gnu -lssl -lcrypto -luuid -lm -lrt -lpthread  -lasound -lSDL2   
# make --no-print-directory -f /home/vsedyshev/Work/1111/pjproject/build/rules.mak SAMPLE_SRCDIR=../src/samples SAMPLE_OBJS=confsample.o SAMPLE_CFLAGS="-DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1 -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -I/home/vsedyshev/Work/1111/pjproject/pjlib/include -I/home/vsedyshev/Work/1111/pjproject/pjlib-util/include -I/home/vsedyshev/Work/1111/pjproject/pjnath/include -I/home/vsedyshev/Work/1111/pjproject/pjmedia/include -I/home/vsedyshev/Work/1111/pjproject/pjsip/include " SAMPLE_CXXFLAGS="-g -O2 -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1 -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -I/home/vsedyshev/Work/1111/pjproject/pjlib/include -I/home/vsedyshev/Work/1111/pjproject/pjlib-util/include -I/home/vsedyshev/Work/1111/pjproject/pjnath/include -I/home/vsedyshev/Work/1111/pjproject/pjmedia/include -I/home/vsedyshev/Work/1111/pjproject/pjsip/include " SAMPLE_LDFLAGS="-L/home/vsedyshev/Work/1111/pjproject/pjlib/lib -L/home/vsedyshev/Work/1111/pjproject/pjlib-util/lib -L/home/vsedyshev/Work/1111/pjproject/pjnath/lib -L/home/vsedyshev/Work/1111/pjproject/pjmedia/lib -L/home/vsedyshev/Work/1111/pjproject/pjsip/lib -L/home/vsedyshev/Work/1111/pjproject/third_party/lib -lSDL2     -lSDL2      -lpjsua-x86_64-unknown-linux-gnu -lpjsip-ua-x86_64-unknown-linux-gnu -lpjsip-simple-x86_64-unknown-linux-gnu -lpjsip-x86_64-unknown-linux-gnu -lpjmedia-codec-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjmedia-videodev-x86_64-unknown-linux-gnu -lpjmedia-audiodev-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjnath-x86_64-unknown-linux-gnu -lpjlib-util-x86_64-unknown-linux-gnu  -lsrtp-x86_64-unknown-linux-gnu -lresample-x86_64-unknown-linux-gnu -lgsmcodec-x86_64-unknown-linux-gnu -lspeex-x86_64-unknown-linux-gnu -lilbccodec-x86_64-unknown-linux-gnu -lg7221codec-x86_64-unknown-linux-gnu -lyuv-x86_64-unknown-linux-gnu -lwebrtc-x86_64-unknown-linux-gnu  -lpj-x86_64-unknown-linux-gnu -lssl -lcrypto -luuid -lm -lrt -lpthread  -lasound -lSDL2   " SAMPLE_EXE=confsample APP=SAMPLE app=sample ../bin/samples/x86_64-unknown-linux-gnu/confsample
# gcc -c -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1 -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -I/home/vsedyshev/Work/1111/pjproject/pjlib/include -I/home/vsedyshev/Work/1111/pjproject/pjlib-util/include -I/home/vsedyshev/Work/1111/pjproject/pjnath/include -I/home/vsedyshev/Work/1111/pjproject/pjmedia/include -I/home/vsedyshev/Work/1111/pjproject/pjsip/include  \
# 	-o output/sample-x86_64-unknown-linux-gnu/confsample.o \
# 	../src/samples/confsample.c 
# if test ! -d ../bin/samples/x86_64-unknown-linux-gnu; then mkdir -p ../bin/samples/x86_64-unknown-linux-gnu; fi
# gcc -o ../bin/samples/x86_64-unknown-linux-gnu/confsample \
#      output/sample-x86_64-unknown-linux-gnu/confsample.o -L/home/vsedyshev/Work/1111/pjproject/pjlib/lib -L/home/vsedyshev/Work/1111/pjproject/pjlib-util/lib -L/home/vsedyshev/Work/1111/pjproject/pjnath/lib -L/home/vsedyshev/Work/1111/pjproject/pjmedia/lib -L/home/vsedyshev/Work/1111/pjproject/pjsip/lib -L/home/vsedyshev/Work/1111/pjproject/third_party/lib -lSDL2     -lSDL2      -lpjsua-x86_64-unknown-linux-gnu -lpjsip-ua-x86_64-unknown-linux-gnu -lpjsip-simple-x86_64-unknown-linux-gnu -lpjsip-x86_64-unknown-linux-gnu -lpjmedia-codec-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjmedia-videodev-x86_64-unknown-linux-gnu -lpjmedia-audiodev-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjnath-x86_64-unknown-linux-gnu -lpjlib-util-x86_64-unknown-linux-gnu  -lsrtp-x86_64-unknown-linux-gnu -lresample-x86_64-unknown-linux-gnu -lgsmcodec-x86_64-unknown-linux-gnu -lspeex-x86_64-unknown-linux-gnu -lilbccodec-x86_64-unknown-linux-gnu -lg7221codec-x86_64-unknown-linux-gnu -lyuv-x86_64-unknown-linux-gnu -lwebrtc-x86_64-unknown-linux-gnu  -lpj-x86_64-unknown-linux-gnu -lssl -lcrypto -luuid -lm -lrt -lpthread  -lasound -lSDL2   
# make --no-print-directory -f /home/vsedyshev/Work/1111/pjproject/build/rules.mak SAMPLE_SRCDIR=../src/samples SAMPLE_OBJS=encdec.o SAMPLE_CFLAGS="-DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1 -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -I/home/vsedyshev/Work/1111/pjproject/pjlib/include -I/home/vsedyshev/Work/1111/pjproject/pjlib-util/include -I/home/vsedyshev/Work/1111/pjproject/pjnath/include -I/home/vsedyshev/Work/1111/pjproject/pjmedia/include -I/home/vsedyshev/Work/1111/pjproject/pjsip/include " SAMPLE_CXXFLAGS="-g -O2 -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1 -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -I/home/vsedyshev/Work/1111/pjproject/pjlib/include -I/home/vsedyshev/Work/1111/pjproject/pjlib-util/include -I/home/vsedyshev/Work/1111/pjproject/pjnath/include -I/home/vsedyshev/Work/1111/pjproject/pjmedia/include -I/home/vsedyshev/Work/1111/pjproject/pjsip/include " SAMPLE_LDFLAGS="-L/home/vsedyshev/Work/1111/pjproject/pjlib/lib -L/home/vsedyshev/Work/1111/pjproject/pjlib-util/lib -L/home/vsedyshev/Work/1111/pjproject/pjnath/lib -L/home/vsedyshev/Work/1111/pjproject/pjmedia/lib -L/home/vsedyshev/Work/1111/pjproject/pjsip/lib -L/home/vsedyshev/Work/1111/pjproject/third_party/lib -lSDL2     -lSDL2      -lpjsua-x86_64-unknown-linux-gnu -lpjsip-ua-x86_64-unknown-linux-gnu -lpjsip-simple-x86_64-unknown-linux-gnu -lpjsip-x86_64-unknown-linux-gnu -lpjmedia-codec-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjmedia-videodev-x86_64-unknown-linux-gnu -lpjmedia-audiodev-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjnath-x86_64-unknown-linux-gnu -lpjlib-util-x86_64-unknown-linux-gnu  -lsrtp-x86_64-unknown-linux-gnu -lresample-x86_64-unknown-linux-gnu -lgsmcodec-x86_64-unknown-linux-gnu -lspeex-x86_64-unknown-linux-gnu -lilbccodec-x86_64-unknown-linux-gnu -lg7221codec-x86_64-unknown-linux-gnu -lyuv-x86_64-unknown-linux-gnu -lwebrtc-x86_64-unknown-linux-gnu  -lpj-x86_64-unknown-linux-gnu -lssl -lcrypto -luuid -lm -lrt -lpthread  -lasound -lSDL2   " SAMPLE_EXE=encdec APP=SAMPLE app=sample ../bin/samples/x86_64-unknown-linux-gnu/encdec
# gcc -c -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1 -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -I/home/vsedyshev/Work/1111/pjproject/pjlib/include -I/home/vsedyshev/Work/1111/pjproject/pjlib-util/include -I/home/vsedyshev/Work/1111/pjproject/pjnath/include -I/home/vsedyshev/Work/1111/pjproject/pjmedia/include -I/home/vsedyshev/Work/1111/pjproject/pjsip/include  \
# 	-o output/sample-x86_64-unknown-linux-gnu/encdec.o \
# 	../src/samples/encdec.c 
# if test ! -d ../bin/samples/x86_64-unknown-linux-gnu; then mkdir -p ../bin/samples/x86_64-unknown-linux-gnu; fi
# gcc -o ../bin/samples/x86_64-unknown-linux-gnu/encdec \
#      output/sample-x86_64-unknown-linux-gnu/encdec.o -L/home/vsedyshev/Work/1111/pjproject/pjlib/lib -L/home/vsedyshev/Work/1111/pjproject/pjlib-util/lib -L/home/vsedyshev/Work/1111/pjproject/pjnath/lib -L/home/vsedyshev/Work/1111/pjproject/pjmedia/lib -L/home/vsedyshev/Work/1111/pjproject/pjsip/lib -L/home/vsedyshev/Work/1111/pjproject/third_party/lib -lSDL2     -lSDL2      -lpjsua-x86_64-unknown-linux-gnu -lpjsip-ua-x86_64-unknown-linux-gnu -lpjsip-simple-x86_64-unknown-linux-gnu -lpjsip-x86_64-unknown-linux-gnu -lpjmedia-codec-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjmedia-videodev-x86_64-unknown-linux-gnu -lpjmedia-audiodev-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjnath-x86_64-unknown-linux-gnu -lpjlib-util-x86_64-unknown-linux-gnu  -lsrtp-x86_64-unknown-linux-gnu -lresample-x86_64-unknown-linux-gnu -lgsmcodec-x86_64-unknown-linux-gnu -lspeex-x86_64-unknown-linux-gnu -lilbccodec-x86_64-unknown-linux-gnu -lg7221codec-x86_64-unknown-linux-gnu -lyuv-x86_64-unknown-linux-gnu -lwebrtc-x86_64-unknown-linux-gnu  -lpj-x86_64-unknown-linux-gnu -lssl -lcrypto -luuid -lm -lrt -lpthread  -lasound -lSDL2   
# make --no-print-directory -f /home/vsedyshev/Work/1111/pjproject/build/rules.mak SAMPLE_SRCDIR=../src/samples SAMPLE_OBJS=httpdemo.o SAMPLE_CFLAGS="-DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1 -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -I/home/vsedyshev/Work/1111/pjproject/pjlib/include -I/home/vsedyshev/Work/1111/pjproject/pjlib-util/include -I/home/vsedyshev/Work/1111/pjproject/pjnath/include -I/home/vsedyshev/Work/1111/pjproject/pjmedia/include -I/home/vsedyshev/Work/1111/pjproject/pjsip/include " SAMPLE_CXXFLAGS="-g -O2 -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1 -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -I/home/vsedyshev/Work/1111/pjproject/pjlib/include -I/home/vsedyshev/Work/1111/pjproject/pjlib-util/include -I/home/vsedyshev/Work/1111/pjproject/pjnath/include -I/home/vsedyshev/Work/1111/pjproject/pjmedia/include -I/home/vsedyshev/Work/1111/pjproject/pjsip/include " SAMPLE_LDFLAGS="-L/home/vsedyshev/Work/1111/pjproject/pjlib/lib -L/home/vsedyshev/Work/1111/pjproject/pjlib-util/lib -L/home/vsedyshev/Work/1111/pjproject/pjnath/lib -L/home/vsedyshev/Work/1111/pjproject/pjmedia/lib -L/home/vsedyshev/Work/1111/pjproject/pjsip/lib -L/home/vsedyshev/Work/1111/pjproject/third_party/lib -lSDL2     -lSDL2      -lpjsua-x86_64-unknown-linux-gnu -lpjsip-ua-x86_64-unknown-linux-gnu -lpjsip-simple-x86_64-unknown-linux-gnu -lpjsip-x86_64-unknown-linux-gnu -lpjmedia-codec-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjmedia-videodev-x86_64-unknown-linux-gnu -lpjmedia-audiodev-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjnath-x86_64-unknown-linux-gnu -lpjlib-util-x86_64-unknown-linux-gnu  -lsrtp-x86_64-unknown-linux-gnu -lresample-x86_64-unknown-linux-gnu -lgsmcodec-x86_64-unknown-linux-gnu -lspeex-x86_64-unknown-linux-gnu -lilbccodec-x86_64-unknown-linux-gnu -lg7221codec-x86_64-unknown-linux-gnu -lyuv-x86_64-unknown-linux-gnu -lwebrtc-x86_64-unknown-linux-gnu  -lpj-x86_64-unknown-linux-gnu -lssl -lcrypto -luuid -lm -lrt -lpthread  -lasound -lSDL2   " SAMPLE_EXE=httpdemo APP=SAMPLE app=sample ../bin/samples/x86_64-unknown-linux-gnu/httpdemo
# gcc -c -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1 -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -I/home/vsedyshev/Work/1111/pjproject/pjlib/include -I/home/vsedyshev/Work/1111/pjproject/pjlib-util/include -I/home/vsedyshev/Work/1111/pjproject/pjnath/include -I/home/vsedyshev/Work/1111/pjproject/pjmedia/include -I/home/vsedyshev/Work/1111/pjproject/pjsip/include  \
# 	-o output/sample-x86_64-unknown-linux-gnu/httpdemo.o \
# 	../src/samples/httpdemo.c 
# if test ! -d ../bin/samples/x86_64-unknown-linux-gnu; then mkdir -p ../bin/samples/x86_64-unknown-linux-gnu; fi
# gcc -o ../bin/samples/x86_64-unknown-linux-gnu/httpdemo \
#      output/sample-x86_64-unknown-linux-gnu/httpdemo.o -L/home/vsedyshev/Work/1111/pjproject/pjlib/lib -L/home/vsedyshev/Work/1111/pjproject/pjlib-util/lib -L/home/vsedyshev/Work/1111/pjproject/pjnath/lib -L/home/vsedyshev/Work/1111/pjproject/pjmedia/lib -L/home/vsedyshev/Work/1111/pjproject/pjsip/lib -L/home/vsedyshev/Work/1111/pjproject/third_party/lib -lSDL2     -lSDL2      -lpjsua-x86_64-unknown-linux-gnu -lpjsip-ua-x86_64-unknown-linux-gnu -lpjsip-simple-x86_64-unknown-linux-gnu -lpjsip-x86_64-unknown-linux-gnu -lpjmedia-codec-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjmedia-videodev-x86_64-unknown-linux-gnu -lpjmedia-audiodev-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjnath-x86_64-unknown-linux-gnu -lpjlib-util-x86_64-unknown-linux-gnu  -lsrtp-x86_64-unknown-linux-gnu -lresample-x86_64-unknown-linux-gnu -lgsmcodec-x86_64-unknown-linux-gnu -lspeex-x86_64-unknown-linux-gnu -lilbccodec-x86_64-unknown-linux-gnu -lg7221codec-x86_64-unknown-linux-gnu -lyuv-x86_64-unknown-linux-gnu -lwebrtc-x86_64-unknown-linux-gnu  -lpj-x86_64-unknown-linux-gnu -lssl -lcrypto -luuid -lm -lrt -lpthread  -lasound -lSDL2   
# make --no-print-directory -f /home/vsedyshev/Work/1111/pjproject/build/rules.mak SAMPLE_SRCDIR=../src/samples SAMPLE_OBJS=icedemo.o SAMPLE_CFLAGS="-DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1 -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -I/home/vsedyshev/Work/1111/pjproject/pjlib/include -I/home/vsedyshev/Work/1111/pjproject/pjlib-util/include -I/home/vsedyshev/Work/1111/pjproject/pjnath/include -I/home/vsedyshev/Work/1111/pjproject/pjmedia/include -I/home/vsedyshev/Work/1111/pjproject/pjsip/include " SAMPLE_CXXFLAGS="-g -O2 -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1 -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -I/home/vsedyshev/Work/1111/pjproject/pjlib/include -I/home/vsedyshev/Work/1111/pjproject/pjlib-util/include -I/home/vsedyshev/Work/1111/pjproject/pjnath/include -I/home/vsedyshev/Work/1111/pjproject/pjmedia/include -I/home/vsedyshev/Work/1111/pjproject/pjsip/include " SAMPLE_LDFLAGS="-L/home/vsedyshev/Work/1111/pjproject/pjlib/lib -L/home/vsedyshev/Work/1111/pjproject/pjlib-util/lib -L/home/vsedyshev/Work/1111/pjproject/pjnath/lib -L/home/vsedyshev/Work/1111/pjproject/pjmedia/lib -L/home/vsedyshev/Work/1111/pjproject/pjsip/lib -L/home/vsedyshev/Work/1111/pjproject/third_party/lib -lSDL2     -lSDL2      -lpjsua-x86_64-unknown-linux-gnu -lpjsip-ua-x86_64-unknown-linux-gnu -lpjsip-simple-x86_64-unknown-linux-gnu -lpjsip-x86_64-unknown-linux-gnu -lpjmedia-codec-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjmedia-videodev-x86_64-unknown-linux-gnu -lpjmedia-audiodev-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjnath-x86_64-unknown-linux-gnu -lpjlib-util-x86_64-unknown-linux-gnu  -lsrtp-x86_64-unknown-linux-gnu -lresample-x86_64-unknown-linux-gnu -lgsmcodec-x86_64-unknown-linux-gnu -lspeex-x86_64-unknown-linux-gnu -lilbccodec-x86_64-unknown-linux-gnu -lg7221codec-x86_64-unknown-linux-gnu -lyuv-x86_64-unknown-linux-gnu -lwebrtc-x86_64-unknown-linux-gnu  -lpj-x86_64-unknown-linux-gnu -lssl -lcrypto -luuid -lm -lrt -lpthread  -lasound -lSDL2   " SAMPLE_EXE=icedemo APP=SAMPLE app=sample ../bin/samples/x86_64-unknown-linux-gnu/icedemo
# gcc -c -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1 -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -I/home/vsedyshev/Work/1111/pjproject/pjlib/include -I/home/vsedyshev/Work/1111/pjproject/pjlib-util/include -I/home/vsedyshev/Work/1111/pjproject/pjnath/include -I/home/vsedyshev/Work/1111/pjproject/pjmedia/include -I/home/vsedyshev/Work/1111/pjproject/pjsip/include  \
# 	-o output/sample-x86_64-unknown-linux-gnu/icedemo.o \
# 	../src/samples/icedemo.c 
# if test ! -d ../bin/samples/x86_64-unknown-linux-gnu; then mkdir -p ../bin/samples/x86_64-unknown-linux-gnu; fi
# gcc -o ../bin/samples/x86_64-unknown-linux-gnu/icedemo \
#      output/sample-x86_64-unknown-linux-gnu/icedemo.o -L/home/vsedyshev/Work/1111/pjproject/pjlib/lib -L/home/vsedyshev/Work/1111/pjproject/pjlib-util/lib -L/home/vsedyshev/Work/1111/pjproject/pjnath/lib -L/home/vsedyshev/Work/1111/pjproject/pjmedia/lib -L/home/vsedyshev/Work/1111/pjproject/pjsip/lib -L/home/vsedyshev/Work/1111/pjproject/third_party/lib -lSDL2     -lSDL2      -lpjsua-x86_64-unknown-linux-gnu -lpjsip-ua-x86_64-unknown-linux-gnu -lpjsip-simple-x86_64-unknown-linux-gnu -lpjsip-x86_64-unknown-linux-gnu -lpjmedia-codec-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjmedia-videodev-x86_64-unknown-linux-gnu -lpjmedia-audiodev-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjnath-x86_64-unknown-linux-gnu -lpjlib-util-x86_64-unknown-linux-gnu  -lsrtp-x86_64-unknown-linux-gnu -lresample-x86_64-unknown-linux-gnu -lgsmcodec-x86_64-unknown-linux-gnu -lspeex-x86_64-unknown-linux-gnu -lilbccodec-x86_64-unknown-linux-gnu -lg7221codec-x86_64-unknown-linux-gnu -lyuv-x86_64-unknown-linux-gnu -lwebrtc-x86_64-unknown-linux-gnu  -lpj-x86_64-unknown-linux-gnu -lssl -lcrypto -luuid -lm -lrt -lpthread  -lasound -lSDL2   
# make --no-print-directory -f /home/vsedyshev/Work/1111/pjproject/build/rules.mak SAMPLE_SRCDIR=../src/samples SAMPLE_OBJS=jbsim.o SAMPLE_CFLAGS="-DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1 -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -I/home/vsedyshev/Work/1111/pjproject/pjlib/include -I/home/vsedyshev/Work/1111/pjproject/pjlib-util/include -I/home/vsedyshev/Work/1111/pjproject/pjnath/include -I/home/vsedyshev/Work/1111/pjproject/pjmedia/include -I/home/vsedyshev/Work/1111/pjproject/pjsip/include " SAMPLE_CXXFLAGS="-g -O2 -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1 -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -I/home/vsedyshev/Work/1111/pjproject/pjlib/include -I/home/vsedyshev/Work/1111/pjproject/pjlib-util/include -I/home/vsedyshev/Work/1111/pjproject/pjnath/include -I/home/vsedyshev/Work/1111/pjproject/pjmedia/include -I/home/vsedyshev/Work/1111/pjproject/pjsip/include " SAMPLE_LDFLAGS="-L/home/vsedyshev/Work/1111/pjproject/pjlib/lib -L/home/vsedyshev/Work/1111/pjproject/pjlib-util/lib -L/home/vsedyshev/Work/1111/pjproject/pjnath/lib -L/home/vsedyshev/Work/1111/pjproject/pjmedia/lib -L/home/vsedyshev/Work/1111/pjproject/pjsip/lib -L/home/vsedyshev/Work/1111/pjproject/third_party/lib -lSDL2     -lSDL2      -lpjsua-x86_64-unknown-linux-gnu -lpjsip-ua-x86_64-unknown-linux-gnu -lpjsip-simple-x86_64-unknown-linux-gnu -lpjsip-x86_64-unknown-linux-gnu -lpjmedia-codec-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjmedia-videodev-x86_64-unknown-linux-gnu -lpjmedia-audiodev-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjnath-x86_64-unknown-linux-gnu -lpjlib-util-x86_64-unknown-linux-gnu  -lsrtp-x86_64-unknown-linux-gnu -lresample-x86_64-unknown-linux-gnu -lgsmcodec-x86_64-unknown-linux-gnu -lspeex-x86_64-unknown-linux-gnu -lilbccodec-x86_64-unknown-linux-gnu -lg7221codec-x86_64-unknown-linux-gnu -lyuv-x86_64-unknown-linux-gnu -lwebrtc-x86_64-unknown-linux-gnu  -lpj-x86_64-unknown-linux-gnu -lssl -lcrypto -luuid -lm -lrt -lpthread  -lasound -lSDL2   " SAMPLE_EXE=jbsim APP=SAMPLE app=sample ../bin/samples/x86_64-unknown-linux-gnu/jbsim
# gcc -c -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1 -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -I/home/vsedyshev/Work/1111/pjproject/pjlib/include -I/home/vsedyshev/Work/1111/pjproject/pjlib-util/include -I/home/vsedyshev/Work/1111/pjproject/pjnath/include -I/home/vsedyshev/Work/1111/pjproject/pjmedia/include -I/home/vsedyshev/Work/1111/pjproject/pjsip/include  \
# 	-o output/sample-x86_64-unknown-linux-gnu/jbsim.o \
# 	../src/samples/jbsim.c 
# if test ! -d ../bin/samples/x86_64-unknown-linux-gnu; then mkdir -p ../bin/samples/x86_64-unknown-linux-gnu; fi
# gcc -o ../bin/samples/x86_64-unknown-linux-gnu/jbsim \
#      output/sample-x86_64-unknown-linux-gnu/jbsim.o -L/home/vsedyshev/Work/1111/pjproject/pjlib/lib -L/home/vsedyshev/Work/1111/pjproject/pjlib-util/lib -L/home/vsedyshev/Work/1111/pjproject/pjnath/lib -L/home/vsedyshev/Work/1111/pjproject/pjmedia/lib -L/home/vsedyshev/Work/1111/pjproject/pjsip/lib -L/home/vsedyshev/Work/1111/pjproject/third_party/lib -lSDL2     -lSDL2      -lpjsua-x86_64-unknown-linux-gnu -lpjsip-ua-x86_64-unknown-linux-gnu -lpjsip-simple-x86_64-unknown-linux-gnu -lpjsip-x86_64-unknown-linux-gnu -lpjmedia-codec-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjmedia-videodev-x86_64-unknown-linux-gnu -lpjmedia-audiodev-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjnath-x86_64-unknown-linux-gnu -lpjlib-util-x86_64-unknown-linux-gnu  -lsrtp-x86_64-unknown-linux-gnu -lresample-x86_64-unknown-linux-gnu -lgsmcodec-x86_64-unknown-linux-gnu -lspeex-x86_64-unknown-linux-gnu -lilbccodec-x86_64-unknown-linux-gnu -lg7221codec-x86_64-unknown-linux-gnu -lyuv-x86_64-unknown-linux-gnu -lwebrtc-x86_64-unknown-linux-gnu  -lpj-x86_64-unknown-linux-gnu -lssl -lcrypto -luuid -lm -lrt -lpthread  -lasound -lSDL2   
# make --no-print-directory -f /home/vsedyshev/Work/1111/pjproject/build/rules.mak SAMPLE_SRCDIR=../src/samples SAMPLE_OBJS=latency.o SAMPLE_CFLAGS="-DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1 -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -I/home/vsedyshev/Work/1111/pjproject/pjlib/include -I/home/vsedyshev/Work/1111/pjproject/pjlib-util/include -I/home/vsedyshev/Work/1111/pjproject/pjnath/include -I/home/vsedyshev/Work/1111/pjproject/pjmedia/include -I/home/vsedyshev/Work/1111/pjproject/pjsip/include " SAMPLE_CXXFLAGS="-g -O2 -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1 -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -I/home/vsedyshev/Work/1111/pjproject/pjlib/include -I/home/vsedyshev/Work/1111/pjproject/pjlib-util/include -I/home/vsedyshev/Work/1111/pjproject/pjnath/include -I/home/vsedyshev/Work/1111/pjproject/pjmedia/include -I/home/vsedyshev/Work/1111/pjproject/pjsip/include " SAMPLE_LDFLAGS="-L/home/vsedyshev/Work/1111/pjproject/pjlib/lib -L/home/vsedyshev/Work/1111/pjproject/pjlib-util/lib -L/home/vsedyshev/Work/1111/pjproject/pjnath/lib -L/home/vsedyshev/Work/1111/pjproject/pjmedia/lib -L/home/vsedyshev/Work/1111/pjproject/pjsip/lib -L/home/vsedyshev/Work/1111/pjproject/third_party/lib -lSDL2     -lSDL2      -lpjsua-x86_64-unknown-linux-gnu -lpjsip-ua-x86_64-unknown-linux-gnu -lpjsip-simple-x86_64-unknown-linux-gnu -lpjsip-x86_64-unknown-linux-gnu -lpjmedia-codec-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjmedia-videodev-x86_64-unknown-linux-gnu -lpjmedia-audiodev-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjnath-x86_64-unknown-linux-gnu -lpjlib-util-x86_64-unknown-linux-gnu  -lsrtp-x86_64-unknown-linux-gnu -lresample-x86_64-unknown-linux-gnu -lgsmcodec-x86_64-unknown-linux-gnu -lspeex-x86_64-unknown-linux-gnu -lilbccodec-x86_64-unknown-linux-gnu -lg7221codec-x86_64-unknown-linux-gnu -lyuv-x86_64-unknown-linux-gnu -lwebrtc-x86_64-unknown-linux-gnu  -lpj-x86_64-unknown-linux-gnu -lssl -lcrypto -luuid -lm -lrt -lpthread  -lasound -lSDL2   " SAMPLE_EXE=latency APP=SAMPLE app=sample ../bin/samples/x86_64-unknown-linux-gnu/latency
# gcc -c -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1 -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -I/home/vsedyshev/Work/1111/pjproject/pjlib/include -I/home/vsedyshev/Work/1111/pjproject/pjlib-util/include -I/home/vsedyshev/Work/1111/pjproject/pjnath/include -I/home/vsedyshev/Work/1111/pjproject/pjmedia/include -I/home/vsedyshev/Work/1111/pjproject/pjsip/include  \
# 	-o output/sample-x86_64-unknown-linux-gnu/latency.o \
# 	../src/samples/latency.c 
# if test ! -d ../bin/samples/x86_64-unknown-linux-gnu; then mkdir -p ../bin/samples/x86_64-unknown-linux-gnu; fi
# gcc -o ../bin/samples/x86_64-unknown-linux-gnu/latency \
#      output/sample-x86_64-unknown-linux-gnu/latency.o -L/home/vsedyshev/Work/1111/pjproject/pjlib/lib -L/home/vsedyshev/Work/1111/pjproject/pjlib-util/lib -L/home/vsedyshev/Work/1111/pjproject/pjnath/lib -L/home/vsedyshev/Work/1111/pjproject/pjmedia/lib -L/home/vsedyshev/Work/1111/pjproject/pjsip/lib -L/home/vsedyshev/Work/1111/pjproject/third_party/lib -lSDL2     -lSDL2      -lpjsua-x86_64-unknown-linux-gnu -lpjsip-ua-x86_64-unknown-linux-gnu -lpjsip-simple-x86_64-unknown-linux-gnu -lpjsip-x86_64-unknown-linux-gnu -lpjmedia-codec-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjmedia-videodev-x86_64-unknown-linux-gnu -lpjmedia-audiodev-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjnath-x86_64-unknown-linux-gnu -lpjlib-util-x86_64-unknown-linux-gnu  -lsrtp-x86_64-unknown-linux-gnu -lresample-x86_64-unknown-linux-gnu -lgsmcodec-x86_64-unknown-linux-gnu -lspeex-x86_64-unknown-linux-gnu -lilbccodec-x86_64-unknown-linux-gnu -lg7221codec-x86_64-unknown-linux-gnu -lyuv-x86_64-unknown-linux-gnu -lwebrtc-x86_64-unknown-linux-gnu  -lpj-x86_64-unknown-linux-gnu -lssl -lcrypto -luuid -lm -lrt -lpthread  -lasound -lSDL2   
# make --no-print-directory -f /home/vsedyshev/Work/1111/pjproject/build/rules.mak SAMPLE_SRCDIR=../src/samples SAMPLE_OBJS=level.o SAMPLE_CFLAGS="-DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1 -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -I/home/vsedyshev/Work/1111/pjproject/pjlib/include -I/home/vsedyshev/Work/1111/pjproject/pjlib-util/include -I/home/vsedyshev/Work/1111/pjproject/pjnath/include -I/home/vsedyshev/Work/1111/pjproject/pjmedia/include -I/home/vsedyshev/Work/1111/pjproject/pjsip/include " SAMPLE_CXXFLAGS="-g -O2 -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1 -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -I/home/vsedyshev/Work/1111/pjproject/pjlib/include -I/home/vsedyshev/Work/1111/pjproject/pjlib-util/include -I/home/vsedyshev/Work/1111/pjproject/pjnath/include -I/home/vsedyshev/Work/1111/pjproject/pjmedia/include -I/home/vsedyshev/Work/1111/pjproject/pjsip/include " SAMPLE_LDFLAGS="-L/home/vsedyshev/Work/1111/pjproject/pjlib/lib -L/home/vsedyshev/Work/1111/pjproject/pjlib-util/lib -L/home/vsedyshev/Work/1111/pjproject/pjnath/lib -L/home/vsedyshev/Work/1111/pjproject/pjmedia/lib -L/home/vsedyshev/Work/1111/pjproject/pjsip/lib -L/home/vsedyshev/Work/1111/pjproject/third_party/lib -lSDL2     -lSDL2      -lpjsua-x86_64-unknown-linux-gnu -lpjsip-ua-x86_64-unknown-linux-gnu -lpjsip-simple-x86_64-unknown-linux-gnu -lpjsip-x86_64-unknown-linux-gnu -lpjmedia-codec-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjmedia-videodev-x86_64-unknown-linux-gnu -lpjmedia-audiodev-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjnath-x86_64-unknown-linux-gnu -lpjlib-util-x86_64-unknown-linux-gnu  -lsrtp-x86_64-unknown-linux-gnu -lresample-x86_64-unknown-linux-gnu -lgsmcodec-x86_64-unknown-linux-gnu -lspeex-x86_64-unknown-linux-gnu -lilbccodec-x86_64-unknown-linux-gnu -lg7221codec-x86_64-unknown-linux-gnu -lyuv-x86_64-unknown-linux-gnu -lwebrtc-x86_64-unknown-linux-gnu  -lpj-x86_64-unknown-linux-gnu -lssl -lcrypto -luuid -lm -lrt -lpthread  -lasound -lSDL2   " SAMPLE_EXE=level APP=SAMPLE app=sample ../bin/samples/x86_64-unknown-linux-gnu/level
# gcc -c -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1 -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -I/home/vsedyshev/Work/1111/pjproject/pjlib/include -I/home/vsedyshev/Work/1111/pjproject/pjlib-util/include -I/home/vsedyshev/Work/1111/pjproject/pjnath/include -I/home/vsedyshev/Work/1111/pjproject/pjmedia/include -I/home/vsedyshev/Work/1111/pjproject/pjsip/include  \
# 	-o output/sample-x86_64-unknown-linux-gnu/level.o \
# 	../src/samples/level.c 
# if test ! -d ../bin/samples/x86_64-unknown-linux-gnu; then mkdir -p ../bin/samples/x86_64-unknown-linux-gnu; fi
# gcc -o ../bin/samples/x86_64-unknown-linux-gnu/level \
#      output/sample-x86_64-unknown-linux-gnu/level.o -L/home/vsedyshev/Work/1111/pjproject/pjlib/lib -L/home/vsedyshev/Work/1111/pjproject/pjlib-util/lib -L/home/vsedyshev/Work/1111/pjproject/pjnath/lib -L/home/vsedyshev/Work/1111/pjproject/pjmedia/lib -L/home/vsedyshev/Work/1111/pjproject/pjsip/lib -L/home/vsedyshev/Work/1111/pjproject/third_party/lib -lSDL2     -lSDL2      -lpjsua-x86_64-unknown-linux-gnu -lpjsip-ua-x86_64-unknown-linux-gnu -lpjsip-simple-x86_64-unknown-linux-gnu -lpjsip-x86_64-unknown-linux-gnu -lpjmedia-codec-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjmedia-videodev-x86_64-unknown-linux-gnu -lpjmedia-audiodev-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjnath-x86_64-unknown-linux-gnu -lpjlib-util-x86_64-unknown-linux-gnu  -lsrtp-x86_64-unknown-linux-gnu -lresample-x86_64-unknown-linux-gnu -lgsmcodec-x86_64-unknown-linux-gnu -lspeex-x86_64-unknown-linux-gnu -lilbccodec-x86_64-unknown-linux-gnu -lg7221codec-x86_64-unknown-linux-gnu -lyuv-x86_64-unknown-linux-gnu -lwebrtc-x86_64-unknown-linux-gnu  -lpj-x86_64-unknown-linux-gnu -lssl -lcrypto -luuid -lm -lrt -lpthread  -lasound -lSDL2   
# make --no-print-directory -f /home/vsedyshev/Work/1111/pjproject/build/rules.mak SAMPLE_SRCDIR=../src/samples SAMPLE_OBJS=mix.o SAMPLE_CFLAGS="-DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1 -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -I/home/vsedyshev/Work/1111/pjproject/pjlib/include -I/home/vsedyshev/Work/1111/pjproject/pjlib-util/include -I/home/vsedyshev/Work/1111/pjproject/pjnath/include -I/home/vsedyshev/Work/1111/pjproject/pjmedia/include -I/home/vsedyshev/Work/1111/pjproject/pjsip/include " SAMPLE_CXXFLAGS="-g -O2 -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1 -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -I/home/vsedyshev/Work/1111/pjproject/pjlib/include -I/home/vsedyshev/Work/1111/pjproject/pjlib-util/include -I/home/vsedyshev/Work/1111/pjproject/pjnath/include -I/home/vsedyshev/Work/1111/pjproject/pjmedia/include -I/home/vsedyshev/Work/1111/pjproject/pjsip/include " SAMPLE_LDFLAGS="-L/home/vsedyshev/Work/1111/pjproject/pjlib/lib -L/home/vsedyshev/Work/1111/pjproject/pjlib-util/lib -L/home/vsedyshev/Work/1111/pjproject/pjnath/lib -L/home/vsedyshev/Work/1111/pjproject/pjmedia/lib -L/home/vsedyshev/Work/1111/pjproject/pjsip/lib -L/home/vsedyshev/Work/1111/pjproject/third_party/lib -lSDL2     -lSDL2      -lpjsua-x86_64-unknown-linux-gnu -lpjsip-ua-x86_64-unknown-linux-gnu -lpjsip-simple-x86_64-unknown-linux-gnu -lpjsip-x86_64-unknown-linux-gnu -lpjmedia-codec-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjmedia-videodev-x86_64-unknown-linux-gnu -lpjmedia-audiodev-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjnath-x86_64-unknown-linux-gnu -lpjlib-util-x86_64-unknown-linux-gnu  -lsrtp-x86_64-unknown-linux-gnu -lresample-x86_64-unknown-linux-gnu -lgsmcodec-x86_64-unknown-linux-gnu -lspeex-x86_64-unknown-linux-gnu -lilbccodec-x86_64-unknown-linux-gnu -lg7221codec-x86_64-unknown-linux-gnu -lyuv-x86_64-unknown-linux-gnu -lwebrtc-x86_64-unknown-linux-gnu  -lpj-x86_64-unknown-linux-gnu -lssl -lcrypto -luuid -lm -lrt -lpthread  -lasound -lSDL2   " SAMPLE_EXE=mix APP=SAMPLE app=sample ../bin/samples/x86_64-unknown-linux-gnu/mix
# gcc -c -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1 -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -I/home/vsedyshev/Work/1111/pjproject/pjlib/include -I/home/vsedyshev/Work/1111/pjproject/pjlib-util/include -I/home/vsedyshev/Work/1111/pjproject/pjnath/include -I/home/vsedyshev/Work/1111/pjproject/pjmedia/include -I/home/vsedyshev/Work/1111/pjproject/pjsip/include  \
# 	-o output/sample-x86_64-unknown-linux-gnu/mix.o \
# 	../src/samples/mix.c 
# if test ! -d ../bin/samples/x86_64-unknown-linux-gnu; then mkdir -p ../bin/samples/x86_64-unknown-linux-gnu; fi
# gcc -o ../bin/samples/x86_64-unknown-linux-gnu/mix \
#      output/sample-x86_64-unknown-linux-gnu/mix.o -L/home/vsedyshev/Work/1111/pjproject/pjlib/lib -L/home/vsedyshev/Work/1111/pjproject/pjlib-util/lib -L/home/vsedyshev/Work/1111/pjproject/pjnath/lib -L/home/vsedyshev/Work/1111/pjproject/pjmedia/lib -L/home/vsedyshev/Work/1111/pjproject/pjsip/lib -L/home/vsedyshev/Work/1111/pjproject/third_party/lib -lSDL2     -lSDL2      -lpjsua-x86_64-unknown-linux-gnu -lpjsip-ua-x86_64-unknown-linux-gnu -lpjsip-simple-x86_64-unknown-linux-gnu -lpjsip-x86_64-unknown-linux-gnu -lpjmedia-codec-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjmedia-videodev-x86_64-unknown-linux-gnu -lpjmedia-audiodev-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjnath-x86_64-unknown-linux-gnu -lpjlib-util-x86_64-unknown-linux-gnu  -lsrtp-x86_64-unknown-linux-gnu -lresample-x86_64-unknown-linux-gnu -lgsmcodec-x86_64-unknown-linux-gnu -lspeex-x86_64-unknown-linux-gnu -lilbccodec-x86_64-unknown-linux-gnu -lg7221codec-x86_64-unknown-linux-gnu -lyuv-x86_64-unknown-linux-gnu -lwebrtc-x86_64-unknown-linux-gnu  -lpj-x86_64-unknown-linux-gnu -lssl -lcrypto -luuid -lm -lrt -lpthread  -lasound -lSDL2   
# make --no-print-directory -f /home/vsedyshev/Work/1111/pjproject/build/rules.mak SAMPLE_SRCDIR=../src/samples SAMPLE_OBJS=pjsip-perf.o SAMPLE_CFLAGS="-DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1 -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -I/home/vsedyshev/Work/1111/pjproject/pjlib/include -I/home/vsedyshev/Work/1111/pjproject/pjlib-util/include -I/home/vsedyshev/Work/1111/pjproject/pjnath/include -I/home/vsedyshev/Work/1111/pjproject/pjmedia/include -I/home/vsedyshev/Work/1111/pjproject/pjsip/include " SAMPLE_CXXFLAGS="-g -O2 -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1 -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -I/home/vsedyshev/Work/1111/pjproject/pjlib/include -I/home/vsedyshev/Work/1111/pjproject/pjlib-util/include -I/home/vsedyshev/Work/1111/pjproject/pjnath/include -I/home/vsedyshev/Work/1111/pjproject/pjmedia/include -I/home/vsedyshev/Work/1111/pjproject/pjsip/include " SAMPLE_LDFLAGS="-L/home/vsedyshev/Work/1111/pjproject/pjlib/lib -L/home/vsedyshev/Work/1111/pjproject/pjlib-util/lib -L/home/vsedyshev/Work/1111/pjproject/pjnath/lib -L/home/vsedyshev/Work/1111/pjproject/pjmedia/lib -L/home/vsedyshev/Work/1111/pjproject/pjsip/lib -L/home/vsedyshev/Work/1111/pjproject/third_party/lib -lSDL2     -lSDL2      -lpjsua-x86_64-unknown-linux-gnu -lpjsip-ua-x86_64-unknown-linux-gnu -lpjsip-simple-x86_64-unknown-linux-gnu -lpjsip-x86_64-unknown-linux-gnu -lpjmedia-codec-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjmedia-videodev-x86_64-unknown-linux-gnu -lpjmedia-audiodev-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjnath-x86_64-unknown-linux-gnu -lpjlib-util-x86_64-unknown-linux-gnu  -lsrtp-x86_64-unknown-linux-gnu -lresample-x86_64-unknown-linux-gnu -lgsmcodec-x86_64-unknown-linux-gnu -lspeex-x86_64-unknown-linux-gnu -lilbccodec-x86_64-unknown-linux-gnu -lg7221codec-x86_64-unknown-linux-gnu -lyuv-x86_64-unknown-linux-gnu -lwebrtc-x86_64-unknown-linux-gnu  -lpj-x86_64-unknown-linux-gnu -lssl -lcrypto -luuid -lm -lrt -lpthread  -lasound -lSDL2   " SAMPLE_EXE=pjsip-perf APP=SAMPLE app=sample ../bin/samples/x86_64-unknown-linux-gnu/pjsip-perf
# gcc -c -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1 -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -I/home/vsedyshev/Work/1111/pjproject/pjlib/include -I/home/vsedyshev/Work/1111/pjproject/pjlib-util/include -I/home/vsedyshev/Work/1111/pjproject/pjnath/include -I/home/vsedyshev/Work/1111/pjproject/pjmedia/include -I/home/vsedyshev/Work/1111/pjproject/pjsip/include  \
# 	-o output/sample-x86_64-unknown-linux-gnu/pjsip-perf.o \
# 	../src/samples/pjsip-perf.c 
# if test ! -d ../bin/samples/x86_64-unknown-linux-gnu; then mkdir -p ../bin/samples/x86_64-unknown-linux-gnu; fi
# gcc -o ../bin/samples/x86_64-unknown-linux-gnu/pjsip-perf \
#      output/sample-x86_64-unknown-linux-gnu/pjsip-perf.o -L/home/vsedyshev/Work/1111/pjproject/pjlib/lib -L/home/vsedyshev/Work/1111/pjproject/pjlib-util/lib -L/home/vsedyshev/Work/1111/pjproject/pjnath/lib -L/home/vsedyshev/Work/1111/pjproject/pjmedia/lib -L/home/vsedyshev/Work/1111/pjproject/pjsip/lib -L/home/vsedyshev/Work/1111/pjproject/third_party/lib -lSDL2     -lSDL2      -lpjsua-x86_64-unknown-linux-gnu -lpjsip-ua-x86_64-unknown-linux-gnu -lpjsip-simple-x86_64-unknown-linux-gnu -lpjsip-x86_64-unknown-linux-gnu -lpjmedia-codec-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjmedia-videodev-x86_64-unknown-linux-gnu -lpjmedia-audiodev-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjnath-x86_64-unknown-linux-gnu -lpjlib-util-x86_64-unknown-linux-gnu  -lsrtp-x86_64-unknown-linux-gnu -lresample-x86_64-unknown-linux-gnu -lgsmcodec-x86_64-unknown-linux-gnu -lspeex-x86_64-unknown-linux-gnu -lilbccodec-x86_64-unknown-linux-gnu -lg7221codec-x86_64-unknown-linux-gnu -lyuv-x86_64-unknown-linux-gnu -lwebrtc-x86_64-unknown-linux-gnu  -lpj-x86_64-unknown-linux-gnu -lssl -lcrypto -luuid -lm -lrt -lpthread  -lasound -lSDL2   
# make --no-print-directory -f /home/vsedyshev/Work/1111/pjproject/build/rules.mak SAMPLE_SRCDIR=../src/samples SAMPLE_OBJS=pcaputil.o SAMPLE_CFLAGS="-DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1 -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -I/home/vsedyshev/Work/1111/pjproject/pjlib/include -I/home/vsedyshev/Work/1111/pjproject/pjlib-util/include -I/home/vsedyshev/Work/1111/pjproject/pjnath/include -I/home/vsedyshev/Work/1111/pjproject/pjmedia/include -I/home/vsedyshev/Work/1111/pjproject/pjsip/include " SAMPLE_CXXFLAGS="-g -O2 -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1 -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -I/home/vsedyshev/Work/1111/pjproject/pjlib/include -I/home/vsedyshev/Work/1111/pjproject/pjlib-util/include -I/home/vsedyshev/Work/1111/pjproject/pjnath/include -I/home/vsedyshev/Work/1111/pjproject/pjmedia/include -I/home/vsedyshev/Work/1111/pjproject/pjsip/include " SAMPLE_LDFLAGS="-L/home/vsedyshev/Work/1111/pjproject/pjlib/lib -L/home/vsedyshev/Work/1111/pjproject/pjlib-util/lib -L/home/vsedyshev/Work/1111/pjproject/pjnath/lib -L/home/vsedyshev/Work/1111/pjproject/pjmedia/lib -L/home/vsedyshev/Work/1111/pjproject/pjsip/lib -L/home/vsedyshev/Work/1111/pjproject/third_party/lib -lSDL2     -lSDL2      -lpjsua-x86_64-unknown-linux-gnu -lpjsip-ua-x86_64-unknown-linux-gnu -lpjsip-simple-x86_64-unknown-linux-gnu -lpjsip-x86_64-unknown-linux-gnu -lpjmedia-codec-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjmedia-videodev-x86_64-unknown-linux-gnu -lpjmedia-audiodev-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjnath-x86_64-unknown-linux-gnu -lpjlib-util-x86_64-unknown-linux-gnu  -lsrtp-x86_64-unknown-linux-gnu -lresample-x86_64-unknown-linux-gnu -lgsmcodec-x86_64-unknown-linux-gnu -lspeex-x86_64-unknown-linux-gnu -lilbccodec-x86_64-unknown-linux-gnu -lg7221codec-x86_64-unknown-linux-gnu -lyuv-x86_64-unknown-linux-gnu -lwebrtc-x86_64-unknown-linux-gnu  -lpj-x86_64-unknown-linux-gnu -lssl -lcrypto -luuid -lm -lrt -lpthread  -lasound -lSDL2   " SAMPLE_EXE=pcaputil APP=SAMPLE app=sample ../bin/samples/x86_64-unknown-linux-gnu/pcaputil
# gcc -c -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1 -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -I/home/vsedyshev/Work/1111/pjproject/pjlib/include -I/home/vsedyshev/Work/1111/pjproject/pjlib-util/include -I/home/vsedyshev/Work/1111/pjproject/pjnath/include -I/home/vsedyshev/Work/1111/pjproject/pjmedia/include -I/home/vsedyshev/Work/1111/pjproject/pjsip/include  \
# 	-o output/sample-x86_64-unknown-linux-gnu/pcaputil.o \
# 	../src/samples/pcaputil.c 
# if test ! -d ../bin/samples/x86_64-unknown-linux-gnu; then mkdir -p ../bin/samples/x86_64-unknown-linux-gnu; fi
# gcc -o ../bin/samples/x86_64-unknown-linux-gnu/pcaputil \
#      output/sample-x86_64-unknown-linux-gnu/pcaputil.o -L/home/vsedyshev/Work/1111/pjproject/pjlib/lib -L/home/vsedyshev/Work/1111/pjproject/pjlib-util/lib -L/home/vsedyshev/Work/1111/pjproject/pjnath/lib -L/home/vsedyshev/Work/1111/pjproject/pjmedia/lib -L/home/vsedyshev/Work/1111/pjproject/pjsip/lib -L/home/vsedyshev/Work/1111/pjproject/third_party/lib -lSDL2     -lSDL2      -lpjsua-x86_64-unknown-linux-gnu -lpjsip-ua-x86_64-unknown-linux-gnu -lpjsip-simple-x86_64-unknown-linux-gnu -lpjsip-x86_64-unknown-linux-gnu -lpjmedia-codec-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjmedia-videodev-x86_64-unknown-linux-gnu -lpjmedia-audiodev-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjnath-x86_64-unknown-linux-gnu -lpjlib-util-x86_64-unknown-linux-gnu  -lsrtp-x86_64-unknown-linux-gnu -lresample-x86_64-unknown-linux-gnu -lgsmcodec-x86_64-unknown-linux-gnu -lspeex-x86_64-unknown-linux-gnu -lilbccodec-x86_64-unknown-linux-gnu -lg7221codec-x86_64-unknown-linux-gnu -lyuv-x86_64-unknown-linux-gnu -lwebrtc-x86_64-unknown-linux-gnu  -lpj-x86_64-unknown-linux-gnu -lssl -lcrypto -luuid -lm -lrt -lpthread  -lasound -lSDL2   
# make --no-print-directory -f /home/vsedyshev/Work/1111/pjproject/build/rules.mak SAMPLE_SRCDIR=../src/samples SAMPLE_OBJS=playfile.o SAMPLE_CFLAGS="-DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1 -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -I/home/vsedyshev/Work/1111/pjproject/pjlib/include -I/home/vsedyshev/Work/1111/pjproject/pjlib-util/include -I/home/vsedyshev/Work/1111/pjproject/pjnath/include -I/home/vsedyshev/Work/1111/pjproject/pjmedia/include -I/home/vsedyshev/Work/1111/pjproject/pjsip/include " SAMPLE_CXXFLAGS="-g -O2 -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1 -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -I/home/vsedyshev/Work/1111/pjproject/pjlib/include -I/home/vsedyshev/Work/1111/pjproject/pjlib-util/include -I/home/vsedyshev/Work/1111/pjproject/pjnath/include -I/home/vsedyshev/Work/1111/pjproject/pjmedia/include -I/home/vsedyshev/Work/1111/pjproject/pjsip/include " SAMPLE_LDFLAGS="-L/home/vsedyshev/Work/1111/pjproject/pjlib/lib -L/home/vsedyshev/Work/1111/pjproject/pjlib-util/lib -L/home/vsedyshev/Work/1111/pjproject/pjnath/lib -L/home/vsedyshev/Work/1111/pjproject/pjmedia/lib -L/home/vsedyshev/Work/1111/pjproject/pjsip/lib -L/home/vsedyshev/Work/1111/pjproject/third_party/lib -lSDL2     -lSDL2      -lpjsua-x86_64-unknown-linux-gnu -lpjsip-ua-x86_64-unknown-linux-gnu -lpjsip-simple-x86_64-unknown-linux-gnu -lpjsip-x86_64-unknown-linux-gnu -lpjmedia-codec-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjmedia-videodev-x86_64-unknown-linux-gnu -lpjmedia-audiodev-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjnath-x86_64-unknown-linux-gnu -lpjlib-util-x86_64-unknown-linux-gnu  -lsrtp-x86_64-unknown-linux-gnu -lresample-x86_64-unknown-linux-gnu -lgsmcodec-x86_64-unknown-linux-gnu -lspeex-x86_64-unknown-linux-gnu -lilbccodec-x86_64-unknown-linux-gnu -lg7221codec-x86_64-unknown-linux-gnu -lyuv-x86_64-unknown-linux-gnu -lwebrtc-x86_64-unknown-linux-gnu  -lpj-x86_64-unknown-linux-gnu -lssl -lcrypto -luuid -lm -lrt -lpthread  -lasound -lSDL2   " SAMPLE_EXE=playfile APP=SAMPLE app=sample ../bin/samples/x86_64-unknown-linux-gnu/playfile
# gcc -c -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1 -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -I/home/vsedyshev/Work/1111/pjproject/pjlib/include -I/home/vsedyshev/Work/1111/pjproject/pjlib-util/include -I/home/vsedyshev/Work/1111/pjproject/pjnath/include -I/home/vsedyshev/Work/1111/pjproject/pjmedia/include -I/home/vsedyshev/Work/1111/pjproject/pjsip/include  \
# 	-o output/sample-x86_64-unknown-linux-gnu/playfile.o \
# 	../src/samples/playfile.c 
# if test ! -d ../bin/samples/x86_64-unknown-linux-gnu; then mkdir -p ../bin/samples/x86_64-unknown-linux-gnu; fi
# gcc -o ../bin/samples/x86_64-unknown-linux-gnu/playfile \
#      output/sample-x86_64-unknown-linux-gnu/playfile.o -L/home/vsedyshev/Work/1111/pjproject/pjlib/lib -L/home/vsedyshev/Work/1111/pjproject/pjlib-util/lib -L/home/vsedyshev/Work/1111/pjproject/pjnath/lib -L/home/vsedyshev/Work/1111/pjproject/pjmedia/lib -L/home/vsedyshev/Work/1111/pjproject/pjsip/lib -L/home/vsedyshev/Work/1111/pjproject/third_party/lib -lSDL2     -lSDL2      -lpjsua-x86_64-unknown-linux-gnu -lpjsip-ua-x86_64-unknown-linux-gnu -lpjsip-simple-x86_64-unknown-linux-gnu -lpjsip-x86_64-unknown-linux-gnu -lpjmedia-codec-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjmedia-videodev-x86_64-unknown-linux-gnu -lpjmedia-audiodev-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjnath-x86_64-unknown-linux-gnu -lpjlib-util-x86_64-unknown-linux-gnu  -lsrtp-x86_64-unknown-linux-gnu -lresample-x86_64-unknown-linux-gnu -lgsmcodec-x86_64-unknown-linux-gnu -lspeex-x86_64-unknown-linux-gnu -lilbccodec-x86_64-unknown-linux-gnu -lg7221codec-x86_64-unknown-linux-gnu -lyuv-x86_64-unknown-linux-gnu -lwebrtc-x86_64-unknown-linux-gnu  -lpj-x86_64-unknown-linux-gnu -lssl -lcrypto -luuid -lm -lrt -lpthread  -lasound -lSDL2   
# make --no-print-directory -f /home/vsedyshev/Work/1111/pjproject/build/rules.mak SAMPLE_SRCDIR=../src/samples SAMPLE_OBJS=playsine.o SAMPLE_CFLAGS="-DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1 -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -I/home/vsedyshev/Work/1111/pjproject/pjlib/include -I/home/vsedyshev/Work/1111/pjproject/pjlib-util/include -I/home/vsedyshev/Work/1111/pjproject/pjnath/include -I/home/vsedyshev/Work/1111/pjproject/pjmedia/include -I/home/vsedyshev/Work/1111/pjproject/pjsip/include " SAMPLE_CXXFLAGS="-g -O2 -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1 -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -I/home/vsedyshev/Work/1111/pjproject/pjlib/include -I/home/vsedyshev/Work/1111/pjproject/pjlib-util/include -I/home/vsedyshev/Work/1111/pjproject/pjnath/include -I/home/vsedyshev/Work/1111/pjproject/pjmedia/include -I/home/vsedyshev/Work/1111/pjproject/pjsip/include " SAMPLE_LDFLAGS="-L/home/vsedyshev/Work/1111/pjproject/pjlib/lib -L/home/vsedyshev/Work/1111/pjproject/pjlib-util/lib -L/home/vsedyshev/Work/1111/pjproject/pjnath/lib -L/home/vsedyshev/Work/1111/pjproject/pjmedia/lib -L/home/vsedyshev/Work/1111/pjproject/pjsip/lib -L/home/vsedyshev/Work/1111/pjproject/third_party/lib -lSDL2     -lSDL2      -lpjsua-x86_64-unknown-linux-gnu -lpjsip-ua-x86_64-unknown-linux-gnu -lpjsip-simple-x86_64-unknown-linux-gnu -lpjsip-x86_64-unknown-linux-gnu -lpjmedia-codec-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjmedia-videodev-x86_64-unknown-linux-gnu -lpjmedia-audiodev-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjnath-x86_64-unknown-linux-gnu -lpjlib-util-x86_64-unknown-linux-gnu  -lsrtp-x86_64-unknown-linux-gnu -lresample-x86_64-unknown-linux-gnu -lgsmcodec-x86_64-unknown-linux-gnu -lspeex-x86_64-unknown-linux-gnu -lilbccodec-x86_64-unknown-linux-gnu -lg7221codec-x86_64-unknown-linux-gnu -lyuv-x86_64-unknown-linux-gnu -lwebrtc-x86_64-unknown-linux-gnu  -lpj-x86_64-unknown-linux-gnu -lssl -lcrypto -luuid -lm -lrt -lpthread  -lasound -lSDL2   " SAMPLE_EXE=playsine APP=SAMPLE app=sample ../bin/samples/x86_64-unknown-linux-gnu/playsine
# gcc -c -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1 -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -I/home/vsedyshev/Work/1111/pjproject/pjlib/include -I/home/vsedyshev/Work/1111/pjproject/pjlib-util/include -I/home/vsedyshev/Work/1111/pjproject/pjnath/include -I/home/vsedyshev/Work/1111/pjproject/pjmedia/include -I/home/vsedyshev/Work/1111/pjproject/pjsip/include  \
# 	-o output/sample-x86_64-unknown-linux-gnu/playsine.o \
# 	../src/samples/playsine.c 
# if test ! -d ../bin/samples/x86_64-unknown-linux-gnu; then mkdir -p ../bin/samples/x86_64-unknown-linux-gnu; fi
# gcc -o ../bin/samples/x86_64-unknown-linux-gnu/playsine \
#      output/sample-x86_64-unknown-linux-gnu/playsine.o -L/home/vsedyshev/Work/1111/pjproject/pjlib/lib -L/home/vsedyshev/Work/1111/pjproject/pjlib-util/lib -L/home/vsedyshev/Work/1111/pjproject/pjnath/lib -L/home/vsedyshev/Work/1111/pjproject/pjmedia/lib -L/home/vsedyshev/Work/1111/pjproject/pjsip/lib -L/home/vsedyshev/Work/1111/pjproject/third_party/lib -lSDL2     -lSDL2      -lpjsua-x86_64-unknown-linux-gnu -lpjsip-ua-x86_64-unknown-linux-gnu -lpjsip-simple-x86_64-unknown-linux-gnu -lpjsip-x86_64-unknown-linux-gnu -lpjmedia-codec-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjmedia-videodev-x86_64-unknown-linux-gnu -lpjmedia-audiodev-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjnath-x86_64-unknown-linux-gnu -lpjlib-util-x86_64-unknown-linux-gnu  -lsrtp-x86_64-unknown-linux-gnu -lresample-x86_64-unknown-linux-gnu -lgsmcodec-x86_64-unknown-linux-gnu -lspeex-x86_64-unknown-linux-gnu -lilbccodec-x86_64-unknown-linux-gnu -lg7221codec-x86_64-unknown-linux-gnu -lyuv-x86_64-unknown-linux-gnu -lwebrtc-x86_64-unknown-linux-gnu  -lpj-x86_64-unknown-linux-gnu -lssl -lcrypto -luuid -lm -lrt -lpthread  -lasound -lSDL2   
# make --no-print-directory -f /home/vsedyshev/Work/1111/pjproject/build/rules.mak SAMPLE_SRCDIR=../src/samples SAMPLE_OBJS=recfile.o SAMPLE_CFLAGS="-DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1 -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -I/home/vsedyshev/Work/1111/pjproject/pjlib/include -I/home/vsedyshev/Work/1111/pjproject/pjlib-util/include -I/home/vsedyshev/Work/1111/pjproject/pjnath/include -I/home/vsedyshev/Work/1111/pjproject/pjmedia/include -I/home/vsedyshev/Work/1111/pjproject/pjsip/include " SAMPLE_CXXFLAGS="-g -O2 -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1 -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -I/home/vsedyshev/Work/1111/pjproject/pjlib/include -I/home/vsedyshev/Work/1111/pjproject/pjlib-util/include -I/home/vsedyshev/Work/1111/pjproject/pjnath/include -I/home/vsedyshev/Work/1111/pjproject/pjmedia/include -I/home/vsedyshev/Work/1111/pjproject/pjsip/include " SAMPLE_LDFLAGS="-L/home/vsedyshev/Work/1111/pjproject/pjlib/lib -L/home/vsedyshev/Work/1111/pjproject/pjlib-util/lib -L/home/vsedyshev/Work/1111/pjproject/pjnath/lib -L/home/vsedyshev/Work/1111/pjproject/pjmedia/lib -L/home/vsedyshev/Work/1111/pjproject/pjsip/lib -L/home/vsedyshev/Work/1111/pjproject/third_party/lib -lSDL2     -lSDL2      -lpjsua-x86_64-unknown-linux-gnu -lpjsip-ua-x86_64-unknown-linux-gnu -lpjsip-simple-x86_64-unknown-linux-gnu -lpjsip-x86_64-unknown-linux-gnu -lpjmedia-codec-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjmedia-videodev-x86_64-unknown-linux-gnu -lpjmedia-audiodev-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjnath-x86_64-unknown-linux-gnu -lpjlib-util-x86_64-unknown-linux-gnu  -lsrtp-x86_64-unknown-linux-gnu -lresample-x86_64-unknown-linux-gnu -lgsmcodec-x86_64-unknown-linux-gnu -lspeex-x86_64-unknown-linux-gnu -lilbccodec-x86_64-unknown-linux-gnu -lg7221codec-x86_64-unknown-linux-gnu -lyuv-x86_64-unknown-linux-gnu -lwebrtc-x86_64-unknown-linux-gnu  -lpj-x86_64-unknown-linux-gnu -lssl -lcrypto -luuid -lm -lrt -lpthread  -lasound -lSDL2   " SAMPLE_EXE=recfile APP=SAMPLE app=sample ../bin/samples/x86_64-unknown-linux-gnu/recfile
# gcc -c -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1 -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -I/home/vsedyshev/Work/1111/pjproject/pjlib/include -I/home/vsedyshev/Work/1111/pjproject/pjlib-util/include -I/home/vsedyshev/Work/1111/pjproject/pjnath/include -I/home/vsedyshev/Work/1111/pjproject/pjmedia/include -I/home/vsedyshev/Work/1111/pjproject/pjsip/include  \
# 	-o output/sample-x86_64-unknown-linux-gnu/recfile.o \
# 	../src/samples/recfile.c 
# if test ! -d ../bin/samples/x86_64-unknown-linux-gnu; then mkdir -p ../bin/samples/x86_64-unknown-linux-gnu; fi
# gcc -o ../bin/samples/x86_64-unknown-linux-gnu/recfile \
#      output/sample-x86_64-unknown-linux-gnu/recfile.o -L/home/vsedyshev/Work/1111/pjproject/pjlib/lib -L/home/vsedyshev/Work/1111/pjproject/pjlib-util/lib -L/home/vsedyshev/Work/1111/pjproject/pjnath/lib -L/home/vsedyshev/Work/1111/pjproject/pjmedia/lib -L/home/vsedyshev/Work/1111/pjproject/pjsip/lib -L/home/vsedyshev/Work/1111/pjproject/third_party/lib -lSDL2     -lSDL2      -lpjsua-x86_64-unknown-linux-gnu -lpjsip-ua-x86_64-unknown-linux-gnu -lpjsip-simple-x86_64-unknown-linux-gnu -lpjsip-x86_64-unknown-linux-gnu -lpjmedia-codec-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjmedia-videodev-x86_64-unknown-linux-gnu -lpjmedia-audiodev-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjnath-x86_64-unknown-linux-gnu -lpjlib-util-x86_64-unknown-linux-gnu  -lsrtp-x86_64-unknown-linux-gnu -lresample-x86_64-unknown-linux-gnu -lgsmcodec-x86_64-unknown-linux-gnu -lspeex-x86_64-unknown-linux-gnu -lilbccodec-x86_64-unknown-linux-gnu -lg7221codec-x86_64-unknown-linux-gnu -lyuv-x86_64-unknown-linux-gnu -lwebrtc-x86_64-unknown-linux-gnu  -lpj-x86_64-unknown-linux-gnu -lssl -lcrypto -luuid -lm -lrt -lpthread  -lasound -lSDL2   
# make --no-print-directory -f /home/vsedyshev/Work/1111/pjproject/build/rules.mak SAMPLE_SRCDIR=../src/samples SAMPLE_OBJS=resampleplay.o SAMPLE_CFLAGS="-DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1 -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -I/home/vsedyshev/Work/1111/pjproject/pjlib/include -I/home/vsedyshev/Work/1111/pjproject/pjlib-util/include -I/home/vsedyshev/Work/1111/pjproject/pjnath/include -I/home/vsedyshev/Work/1111/pjproject/pjmedia/include -I/home/vsedyshev/Work/1111/pjproject/pjsip/include " SAMPLE_CXXFLAGS="-g -O2 -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1 -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -I/home/vsedyshev/Work/1111/pjproject/pjlib/include -I/home/vsedyshev/Work/1111/pjproject/pjlib-util/include -I/home/vsedyshev/Work/1111/pjproject/pjnath/include -I/home/vsedyshev/Work/1111/pjproject/pjmedia/include -I/home/vsedyshev/Work/1111/pjproject/pjsip/include " SAMPLE_LDFLAGS="-L/home/vsedyshev/Work/1111/pjproject/pjlib/lib -L/home/vsedyshev/Work/1111/pjproject/pjlib-util/lib -L/home/vsedyshev/Work/1111/pjproject/pjnath/lib -L/home/vsedyshev/Work/1111/pjproject/pjmedia/lib -L/home/vsedyshev/Work/1111/pjproject/pjsip/lib -L/home/vsedyshev/Work/1111/pjproject/third_party/lib -lSDL2     -lSDL2      -lpjsua-x86_64-unknown-linux-gnu -lpjsip-ua-x86_64-unknown-linux-gnu -lpjsip-simple-x86_64-unknown-linux-gnu -lpjsip-x86_64-unknown-linux-gnu -lpjmedia-codec-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjmedia-videodev-x86_64-unknown-linux-gnu -lpjmedia-audiodev-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjnath-x86_64-unknown-linux-gnu -lpjlib-util-x86_64-unknown-linux-gnu  -lsrtp-x86_64-unknown-linux-gnu -lresample-x86_64-unknown-linux-gnu -lgsmcodec-x86_64-unknown-linux-gnu -lspeex-x86_64-unknown-linux-gnu -lilbccodec-x86_64-unknown-linux-gnu -lg7221codec-x86_64-unknown-linux-gnu -lyuv-x86_64-unknown-linux-gnu -lwebrtc-x86_64-unknown-linux-gnu  -lpj-x86_64-unknown-linux-gnu -lssl -lcrypto -luuid -lm -lrt -lpthread  -lasound -lSDL2   " SAMPLE_EXE=resampleplay APP=SAMPLE app=sample ../bin/samples/x86_64-unknown-linux-gnu/resampleplay
# gcc -c -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1 -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -I/home/vsedyshev/Work/1111/pjproject/pjlib/include -I/home/vsedyshev/Work/1111/pjproject/pjlib-util/include -I/home/vsedyshev/Work/1111/pjproject/pjnath/include -I/home/vsedyshev/Work/1111/pjproject/pjmedia/include -I/home/vsedyshev/Work/1111/pjproject/pjsip/include  \
# 	-o output/sample-x86_64-unknown-linux-gnu/resampleplay.o \
# 	../src/samples/resampleplay.c 
# if test ! -d ../bin/samples/x86_64-unknown-linux-gnu; then mkdir -p ../bin/samples/x86_64-unknown-linux-gnu; fi
# gcc -o ../bin/samples/x86_64-unknown-linux-gnu/resampleplay \
#      output/sample-x86_64-unknown-linux-gnu/resampleplay.o -L/home/vsedyshev/Work/1111/pjproject/pjlib/lib -L/home/vsedyshev/Work/1111/pjproject/pjlib-util/lib -L/home/vsedyshev/Work/1111/pjproject/pjnath/lib -L/home/vsedyshev/Work/1111/pjproject/pjmedia/lib -L/home/vsedyshev/Work/1111/pjproject/pjsip/lib -L/home/vsedyshev/Work/1111/pjproject/third_party/lib -lSDL2     -lSDL2      -lpjsua-x86_64-unknown-linux-gnu -lpjsip-ua-x86_64-unknown-linux-gnu -lpjsip-simple-x86_64-unknown-linux-gnu -lpjsip-x86_64-unknown-linux-gnu -lpjmedia-codec-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjmedia-videodev-x86_64-unknown-linux-gnu -lpjmedia-audiodev-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjnath-x86_64-unknown-linux-gnu -lpjlib-util-x86_64-unknown-linux-gnu  -lsrtp-x86_64-unknown-linux-gnu -lresample-x86_64-unknown-linux-gnu -lgsmcodec-x86_64-unknown-linux-gnu -lspeex-x86_64-unknown-linux-gnu -lilbccodec-x86_64-unknown-linux-gnu -lg7221codec-x86_64-unknown-linux-gnu -lyuv-x86_64-unknown-linux-gnu -lwebrtc-x86_64-unknown-linux-gnu  -lpj-x86_64-unknown-linux-gnu -lssl -lcrypto -luuid -lm -lrt -lpthread  -lasound -lSDL2   
# make --no-print-directory -f /home/vsedyshev/Work/1111/pjproject/build/rules.mak SAMPLE_SRCDIR=../src/samples SAMPLE_OBJS=simpleua.o SAMPLE_CFLAGS="-DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1 -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -I/home/vsedyshev/Work/1111/pjproject/pjlib/include -I/home/vsedyshev/Work/1111/pjproject/pjlib-util/include -I/home/vsedyshev/Work/1111/pjproject/pjnath/include -I/home/vsedyshev/Work/1111/pjproject/pjmedia/include -I/home/vsedyshev/Work/1111/pjproject/pjsip/include " SAMPLE_CXXFLAGS="-g -O2 -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1 -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -I/home/vsedyshev/Work/1111/pjproject/pjlib/include -I/home/vsedyshev/Work/1111/pjproject/pjlib-util/include -I/home/vsedyshev/Work/1111/pjproject/pjnath/include -I/home/vsedyshev/Work/1111/pjproject/pjmedia/include -I/home/vsedyshev/Work/1111/pjproject/pjsip/include " SAMPLE_LDFLAGS="-L/home/vsedyshev/Work/1111/pjproject/pjlib/lib -L/home/vsedyshev/Work/1111/pjproject/pjlib-util/lib -L/home/vsedyshev/Work/1111/pjproject/pjnath/lib -L/home/vsedyshev/Work/1111/pjproject/pjmedia/lib -L/home/vsedyshev/Work/1111/pjproject/pjsip/lib -L/home/vsedyshev/Work/1111/pjproject/third_party/lib -lSDL2     -lSDL2      -lpjsua-x86_64-unknown-linux-gnu -lpjsip-ua-x86_64-unknown-linux-gnu -lpjsip-simple-x86_64-unknown-linux-gnu -lpjsip-x86_64-unknown-linux-gnu -lpjmedia-codec-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjmedia-videodev-x86_64-unknown-linux-gnu -lpjmedia-audiodev-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjnath-x86_64-unknown-linux-gnu -lpjlib-util-x86_64-unknown-linux-gnu  -lsrtp-x86_64-unknown-linux-gnu -lresample-x86_64-unknown-linux-gnu -lgsmcodec-x86_64-unknown-linux-gnu -lspeex-x86_64-unknown-linux-gnu -lilbccodec-x86_64-unknown-linux-gnu -lg7221codec-x86_64-unknown-linux-gnu -lyuv-x86_64-unknown-linux-gnu -lwebrtc-x86_64-unknown-linux-gnu  -lpj-x86_64-unknown-linux-gnu -lssl -lcrypto -luuid -lm -lrt -lpthread  -lasound -lSDL2   " SAMPLE_EXE=simpleua APP=SAMPLE app=sample ../bin/samples/x86_64-unknown-linux-gnu/simpleua
# gcc -c -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1 -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -I/home/vsedyshev/Work/1111/pjproject/pjlib/include -I/home/vsedyshev/Work/1111/pjproject/pjlib-util/include -I/home/vsedyshev/Work/1111/pjproject/pjnath/include -I/home/vsedyshev/Work/1111/pjproject/pjmedia/include -I/home/vsedyshev/Work/1111/pjproject/pjsip/include  \
# 	-o output/sample-x86_64-unknown-linux-gnu/simpleua.o \
# 	../src/samples/simpleua.c 
# if test ! -d ../bin/samples/x86_64-unknown-linux-gnu; then mkdir -p ../bin/samples/x86_64-unknown-linux-gnu; fi
# gcc -o ../bin/samples/x86_64-unknown-linux-gnu/simpleua \
#      output/sample-x86_64-unknown-linux-gnu/simpleua.o -L/home/vsedyshev/Work/1111/pjproject/pjlib/lib -L/home/vsedyshev/Work/1111/pjproject/pjlib-util/lib -L/home/vsedyshev/Work/1111/pjproject/pjnath/lib -L/home/vsedyshev/Work/1111/pjproject/pjmedia/lib -L/home/vsedyshev/Work/1111/pjproject/pjsip/lib -L/home/vsedyshev/Work/1111/pjproject/third_party/lib -lSDL2     -lSDL2      -lpjsua-x86_64-unknown-linux-gnu -lpjsip-ua-x86_64-unknown-linux-gnu -lpjsip-simple-x86_64-unknown-linux-gnu -lpjsip-x86_64-unknown-linux-gnu -lpjmedia-codec-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjmedia-videodev-x86_64-unknown-linux-gnu -lpjmedia-audiodev-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjnath-x86_64-unknown-linux-gnu -lpjlib-util-x86_64-unknown-linux-gnu  -lsrtp-x86_64-unknown-linux-gnu -lresample-x86_64-unknown-linux-gnu -lgsmcodec-x86_64-unknown-linux-gnu -lspeex-x86_64-unknown-linux-gnu -lilbccodec-x86_64-unknown-linux-gnu -lg7221codec-x86_64-unknown-linux-gnu -lyuv-x86_64-unknown-linux-gnu -lwebrtc-x86_64-unknown-linux-gnu  -lpj-x86_64-unknown-linux-gnu -lssl -lcrypto -luuid -lm -lrt -lpthread  -lasound -lSDL2   
# make --no-print-directory -f /home/vsedyshev/Work/1111/pjproject/build/rules.mak SAMPLE_SRCDIR=../src/samples SAMPLE_OBJS=simple_pjsua.o SAMPLE_CFLAGS="-DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1 -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -I/home/vsedyshev/Work/1111/pjproject/pjlib/include -I/home/vsedyshev/Work/1111/pjproject/pjlib-util/include -I/home/vsedyshev/Work/1111/pjproject/pjnath/include -I/home/vsedyshev/Work/1111/pjproject/pjmedia/include -I/home/vsedyshev/Work/1111/pjproject/pjsip/include " SAMPLE_CXXFLAGS="-g -O2 -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1 -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -I/home/vsedyshev/Work/1111/pjproject/pjlib/include -I/home/vsedyshev/Work/1111/pjproject/pjlib-util/include -I/home/vsedyshev/Work/1111/pjproject/pjnath/include -I/home/vsedyshev/Work/1111/pjproject/pjmedia/include -I/home/vsedyshev/Work/1111/pjproject/pjsip/include " SAMPLE_LDFLAGS="-L/home/vsedyshev/Work/1111/pjproject/pjlib/lib -L/home/vsedyshev/Work/1111/pjproject/pjlib-util/lib -L/home/vsedyshev/Work/1111/pjproject/pjnath/lib -L/home/vsedyshev/Work/1111/pjproject/pjmedia/lib -L/home/vsedyshev/Work/1111/pjproject/pjsip/lib -L/home/vsedyshev/Work/1111/pjproject/third_party/lib -lSDL2     -lSDL2      -lpjsua-x86_64-unknown-linux-gnu -lpjsip-ua-x86_64-unknown-linux-gnu -lpjsip-simple-x86_64-unknown-linux-gnu -lpjsip-x86_64-unknown-linux-gnu -lpjmedia-codec-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjmedia-videodev-x86_64-unknown-linux-gnu -lpjmedia-audiodev-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjnath-x86_64-unknown-linux-gnu -lpjlib-util-x86_64-unknown-linux-gnu  -lsrtp-x86_64-unknown-linux-gnu -lresample-x86_64-unknown-linux-gnu -lgsmcodec-x86_64-unknown-linux-gnu -lspeex-x86_64-unknown-linux-gnu -lilbccodec-x86_64-unknown-linux-gnu -lg7221codec-x86_64-unknown-linux-gnu -lyuv-x86_64-unknown-linux-gnu -lwebrtc-x86_64-unknown-linux-gnu  -lpj-x86_64-unknown-linux-gnu -lssl -lcrypto -luuid -lm -lrt -lpthread  -lasound -lSDL2   " SAMPLE_EXE=simple_pjsua APP=SAMPLE app=sample ../bin/samples/x86_64-unknown-linux-gnu/simple_pjsua
# gcc -c -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1 -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -I/home/vsedyshev/Work/1111/pjproject/pjlib/include -I/home/vsedyshev/Work/1111/pjproject/pjlib-util/include -I/home/vsedyshev/Work/1111/pjproject/pjnath/include -I/home/vsedyshev/Work/1111/pjproject/pjmedia/include -I/home/vsedyshev/Work/1111/pjproject/pjsip/include  \
# 	-o output/sample-x86_64-unknown-linux-gnu/simple_pjsua.o \
# 	../src/samples/simple_pjsua.c 
# if test ! -d ../bin/samples/x86_64-unknown-linux-gnu; then mkdir -p ../bin/samples/x86_64-unknown-linux-gnu; fi
# gcc -o ../bin/samples/x86_64-unknown-linux-gnu/simple_pjsua \
#      output/sample-x86_64-unknown-linux-gnu/simple_pjsua.o -L/home/vsedyshev/Work/1111/pjproject/pjlib/lib -L/home/vsedyshev/Work/1111/pjproject/pjlib-util/lib -L/home/vsedyshev/Work/1111/pjproject/pjnath/lib -L/home/vsedyshev/Work/1111/pjproject/pjmedia/lib -L/home/vsedyshev/Work/1111/pjproject/pjsip/lib -L/home/vsedyshev/Work/1111/pjproject/third_party/lib -lSDL2     -lSDL2      -lpjsua-x86_64-unknown-linux-gnu -lpjsip-ua-x86_64-unknown-linux-gnu -lpjsip-simple-x86_64-unknown-linux-gnu -lpjsip-x86_64-unknown-linux-gnu -lpjmedia-codec-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjmedia-videodev-x86_64-unknown-linux-gnu -lpjmedia-audiodev-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjnath-x86_64-unknown-linux-gnu -lpjlib-util-x86_64-unknown-linux-gnu  -lsrtp-x86_64-unknown-linux-gnu -lresample-x86_64-unknown-linux-gnu -lgsmcodec-x86_64-unknown-linux-gnu -lspeex-x86_64-unknown-linux-gnu -lilbccodec-x86_64-unknown-linux-gnu -lg7221codec-x86_64-unknown-linux-gnu -lyuv-x86_64-unknown-linux-gnu -lwebrtc-x86_64-unknown-linux-gnu  -lpj-x86_64-unknown-linux-gnu -lssl -lcrypto -luuid -lm -lrt -lpthread  -lasound -lSDL2   
# make --no-print-directory -f /home/vsedyshev/Work/1111/pjproject/build/rules.mak SAMPLE_SRCDIR=../src/samples SAMPLE_OBJS=sipecho.o SAMPLE_CFLAGS="-DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1 -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -I/home/vsedyshev/Work/1111/pjproject/pjlib/include -I/home/vsedyshev/Work/1111/pjproject/pjlib-util/include -I/home/vsedyshev/Work/1111/pjproject/pjnath/include -I/home/vsedyshev/Work/1111/pjproject/pjmedia/include -I/home/vsedyshev/Work/1111/pjproject/pjsip/include " SAMPLE_CXXFLAGS="-g -O2 -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1 -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -I/home/vsedyshev/Work/1111/pjproject/pjlib/include -I/home/vsedyshev/Work/1111/pjproject/pjlib-util/include -I/home/vsedyshev/Work/1111/pjproject/pjnath/include -I/home/vsedyshev/Work/1111/pjproject/pjmedia/include -I/home/vsedyshev/Work/1111/pjproject/pjsip/include " SAMPLE_LDFLAGS="-L/home/vsedyshev/Work/1111/pjproject/pjlib/lib -L/home/vsedyshev/Work/1111/pjproject/pjlib-util/lib -L/home/vsedyshev/Work/1111/pjproject/pjnath/lib -L/home/vsedyshev/Work/1111/pjproject/pjmedia/lib -L/home/vsedyshev/Work/1111/pjproject/pjsip/lib -L/home/vsedyshev/Work/1111/pjproject/third_party/lib -lSDL2     -lSDL2      -lpjsua-x86_64-unknown-linux-gnu -lpjsip-ua-x86_64-unknown-linux-gnu -lpjsip-simple-x86_64-unknown-linux-gnu -lpjsip-x86_64-unknown-linux-gnu -lpjmedia-codec-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjmedia-videodev-x86_64-unknown-linux-gnu -lpjmedia-audiodev-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjnath-x86_64-unknown-linux-gnu -lpjlib-util-x86_64-unknown-linux-gnu  -lsrtp-x86_64-unknown-linux-gnu -lresample-x86_64-unknown-linux-gnu -lgsmcodec-x86_64-unknown-linux-gnu -lspeex-x86_64-unknown-linux-gnu -lilbccodec-x86_64-unknown-linux-gnu -lg7221codec-x86_64-unknown-linux-gnu -lyuv-x86_64-unknown-linux-gnu -lwebrtc-x86_64-unknown-linux-gnu  -lpj-x86_64-unknown-linux-gnu -lssl -lcrypto -luuid -lm -lrt -lpthread  -lasound -lSDL2   " SAMPLE_EXE=sipecho APP=SAMPLE app=sample ../bin/samples/x86_64-unknown-linux-gnu/sipecho
# gcc -c -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1 -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -I/home/vsedyshev/Work/1111/pjproject/pjlib/include -I/home/vsedyshev/Work/1111/pjproject/pjlib-util/include -I/home/vsedyshev/Work/1111/pjproject/pjnath/include -I/home/vsedyshev/Work/1111/pjproject/pjmedia/include -I/home/vsedyshev/Work/1111/pjproject/pjsip/include  \
# 	-o output/sample-x86_64-unknown-linux-gnu/sipecho.o \
# 	../src/samples/sipecho.c 
# if test ! -d ../bin/samples/x86_64-unknown-linux-gnu; then mkdir -p ../bin/samples/x86_64-unknown-linux-gnu; fi
# gcc -o ../bin/samples/x86_64-unknown-linux-gnu/sipecho \
#      output/sample-x86_64-unknown-linux-gnu/sipecho.o -L/home/vsedyshev/Work/1111/pjproject/pjlib/lib -L/home/vsedyshev/Work/1111/pjproject/pjlib-util/lib -L/home/vsedyshev/Work/1111/pjproject/pjnath/lib -L/home/vsedyshev/Work/1111/pjproject/pjmedia/lib -L/home/vsedyshev/Work/1111/pjproject/pjsip/lib -L/home/vsedyshev/Work/1111/pjproject/third_party/lib -lSDL2     -lSDL2      -lpjsua-x86_64-unknown-linux-gnu -lpjsip-ua-x86_64-unknown-linux-gnu -lpjsip-simple-x86_64-unknown-linux-gnu -lpjsip-x86_64-unknown-linux-gnu -lpjmedia-codec-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjmedia-videodev-x86_64-unknown-linux-gnu -lpjmedia-audiodev-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjnath-x86_64-unknown-linux-gnu -lpjlib-util-x86_64-unknown-linux-gnu  -lsrtp-x86_64-unknown-linux-gnu -lresample-x86_64-unknown-linux-gnu -lgsmcodec-x86_64-unknown-linux-gnu -lspeex-x86_64-unknown-linux-gnu -lilbccodec-x86_64-unknown-linux-gnu -lg7221codec-x86_64-unknown-linux-gnu -lyuv-x86_64-unknown-linux-gnu -lwebrtc-x86_64-unknown-linux-gnu  -lpj-x86_64-unknown-linux-gnu -lssl -lcrypto -luuid -lm -lrt -lpthread  -lasound -lSDL2   
# make --no-print-directory -f /home/vsedyshev/Work/1111/pjproject/build/rules.mak SAMPLE_SRCDIR=../src/samples SAMPLE_OBJS=siprtp.o SAMPLE_CFLAGS="-DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1 -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -I/home/vsedyshev/Work/1111/pjproject/pjlib/include -I/home/vsedyshev/Work/1111/pjproject/pjlib-util/include -I/home/vsedyshev/Work/1111/pjproject/pjnath/include -I/home/vsedyshev/Work/1111/pjproject/pjmedia/include -I/home/vsedyshev/Work/1111/pjproject/pjsip/include " SAMPLE_CXXFLAGS="-g -O2 -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1 -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -I/home/vsedyshev/Work/1111/pjproject/pjlib/include -I/home/vsedyshev/Work/1111/pjproject/pjlib-util/include -I/home/vsedyshev/Work/1111/pjproject/pjnath/include -I/home/vsedyshev/Work/1111/pjproject/pjmedia/include -I/home/vsedyshev/Work/1111/pjproject/pjsip/include " SAMPLE_LDFLAGS="-L/home/vsedyshev/Work/1111/pjproject/pjlib/lib -L/home/vsedyshev/Work/1111/pjproject/pjlib-util/lib -L/home/vsedyshev/Work/1111/pjproject/pjnath/lib -L/home/vsedyshev/Work/1111/pjproject/pjmedia/lib -L/home/vsedyshev/Work/1111/pjproject/pjsip/lib -L/home/vsedyshev/Work/1111/pjproject/third_party/lib -lSDL2     -lSDL2      -lpjsua-x86_64-unknown-linux-gnu -lpjsip-ua-x86_64-unknown-linux-gnu -lpjsip-simple-x86_64-unknown-linux-gnu -lpjsip-x86_64-unknown-linux-gnu -lpjmedia-codec-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjmedia-videodev-x86_64-unknown-linux-gnu -lpjmedia-audiodev-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjnath-x86_64-unknown-linux-gnu -lpjlib-util-x86_64-unknown-linux-gnu  -lsrtp-x86_64-unknown-linux-gnu -lresample-x86_64-unknown-linux-gnu -lgsmcodec-x86_64-unknown-linux-gnu -lspeex-x86_64-unknown-linux-gnu -lilbccodec-x86_64-unknown-linux-gnu -lg7221codec-x86_64-unknown-linux-gnu -lyuv-x86_64-unknown-linux-gnu -lwebrtc-x86_64-unknown-linux-gnu  -lpj-x86_64-unknown-linux-gnu -lssl -lcrypto -luuid -lm -lrt -lpthread  -lasound -lSDL2   " SAMPLE_EXE=siprtp APP=SAMPLE app=sample ../bin/samples/x86_64-unknown-linux-gnu/siprtp
# gcc -c -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1 -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -I/home/vsedyshev/Work/1111/pjproject/pjlib/include -I/home/vsedyshev/Work/1111/pjproject/pjlib-util/include -I/home/vsedyshev/Work/1111/pjproject/pjnath/include -I/home/vsedyshev/Work/1111/pjproject/pjmedia/include -I/home/vsedyshev/Work/1111/pjproject/pjsip/include  \
# 	-o output/sample-x86_64-unknown-linux-gnu/siprtp.o \
# 	../src/samples/siprtp.c 
# if test ! -d ../bin/samples/x86_64-unknown-linux-gnu; then mkdir -p ../bin/samples/x86_64-unknown-linux-gnu; fi
# gcc -o ../bin/samples/x86_64-unknown-linux-gnu/siprtp \
#      output/sample-x86_64-unknown-linux-gnu/siprtp.o -L/home/vsedyshev/Work/1111/pjproject/pjlib/lib -L/home/vsedyshev/Work/1111/pjproject/pjlib-util/lib -L/home/vsedyshev/Work/1111/pjproject/pjnath/lib -L/home/vsedyshev/Work/1111/pjproject/pjmedia/lib -L/home/vsedyshev/Work/1111/pjproject/pjsip/lib -L/home/vsedyshev/Work/1111/pjproject/third_party/lib -lSDL2     -lSDL2      -lpjsua-x86_64-unknown-linux-gnu -lpjsip-ua-x86_64-unknown-linux-gnu -lpjsip-simple-x86_64-unknown-linux-gnu -lpjsip-x86_64-unknown-linux-gnu -lpjmedia-codec-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjmedia-videodev-x86_64-unknown-linux-gnu -lpjmedia-audiodev-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjnath-x86_64-unknown-linux-gnu -lpjlib-util-x86_64-unknown-linux-gnu  -lsrtp-x86_64-unknown-linux-gnu -lresample-x86_64-unknown-linux-gnu -lgsmcodec-x86_64-unknown-linux-gnu -lspeex-x86_64-unknown-linux-gnu -lilbccodec-x86_64-unknown-linux-gnu -lg7221codec-x86_64-unknown-linux-gnu -lyuv-x86_64-unknown-linux-gnu -lwebrtc-x86_64-unknown-linux-gnu  -lpj-x86_64-unknown-linux-gnu -lssl -lcrypto -luuid -lm -lrt -lpthread  -lasound -lSDL2   
# make --no-print-directory -f /home/vsedyshev/Work/1111/pjproject/build/rules.mak SAMPLE_SRCDIR=../src/samples SAMPLE_OBJS=sipstateless.o SAMPLE_CFLAGS="-DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1 -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -I/home/vsedyshev/Work/1111/pjproject/pjlib/include -I/home/vsedyshev/Work/1111/pjproject/pjlib-util/include -I/home/vsedyshev/Work/1111/pjproject/pjnath/include -I/home/vsedyshev/Work/1111/pjproject/pjmedia/include -I/home/vsedyshev/Work/1111/pjproject/pjsip/include " SAMPLE_CXXFLAGS="-g -O2 -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1 -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -I/home/vsedyshev/Work/1111/pjproject/pjlib/include -I/home/vsedyshev/Work/1111/pjproject/pjlib-util/include -I/home/vsedyshev/Work/1111/pjproject/pjnath/include -I/home/vsedyshev/Work/1111/pjproject/pjmedia/include -I/home/vsedyshev/Work/1111/pjproject/pjsip/include " SAMPLE_LDFLAGS="-L/home/vsedyshev/Work/1111/pjproject/pjlib/lib -L/home/vsedyshev/Work/1111/pjproject/pjlib-util/lib -L/home/vsedyshev/Work/1111/pjproject/pjnath/lib -L/home/vsedyshev/Work/1111/pjproject/pjmedia/lib -L/home/vsedyshev/Work/1111/pjproject/pjsip/lib -L/home/vsedyshev/Work/1111/pjproject/third_party/lib -lSDL2     -lSDL2      -lpjsua-x86_64-unknown-linux-gnu -lpjsip-ua-x86_64-unknown-linux-gnu -lpjsip-simple-x86_64-unknown-linux-gnu -lpjsip-x86_64-unknown-linux-gnu -lpjmedia-codec-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjmedia-videodev-x86_64-unknown-linux-gnu -lpjmedia-audiodev-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjnath-x86_64-unknown-linux-gnu -lpjlib-util-x86_64-unknown-linux-gnu  -lsrtp-x86_64-unknown-linux-gnu -lresample-x86_64-unknown-linux-gnu -lgsmcodec-x86_64-unknown-linux-gnu -lspeex-x86_64-unknown-linux-gnu -lilbccodec-x86_64-unknown-linux-gnu -lg7221codec-x86_64-unknown-linux-gnu -lyuv-x86_64-unknown-linux-gnu -lwebrtc-x86_64-unknown-linux-gnu  -lpj-x86_64-unknown-linux-gnu -lssl -lcrypto -luuid -lm -lrt -lpthread  -lasound -lSDL2   " SAMPLE_EXE=sipstateless APP=SAMPLE app=sample ../bin/samples/x86_64-unknown-linux-gnu/sipstateless
# gcc -c -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1 -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -I/home/vsedyshev/Work/1111/pjproject/pjlib/include -I/home/vsedyshev/Work/1111/pjproject/pjlib-util/include -I/home/vsedyshev/Work/1111/pjproject/pjnath/include -I/home/vsedyshev/Work/1111/pjproject/pjmedia/include -I/home/vsedyshev/Work/1111/pjproject/pjsip/include  \
# 	-o output/sample-x86_64-unknown-linux-gnu/sipstateless.o \
# 	../src/samples/sipstateless.c 
# if test ! -d ../bin/samples/x86_64-unknown-linux-gnu; then mkdir -p ../bin/samples/x86_64-unknown-linux-gnu; fi
# gcc -o ../bin/samples/x86_64-unknown-linux-gnu/sipstateless \
#      output/sample-x86_64-unknown-linux-gnu/sipstateless.o -L/home/vsedyshev/Work/1111/pjproject/pjlib/lib -L/home/vsedyshev/Work/1111/pjproject/pjlib-util/lib -L/home/vsedyshev/Work/1111/pjproject/pjnath/lib -L/home/vsedyshev/Work/1111/pjproject/pjmedia/lib -L/home/vsedyshev/Work/1111/pjproject/pjsip/lib -L/home/vsedyshev/Work/1111/pjproject/third_party/lib -lSDL2     -lSDL2      -lpjsua-x86_64-unknown-linux-gnu -lpjsip-ua-x86_64-unknown-linux-gnu -lpjsip-simple-x86_64-unknown-linux-gnu -lpjsip-x86_64-unknown-linux-gnu -lpjmedia-codec-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjmedia-videodev-x86_64-unknown-linux-gnu -lpjmedia-audiodev-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjnath-x86_64-unknown-linux-gnu -lpjlib-util-x86_64-unknown-linux-gnu  -lsrtp-x86_64-unknown-linux-gnu -lresample-x86_64-unknown-linux-gnu -lgsmcodec-x86_64-unknown-linux-gnu -lspeex-x86_64-unknown-linux-gnu -lilbccodec-x86_64-unknown-linux-gnu -lg7221codec-x86_64-unknown-linux-gnu -lyuv-x86_64-unknown-linux-gnu -lwebrtc-x86_64-unknown-linux-gnu  -lpj-x86_64-unknown-linux-gnu -lssl -lcrypto -luuid -lm -lrt -lpthread  -lasound -lSDL2   
# make --no-print-directory -f /home/vsedyshev/Work/1111/pjproject/build/rules.mak SAMPLE_SRCDIR=../src/samples SAMPLE_OBJS=stateful_proxy.o SAMPLE_CFLAGS="-DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1 -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -I/home/vsedyshev/Work/1111/pjproject/pjlib/include -I/home/vsedyshev/Work/1111/pjproject/pjlib-util/include -I/home/vsedyshev/Work/1111/pjproject/pjnath/include -I/home/vsedyshev/Work/1111/pjproject/pjmedia/include -I/home/vsedyshev/Work/1111/pjproject/pjsip/include " SAMPLE_CXXFLAGS="-g -O2 -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1 -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -I/home/vsedyshev/Work/1111/pjproject/pjlib/include -I/home/vsedyshev/Work/1111/pjproject/pjlib-util/include -I/home/vsedyshev/Work/1111/pjproject/pjnath/include -I/home/vsedyshev/Work/1111/pjproject/pjmedia/include -I/home/vsedyshev/Work/1111/pjproject/pjsip/include " SAMPLE_LDFLAGS="-L/home/vsedyshev/Work/1111/pjproject/pjlib/lib -L/home/vsedyshev/Work/1111/pjproject/pjlib-util/lib -L/home/vsedyshev/Work/1111/pjproject/pjnath/lib -L/home/vsedyshev/Work/1111/pjproject/pjmedia/lib -L/home/vsedyshev/Work/1111/pjproject/pjsip/lib -L/home/vsedyshev/Work/1111/pjproject/third_party/lib -lSDL2     -lSDL2      -lpjsua-x86_64-unknown-linux-gnu -lpjsip-ua-x86_64-unknown-linux-gnu -lpjsip-simple-x86_64-unknown-linux-gnu -lpjsip-x86_64-unknown-linux-gnu -lpjmedia-codec-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjmedia-videodev-x86_64-unknown-linux-gnu -lpjmedia-audiodev-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjnath-x86_64-unknown-linux-gnu -lpjlib-util-x86_64-unknown-linux-gnu  -lsrtp-x86_64-unknown-linux-gnu -lresample-x86_64-unknown-linux-gnu -lgsmcodec-x86_64-unknown-linux-gnu -lspeex-x86_64-unknown-linux-gnu -lilbccodec-x86_64-unknown-linux-gnu -lg7221codec-x86_64-unknown-linux-gnu -lyuv-x86_64-unknown-linux-gnu -lwebrtc-x86_64-unknown-linux-gnu  -lpj-x86_64-unknown-linux-gnu -lssl -lcrypto -luuid -lm -lrt -lpthread  -lasound -lSDL2   " SAMPLE_EXE=stateful_proxy APP=SAMPLE app=sample ../bin/samples/x86_64-unknown-linux-gnu/stateful_proxy
# gcc -c -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1 -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -I/home/vsedyshev/Work/1111/pjproject/pjlib/include -I/home/vsedyshev/Work/1111/pjproject/pjlib-util/include -I/home/vsedyshev/Work/1111/pjproject/pjnath/include -I/home/vsedyshev/Work/1111/pjproject/pjmedia/include -I/home/vsedyshev/Work/1111/pjproject/pjsip/include  \
# 	-o output/sample-x86_64-unknown-linux-gnu/stateful_proxy.o \
# 	../src/samples/stateful_proxy.c 
# if test ! -d ../bin/samples/x86_64-unknown-linux-gnu; then mkdir -p ../bin/samples/x86_64-unknown-linux-gnu; fi
# gcc -o ../bin/samples/x86_64-unknown-linux-gnu/stateful_proxy \
#      output/sample-x86_64-unknown-linux-gnu/stateful_proxy.o -L/home/vsedyshev/Work/1111/pjproject/pjlib/lib -L/home/vsedyshev/Work/1111/pjproject/pjlib-util/lib -L/home/vsedyshev/Work/1111/pjproject/pjnath/lib -L/home/vsedyshev/Work/1111/pjproject/pjmedia/lib -L/home/vsedyshev/Work/1111/pjproject/pjsip/lib -L/home/vsedyshev/Work/1111/pjproject/third_party/lib -lSDL2     -lSDL2      -lpjsua-x86_64-unknown-linux-gnu -lpjsip-ua-x86_64-unknown-linux-gnu -lpjsip-simple-x86_64-unknown-linux-gnu -lpjsip-x86_64-unknown-linux-gnu -lpjmedia-codec-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjmedia-videodev-x86_64-unknown-linux-gnu -lpjmedia-audiodev-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjnath-x86_64-unknown-linux-gnu -lpjlib-util-x86_64-unknown-linux-gnu  -lsrtp-x86_64-unknown-linux-gnu -lresample-x86_64-unknown-linux-gnu -lgsmcodec-x86_64-unknown-linux-gnu -lspeex-x86_64-unknown-linux-gnu -lilbccodec-x86_64-unknown-linux-gnu -lg7221codec-x86_64-unknown-linux-gnu -lyuv-x86_64-unknown-linux-gnu -lwebrtc-x86_64-unknown-linux-gnu  -lpj-x86_64-unknown-linux-gnu -lssl -lcrypto -luuid -lm -lrt -lpthread  -lasound -lSDL2   
# make --no-print-directory -f /home/vsedyshev/Work/1111/pjproject/build/rules.mak SAMPLE_SRCDIR=../src/samples SAMPLE_OBJS=stateless_proxy.o SAMPLE_CFLAGS="-DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1 -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -I/home/vsedyshev/Work/1111/pjproject/pjlib/include -I/home/vsedyshev/Work/1111/pjproject/pjlib-util/include -I/home/vsedyshev/Work/1111/pjproject/pjnath/include -I/home/vsedyshev/Work/1111/pjproject/pjmedia/include -I/home/vsedyshev/Work/1111/pjproject/pjsip/include " SAMPLE_CXXFLAGS="-g -O2 -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1 -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -I/home/vsedyshev/Work/1111/pjproject/pjlib/include -I/home/vsedyshev/Work/1111/pjproject/pjlib-util/include -I/home/vsedyshev/Work/1111/pjproject/pjnath/include -I/home/vsedyshev/Work/1111/pjproject/pjmedia/include -I/home/vsedyshev/Work/1111/pjproject/pjsip/include " SAMPLE_LDFLAGS="-L/home/vsedyshev/Work/1111/pjproject/pjlib/lib -L/home/vsedyshev/Work/1111/pjproject/pjlib-util/lib -L/home/vsedyshev/Work/1111/pjproject/pjnath/lib -L/home/vsedyshev/Work/1111/pjproject/pjmedia/lib -L/home/vsedyshev/Work/1111/pjproject/pjsip/lib -L/home/vsedyshev/Work/1111/pjproject/third_party/lib -lSDL2     -lSDL2      -lpjsua-x86_64-unknown-linux-gnu -lpjsip-ua-x86_64-unknown-linux-gnu -lpjsip-simple-x86_64-unknown-linux-gnu -lpjsip-x86_64-unknown-linux-gnu -lpjmedia-codec-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjmedia-videodev-x86_64-unknown-linux-gnu -lpjmedia-audiodev-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjnath-x86_64-unknown-linux-gnu -lpjlib-util-x86_64-unknown-linux-gnu  -lsrtp-x86_64-unknown-linux-gnu -lresample-x86_64-unknown-linux-gnu -lgsmcodec-x86_64-unknown-linux-gnu -lspeex-x86_64-unknown-linux-gnu -lilbccodec-x86_64-unknown-linux-gnu -lg7221codec-x86_64-unknown-linux-gnu -lyuv-x86_64-unknown-linux-gnu -lwebrtc-x86_64-unknown-linux-gnu  -lpj-x86_64-unknown-linux-gnu -lssl -lcrypto -luuid -lm -lrt -lpthread  -lasound -lSDL2   " SAMPLE_EXE=stateless_proxy APP=SAMPLE app=sample ../bin/samples/x86_64-unknown-linux-gnu/stateless_proxy
# gcc -c -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1 -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -I/home/vsedyshev/Work/1111/pjproject/pjlib/include -I/home/vsedyshev/Work/1111/pjproject/pjlib-util/include -I/home/vsedyshev/Work/1111/pjproject/pjnath/include -I/home/vsedyshev/Work/1111/pjproject/pjmedia/include -I/home/vsedyshev/Work/1111/pjproject/pjsip/include  \
# 	-o output/sample-x86_64-unknown-linux-gnu/stateless_proxy.o \
# 	../src/samples/stateless_proxy.c 
# if test ! -d ../bin/samples/x86_64-unknown-linux-gnu; then mkdir -p ../bin/samples/x86_64-unknown-linux-gnu; fi
# gcc -o ../bin/samples/x86_64-unknown-linux-gnu/stateless_proxy \
#      output/sample-x86_64-unknown-linux-gnu/stateless_proxy.o -L/home/vsedyshev/Work/1111/pjproject/pjlib/lib -L/home/vsedyshev/Work/1111/pjproject/pjlib-util/lib -L/home/vsedyshev/Work/1111/pjproject/pjnath/lib -L/home/vsedyshev/Work/1111/pjproject/pjmedia/lib -L/home/vsedyshev/Work/1111/pjproject/pjsip/lib -L/home/vsedyshev/Work/1111/pjproject/third_party/lib -lSDL2     -lSDL2      -lpjsua-x86_64-unknown-linux-gnu -lpjsip-ua-x86_64-unknown-linux-gnu -lpjsip-simple-x86_64-unknown-linux-gnu -lpjsip-x86_64-unknown-linux-gnu -lpjmedia-codec-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjmedia-videodev-x86_64-unknown-linux-gnu -lpjmedia-audiodev-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjnath-x86_64-unknown-linux-gnu -lpjlib-util-x86_64-unknown-linux-gnu  -lsrtp-x86_64-unknown-linux-gnu -lresample-x86_64-unknown-linux-gnu -lgsmcodec-x86_64-unknown-linux-gnu -lspeex-x86_64-unknown-linux-gnu -lilbccodec-x86_64-unknown-linux-gnu -lg7221codec-x86_64-unknown-linux-gnu -lyuv-x86_64-unknown-linux-gnu -lwebrtc-x86_64-unknown-linux-gnu  -lpj-x86_64-unknown-linux-gnu -lssl -lcrypto -luuid -lm -lrt -lpthread  -lasound -lSDL2   
# make --no-print-directory -f /home/vsedyshev/Work/1111/pjproject/build/rules.mak SAMPLE_SRCDIR=../src/samples SAMPLE_OBJS=stereotest.o SAMPLE_CFLAGS="-DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1 -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -I/home/vsedyshev/Work/1111/pjproject/pjlib/include -I/home/vsedyshev/Work/1111/pjproject/pjlib-util/include -I/home/vsedyshev/Work/1111/pjproject/pjnath/include -I/home/vsedyshev/Work/1111/pjproject/pjmedia/include -I/home/vsedyshev/Work/1111/pjproject/pjsip/include " SAMPLE_CXXFLAGS="-g -O2 -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1 -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -I/home/vsedyshev/Work/1111/pjproject/pjlib/include -I/home/vsedyshev/Work/1111/pjproject/pjlib-util/include -I/home/vsedyshev/Work/1111/pjproject/pjnath/include -I/home/vsedyshev/Work/1111/pjproject/pjmedia/include -I/home/vsedyshev/Work/1111/pjproject/pjsip/include " SAMPLE_LDFLAGS="-L/home/vsedyshev/Work/1111/pjproject/pjlib/lib -L/home/vsedyshev/Work/1111/pjproject/pjlib-util/lib -L/home/vsedyshev/Work/1111/pjproject/pjnath/lib -L/home/vsedyshev/Work/1111/pjproject/pjmedia/lib -L/home/vsedyshev/Work/1111/pjproject/pjsip/lib -L/home/vsedyshev/Work/1111/pjproject/third_party/lib -lSDL2     -lSDL2      -lpjsua-x86_64-unknown-linux-gnu -lpjsip-ua-x86_64-unknown-linux-gnu -lpjsip-simple-x86_64-unknown-linux-gnu -lpjsip-x86_64-unknown-linux-gnu -lpjmedia-codec-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjmedia-videodev-x86_64-unknown-linux-gnu -lpjmedia-audiodev-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjnath-x86_64-unknown-linux-gnu -lpjlib-util-x86_64-unknown-linux-gnu  -lsrtp-x86_64-unknown-linux-gnu -lresample-x86_64-unknown-linux-gnu -lgsmcodec-x86_64-unknown-linux-gnu -lspeex-x86_64-unknown-linux-gnu -lilbccodec-x86_64-unknown-linux-gnu -lg7221codec-x86_64-unknown-linux-gnu -lyuv-x86_64-unknown-linux-gnu -lwebrtc-x86_64-unknown-linux-gnu  -lpj-x86_64-unknown-linux-gnu -lssl -lcrypto -luuid -lm -lrt -lpthread  -lasound -lSDL2   " SAMPLE_EXE=stereotest APP=SAMPLE app=sample ../bin/samples/x86_64-unknown-linux-gnu/stereotest
# gcc -c -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1 -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -I/home/vsedyshev/Work/1111/pjproject/pjlib/include -I/home/vsedyshev/Work/1111/pjproject/pjlib-util/include -I/home/vsedyshev/Work/1111/pjproject/pjnath/include -I/home/vsedyshev/Work/1111/pjproject/pjmedia/include -I/home/vsedyshev/Work/1111/pjproject/pjsip/include  \
# 	-o output/sample-x86_64-unknown-linux-gnu/stereotest.o \
# 	../src/samples/stereotest.c 
# if test ! -d ../bin/samples/x86_64-unknown-linux-gnu; then mkdir -p ../bin/samples/x86_64-unknown-linux-gnu; fi
# gcc -o ../bin/samples/x86_64-unknown-linux-gnu/stereotest \
#      output/sample-x86_64-unknown-linux-gnu/stereotest.o -L/home/vsedyshev/Work/1111/pjproject/pjlib/lib -L/home/vsedyshev/Work/1111/pjproject/pjlib-util/lib -L/home/vsedyshev/Work/1111/pjproject/pjnath/lib -L/home/vsedyshev/Work/1111/pjproject/pjmedia/lib -L/home/vsedyshev/Work/1111/pjproject/pjsip/lib -L/home/vsedyshev/Work/1111/pjproject/third_party/lib -lSDL2     -lSDL2      -lpjsua-x86_64-unknown-linux-gnu -lpjsip-ua-x86_64-unknown-linux-gnu -lpjsip-simple-x86_64-unknown-linux-gnu -lpjsip-x86_64-unknown-linux-gnu -lpjmedia-codec-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjmedia-videodev-x86_64-unknown-linux-gnu -lpjmedia-audiodev-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjnath-x86_64-unknown-linux-gnu -lpjlib-util-x86_64-unknown-linux-gnu  -lsrtp-x86_64-unknown-linux-gnu -lresample-x86_64-unknown-linux-gnu -lgsmcodec-x86_64-unknown-linux-gnu -lspeex-x86_64-unknown-linux-gnu -lilbccodec-x86_64-unknown-linux-gnu -lg7221codec-x86_64-unknown-linux-gnu -lyuv-x86_64-unknown-linux-gnu -lwebrtc-x86_64-unknown-linux-gnu  -lpj-x86_64-unknown-linux-gnu -lssl -lcrypto -luuid -lm -lrt -lpthread  -lasound -lSDL2   
# make --no-print-directory -f /home/vsedyshev/Work/1111/pjproject/build/rules.mak SAMPLE_SRCDIR=../src/samples SAMPLE_OBJS=streamutil.o SAMPLE_CFLAGS="-DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1 -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -I/home/vsedyshev/Work/1111/pjproject/pjlib/include -I/home/vsedyshev/Work/1111/pjproject/pjlib-util/include -I/home/vsedyshev/Work/1111/pjproject/pjnath/include -I/home/vsedyshev/Work/1111/pjproject/pjmedia/include -I/home/vsedyshev/Work/1111/pjproject/pjsip/include " SAMPLE_CXXFLAGS="-g -O2 -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1 -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -I/home/vsedyshev/Work/1111/pjproject/pjlib/include -I/home/vsedyshev/Work/1111/pjproject/pjlib-util/include -I/home/vsedyshev/Work/1111/pjproject/pjnath/include -I/home/vsedyshev/Work/1111/pjproject/pjmedia/include -I/home/vsedyshev/Work/1111/pjproject/pjsip/include " SAMPLE_LDFLAGS="-L/home/vsedyshev/Work/1111/pjproject/pjlib/lib -L/home/vsedyshev/Work/1111/pjproject/pjlib-util/lib -L/home/vsedyshev/Work/1111/pjproject/pjnath/lib -L/home/vsedyshev/Work/1111/pjproject/pjmedia/lib -L/home/vsedyshev/Work/1111/pjproject/pjsip/lib -L/home/vsedyshev/Work/1111/pjproject/third_party/lib -lSDL2     -lSDL2      -lpjsua-x86_64-unknown-linux-gnu -lpjsip-ua-x86_64-unknown-linux-gnu -lpjsip-simple-x86_64-unknown-linux-gnu -lpjsip-x86_64-unknown-linux-gnu -lpjmedia-codec-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjmedia-videodev-x86_64-unknown-linux-gnu -lpjmedia-audiodev-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjnath-x86_64-unknown-linux-gnu -lpjlib-util-x86_64-unknown-linux-gnu  -lsrtp-x86_64-unknown-linux-gnu -lresample-x86_64-unknown-linux-gnu -lgsmcodec-x86_64-unknown-linux-gnu -lspeex-x86_64-unknown-linux-gnu -lilbccodec-x86_64-unknown-linux-gnu -lg7221codec-x86_64-unknown-linux-gnu -lyuv-x86_64-unknown-linux-gnu -lwebrtc-x86_64-unknown-linux-gnu  -lpj-x86_64-unknown-linux-gnu -lssl -lcrypto -luuid -lm -lrt -lpthread  -lasound -lSDL2   " SAMPLE_EXE=streamutil APP=SAMPLE app=sample ../bin/samples/x86_64-unknown-linux-gnu/streamutil
# gcc -c -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1 -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -I/home/vsedyshev/Work/1111/pjproject/pjlib/include -I/home/vsedyshev/Work/1111/pjproject/pjlib-util/include -I/home/vsedyshev/Work/1111/pjproject/pjnath/include -I/home/vsedyshev/Work/1111/pjproject/pjmedia/include -I/home/vsedyshev/Work/1111/pjproject/pjsip/include  \
# 	-o output/sample-x86_64-unknown-linux-gnu/streamutil.o \
# 	../src/samples/streamutil.c 
# if test ! -d ../bin/samples/x86_64-unknown-linux-gnu; then mkdir -p ../bin/samples/x86_64-unknown-linux-gnu; fi
# gcc -o ../bin/samples/x86_64-unknown-linux-gnu/streamutil \
#      output/sample-x86_64-unknown-linux-gnu/streamutil.o -L/home/vsedyshev/Work/1111/pjproject/pjlib/lib -L/home/vsedyshev/Work/1111/pjproject/pjlib-util/lib -L/home/vsedyshev/Work/1111/pjproject/pjnath/lib -L/home/vsedyshev/Work/1111/pjproject/pjmedia/lib -L/home/vsedyshev/Work/1111/pjproject/pjsip/lib -L/home/vsedyshev/Work/1111/pjproject/third_party/lib -lSDL2     -lSDL2      -lpjsua-x86_64-unknown-linux-gnu -lpjsip-ua-x86_64-unknown-linux-gnu -lpjsip-simple-x86_64-unknown-linux-gnu -lpjsip-x86_64-unknown-linux-gnu -lpjmedia-codec-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjmedia-videodev-x86_64-unknown-linux-gnu -lpjmedia-audiodev-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjnath-x86_64-unknown-linux-gnu -lpjlib-util-x86_64-unknown-linux-gnu  -lsrtp-x86_64-unknown-linux-gnu -lresample-x86_64-unknown-linux-gnu -lgsmcodec-x86_64-unknown-linux-gnu -lspeex-x86_64-unknown-linux-gnu -lilbccodec-x86_64-unknown-linux-gnu -lg7221codec-x86_64-unknown-linux-gnu -lyuv-x86_64-unknown-linux-gnu -lwebrtc-x86_64-unknown-linux-gnu  -lpj-x86_64-unknown-linux-gnu -lssl -lcrypto -luuid -lm -lrt -lpthread  -lasound -lSDL2   
# make --no-print-directory -f /home/vsedyshev/Work/1111/pjproject/build/rules.mak SAMPLE_SRCDIR=../src/samples SAMPLE_OBJS=strerror.o SAMPLE_CFLAGS="-DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1 -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -I/home/vsedyshev/Work/1111/pjproject/pjlib/include -I/home/vsedyshev/Work/1111/pjproject/pjlib-util/include -I/home/vsedyshev/Work/1111/pjproject/pjnath/include -I/home/vsedyshev/Work/1111/pjproject/pjmedia/include -I/home/vsedyshev/Work/1111/pjproject/pjsip/include " SAMPLE_CXXFLAGS="-g -O2 -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1 -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -I/home/vsedyshev/Work/1111/pjproject/pjlib/include -I/home/vsedyshev/Work/1111/pjproject/pjlib-util/include -I/home/vsedyshev/Work/1111/pjproject/pjnath/include -I/home/vsedyshev/Work/1111/pjproject/pjmedia/include -I/home/vsedyshev/Work/1111/pjproject/pjsip/include " SAMPLE_LDFLAGS="-L/home/vsedyshev/Work/1111/pjproject/pjlib/lib -L/home/vsedyshev/Work/1111/pjproject/pjlib-util/lib -L/home/vsedyshev/Work/1111/pjproject/pjnath/lib -L/home/vsedyshev/Work/1111/pjproject/pjmedia/lib -L/home/vsedyshev/Work/1111/pjproject/pjsip/lib -L/home/vsedyshev/Work/1111/pjproject/third_party/lib -lSDL2     -lSDL2      -lpjsua-x86_64-unknown-linux-gnu -lpjsip-ua-x86_64-unknown-linux-gnu -lpjsip-simple-x86_64-unknown-linux-gnu -lpjsip-x86_64-unknown-linux-gnu -lpjmedia-codec-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjmedia-videodev-x86_64-unknown-linux-gnu -lpjmedia-audiodev-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjnath-x86_64-unknown-linux-gnu -lpjlib-util-x86_64-unknown-linux-gnu  -lsrtp-x86_64-unknown-linux-gnu -lresample-x86_64-unknown-linux-gnu -lgsmcodec-x86_64-unknown-linux-gnu -lspeex-x86_64-unknown-linux-gnu -lilbccodec-x86_64-unknown-linux-gnu -lg7221codec-x86_64-unknown-linux-gnu -lyuv-x86_64-unknown-linux-gnu -lwebrtc-x86_64-unknown-linux-gnu  -lpj-x86_64-unknown-linux-gnu -lssl -lcrypto -luuid -lm -lrt -lpthread  -lasound -lSDL2   " SAMPLE_EXE=strerror APP=SAMPLE app=sample ../bin/samples/x86_64-unknown-linux-gnu/strerror
# gcc -c -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1 -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -I/home/vsedyshev/Work/1111/pjproject/pjlib/include -I/home/vsedyshev/Work/1111/pjproject/pjlib-util/include -I/home/vsedyshev/Work/1111/pjproject/pjnath/include -I/home/vsedyshev/Work/1111/pjproject/pjmedia/include -I/home/vsedyshev/Work/1111/pjproject/pjsip/include  \
# 	-o output/sample-x86_64-unknown-linux-gnu/strerror.o \
# 	../src/samples/strerror.c 
# if test ! -d ../bin/samples/x86_64-unknown-linux-gnu; then mkdir -p ../bin/samples/x86_64-unknown-linux-gnu; fi
# gcc -o ../bin/samples/x86_64-unknown-linux-gnu/strerror \
#      output/sample-x86_64-unknown-linux-gnu/strerror.o -L/home/vsedyshev/Work/1111/pjproject/pjlib/lib -L/home/vsedyshev/Work/1111/pjproject/pjlib-util/lib -L/home/vsedyshev/Work/1111/pjproject/pjnath/lib -L/home/vsedyshev/Work/1111/pjproject/pjmedia/lib -L/home/vsedyshev/Work/1111/pjproject/pjsip/lib -L/home/vsedyshev/Work/1111/pjproject/third_party/lib -lSDL2     -lSDL2      -lpjsua-x86_64-unknown-linux-gnu -lpjsip-ua-x86_64-unknown-linux-gnu -lpjsip-simple-x86_64-unknown-linux-gnu -lpjsip-x86_64-unknown-linux-gnu -lpjmedia-codec-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjmedia-videodev-x86_64-unknown-linux-gnu -lpjmedia-audiodev-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjnath-x86_64-unknown-linux-gnu -lpjlib-util-x86_64-unknown-linux-gnu  -lsrtp-x86_64-unknown-linux-gnu -lresample-x86_64-unknown-linux-gnu -lgsmcodec-x86_64-unknown-linux-gnu -lspeex-x86_64-unknown-linux-gnu -lilbccodec-x86_64-unknown-linux-gnu -lg7221codec-x86_64-unknown-linux-gnu -lyuv-x86_64-unknown-linux-gnu -lwebrtc-x86_64-unknown-linux-gnu  -lpj-x86_64-unknown-linux-gnu -lssl -lcrypto -luuid -lm -lrt -lpthread  -lasound -lSDL2   
# make --no-print-directory -f /home/vsedyshev/Work/1111/pjproject/build/rules.mak SAMPLE_SRCDIR=../src/samples SAMPLE_OBJS=tonegen.o SAMPLE_CFLAGS="-DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1 -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -I/home/vsedyshev/Work/1111/pjproject/pjlib/include -I/home/vsedyshev/Work/1111/pjproject/pjlib-util/include -I/home/vsedyshev/Work/1111/pjproject/pjnath/include -I/home/vsedyshev/Work/1111/pjproject/pjmedia/include -I/home/vsedyshev/Work/1111/pjproject/pjsip/include " SAMPLE_CXXFLAGS="-g -O2 -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1 -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -I/home/vsedyshev/Work/1111/pjproject/pjlib/include -I/home/vsedyshev/Work/1111/pjproject/pjlib-util/include -I/home/vsedyshev/Work/1111/pjproject/pjnath/include -I/home/vsedyshev/Work/1111/pjproject/pjmedia/include -I/home/vsedyshev/Work/1111/pjproject/pjsip/include " SAMPLE_LDFLAGS="-L/home/vsedyshev/Work/1111/pjproject/pjlib/lib -L/home/vsedyshev/Work/1111/pjproject/pjlib-util/lib -L/home/vsedyshev/Work/1111/pjproject/pjnath/lib -L/home/vsedyshev/Work/1111/pjproject/pjmedia/lib -L/home/vsedyshev/Work/1111/pjproject/pjsip/lib -L/home/vsedyshev/Work/1111/pjproject/third_party/lib -lSDL2     -lSDL2      -lpjsua-x86_64-unknown-linux-gnu -lpjsip-ua-x86_64-unknown-linux-gnu -lpjsip-simple-x86_64-unknown-linux-gnu -lpjsip-x86_64-unknown-linux-gnu -lpjmedia-codec-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjmedia-videodev-x86_64-unknown-linux-gnu -lpjmedia-audiodev-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjnath-x86_64-unknown-linux-gnu -lpjlib-util-x86_64-unknown-linux-gnu  -lsrtp-x86_64-unknown-linux-gnu -lresample-x86_64-unknown-linux-gnu -lgsmcodec-x86_64-unknown-linux-gnu -lspeex-x86_64-unknown-linux-gnu -lilbccodec-x86_64-unknown-linux-gnu -lg7221codec-x86_64-unknown-linux-gnu -lyuv-x86_64-unknown-linux-gnu -lwebrtc-x86_64-unknown-linux-gnu  -lpj-x86_64-unknown-linux-gnu -lssl -lcrypto -luuid -lm -lrt -lpthread  -lasound -lSDL2   " SAMPLE_EXE=tonegen APP=SAMPLE app=sample ../bin/samples/x86_64-unknown-linux-gnu/tonegen
# gcc -c -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1 -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -I/home/vsedyshev/Work/1111/pjproject/pjlib/include -I/home/vsedyshev/Work/1111/pjproject/pjlib-util/include -I/home/vsedyshev/Work/1111/pjproject/pjnath/include -I/home/vsedyshev/Work/1111/pjproject/pjmedia/include -I/home/vsedyshev/Work/1111/pjproject/pjsip/include  \
# 	-o output/sample-x86_64-unknown-linux-gnu/tonegen.o \
# 	../src/samples/tonegen.c 
# if test ! -d ../bin/samples/x86_64-unknown-linux-gnu; then mkdir -p ../bin/samples/x86_64-unknown-linux-gnu; fi
# gcc -o ../bin/samples/x86_64-unknown-linux-gnu/tonegen \
#      output/sample-x86_64-unknown-linux-gnu/tonegen.o -L/home/vsedyshev/Work/1111/pjproject/pjlib/lib -L/home/vsedyshev/Work/1111/pjproject/pjlib-util/lib -L/home/vsedyshev/Work/1111/pjproject/pjnath/lib -L/home/vsedyshev/Work/1111/pjproject/pjmedia/lib -L/home/vsedyshev/Work/1111/pjproject/pjsip/lib -L/home/vsedyshev/Work/1111/pjproject/third_party/lib -lSDL2     -lSDL2      -lpjsua-x86_64-unknown-linux-gnu -lpjsip-ua-x86_64-unknown-linux-gnu -lpjsip-simple-x86_64-unknown-linux-gnu -lpjsip-x86_64-unknown-linux-gnu -lpjmedia-codec-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjmedia-videodev-x86_64-unknown-linux-gnu -lpjmedia-audiodev-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjnath-x86_64-unknown-linux-gnu -lpjlib-util-x86_64-unknown-linux-gnu  -lsrtp-x86_64-unknown-linux-gnu -lresample-x86_64-unknown-linux-gnu -lgsmcodec-x86_64-unknown-linux-gnu -lspeex-x86_64-unknown-linux-gnu -lilbccodec-x86_64-unknown-linux-gnu -lg7221codec-x86_64-unknown-linux-gnu -lyuv-x86_64-unknown-linux-gnu -lwebrtc-x86_64-unknown-linux-gnu  -lpj-x86_64-unknown-linux-gnu -lssl -lcrypto -luuid -lm -lrt -lpthread  -lasound -lSDL2   
# make --no-print-directory -f /home/vsedyshev/Work/1111/pjproject/build/rules.mak SAMPLE_SRCDIR=../src/samples SAMPLE_OBJS=vid_codec_test.o SAMPLE_CFLAGS="-DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1 -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -I/home/vsedyshev/Work/1111/pjproject/pjlib/include -I/home/vsedyshev/Work/1111/pjproject/pjlib-util/include -I/home/vsedyshev/Work/1111/pjproject/pjnath/include -I/home/vsedyshev/Work/1111/pjproject/pjmedia/include -I/home/vsedyshev/Work/1111/pjproject/pjsip/include " SAMPLE_CXXFLAGS="-g -O2 -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1 -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -I/home/vsedyshev/Work/1111/pjproject/pjlib/include -I/home/vsedyshev/Work/1111/pjproject/pjlib-util/include -I/home/vsedyshev/Work/1111/pjproject/pjnath/include -I/home/vsedyshev/Work/1111/pjproject/pjmedia/include -I/home/vsedyshev/Work/1111/pjproject/pjsip/include " SAMPLE_LDFLAGS="-L/home/vsedyshev/Work/1111/pjproject/pjlib/lib -L/home/vsedyshev/Work/1111/pjproject/pjlib-util/lib -L/home/vsedyshev/Work/1111/pjproject/pjnath/lib -L/home/vsedyshev/Work/1111/pjproject/pjmedia/lib -L/home/vsedyshev/Work/1111/pjproject/pjsip/lib -L/home/vsedyshev/Work/1111/pjproject/third_party/lib -lSDL2     -lSDL2      -lpjsua-x86_64-unknown-linux-gnu -lpjsip-ua-x86_64-unknown-linux-gnu -lpjsip-simple-x86_64-unknown-linux-gnu -lpjsip-x86_64-unknown-linux-gnu -lpjmedia-codec-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjmedia-videodev-x86_64-unknown-linux-gnu -lpjmedia-audiodev-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjnath-x86_64-unknown-linux-gnu -lpjlib-util-x86_64-unknown-linux-gnu  -lsrtp-x86_64-unknown-linux-gnu -lresample-x86_64-unknown-linux-gnu -lgsmcodec-x86_64-unknown-linux-gnu -lspeex-x86_64-unknown-linux-gnu -lilbccodec-x86_64-unknown-linux-gnu -lg7221codec-x86_64-unknown-linux-gnu -lyuv-x86_64-unknown-linux-gnu -lwebrtc-x86_64-unknown-linux-gnu  -lpj-x86_64-unknown-linux-gnu -lssl -lcrypto -luuid -lm -lrt -lpthread  -lasound -lSDL2   " SAMPLE_EXE=vid_codec_test APP=SAMPLE app=sample ../bin/samples/x86_64-unknown-linux-gnu/vid_codec_test
# gcc -c -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1 -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -I/home/vsedyshev/Work/1111/pjproject/pjlib/include -I/home/vsedyshev/Work/1111/pjproject/pjlib-util/include -I/home/vsedyshev/Work/1111/pjproject/pjnath/include -I/home/vsedyshev/Work/1111/pjproject/pjmedia/include -I/home/vsedyshev/Work/1111/pjproject/pjsip/include  \
# 	-o output/sample-x86_64-unknown-linux-gnu/vid_codec_test.o \
# 	../src/samples/vid_codec_test.c 
# if test ! -d ../bin/samples/x86_64-unknown-linux-gnu; then mkdir -p ../bin/samples/x86_64-unknown-linux-gnu; fi
# gcc -o ../bin/samples/x86_64-unknown-linux-gnu/vid_codec_test \
#      output/sample-x86_64-unknown-linux-gnu/vid_codec_test.o -L/home/vsedyshev/Work/1111/pjproject/pjlib/lib -L/home/vsedyshev/Work/1111/pjproject/pjlib-util/lib -L/home/vsedyshev/Work/1111/pjproject/pjnath/lib -L/home/vsedyshev/Work/1111/pjproject/pjmedia/lib -L/home/vsedyshev/Work/1111/pjproject/pjsip/lib -L/home/vsedyshev/Work/1111/pjproject/third_party/lib -lSDL2     -lSDL2      -lpjsua-x86_64-unknown-linux-gnu -lpjsip-ua-x86_64-unknown-linux-gnu -lpjsip-simple-x86_64-unknown-linux-gnu -lpjsip-x86_64-unknown-linux-gnu -lpjmedia-codec-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjmedia-videodev-x86_64-unknown-linux-gnu -lpjmedia-audiodev-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjnath-x86_64-unknown-linux-gnu -lpjlib-util-x86_64-unknown-linux-gnu  -lsrtp-x86_64-unknown-linux-gnu -lresample-x86_64-unknown-linux-gnu -lgsmcodec-x86_64-unknown-linux-gnu -lspeex-x86_64-unknown-linux-gnu -lilbccodec-x86_64-unknown-linux-gnu -lg7221codec-x86_64-unknown-linux-gnu -lyuv-x86_64-unknown-linux-gnu -lwebrtc-x86_64-unknown-linux-gnu  -lpj-x86_64-unknown-linux-gnu -lssl -lcrypto -luuid -lm -lrt -lpthread  -lasound -lSDL2   
# make --no-print-directory -f /home/vsedyshev/Work/1111/pjproject/build/rules.mak SAMPLE_SRCDIR=../src/samples SAMPLE_OBJS=vid_streamutil.o SAMPLE_CFLAGS="-DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1 -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -I/home/vsedyshev/Work/1111/pjproject/pjlib/include -I/home/vsedyshev/Work/1111/pjproject/pjlib-util/include -I/home/vsedyshev/Work/1111/pjproject/pjnath/include -I/home/vsedyshev/Work/1111/pjproject/pjmedia/include -I/home/vsedyshev/Work/1111/pjproject/pjsip/include " SAMPLE_CXXFLAGS="-g -O2 -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1 -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -I/home/vsedyshev/Work/1111/pjproject/pjlib/include -I/home/vsedyshev/Work/1111/pjproject/pjlib-util/include -I/home/vsedyshev/Work/1111/pjproject/pjnath/include -I/home/vsedyshev/Work/1111/pjproject/pjmedia/include -I/home/vsedyshev/Work/1111/pjproject/pjsip/include " SAMPLE_LDFLAGS="-L/home/vsedyshev/Work/1111/pjproject/pjlib/lib -L/home/vsedyshev/Work/1111/pjproject/pjlib-util/lib -L/home/vsedyshev/Work/1111/pjproject/pjnath/lib -L/home/vsedyshev/Work/1111/pjproject/pjmedia/lib -L/home/vsedyshev/Work/1111/pjproject/pjsip/lib -L/home/vsedyshev/Work/1111/pjproject/third_party/lib -lSDL2     -lSDL2      -lpjsua-x86_64-unknown-linux-gnu -lpjsip-ua-x86_64-unknown-linux-gnu -lpjsip-simple-x86_64-unknown-linux-gnu -lpjsip-x86_64-unknown-linux-gnu -lpjmedia-codec-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjmedia-videodev-x86_64-unknown-linux-gnu -lpjmedia-audiodev-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjnath-x86_64-unknown-linux-gnu -lpjlib-util-x86_64-unknown-linux-gnu  -lsrtp-x86_64-unknown-linux-gnu -lresample-x86_64-unknown-linux-gnu -lgsmcodec-x86_64-unknown-linux-gnu -lspeex-x86_64-unknown-linux-gnu -lilbccodec-x86_64-unknown-linux-gnu -lg7221codec-x86_64-unknown-linux-gnu -lyuv-x86_64-unknown-linux-gnu -lwebrtc-x86_64-unknown-linux-gnu  -lpj-x86_64-unknown-linux-gnu -lssl -lcrypto -luuid -lm -lrt -lpthread  -lasound -lSDL2   " SAMPLE_EXE=vid_streamutil APP=SAMPLE app=sample ../bin/samples/x86_64-unknown-linux-gnu/vid_streamutil
# gcc -c -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1 -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -I/home/vsedyshev/Work/1111/pjproject/pjlib/include -I/home/vsedyshev/Work/1111/pjproject/pjlib-util/include -I/home/vsedyshev/Work/1111/pjproject/pjnath/include -I/home/vsedyshev/Work/1111/pjproject/pjmedia/include -I/home/vsedyshev/Work/1111/pjproject/pjsip/include  \
# 	-o output/sample-x86_64-unknown-linux-gnu/vid_streamutil.o \
# 	../src/samples/vid_streamutil.c 
# if test ! -d ../bin/samples/x86_64-unknown-linux-gnu; then mkdir -p ../bin/samples/x86_64-unknown-linux-gnu; fi
# gcc -o ../bin/samples/x86_64-unknown-linux-gnu/vid_streamutil \
#      output/sample-x86_64-unknown-linux-gnu/vid_streamutil.o -L/home/vsedyshev/Work/1111/pjproject/pjlib/lib -L/home/vsedyshev/Work/1111/pjproject/pjlib-util/lib -L/home/vsedyshev/Work/1111/pjproject/pjnath/lib -L/home/vsedyshev/Work/1111/pjproject/pjmedia/lib -L/home/vsedyshev/Work/1111/pjproject/pjsip/lib -L/home/vsedyshev/Work/1111/pjproject/third_party/lib -lSDL2     -lSDL2      -lpjsua-x86_64-unknown-linux-gnu -lpjsip-ua-x86_64-unknown-linux-gnu -lpjsip-simple-x86_64-unknown-linux-gnu -lpjsip-x86_64-unknown-linux-gnu -lpjmedia-codec-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjmedia-videodev-x86_64-unknown-linux-gnu -lpjmedia-audiodev-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjnath-x86_64-unknown-linux-gnu -lpjlib-util-x86_64-unknown-linux-gnu  -lsrtp-x86_64-unknown-linux-gnu -lresample-x86_64-unknown-linux-gnu -lgsmcodec-x86_64-unknown-linux-gnu -lspeex-x86_64-unknown-linux-gnu -lilbccodec-x86_64-unknown-linux-gnu -lg7221codec-x86_64-unknown-linux-gnu -lyuv-x86_64-unknown-linux-gnu -lwebrtc-x86_64-unknown-linux-gnu  -lpj-x86_64-unknown-linux-gnu -lssl -lcrypto -luuid -lm -lrt -lpthread  -lasound -lSDL2   
# make --no-print-directory -f /home/vsedyshev/Work/1111/pjproject/build/rules.mak PJSUA2_SAMPLE_SRCDIR=../src/samples PJSUA2_SAMPLE_OBJS=pjsua2_demo.o PJSUA2_SAMPLE_CFLAGS="-DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1 -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -I/home/vsedyshev/Work/1111/pjproject/pjlib/include -I/home/vsedyshev/Work/1111/pjproject/pjlib-util/include -I/home/vsedyshev/Work/1111/pjproject/pjnath/include -I/home/vsedyshev/Work/1111/pjproject/pjmedia/include -I/home/vsedyshev/Work/1111/pjproject/pjsip/include " PJSUA2_SAMPLE_CXXFLAGS="-g -O2 -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1 -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -I/home/vsedyshev/Work/1111/pjproject/pjlib/include -I/home/vsedyshev/Work/1111/pjproject/pjlib-util/include -I/home/vsedyshev/Work/1111/pjproject/pjnath/include -I/home/vsedyshev/Work/1111/pjproject/pjmedia/include -I/home/vsedyshev/Work/1111/pjproject/pjsip/include " PJSUA2_SAMPLE_LDFLAGS="-L/home/vsedyshev/Work/1111/pjproject/pjlib/lib -L/home/vsedyshev/Work/1111/pjproject/pjlib-util/lib -L/home/vsedyshev/Work/1111/pjproject/pjnath/lib -L/home/vsedyshev/Work/1111/pjproject/pjmedia/lib -L/home/vsedyshev/Work/1111/pjproject/pjsip/lib -L/home/vsedyshev/Work/1111/pjproject/third_party/lib -lSDL2     -lSDL2      -lpjsua2-x86_64-unknown-linux-gnu -lstdc++ -lpjsua-x86_64-unknown-linux-gnu -lpjsip-ua-x86_64-unknown-linux-gnu -lpjsip-simple-x86_64-unknown-linux-gnu -lpjsip-x86_64-unknown-linux-gnu -lpjmedia-codec-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjmedia-videodev-x86_64-unknown-linux-gnu -lpjmedia-audiodev-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjnath-x86_64-unknown-linux-gnu -lpjlib-util-x86_64-unknown-linux-gnu  -lsrtp-x86_64-unknown-linux-gnu -lresample-x86_64-unknown-linux-gnu -lgsmcodec-x86_64-unknown-linux-gnu -lspeex-x86_64-unknown-linux-gnu -lilbccodec-x86_64-unknown-linux-gnu -lg7221codec-x86_64-unknown-linux-gnu -lyuv-x86_64-unknown-linux-gnu -lwebrtc-x86_64-unknown-linux-gnu  -lpj-x86_64-unknown-linux-gnu -lssl -lcrypto -luuid -lm -lrt -lpthread  -lasound -lSDL2   " PJSUA2_SAMPLE_EXE=pjsua2_demo APP=PJSUA2_SAMPLE app=pjsua2_sample ../bin/samples/x86_64-unknown-linux-gnu/pjsua2_demo
# mkdir -p output/pjsua2_sample-x86_64-unknown-linux-gnu/
# g++ -c -g -O2 -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1 -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -I/home/vsedyshev/Work/1111/pjproject/pjlib/include -I/home/vsedyshev/Work/1111/pjproject/pjlib-util/include -I/home/vsedyshev/Work/1111/pjproject/pjnath/include -I/home/vsedyshev/Work/1111/pjproject/pjmedia/include -I/home/vsedyshev/Work/1111/pjproject/pjsip/include  \
# 	-o output/pjsua2_sample-x86_64-unknown-linux-gnu/pjsua2_demo.o \
# 	../src/samples/pjsua2_demo.cpp
# if test ! -d ../bin/samples/x86_64-unknown-linux-gnu; then mkdir -p ../bin/samples/x86_64-unknown-linux-gnu; fi
# gcc -o ../bin/samples/x86_64-unknown-linux-gnu/pjsua2_demo \
#      output/pjsua2_sample-x86_64-unknown-linux-gnu/pjsua2_demo.o -L/home/vsedyshev/Work/1111/pjproject/pjlib/lib -L/home/vsedyshev/Work/1111/pjproject/pjlib-util/lib -L/home/vsedyshev/Work/1111/pjproject/pjnath/lib -L/home/vsedyshev/Work/1111/pjproject/pjmedia/lib -L/home/vsedyshev/Work/1111/pjproject/pjsip/lib -L/home/vsedyshev/Work/1111/pjproject/third_party/lib -lSDL2     -lSDL2      -lpjsua2-x86_64-unknown-linux-gnu -lstdc++ -lpjsua-x86_64-unknown-linux-gnu -lpjsip-ua-x86_64-unknown-linux-gnu -lpjsip-simple-x86_64-unknown-linux-gnu -lpjsip-x86_64-unknown-linux-gnu -lpjmedia-codec-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjmedia-videodev-x86_64-unknown-linux-gnu -lpjmedia-audiodev-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjnath-x86_64-unknown-linux-gnu -lpjlib-util-x86_64-unknown-linux-gnu  -lsrtp-x86_64-unknown-linux-gnu -lresample-x86_64-unknown-linux-gnu -lgsmcodec-x86_64-unknown-linux-gnu -lspeex-x86_64-unknown-linux-gnu -lilbccodec-x86_64-unknown-linux-gnu -lg7221codec-x86_64-unknown-linux-gnu -lyuv-x86_64-unknown-linux-gnu -lwebrtc-x86_64-unknown-linux-gnu  -lpj-x86_64-unknown-linux-gnu -lssl -lcrypto -luuid -lm -lrt -lpthread  -lasound -lSDL2   
# make[2]: Leaving directory '/home/vsedyshev/Work/1111/pjproject/pjsip-apps/build'
# make[1]: Leaving directory '/home/vsedyshev/Work/1111/pjproject/pjsip-apps/build'
