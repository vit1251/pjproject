project('pjproject', ['c', 'cpp'], license: 'GPL2', subproject_dir: 'third_party', version: '2.10')

# include directory

pjlib_inc = include_directories('pjlib/include')
pjlib_util_inc = include_directories('pjlib-util/include')
pjmedia_inc = include_directories('pjmedia/include')
pjsip_inc = include_directories('pjsip/include')
pjnath_inc = include_directories('pjnath/include')

# compilers

c_compiler = meson.get_compiler('c')

# dependencies

openssl_dep = dependency('openssl') #-lssl -lcrypto
uuid_dep = dependency('uuid') #-luuid
m_dep = c_compiler.find_library('m') #-lm
rt_dep = c_compiler.find_library('rt') #-lrt
pthread_dep = dependency('threads') #-lpthread
asound_dep = c_compiler.find_library('asound') #-lasound
SDL2_dep = dependency('SDL2') #-lSDL2

# subprojects

#if %system_speex%
#speex_dep = dependency('speex') #-lspeex
#else
#speex_proj = subproject('speex')
#speex_dep = speex_proj.get_variable('speex_dep')
#end

# pjlib

pjlib_sources = [
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

pjlib = static_library('pjlib', pjlib_sources,
        include_directories: [pjlib_inc],
        c_args: ['-Wall', '-DPJ_LINUX=1', '-O2', '-DPJ_IS_BIG_ENDIAN=0', '-DPJ_IS_LITTLE_ENDIAN=1'],
    )
pjlib_dep = declare_dependency(
        link_with: pjlib,
        include_directories: [pjlib_inc],
    )

# pjlib-test

pjlib_test_sources = [
    'pjlib/src/pjlib-test/main.c',
    'pjlib/src/pjlib-test/activesock.c',
    'pjlib/src/pjlib-test/atomic.c',
    'pjlib/src/pjlib-test/echo_clt.c',
    'pjlib/src/pjlib-test/errno.c',
    'pjlib/src/pjlib-test/exception.c',
    'pjlib/src/pjlib-test/fifobuf.c',
    'pjlib/src/pjlib-test/file.c',
    'pjlib/src/pjlib-test/hash_test.c',
    'pjlib/src/pjlib-test/ioq_perf.c',
    'pjlib/src/pjlib-test/ioq_udp.c',
    'pjlib/src/pjlib-test/ioq_unreg.c',
    'pjlib/src/pjlib-test/ioq_tcp.c',
    'pjlib/src/pjlib-test/list.c',
    'pjlib/src/pjlib-test/mutex.c',
    'pjlib/src/pjlib-test/os.c',
    'pjlib/src/pjlib-test/pool.c',
    'pjlib/src/pjlib-test/pool_perf.c',
    'pjlib/src/pjlib-test/rand.c',
    'pjlib/src/pjlib-test/rbtree.c',
    'pjlib/src/pjlib-test/select.c',
    'pjlib/src/pjlib-test/sleep.c',
    'pjlib/src/pjlib-test/sock.c',
    'pjlib/src/pjlib-test/sock_perf.c',
    'pjlib/src/pjlib-test/ssl_sock.c',
    'pjlib/src/pjlib-test/string.c',
    'pjlib/src/pjlib-test/test.c',
    'pjlib/src/pjlib-test/thread.c',
    'pjlib/src/pjlib-test/timer.c',
    'pjlib/src/pjlib-test/timestamp.c',
    'pjlib/src/pjlib-test/udp_echo_srv_sync.c',
    'pjlib/src/pjlib-test/udp_echo_srv_ioqueue.c',
    'pjlib/src/pjlib-test/util.c',
]



pjlib_test = executable('pjlib-test', pjlib_test_sources,
        include_directories: [pjlib_inc],
        dependencies: [pjlib_dep, openssl_dep, uuid_dep, m_dep, rt_dep, pthread_dep, asound_dep, SDL2_dep],
        c_args: ['-Wall', '-DPJ_LINUX=1', '-O2', '-DPJ_IS_BIG_ENDIAN=0', '-DPJ_IS_LITTLE_ENDIAN=1'],
    )
test('Check pjlib', pjlib_test, timeout: 360, protocol: 'exitcode', is_parallel: false)

# pjlib-util

pjlib_util_sources = [
    'pjlib-util/src/pjlib-util/base64.c',
    'pjlib-util/src/pjlib-util/cli.c',
    'pjlib-util/src/pjlib-util/cli_console.c',
    'pjlib-util/src/pjlib-util/cli_telnet.c',
    'pjlib-util/src/pjlib-util/crc32.c',
    'pjlib-util/src/pjlib-util/errno.c',
    'pjlib-util/src/pjlib-util/dns.c',
    'pjlib-util/src/pjlib-util/dns_dump.c',
    'pjlib-util/src/pjlib-util/dns_server.c',
    'pjlib-util/src/pjlib-util/getopt.c',
    'pjlib-util/src/pjlib-util/hmac_md5.c',
    'pjlib-util/src/pjlib-util/hmac_sha1.c',
    'pjlib-util/src/pjlib-util/http_client.c',
    'pjlib-util/src/pjlib-util/json.c',
    'pjlib-util/src/pjlib-util/md5.c',
    'pjlib-util/src/pjlib-util/pcap.c',
    'pjlib-util/src/pjlib-util/resolver.c',
    'pjlib-util/src/pjlib-util/scanner.c',
    'pjlib-util/src/pjlib-util/sha1.c',
    'pjlib-util/src/pjlib-util/srv_resolver.c',
    'pjlib-util/src/pjlib-util/string.c',
    'pjlib-util/src/pjlib-util/stun_simple.c',
    'pjlib-util/src/pjlib-util/stun_simple_client.c',
    'pjlib-util/src/pjlib-util/xml.c',
]

pjlib_util = static_library('pjlib-util', pjlib_util_sources,
        include_directories: [pjlib_inc, pjlib_util_inc],
        c_args: ['-Wall', '-DPJ_LINUX=1', '-O2', '-DPJ_IS_BIG_ENDIAN=0', '-DPJ_IS_LITTLE_ENDIAN=1'],
    )
pjlib_util_dep = declare_dependency(
        link_with: pjlib_util,
        include_directories: [pjlib_util_inc],
    )

# pjlib-util-test

pjlib_util_test_sources = [
    'pjlib-util/src/pjlib-util-test/main.c',
    'pjlib-util/src/pjlib-util-test/xml.c',
    'pjlib-util/src/pjlib-util-test/encryption.c',
    'pjlib-util/src/pjlib-util-test/stun.c',
    'pjlib-util/src/pjlib-util-test/resolver_test.c',
    'pjlib-util/src/pjlib-util-test/test.c',
    'pjlib-util/src/pjlib-util-test/json_test.c',
    'pjlib-util/src/pjlib-util-test/http_client.c',
]

# -lssl
# -lcrypto
# -luuid
# -lm
# -lrt
# -lpthread
# -lasound
# -lSDL2

pjlib_util_test = executable('pjlib-util-test', pjlib_util_test_sources,
        include_directories: [pjlib_inc, pjlib_util_inc],
        dependencies: [pjlib_dep, pjlib_util_dep, openssl_dep, uuid_dep, m_dep, rt_dep, pthread_dep, asound_dep, SDL2_dep],
        c_args: ['-Wall', '-DPJ_LINUX=1', '-O2', '-DPJ_IS_BIG_ENDIAN=0', '-DPJ_IS_LITTLE_ENDIAN=1'],
    )
test('Check pjlib-util', pjlib_util_test, timeout: 360, protocol: 'exitcode', is_parallel: false)

# pjnath

pjnath_sources = [
    'pjnath/src/pjnath/errno.c',
    'pjnath/src/pjnath/ice_session.c',
    'pjnath/src/pjnath/ice_strans.c',
    'pjnath/src/pjnath/nat_detect.c',
    'pjnath/src/pjnath/stun_auth.c',
    'pjnath/src/pjnath/stun_msg.c',
    'pjnath/src/pjnath/stun_msg_dump.c',
    'pjnath/src/pjnath/stun_session.c',
    'pjnath/src/pjnath/stun_sock.c',
    'pjnath/src/pjnath/stun_transaction.c',
    'pjnath/src/pjnath/turn_session.c',
    'pjnath/src/pjnath/turn_sock.c',
]

pjnath = static_library('pjnath', pjnath_sources,
        include_directories: [pjlib_inc, pjlib_util_inc, pjnath_inc],
        c_args: ['-Wall', '-DPJ_LINUX=1', '-O2', '-DPJ_IS_BIG_ENDIAN=0', '-DPJ_IS_LITTLE_ENDIAN=1'],
    )
pjnath_dep = declare_dependency(
        link_with: pjnath,
        include_directories: [pjlib_inc, pjlib_util_inc, pjnath_inc],
    )

# pjnath-test

pjnath_test_sources = [
    'pjnath/src/pjnath-test/main.c',
    'pjnath/src/pjnath-test/ice_test.c',
    'pjnath/src/pjnath-test/stun.c',
    'pjnath/src/pjnath-test/sess_auth.c',
    'pjnath/src/pjnath-test/server.c',
    'pjnath/src/pjnath-test/concur_test.c',
    'pjnath/src/pjnath-test/stun_sock_test.c',
    'pjnath/src/pjnath-test/turn_sock_test.c',
    'pjnath/src/pjnath-test/test.c',
]

pjnath_test_dependencies = []

pjnath_test_dependencies += pjnath_dep # -lpjnath
pjnath_test_dependencies += pjlib_util_dep # -lpjlib-util
pjnath_test_dependencies += pjlib_dep # -lpj
pjnath_test_dependencies += openssl_dep # -lssl -lcrypto
pjnath_test_dependencies += uuid_dep # -luuid
pjnath_test_dependencies += m_dep # -lm
pjnath_test_dependencies += rt_dep # -lrt
pjnath_test_dependencies += pthread_dep # -lpthread
# -lasound
# -lSDL2

pjnath_test = executable('pjnath-test', pjnath_test_sources,
        dependencies: pjnath_test_dependencies,
        c_args: [
            '-Wall', '-DPJ_LINUX=1', '-O2', '-DPJ_IS_BIG_ENDIAN=0', '-DPJ_IS_LITTLE_ENDIAN=1',
        ],
    )
#test('Check pjnath', pjnath_test, ...)

# pjturn-client

# -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1

pjturn_client_sources = [
# 	../src/pjturn-client/client_main.c 
]

# -lpjnath
# -lpjlib-util
# -lpj
# -lssl
# -lcrypto
# -luuid
# -lm
# -lrt
# -lpthread
# -lasound
# -lSDL2

#executable('pjturn-client', pjturn_client_sources,
#    )

# pjturn-srv

# -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1    -I../include -I../../pjlib/include -I../../pjlib-util/include \

pjturn_srv_sources = [
# 	../src/pjturn-srv/allocation.c 
# 	../src/pjturn-srv/auth.c 
# 	../src/pjturn-srv/listener_udp.c 
# 	../src/pjturn-srv/listener_tcp.c 
# 	../src/pjturn-srv/server.c 
# 	../src/pjturn-srv/main.c 
]

# -lpjnath
# -lpjlib-util
# -lpj
# -lssl
# -lcrypto
# -luuid
# -lm
# -lrt
# -lpthread
# -lasound
# -lSDL2

#executable('pjturn', pjturn_srv_sources,
#    )

# pjmedia

pjmedia_sources = [
    'pjmedia/src/pjmedia/echo_speex.c',
    'pjmedia/src/pjmedia/alaw_ulaw.c',
    'pjmedia/src/pjmedia/alaw_ulaw_table.c',
    'pjmedia/src/pjmedia/avi_player.c',
    'pjmedia/src/pjmedia/bidirectional.c',
    'pjmedia/src/pjmedia/clock_thread.c',
    'pjmedia/src/pjmedia/codec.c',
    'pjmedia/src/pjmedia/conference.c',
    'pjmedia/src/pjmedia/conf_switch.c',
    'pjmedia/src/pjmedia/converter.c',
    'pjmedia/src/pjmedia/converter_libswscale.c',
    'pjmedia/src/pjmedia/converter_libyuv.c',
    'pjmedia/src/pjmedia/delaybuf.c',
    'pjmedia/src/pjmedia/echo_common.c',
    'pjmedia/src/pjmedia/echo_port.c',
    'pjmedia/src/pjmedia/echo_suppress.c',
    'pjmedia/src/pjmedia/echo_webrtc.c',
    'pjmedia/src/pjmedia/endpoint.c',
    'pjmedia/src/pjmedia/errno.c',
    'pjmedia/src/pjmedia/event.c',
    'pjmedia/src/pjmedia/format.c',
    'pjmedia/src/pjmedia/ffmpeg_util.c',
    'pjmedia/src/pjmedia/g711.c',
    'pjmedia/src/pjmedia/jbuf.c',
    'pjmedia/src/pjmedia/master_port.c',
    'pjmedia/src/pjmedia/mem_capture.c',
    'pjmedia/src/pjmedia/mem_player.c',
    'pjmedia/src/pjmedia/null_port.c',
    'pjmedia/src/pjmedia/plc_common.c',
    'pjmedia/src/pjmedia/port.c',
    'pjmedia/src/pjmedia/splitcomb.c',
    'pjmedia/src/pjmedia/resample_resample.c',
    'pjmedia/src/pjmedia/resample_libsamplerate.c',
    'pjmedia/src/pjmedia/resample_speex.c',
    'pjmedia/src/pjmedia/resample_port.c',
    'pjmedia/src/pjmedia/rtcp.c',
    'pjmedia/src/pjmedia/rtcp_xr.c',
    'pjmedia/src/pjmedia/rtcp_fb.c',
    'pjmedia/src/pjmedia/rtp.c',
    'pjmedia/src/pjmedia/sdp.c',
    'pjmedia/src/pjmedia/sdp_cmp.c',
    'pjmedia/src/pjmedia/sdp_neg.c',
    'pjmedia/src/pjmedia/session.c',
    'pjmedia/src/pjmedia/silencedet.c',
    'pjmedia/src/pjmedia/sound_legacy.c',
    'pjmedia/src/pjmedia/sound_port.c',
    'pjmedia/src/pjmedia/stereo_port.c',
    'pjmedia/src/pjmedia/stream_common.c',
    'pjmedia/src/pjmedia/stream.c',
    'pjmedia/src/pjmedia/stream_info.c',
    'pjmedia/src/pjmedia/tonegen.c',
    'pjmedia/src/pjmedia/transport_adapter_sample.c',
    'pjmedia/src/pjmedia/transport_ice.c',
    'pjmedia/src/pjmedia/transport_loop.c',
    'pjmedia/src/pjmedia/transport_srtp.c',
    'pjmedia/src/pjmedia/transport_udp.c',
    'pjmedia/src/pjmedia/types.c',
    'pjmedia/src/pjmedia/vid_codec.c',
    'pjmedia/src/pjmedia/vid_codec_util.c',
    'pjmedia/src/pjmedia/vid_port.c',
    'pjmedia/src/pjmedia/vid_stream.c',
    'pjmedia/src/pjmedia/vid_stream_info.c',
    'pjmedia/src/pjmedia/vid_conf.c',
    'pjmedia/src/pjmedia/wav_player.c',
    'pjmedia/src/pjmedia/wav_playlist.c',
    'pjmedia/src/pjmedia/wav_writer.c',
    'pjmedia/src/pjmedia/wave.c',
    'pjmedia/src/pjmedia/wsola.c',
    'pjmedia/src/pjmedia/audiodev.c',
    'pjmedia/src/pjmedia/videodev.c',
]

#pjmedia = static_library('pjmedia', pjmedia_sources,
#        include_directories: [pjlib_inc, pjmedia_inc],
#        dependencies: [speex_dep],
#        c_args: [
#            '-Wall', '-DPJ_LINUX=1', '-O2', '-DPJ_IS_BIG_ENDIAN=0', '-DPJ_IS_LITTLE_ENDIAN=1', '-DPJMEDIA_VIDEO_DEV_HAS_SDL=1',
#            '-D_REENTRANT', '-DPJMEDIA_USE_OLD_FFMPEG=1', '-DPJMEDIA_HAS_OPENCORE_AMRNB_CODEC=0', '-DPJMEDIA_HAS_OPENCORE_AMRWB_CODEC=0',
#            '-DPJMEDIA_RESAMPLE_IMP=PJMEDIA_RESAMPLE_LIBRESAMPLE', '-DPJMEDIA_HAS_LIBYUV=1', '-DPJMEDIA_HAS_WEBRTC_AEC=1',
#            '-DPJMEDIA_AUDIO_DEV_HAS_ALSA=1', '-DPJMEDIA_AUDIO_DEV_HAS_PORTAUDIO=0', '-DPJMEDIA_AUDIO_DEV_HAS_WMME=0',
#            '-DPJMEDIA_AUDIO_DEV_HAS_WMME=0',
#        ]
#    )

# pjmedia-codec

#-Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1   -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1        -I/home/vsedyshev/Work/1111/pjproject/third_party/build/speex -I/home/vsedyshev/Work/1111/pjproject/third_party/speex/include -DPJMEDIA_HAS_OPENCORE_AMRNB_CODEC=0 -DPJMEDIA_HAS_OPENCORE_AMRWB_CODEC=0 -I/home/vsedyshev/Work/1111/pjproject/third_party/build/srtp -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/crypto/include -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/include -DPJMEDIA_RESAMPLE_IMP=PJMEDIA_RESAMPLE_LIBRESAMPLE -DPJMEDIA_HAS_LIBYUV=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/yuv/include -DPJMEDIA_HAS_WEBRTC_AEC=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/webrtc/src -DPJMEDIA_AUDIO_DEV_HAS_ALSA=1 -DPJMEDIA_AUDIO_DEV_HAS_PORTAUDIO=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjmedia/include -I../../pjnath/include -I../..     -I/home/vsedyshev/Work/1111/pjproject/third_party

#pjmedia_codec_sources = [
# 	../src/pjmedia-codec/audio_codecs.c 
# 	../src/pjmedia-codec/ffmpeg_vid_codecs.c 
# 	../src/pjmedia-codec/openh264.cpp
# 	../src/pjmedia-codec/h263_packetizer.c 
# 	../src/pjmedia-codec/h264_packetizer.c 
# 	../src/pjmedia-codec/ipp_codecs.c 
# 	../src/pjmedia-codec/silk.c 
# 	../src/pjmedia-codec/opus.c 
# 	../src/pjmedia-codec/l16.c 
# 	../src/pjmedia-codec/gsm.c 
# 	../src/pjmedia-codec/speex_codec.c 
# 	../src/pjmedia-codec/ilbc.c 
# 	../src/pjmedia-codec/g722.c 
# 	../src/pjmedia-codec/g722/g722_enc.c 
# 	../src/pjmedia-codec/g722/g722_dec.c 
# 	../src/pjmedia-codec/g7221.c 
# 	../src/pjmedia-codec/g7221_sdp_match.c 
# 	../src/pjmedia-codec/amr_sdp_match.c 
# 	../src/pjmedia-codec/passthrough.c 
# 	../src/pjmedia-codec/vpx.c 
#]

#pjmedia_codec = static_library('pjmedia_codec', pjmedia_codec_sources,
#    )

# pjmedia-videodev

# -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1   -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1        -I/home/vsedyshev/Work/1111/pjproject/third_party/build/speex -I/home/vsedyshev/Work/1111/pjproject/third_party/speex/include -DPJMEDIA_HAS_OPENCORE_AMRNB_CODEC=0 -DPJMEDIA_HAS_OPENCORE_AMRWB_CODEC=0 -I/home/vsedyshev/Work/1111/pjproject/third_party/build/srtp -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/crypto/include -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/include -DPJMEDIA_RESAMPLE_IMP=PJMEDIA_RESAMPLE_LIBRESAMPLE -DPJMEDIA_HAS_LIBYUV=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/yuv/include -DPJMEDIA_HAS_WEBRTC_AEC=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/webrtc/src -DPJMEDIA_AUDIO_DEV_HAS_ALSA=1 -DPJMEDIA_AUDIO_DEV_HAS_PORTAUDIO=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjmedia/include -I../../pjnath/include -I../.. \

#pjmedia_videodev_sources = [
# 	../src/pjmedia-videodev/sdl_dev.c 
# 	../src/pjmedia-videodev/videodev.c 
# 	../src/pjmedia-videodev/errno.c 
# 	../src/pjmedia-videodev/avi_dev.c 
# 	../src/pjmedia-videodev/ffmpeg_dev.c 
# 	../src/pjmedia-videodev/colorbar_dev.c 
# 	../src/pjmedia-videodev/v4l2_dev.c 
# 	../src/pjmedia-videodev/opengl_dev.c 
# 	../src/pjmedia-videodev/util.c 
#]

#pjmedia_videodev = static_library('pjmedia_videodev', pjmedia_videodev_sources,
#    )

# pjmedia-audiodev

# -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1   -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1        -I/home/vsedyshev/Work/1111/pjproject/third_party/build/speex -I/home/vsedyshev/Work/1111/pjproject/third_party/speex/include -DPJMEDIA_HAS_OPENCORE_AMRNB_CODEC=0 -DPJMEDIA_HAS_OPENCORE_AMRWB_CODEC=0 -I/home/vsedyshev/Work/1111/pjproject/third_party/build/srtp -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/crypto/include -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/include -DPJMEDIA_RESAMPLE_IMP=PJMEDIA_RESAMPLE_LIBRESAMPLE -DPJMEDIA_HAS_LIBYUV=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/yuv/include -DPJMEDIA_HAS_WEBRTC_AEC=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/webrtc/src -DPJMEDIA_AUDIO_DEV_HAS_ALSA=1 -DPJMEDIA_AUDIO_DEV_HAS_PORTAUDIO=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjmedia/include -I../../pjnath/include -I../.. \

#pjmedia_audiodev_sources = [
# 	../src/pjmedia-audiodev/audiodev.c 
# 	../src/pjmedia-audiodev/audiotest.c 
# 	../src/pjmedia-audiodev/errno.c 
# 	../src/pjmedia-audiodev/legacy_dev.c 
# 	../src/pjmedia-audiodev/null_dev.c 
# 	../src/pjmedia-audiodev/pa_dev.c 
# 	../src/pjmedia-audiodev/wmme_dev.c 
# 	../src/pjmedia-audiodev/alsa_dev.c 
# 	../src/pjmedia-audiodev/bb10_dev.c 
# 	../src/pjmedia-audiodev/bdimad_dev.c 
# 	../src/pjmedia-audiodev/android_jni_dev.c 
# 	../src/pjmedia-audiodev/opensl_dev.c 
#]

#pjmedia_audiodev = static_library('pjmedia_audiodev', pjmedia_audiodev_sources
#    )

# pjsdp

pjsdp_sources = [
    'pjmedia/src/pjmedia/errno.c',
    'pjmedia/src/pjmedia/sdp.c',
    'pjmedia/src/pjmedia/sdp_cmp.c',
    'pjmedia/src/pjmedia/sdp_neg.c',
]

pjsdp = static_library('pjsdp', pjsdp_sources,
        include_directories: [pjlib_inc, pjlib_util_inc, pjmedia_inc],
        c_args: [
            '-Wall', '-DPJ_LINUX=1', '-O2', '-DPJ_IS_BIG_ENDIAN=0', '-DPJ_IS_LITTLE_ENDIAN=1', '-DPJMEDIA_VIDEO_DEV_HAS_SDL=1',
            '-D_REENTRANT', '-DPJMEDIA_USE_OLD_FFMPEG=1', '-DPJMEDIA_HAS_OPENCORE_AMRNB_CODEC=0', '-DPJMEDIA_HAS_OPENCORE_AMRWB_CODEC=0',
            '-DPJMEDIA_RESAMPLE_IMP=PJMEDIA_RESAMPLE_LIBRESAMPLE', '-DPJMEDIA_HAS_LIBYUV=1', '-DPJMEDIA_HAS_WEBRTC_AEC=1',
            '-DPJMEDIA_AUDIO_DEV_HAS_ALSA=1', '-DPJMEDIA_AUDIO_DEV_HAS_PORTAUDIO=0', '-DPJMEDIA_AUDIO_DEV_HAS_WMME=0',
            '-DPJMEDIA_AUDIO_DEV_HAS_WMME=0'
        ],
    )
pjsdp_dep = declare_dependency(
        link_with: pjsdp,
        include_directories: [pjlib_inc, pjlib_util_inc, pjmedia_inc],
    )

# pjmedia-test

# -Wall -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1   -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1        -I/home/vsedyshev/Work/1111/pjproject/third_party/build/speex -I/home/vsedyshev/Work/1111/pjproject/third_party/speex/include -DPJMEDIA_HAS_OPENCORE_AMRNB_CODEC=0 -DPJMEDIA_HAS_OPENCORE_AMRWB_CODEC=0 -I/home/vsedyshev/Work/1111/pjproject/third_party/build/srtp -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/crypto/include -I/home/vsedyshev/Work/1111/pjproject/third_party/srtp/include -DPJMEDIA_RESAMPLE_IMP=PJMEDIA_RESAMPLE_LIBRESAMPLE -DPJMEDIA_HAS_LIBYUV=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/yuv/include -DPJMEDIA_HAS_WEBRTC_AEC=1 -I/home/vsedyshev/Work/1111/pjproject/third_party/webrtc/src -DPJMEDIA_AUDIO_DEV_HAS_ALSA=1 -DPJMEDIA_AUDIO_DEV_HAS_PORTAUDIO=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -DPJMEDIA_AUDIO_DEV_HAS_WMME=0 -I../include -I../../pjlib/include -I../../pjlib-util/include -I../../pjmedia/include -I../../pjnath/include -I../.. \

#pjmedia_test_sources = [
# 	../src/test/codec_vectors.c 
# 	../src/test/jbuf_test.c 
# 	../src/test/main.c 
# 	../src/test/mips_test.c 
# 	../src/test/vid_codec_test.c 
# 	../src/test/vid_dev_test.c 
# 	../src/test/vid_port_test.c 
# 	../src/test/rtp_test.c 
# 	../src/test/test.c 
# 	../src/test/sdp_neg_test.c 
#]

# -lpjmedia-codec
# -lpjmedia-videodev
# -lpjmedia-audiodev
# -lpjmedia
# -lpjnath
# -lpjlib-util
# -lpj
# -lsrtp
# -lresample
# -lgsmcodec
# -lspeex
# -lilbccodec
# -lg7221codec
# -lyuv
# -lwebrtc
# -lssl
# -lcrypto
# -luuid
# -lm
# -lrt
# -lpthread
# -lasound
# -lSDL2

#pjmedia_test = executable('pjmedia-test', pjmedia_test_sources
#    )

#test('Check pjmedia', pjmedia_test, ...

# pjsip

pjsip_sources = [
    'pjsip/src/pjsip/sip_config.c',
    'pjsip/src/pjsip/sip_multipart.c',
    'pjsip/src/pjsip/sip_errno.c',
    'pjsip/src/pjsip/sip_msg.c',
    'pjsip/src/pjsip/sip_parser.c',
    'pjsip/src/pjsip/sip_tel_uri.c',
    'pjsip/src/pjsip/sip_uri.c',
    'pjsip/src/pjsip/sip_endpoint.c',
    'pjsip/src/pjsip/sip_util.c',
    'pjsip/src/pjsip/sip_util_proxy.c',
    'pjsip/src/pjsip/sip_resolve.c',
    'pjsip/src/pjsip/sip_transport.c',
    'pjsip/src/pjsip/sip_transport_loop.c',
    'pjsip/src/pjsip/sip_transport_udp.c',
    'pjsip/src/pjsip/sip_transport_tcp.c',
    'pjsip/src/pjsip/sip_transport_tls.c',
    'pjsip/src/pjsip/sip_auth_aka.c',
    'pjsip/src/pjsip/sip_auth_client.c',
    'pjsip/src/pjsip/sip_auth_msg.c',
    'pjsip/src/pjsip/sip_auth_parser.c',
    'pjsip/src/pjsip/sip_auth_server.c',
    'pjsip/src/pjsip/sip_transaction.c',
    'pjsip/src/pjsip/sip_util_statefull.c',
    'pjsip/src/pjsip/sip_dialog.c',
    'pjsip/src/pjsip/sip_ua_layer.c',
]

pjsip = static_library('pjsip', pjsip_sources,
        include_directories: [pjlib_inc, pjlib_util_inc, pjsip_inc],
        c_args: [
            '-Wall', '-DPJ_LINUX=1', '-O2', '-DPJ_IS_BIG_ENDIAN=0', '-DPJ_IS_LITTLE_ENDIAN=1',
        ],
    )
pjsip_dep = declare_dependency(
        link_with: pjsip,
        include_directories: [pjlib_inc, pjlib_util_inc, pjsip_inc],
    )

# pjsip-simple

pjsip_simple_sources = [
    'pjsip/src/pjsip-simple/errno.c',
    'pjsip/src/pjsip-simple/evsub.c',
    'pjsip/src/pjsip-simple/evsub_msg.c',
    'pjsip/src/pjsip-simple/iscomposing.c',
    'pjsip/src/pjsip-simple/mwi.c',
    'pjsip/src/pjsip-simple/pidf.c',
    'pjsip/src/pjsip-simple/presence.c',
    'pjsip/src/pjsip-simple/presence_body.c',
    'pjsip/src/pjsip-simple/publishc.c',
    'pjsip/src/pjsip-simple/rpid.c',
    'pjsip/src/pjsip-simple/xpidf.c',
]

pjsip_simple = static_library('pjsip-simple', pjsip_simple_sources,
        include_directories: [pjlib_inc, pjlib_util_inc, pjsip_inc],
        c_args: [
            '-Wall', '-DPJ_LINUX=1', '-O2', '-DPJ_IS_BIG_ENDIAN=0', '-DPJ_IS_LITTLE_ENDIAN=1',
        ]
    )
pjsip_simple_dep = declare_dependency(
        link_with: pjsip_simple,
        include_directories: [pjlib_inc, pjlib_util_inc, pjsip_inc],
    )

# pjsip-ua

pjsip_ua_sources = [
    'pjsip/src/pjsip-ua/sip_inv.c',
    'pjsip/src/pjsip-ua/sip_reg.c',
    'pjsip/src/pjsip-ua/sip_replaces.c',
    'pjsip/src/pjsip-ua/sip_xfer.c',
    'pjsip/src/pjsip-ua/sip_100rel.c',
    'pjsip/src/pjsip-ua/sip_timer.c',
]

pjsip_ua = static_library('pjsip-ua', pjsip_ua_sources,
        include_directories: [pjlib_inc, pjlib_util_inc, pjsip_inc, pjmedia_inc],
        c_args: [
            '-Wall', '-DPJ_LINUX=1', '-O2', '-DPJ_IS_BIG_ENDIAN=0', '-DPJ_IS_LITTLE_ENDIAN=1'
        ],
    )
pjsip_ua_dep = declare_dependency(
        link_with: pjsip_ua,
        include_directories: [pjlib_inc, pjlib_util_inc, pjsip_inc, pjmedia_inc],
    )

# pjsua-lib

pjsua_lib_sources = [
    'pjsip/src/pjsua-lib/pjsua_acc.c',
    'pjsip/src/pjsua-lib/pjsua_call.c',
    'pjsip/src/pjsua-lib/pjsua_core.c',
    'pjsip/src/pjsua-lib/pjsua_im.c',
    'pjsip/src/pjsua-lib/pjsua_media.c',
    'pjsip/src/pjsua-lib/pjsua_pres.c',
    'pjsip/src/pjsua-lib/pjsua_dump.c',
    'pjsip/src/pjsua-lib/pjsua_aud.c',
    'pjsip/src/pjsua-lib/pjsua_vid.c',
]

pjsua = static_library('pjsua', pjsua_lib_sources,
        include_directories: [pjlib_inc, pjlib_util_inc, pjsip_inc, pjmedia_inc, pjnath_inc],
        c_args: [
            '-Wall', '-DPJ_LINUX=1', '-O2', '-DPJ_IS_BIG_ENDIAN=0', '-DPJ_IS_LITTLE_ENDIAN=1', '-DPJMEDIA_VIDEO_DEV_HAS_SDL=1',
            '-D_REENTRANT', '-DPJMEDIA_USE_OLD_FFMPEG=1',
        ]
    )
pjsua_dep = declare_dependency(
        link_with: pjsua,
        include_directories: [pjlib_inc, pjlib_util_inc, pjsip_inc, pjmedia_inc, pjnath_inc],
    )

# pjsua2-lib

pjsua2_lib_sources = [
    'pjsip/src/pjsua2/account.cpp',
    'pjsip/src/pjsua2/endpoint.cpp',
    'pjsip/src/pjsua2/json.cpp',
    'pjsip/src/pjsua2/persistent.cpp',
    'pjsip/src/pjsua2/types.cpp',
    'pjsip/src/pjsua2/siptypes.cpp',
    'pjsip/src/pjsua2/call.cpp',
    'pjsip/src/pjsua2/presence.cpp',
    'pjsip/src/pjsua2/media.cpp',
]

pjsua2 = static_library('pjsua2', pjsua2_lib_sources,
        include_directories: [pjlib_inc, pjlib_util_inc, pjsip_inc, pjmedia_inc, pjnath_inc],
        cpp_args: [
            '-DPJ_LINUX=1', '-g', '-O2', '-Wall', '-DPJ_IS_BIG_ENDIAN=0', '-DPJ_IS_LITTLE_ENDIAN=1',
            '-DPJMEDIA_VIDEO_DEV_HAS_SDL=1', '-D_REENTRANT', '-DPJMEDIA_USE_OLD_FFMPEG=1',
        ],
    )
pjsua2_dep = declare_dependency(
        link_with: pjsua2,
        include_directories: [pjlib_inc, pjlib_util_inc, pjsip_inc, pjmedia_inc, pjnath_inc],
    )

# pjsip-test

pjsip_test_sources = [
    'pjsip/src/test/main.c',
    'pjsip/src/test/dlg_core_test.c',
    'pjsip/src/test/dns_test.c',
    'pjsip/src/test/msg_err_test.c',
    'pjsip/src/test/msg_logger.c',
    'pjsip/src/test/msg_test.c',
    'pjsip/src/test/multipart_test.c',
    'pjsip/src/test/regc_test.c',
    'pjsip/src/test/test.c',
    'pjsip/src/test/transport_loop_test.c',
    'pjsip/src/test/transport_tcp_test.c',
    'pjsip/src/test/transport_test.c',
    'pjsip/src/test/transport_udp_test.c',
    'pjsip/src/test/tsx_basic_test.c',
    'pjsip/src/test/tsx_bench.c',
    'pjsip/src/test/tsx_uac_test.c',
    'pjsip/src/test/tsx_uas_test.c',
    'pjsip/src/test/txdata_test.c',
    'pjsip/src/test/uri_test.c',
    'pjsip/src/test/inv_offer_answer_test.c',
]

pjsip_test_dependencies = []
pjsip_test_dependencies += pjsip_dep # -lpjsip
pjsip_test_dependencies += pjsip_ua_dep # -lpjsip-ua
pjsip_test_dependencies += pjsip_simple_dep # -lpjsip-simple
# -lpjmedia-codec
# -lpjmedia-videodev
# -lpjmedia
# -lpjmedia-audiodev
pjsip_test_dependencies += pjlib_util_dep # -lpjlib-util
# -lpjnath
pjsip_test_dependencies += pjlib_dep # -lpj
# -lsrtp
# -lresample
# -lgsmcodec
# -lspeex
# -lilbccodec
# -lg7221codec
# -lyuv
# -lwebrtc
pjsip_test_dependencies += openssl_dep # -lssl
# -lcrypto
pjsip_test_dependencies += uuid_dep # -luuid
pjsip_test_dependencies += m_dep # -lm
pjsip_test_dependencies += rt_dep # -lrt
pjsip_test_dependencies += pthread_dep # -lpthread
# -lasound
# -lSDL2

pjsip_test_dependencies += pjsdp_dep

pjsip_test = executable('pjsip-test', pjsip_test_sources,
        dependencies: pjsip_test_dependencies,
        c_args: [
            '-Wall', '-DPJ_LINUX=1', '-O2', '-DPJ_IS_BIG_ENDIAN=0', '-DPJ_IS_LITTLE_ENDIAN=1',
        ]
    )
test('Check pjsip', pjsip_test, timeout: 360, protocol: 'exitcode', is_parallel: false)

# pjsua2-test

pjsua2_test_sources = [
    'pjsip/src/pjsua2-test/main.cpp',
]

pjsua2_test_dependencies = []

pjsua2_test_dependencies += pjsua2_dep # -lpjsua2
# -lstdc++
pjsua2_test_dependencies += pjsua_dep # -lpjsua
pjsua2_test_dependencies += pjsip_ua_dep # -lpjsip-ua
pjsua2_test_dependencies += pjsip_simple_dep # -lpjsip-simple
pjsua2_test_dependencies += pjsip_dep # -lpjsip
# -lpjmedia-codec
# -lpjmedia
# -lpjmedia-videodev
# -lpjmedia-audiodev
# -lpjmedia
# -lpjnath
pjsua2_test_dependencies += pjlib_util_dep # -lpjlib-util
# -lsrtp
# -lresample
# -lgsmcodec
# -lspeex
# -lilbccodec
# -lg7221codec
# -lyuv
# -lwebrtc
pjsua2_test_dependencies += pjlib_dep # -lpj
pjsua2_test_dependencies += openssl_dep # -lssl -lcrypto
pjsua2_test_dependencies += uuid_dep # -luuid
pjsua2_test_dependencies += m_dep # -lm
pjsua2_test_dependencies += rt_dep # -lrt
pjsua2_test_dependencies += pthread_dep # -lpthread
# -lasound
# -lSDL2

#executable('pjsua2-test', pjsua2_test_sources,
#        dependencies: pjsua2_test_dependencies,
#        cpp_args: [
#            '-DPJ_LINUX=1', '-g', '-O2', '-Wall', '-DPJ_IS_BIG_ENDIAN=0', '-DPJ_IS_LITTLE_ENDIAN=1',
#            '-DPJMEDIA_VIDEO_DEV_HAS_SDL=1', '-D_REENTRANT', '-DPJMEDIA_USE_OLD_FFMPEG=1',
#        ],
#    )

# pjsua (i.e. pjsua app)

#pjsua_sources = [
# 	../src/pjsua/main.c 
# 	../src/pjsua/pjsua_app.c 
# 	../src/pjsua/pjsua_app_cli.c 
# 	../src/pjsua/pjsua_app_common.c 
# 	../src/pjsua/pjsua_app_config.c 
# 	../src/pjsua/pjsua_app_legacy.c 
#]

# -lpjsua
# -lpjsip-ua
# -lpjsip-simple
# -lpjsip
# -lpjmedia-codec
# -lpjmedia
# -lpjmedia-videodev
# -lpjmedia-audiodev
# -lpjmedia
# -lpjnath
# -lpjlib-util
# -lsrtp
# -lresample
# -lgsmcodec
# -lspeex
# -lilbccodec
# -lg7221codec
# -lyuv
# -lwebrtc
# -lpj
# -lssl
# -lcrypto
# -luuid
# -lm
# -lrt
# -lpthread
# -lasound
# -lSDL2

#pjsua = executable('pjsua', pjsua_sources,
#        c_args: [
#            '-DPJ_LINUX=1', '-O2', '-DPJ_IS_BIG_ENDIAN=0', '-DPJ_IS_LITTLE_ENDIAN=1', '-DPJMEDIA_VIDEO_DEV_HAS_SDL=1',
#            '-D_REENTRANT', '-DPJMEDIA_USE_OLD_FFMPEG=1', '-DPJMEDIA_VIDEO_DEV_HAS_SDL=1',
#        ],
#    )

# pjsystest

pjsystest_sources = [
# 	../src/pjsystest/systest.c 
# 	../src/pjsystest/main_console.c 
]

# -lpjsua
# -lpjsip-ua
# -lpjsip-simple
# -lpjsip
# -lpjmedia-codec
# -lpjmedia
# -lpjmedia-videodev
# -lpjmedia-audiodev
# -lpjmedia
# -lpjnath
# -lpjlib-util
# -lsrtp
# -lresample
# -lgsmcodec
# -lspeex
# -lilbccodec
# -lg7221codec
# -lyuv
# -lwebrtc
# -lpj
# -lssl -lcrypto
# -luuid
# -lm
# -lrt
# -lpthread
# -lasound
# -lSDL2

#pjsystest = executable('pjsystest', pjsystest_sources,
#        c_args: [
#            '-DPJ_LINUX=1', '-O2', '-DPJ_IS_BIG_ENDIAN=0', '-DPJ_IS_LITTLE_ENDIAN=1', '-DPJMEDIA_VIDEO_DEV_HAS_SDL=1',
#            '-D_REENTRANT', '-DPJMEDIA_USE_OLD_FFMPEG=1',
#        }
#    )

# samples

samples_dependencies = []

# -lpjsua
samples_dependencies += pjsip_ua_dep # -lpjsip-ua
samples_dependencies += pjsip_simple_dep # -lpjsip-simple
samples_dependencies += pjsip_dep # -lpjsip
# -lpjmedia-codec
# -lpjmedia
# -lpjmedia-videodev
# -lpjmedia-audiodev
# -lpjmedia
samples_dependencies += pjnath_dep # -lpjnath
samples_dependencies += pjlib_util_dep # -lpjlib-util
# -lsrtp
# -lresample
# -lgsmcodec
# -lspeex
# -lilbccodec
# -lg7221codec
# -lyuv
# -lwebrtc
samples_dependencies += pjlib_dep # -lpj
samples_dependencies += openssl_dep # -lssl -lcrypto
samples_dependencies += uuid_dep # -luuid
samples_dependencies += m_dep # -lm
samples_dependencies += rt_dep # -lrt
samples_dependencies += pthread_dep # -lpthread
# -lasound
# -lSDL2

#executable('auddemo', 'pjsip-apps/src/samples/auddemo.c',
#        dependencies: samples_dependencies,
#        c_args: [
#            '-DPJ_LINUX=1', '-O2', '-DPJ_IS_BIG_ENDIAN=0', '-DPJ_IS_LITTLE_ENDIAN=1', '-DPJMEDIA_VIDEO_DEV_HAS_SDL=1',
#            '-D_REENTRANT', '-DPJMEDIA_USE_OLD_FFMPEG=1',
#        ],
#    )

executable('aviplay', 'pjsip-apps/src/samples/aviplay.c',
        dependencies: samples_dependencies,
        c_args: [
            '-DPJ_LINUX=1', '-O2', '-DPJ_IS_BIG_ENDIAN=0', '-DPJ_IS_LITTLE_ENDIAN=1', '-DPJMEDIA_VIDEO_DEV_HAS_SDL=1',
            '-D_REENTRANT', '-DPJMEDIA_USE_OLD_FFMPEG=1',
        ],
    )

#executable('aectest', 'pjsip-apps/src/samples/aectest.c',
#        dependencies: samples_dependencies,
#        c_args: [
#            '-DPJ_LINUX=1', '-O2', '-DPJ_IS_BIG_ENDIAN=0', '-DPJ_IS_LITTLE_ENDIAN=1', '-DPJMEDIA_VIDEO_DEV_HAS_SDL=1',
#            '-D_REENTRANT', '-DPJMEDIA_USE_OLD_FFMPEG=1',
#        ],
#    )

executable('clidemo', 'pjsip-apps/src/samples/clidemo.c',
        dependencies: samples_dependencies,
        c_args: [
            '-DPJ_LINUX=1', '-O2', '-DPJ_IS_BIG_ENDIAN=0', '-DPJ_IS_LITTLE_ENDIAN=1', '-DPJMEDIA_VIDEO_DEV_HAS_SDL=1',
            '-D_REENTRANT', '-DPJMEDIA_USE_OLD_FFMPEG=1',
        ],
    )

# gcc -c -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1 -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -I/home/vsedyshev/Work/1111/pjproject/pjlib/include -I/home/vsedyshev/Work/1111/pjproject/pjlib-util/include -I/home/vsedyshev/Work/1111/pjproject/pjnath/include -I/home/vsedyshev/Work/1111/pjproject/pjmedia/include -I/home/vsedyshev/Work/1111/pjproject/pjsip/include  \
# 	-o output/sample-x86_64-unknown-linux-gnu/confsample.o \
# 	../src/samples/confsample.c 
# gcc -o ../bin/samples/x86_64-unknown-linux-gnu/confsample \
#      output/sample-x86_64-unknown-linux-gnu/confsample.o -L/home/vsedyshev/Work/1111/pjproject/pjlib/lib -L/home/vsedyshev/Work/1111/pjproject/pjlib-util/lib -L/home/vsedyshev/Work/1111/pjproject/pjnath/lib -L/home/vsedyshev/Work/1111/pjproject/pjmedia/lib -L/home/vsedyshev/Work/1111/pjproject/pjsip/lib -L/home/vsedyshev/Work/1111/pjproject/third_party/lib -lSDL2     -lSDL2      -lpjsua-x86_64-unknown-linux-gnu -lpjsip-ua-x86_64-unknown-linux-gnu -lpjsip-simple-x86_64-unknown-linux-gnu -lpjsip-x86_64-unknown-linux-gnu -lpjmedia-codec-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjmedia-videodev-x86_64-unknown-linux-gnu -lpjmedia-audiodev-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjnath-x86_64-unknown-linux-gnu -lpjlib-util-x86_64-unknown-linux-gnu  -lsrtp-x86_64-unknown-linux-gnu -lresample-x86_64-unknown-linux-gnu -lgsmcodec-x86_64-unknown-linux-gnu -lspeex-x86_64-unknown-linux-gnu -lilbccodec-x86_64-unknown-linux-gnu -lg7221codec-x86_64-unknown-linux-gnu -lyuv-x86_64-unknown-linux-gnu -lwebrtc-x86_64-unknown-linux-gnu  -lpj-x86_64-unknown-linux-gnu -lssl -lcrypto -luuid -lm -lrt -lpthread  -lasound -lSDL2   

# gcc -c -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1 -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -I/home/vsedyshev/Work/1111/pjproject/pjlib/include -I/home/vsedyshev/Work/1111/pjproject/pjlib-util/include -I/home/vsedyshev/Work/1111/pjproject/pjnath/include -I/home/vsedyshev/Work/1111/pjproject/pjmedia/include -I/home/vsedyshev/Work/1111/pjproject/pjsip/include  \
# 	-o output/sample-x86_64-unknown-linux-gnu/encdec.o \
# 	../src/samples/encdec.c 
# gcc -o ../bin/samples/x86_64-unknown-linux-gnu/encdec \
#      output/sample-x86_64-unknown-linux-gnu/encdec.o -L/home/vsedyshev/Work/1111/pjproject/pjlib/lib -L/home/vsedyshev/Work/1111/pjproject/pjlib-util/lib -L/home/vsedyshev/Work/1111/pjproject/pjnath/lib -L/home/vsedyshev/Work/1111/pjproject/pjmedia/lib -L/home/vsedyshev/Work/1111/pjproject/pjsip/lib -L/home/vsedyshev/Work/1111/pjproject/third_party/lib -lSDL2     -lSDL2      -lpjsua-x86_64-unknown-linux-gnu -lpjsip-ua-x86_64-unknown-linux-gnu -lpjsip-simple-x86_64-unknown-linux-gnu -lpjsip-x86_64-unknown-linux-gnu -lpjmedia-codec-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjmedia-videodev-x86_64-unknown-linux-gnu -lpjmedia-audiodev-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjnath-x86_64-unknown-linux-gnu -lpjlib-util-x86_64-unknown-linux-gnu  -lsrtp-x86_64-unknown-linux-gnu -lresample-x86_64-unknown-linux-gnu -lgsmcodec-x86_64-unknown-linux-gnu -lspeex-x86_64-unknown-linux-gnu -lilbccodec-x86_64-unknown-linux-gnu -lg7221codec-x86_64-unknown-linux-gnu -lyuv-x86_64-unknown-linux-gnu -lwebrtc-x86_64-unknown-linux-gnu  -lpj-x86_64-unknown-linux-gnu -lssl -lcrypto -luuid -lm -lrt -lpthread  -lasound -lSDL2   

# gcc -c -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1 -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -I/home/vsedyshev/Work/1111/pjproject/pjlib/include -I/home/vsedyshev/Work/1111/pjproject/pjlib-util/include -I/home/vsedyshev/Work/1111/pjproject/pjnath/include -I/home/vsedyshev/Work/1111/pjproject/pjmedia/include -I/home/vsedyshev/Work/1111/pjproject/pjsip/include  \
# 	-o output/sample-x86_64-unknown-linux-gnu/httpdemo.o \
# 	../src/samples/httpdemo.c 
# gcc -o ../bin/samples/x86_64-unknown-linux-gnu/httpdemo \
#      output/sample-x86_64-unknown-linux-gnu/httpdemo.o -L/home/vsedyshev/Work/1111/pjproject/pjlib/lib -L/home/vsedyshev/Work/1111/pjproject/pjlib-util/lib -L/home/vsedyshev/Work/1111/pjproject/pjnath/lib -L/home/vsedyshev/Work/1111/pjproject/pjmedia/lib -L/home/vsedyshev/Work/1111/pjproject/pjsip/lib -L/home/vsedyshev/Work/1111/pjproject/third_party/lib -lSDL2     -lSDL2      -lpjsua-x86_64-unknown-linux-gnu -lpjsip-ua-x86_64-unknown-linux-gnu -lpjsip-simple-x86_64-unknown-linux-gnu -lpjsip-x86_64-unknown-linux-gnu -lpjmedia-codec-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjmedia-videodev-x86_64-unknown-linux-gnu -lpjmedia-audiodev-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjnath-x86_64-unknown-linux-gnu -lpjlib-util-x86_64-unknown-linux-gnu  -lsrtp-x86_64-unknown-linux-gnu -lresample-x86_64-unknown-linux-gnu -lgsmcodec-x86_64-unknown-linux-gnu -lspeex-x86_64-unknown-linux-gnu -lilbccodec-x86_64-unknown-linux-gnu -lg7221codec-x86_64-unknown-linux-gnu -lyuv-x86_64-unknown-linux-gnu -lwebrtc-x86_64-unknown-linux-gnu  -lpj-x86_64-unknown-linux-gnu -lssl -lcrypto -luuid -lm -lrt -lpthread  -lasound -lSDL2   

# gcc -c -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1 -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -I/home/vsedyshev/Work/1111/pjproject/pjlib/include -I/home/vsedyshev/Work/1111/pjproject/pjlib-util/include -I/home/vsedyshev/Work/1111/pjproject/pjnath/include -I/home/vsedyshev/Work/1111/pjproject/pjmedia/include -I/home/vsedyshev/Work/1111/pjproject/pjsip/include  \
# 	-o output/sample-x86_64-unknown-linux-gnu/icedemo.o \
# 	../src/samples/icedemo.c 
# gcc -o ../bin/samples/x86_64-unknown-linux-gnu/icedemo \
#      output/sample-x86_64-unknown-linux-gnu/icedemo.o -L/home/vsedyshev/Work/1111/pjproject/pjlib/lib -L/home/vsedyshev/Work/1111/pjproject/pjlib-util/lib -L/home/vsedyshev/Work/1111/pjproject/pjnath/lib -L/home/vsedyshev/Work/1111/pjproject/pjmedia/lib -L/home/vsedyshev/Work/1111/pjproject/pjsip/lib -L/home/vsedyshev/Work/1111/pjproject/third_party/lib -lSDL2     -lSDL2      -lpjsua-x86_64-unknown-linux-gnu -lpjsip-ua-x86_64-unknown-linux-gnu -lpjsip-simple-x86_64-unknown-linux-gnu -lpjsip-x86_64-unknown-linux-gnu -lpjmedia-codec-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjmedia-videodev-x86_64-unknown-linux-gnu -lpjmedia-audiodev-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjnath-x86_64-unknown-linux-gnu -lpjlib-util-x86_64-unknown-linux-gnu  -lsrtp-x86_64-unknown-linux-gnu -lresample-x86_64-unknown-linux-gnu -lgsmcodec-x86_64-unknown-linux-gnu -lspeex-x86_64-unknown-linux-gnu -lilbccodec-x86_64-unknown-linux-gnu -lg7221codec-x86_64-unknown-linux-gnu -lyuv-x86_64-unknown-linux-gnu -lwebrtc-x86_64-unknown-linux-gnu  -lpj-x86_64-unknown-linux-gnu -lssl -lcrypto -luuid -lm -lrt -lpthread  -lasound -lSDL2   

# gcc -c -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1 -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -I/home/vsedyshev/Work/1111/pjproject/pjlib/include -I/home/vsedyshev/Work/1111/pjproject/pjlib-util/include -I/home/vsedyshev/Work/1111/pjproject/pjnath/include -I/home/vsedyshev/Work/1111/pjproject/pjmedia/include -I/home/vsedyshev/Work/1111/pjproject/pjsip/include  \
# 	-o output/sample-x86_64-unknown-linux-gnu/jbsim.o \
# 	../src/samples/jbsim.c 
# gcc -o ../bin/samples/x86_64-unknown-linux-gnu/jbsim \
#      output/sample-x86_64-unknown-linux-gnu/jbsim.o -L/home/vsedyshev/Work/1111/pjproject/pjlib/lib -L/home/vsedyshev/Work/1111/pjproject/pjlib-util/lib -L/home/vsedyshev/Work/1111/pjproject/pjnath/lib -L/home/vsedyshev/Work/1111/pjproject/pjmedia/lib -L/home/vsedyshev/Work/1111/pjproject/pjsip/lib -L/home/vsedyshev/Work/1111/pjproject/third_party/lib -lSDL2     -lSDL2      -lpjsua-x86_64-unknown-linux-gnu -lpjsip-ua-x86_64-unknown-linux-gnu -lpjsip-simple-x86_64-unknown-linux-gnu -lpjsip-x86_64-unknown-linux-gnu -lpjmedia-codec-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjmedia-videodev-x86_64-unknown-linux-gnu -lpjmedia-audiodev-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjnath-x86_64-unknown-linux-gnu -lpjlib-util-x86_64-unknown-linux-gnu  -lsrtp-x86_64-unknown-linux-gnu -lresample-x86_64-unknown-linux-gnu -lgsmcodec-x86_64-unknown-linux-gnu -lspeex-x86_64-unknown-linux-gnu -lilbccodec-x86_64-unknown-linux-gnu -lg7221codec-x86_64-unknown-linux-gnu -lyuv-x86_64-unknown-linux-gnu -lwebrtc-x86_64-unknown-linux-gnu  -lpj-x86_64-unknown-linux-gnu -lssl -lcrypto -luuid -lm -lrt -lpthread  -lasound -lSDL2   

# gcc -c -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1 -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -I/home/vsedyshev/Work/1111/pjproject/pjlib/include -I/home/vsedyshev/Work/1111/pjproject/pjlib-util/include -I/home/vsedyshev/Work/1111/pjproject/pjnath/include -I/home/vsedyshev/Work/1111/pjproject/pjmedia/include -I/home/vsedyshev/Work/1111/pjproject/pjsip/include  \
# 	-o output/sample-x86_64-unknown-linux-gnu/latency.o \
# 	../src/samples/latency.c 
# gcc -o ../bin/samples/x86_64-unknown-linux-gnu/latency \
#      output/sample-x86_64-unknown-linux-gnu/latency.o -L/home/vsedyshev/Work/1111/pjproject/pjlib/lib -L/home/vsedyshev/Work/1111/pjproject/pjlib-util/lib -L/home/vsedyshev/Work/1111/pjproject/pjnath/lib -L/home/vsedyshev/Work/1111/pjproject/pjmedia/lib -L/home/vsedyshev/Work/1111/pjproject/pjsip/lib -L/home/vsedyshev/Work/1111/pjproject/third_party/lib -lSDL2     -lSDL2      -lpjsua-x86_64-unknown-linux-gnu -lpjsip-ua-x86_64-unknown-linux-gnu -lpjsip-simple-x86_64-unknown-linux-gnu -lpjsip-x86_64-unknown-linux-gnu -lpjmedia-codec-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjmedia-videodev-x86_64-unknown-linux-gnu -lpjmedia-audiodev-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjnath-x86_64-unknown-linux-gnu -lpjlib-util-x86_64-unknown-linux-gnu  -lsrtp-x86_64-unknown-linux-gnu -lresample-x86_64-unknown-linux-gnu -lgsmcodec-x86_64-unknown-linux-gnu -lspeex-x86_64-unknown-linux-gnu -lilbccodec-x86_64-unknown-linux-gnu -lg7221codec-x86_64-unknown-linux-gnu -lyuv-x86_64-unknown-linux-gnu -lwebrtc-x86_64-unknown-linux-gnu  -lpj-x86_64-unknown-linux-gnu -lssl -lcrypto -luuid -lm -lrt -lpthread  -lasound -lSDL2   

# gcc -c -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1 -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -I/home/vsedyshev/Work/1111/pjproject/pjlib/include -I/home/vsedyshev/Work/1111/pjproject/pjlib-util/include -I/home/vsedyshev/Work/1111/pjproject/pjnath/include -I/home/vsedyshev/Work/1111/pjproject/pjmedia/include -I/home/vsedyshev/Work/1111/pjproject/pjsip/include  \
# 	-o output/sample-x86_64-unknown-linux-gnu/level.o \
# 	../src/samples/level.c 
# gcc -o ../bin/samples/x86_64-unknown-linux-gnu/level \
#      output/sample-x86_64-unknown-linux-gnu/level.o -L/home/vsedyshev/Work/1111/pjproject/pjlib/lib -L/home/vsedyshev/Work/1111/pjproject/pjlib-util/lib -L/home/vsedyshev/Work/1111/pjproject/pjnath/lib -L/home/vsedyshev/Work/1111/pjproject/pjmedia/lib -L/home/vsedyshev/Work/1111/pjproject/pjsip/lib -L/home/vsedyshev/Work/1111/pjproject/third_party/lib -lSDL2     -lSDL2      -lpjsua-x86_64-unknown-linux-gnu -lpjsip-ua-x86_64-unknown-linux-gnu -lpjsip-simple-x86_64-unknown-linux-gnu -lpjsip-x86_64-unknown-linux-gnu -lpjmedia-codec-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjmedia-videodev-x86_64-unknown-linux-gnu -lpjmedia-audiodev-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjnath-x86_64-unknown-linux-gnu -lpjlib-util-x86_64-unknown-linux-gnu  -lsrtp-x86_64-unknown-linux-gnu -lresample-x86_64-unknown-linux-gnu -lgsmcodec-x86_64-unknown-linux-gnu -lspeex-x86_64-unknown-linux-gnu -lilbccodec-x86_64-unknown-linux-gnu -lg7221codec-x86_64-unknown-linux-gnu -lyuv-x86_64-unknown-linux-gnu -lwebrtc-x86_64-unknown-linux-gnu  -lpj-x86_64-unknown-linux-gnu -lssl -lcrypto -luuid -lm -lrt -lpthread  -lasound -lSDL2   

# gcc -c -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1 -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -I/home/vsedyshev/Work/1111/pjproject/pjlib/include -I/home/vsedyshev/Work/1111/pjproject/pjlib-util/include -I/home/vsedyshev/Work/1111/pjproject/pjnath/include -I/home/vsedyshev/Work/1111/pjproject/pjmedia/include -I/home/vsedyshev/Work/1111/pjproject/pjsip/include  \
# 	-o output/sample-x86_64-unknown-linux-gnu/mix.o \
# 	../src/samples/mix.c 
# gcc -o ../bin/samples/x86_64-unknown-linux-gnu/mix \
#      output/sample-x86_64-unknown-linux-gnu/mix.o -L/home/vsedyshev/Work/1111/pjproject/pjlib/lib -L/home/vsedyshev/Work/1111/pjproject/pjlib-util/lib -L/home/vsedyshev/Work/1111/pjproject/pjnath/lib -L/home/vsedyshev/Work/1111/pjproject/pjmedia/lib -L/home/vsedyshev/Work/1111/pjproject/pjsip/lib -L/home/vsedyshev/Work/1111/pjproject/third_party/lib -lSDL2     -lSDL2      -lpjsua-x86_64-unknown-linux-gnu -lpjsip-ua-x86_64-unknown-linux-gnu -lpjsip-simple-x86_64-unknown-linux-gnu -lpjsip-x86_64-unknown-linux-gnu -lpjmedia-codec-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjmedia-videodev-x86_64-unknown-linux-gnu -lpjmedia-audiodev-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjnath-x86_64-unknown-linux-gnu -lpjlib-util-x86_64-unknown-linux-gnu  -lsrtp-x86_64-unknown-linux-gnu -lresample-x86_64-unknown-linux-gnu -lgsmcodec-x86_64-unknown-linux-gnu -lspeex-x86_64-unknown-linux-gnu -lilbccodec-x86_64-unknown-linux-gnu -lg7221codec-x86_64-unknown-linux-gnu -lyuv-x86_64-unknown-linux-gnu -lwebrtc-x86_64-unknown-linux-gnu  -lpj-x86_64-unknown-linux-gnu -lssl -lcrypto -luuid -lm -lrt -lpthread  -lasound -lSDL2   

# gcc -c -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1 -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -I/home/vsedyshev/Work/1111/pjproject/pjlib/include -I/home/vsedyshev/Work/1111/pjproject/pjlib-util/include -I/home/vsedyshev/Work/1111/pjproject/pjnath/include -I/home/vsedyshev/Work/1111/pjproject/pjmedia/include -I/home/vsedyshev/Work/1111/pjproject/pjsip/include  \
# 	-o output/sample-x86_64-unknown-linux-gnu/pjsip-perf.o \
# 	../src/samples/pjsip-perf.c 
# gcc -o ../bin/samples/x86_64-unknown-linux-gnu/pjsip-perf \
#      output/sample-x86_64-unknown-linux-gnu/pjsip-perf.o -L/home/vsedyshev/Work/1111/pjproject/pjlib/lib -L/home/vsedyshev/Work/1111/pjproject/pjlib-util/lib -L/home/vsedyshev/Work/1111/pjproject/pjnath/lib -L/home/vsedyshev/Work/1111/pjproject/pjmedia/lib -L/home/vsedyshev/Work/1111/pjproject/pjsip/lib -L/home/vsedyshev/Work/1111/pjproject/third_party/lib -lSDL2     -lSDL2      -lpjsua-x86_64-unknown-linux-gnu -lpjsip-ua-x86_64-unknown-linux-gnu -lpjsip-simple-x86_64-unknown-linux-gnu -lpjsip-x86_64-unknown-linux-gnu -lpjmedia-codec-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjmedia-videodev-x86_64-unknown-linux-gnu -lpjmedia-audiodev-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjnath-x86_64-unknown-linux-gnu -lpjlib-util-x86_64-unknown-linux-gnu  -lsrtp-x86_64-unknown-linux-gnu -lresample-x86_64-unknown-linux-gnu -lgsmcodec-x86_64-unknown-linux-gnu -lspeex-x86_64-unknown-linux-gnu -lilbccodec-x86_64-unknown-linux-gnu -lg7221codec-x86_64-unknown-linux-gnu -lyuv-x86_64-unknown-linux-gnu -lwebrtc-x86_64-unknown-linux-gnu  -lpj-x86_64-unknown-linux-gnu -lssl -lcrypto -luuid -lm -lrt -lpthread  -lasound -lSDL2   

# gcc -c -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1 -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -I/home/vsedyshev/Work/1111/pjproject/pjlib/include -I/home/vsedyshev/Work/1111/pjproject/pjlib-util/include -I/home/vsedyshev/Work/1111/pjproject/pjnath/include -I/home/vsedyshev/Work/1111/pjproject/pjmedia/include -I/home/vsedyshev/Work/1111/pjproject/pjsip/include  \
# 	-o output/sample-x86_64-unknown-linux-gnu/pcaputil.o \
# 	../src/samples/pcaputil.c 
# gcc -o ../bin/samples/x86_64-unknown-linux-gnu/pcaputil \
#      output/sample-x86_64-unknown-linux-gnu/pcaputil.o -L/home/vsedyshev/Work/1111/pjproject/pjlib/lib -L/home/vsedyshev/Work/1111/pjproject/pjlib-util/lib -L/home/vsedyshev/Work/1111/pjproject/pjnath/lib -L/home/vsedyshev/Work/1111/pjproject/pjmedia/lib -L/home/vsedyshev/Work/1111/pjproject/pjsip/lib -L/home/vsedyshev/Work/1111/pjproject/third_party/lib -lSDL2     -lSDL2      -lpjsua-x86_64-unknown-linux-gnu -lpjsip-ua-x86_64-unknown-linux-gnu -lpjsip-simple-x86_64-unknown-linux-gnu -lpjsip-x86_64-unknown-linux-gnu -lpjmedia-codec-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjmedia-videodev-x86_64-unknown-linux-gnu -lpjmedia-audiodev-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjnath-x86_64-unknown-linux-gnu -lpjlib-util-x86_64-unknown-linux-gnu  -lsrtp-x86_64-unknown-linux-gnu -lresample-x86_64-unknown-linux-gnu -lgsmcodec-x86_64-unknown-linux-gnu -lspeex-x86_64-unknown-linux-gnu -lilbccodec-x86_64-unknown-linux-gnu -lg7221codec-x86_64-unknown-linux-gnu -lyuv-x86_64-unknown-linux-gnu -lwebrtc-x86_64-unknown-linux-gnu  -lpj-x86_64-unknown-linux-gnu -lssl -lcrypto -luuid -lm -lrt -lpthread  -lasound -lSDL2   

# gcc -c -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1 -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -I/home/vsedyshev/Work/1111/pjproject/pjlib/include -I/home/vsedyshev/Work/1111/pjproject/pjlib-util/include -I/home/vsedyshev/Work/1111/pjproject/pjnath/include -I/home/vsedyshev/Work/1111/pjproject/pjmedia/include -I/home/vsedyshev/Work/1111/pjproject/pjsip/include  \
# 	-o output/sample-x86_64-unknown-linux-gnu/playfile.o \
# 	../src/samples/playfile.c 
# gcc -o ../bin/samples/x86_64-unknown-linux-gnu/playfile \
#      output/sample-x86_64-unknown-linux-gnu/playfile.o -L/home/vsedyshev/Work/1111/pjproject/pjlib/lib -L/home/vsedyshev/Work/1111/pjproject/pjlib-util/lib -L/home/vsedyshev/Work/1111/pjproject/pjnath/lib -L/home/vsedyshev/Work/1111/pjproject/pjmedia/lib -L/home/vsedyshev/Work/1111/pjproject/pjsip/lib -L/home/vsedyshev/Work/1111/pjproject/third_party/lib -lSDL2     -lSDL2      -lpjsua-x86_64-unknown-linux-gnu -lpjsip-ua-x86_64-unknown-linux-gnu -lpjsip-simple-x86_64-unknown-linux-gnu -lpjsip-x86_64-unknown-linux-gnu -lpjmedia-codec-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjmedia-videodev-x86_64-unknown-linux-gnu -lpjmedia-audiodev-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjnath-x86_64-unknown-linux-gnu -lpjlib-util-x86_64-unknown-linux-gnu  -lsrtp-x86_64-unknown-linux-gnu -lresample-x86_64-unknown-linux-gnu -lgsmcodec-x86_64-unknown-linux-gnu -lspeex-x86_64-unknown-linux-gnu -lilbccodec-x86_64-unknown-linux-gnu -lg7221codec-x86_64-unknown-linux-gnu -lyuv-x86_64-unknown-linux-gnu -lwebrtc-x86_64-unknown-linux-gnu  -lpj-x86_64-unknown-linux-gnu -lssl -lcrypto -luuid -lm -lrt -lpthread  -lasound -lSDL2   

# gcc -c -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1 -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -I/home/vsedyshev/Work/1111/pjproject/pjlib/include -I/home/vsedyshev/Work/1111/pjproject/pjlib-util/include -I/home/vsedyshev/Work/1111/pjproject/pjnath/include -I/home/vsedyshev/Work/1111/pjproject/pjmedia/include -I/home/vsedyshev/Work/1111/pjproject/pjsip/include  \
# 	-o output/sample-x86_64-unknown-linux-gnu/playsine.o \
# 	../src/samples/playsine.c 
# gcc -o ../bin/samples/x86_64-unknown-linux-gnu/playsine \
#      output/sample-x86_64-unknown-linux-gnu/playsine.o -L/home/vsedyshev/Work/1111/pjproject/pjlib/lib -L/home/vsedyshev/Work/1111/pjproject/pjlib-util/lib -L/home/vsedyshev/Work/1111/pjproject/pjnath/lib -L/home/vsedyshev/Work/1111/pjproject/pjmedia/lib -L/home/vsedyshev/Work/1111/pjproject/pjsip/lib -L/home/vsedyshev/Work/1111/pjproject/third_party/lib -lSDL2     -lSDL2      -lpjsua-x86_64-unknown-linux-gnu -lpjsip-ua-x86_64-unknown-linux-gnu -lpjsip-simple-x86_64-unknown-linux-gnu -lpjsip-x86_64-unknown-linux-gnu -lpjmedia-codec-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjmedia-videodev-x86_64-unknown-linux-gnu -lpjmedia-audiodev-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjnath-x86_64-unknown-linux-gnu -lpjlib-util-x86_64-unknown-linux-gnu  -lsrtp-x86_64-unknown-linux-gnu -lresample-x86_64-unknown-linux-gnu -lgsmcodec-x86_64-unknown-linux-gnu -lspeex-x86_64-unknown-linux-gnu -lilbccodec-x86_64-unknown-linux-gnu -lg7221codec-x86_64-unknown-linux-gnu -lyuv-x86_64-unknown-linux-gnu -lwebrtc-x86_64-unknown-linux-gnu  -lpj-x86_64-unknown-linux-gnu -lssl -lcrypto -luuid -lm -lrt -lpthread  -lasound -lSDL2   

# gcc -c -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1 -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -I/home/vsedyshev/Work/1111/pjproject/pjlib/include -I/home/vsedyshev/Work/1111/pjproject/pjlib-util/include -I/home/vsedyshev/Work/1111/pjproject/pjnath/include -I/home/vsedyshev/Work/1111/pjproject/pjmedia/include -I/home/vsedyshev/Work/1111/pjproject/pjsip/include  \
# 	-o output/sample-x86_64-unknown-linux-gnu/recfile.o \
# 	../src/samples/recfile.c 
# gcc -o ../bin/samples/x86_64-unknown-linux-gnu/recfile \
#      output/sample-x86_64-unknown-linux-gnu/recfile.o -L/home/vsedyshev/Work/1111/pjproject/pjlib/lib -L/home/vsedyshev/Work/1111/pjproject/pjlib-util/lib -L/home/vsedyshev/Work/1111/pjproject/pjnath/lib -L/home/vsedyshev/Work/1111/pjproject/pjmedia/lib -L/home/vsedyshev/Work/1111/pjproject/pjsip/lib -L/home/vsedyshev/Work/1111/pjproject/third_party/lib -lSDL2     -lSDL2      -lpjsua-x86_64-unknown-linux-gnu -lpjsip-ua-x86_64-unknown-linux-gnu -lpjsip-simple-x86_64-unknown-linux-gnu -lpjsip-x86_64-unknown-linux-gnu -lpjmedia-codec-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjmedia-videodev-x86_64-unknown-linux-gnu -lpjmedia-audiodev-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjnath-x86_64-unknown-linux-gnu -lpjlib-util-x86_64-unknown-linux-gnu  -lsrtp-x86_64-unknown-linux-gnu -lresample-x86_64-unknown-linux-gnu -lgsmcodec-x86_64-unknown-linux-gnu -lspeex-x86_64-unknown-linux-gnu -lilbccodec-x86_64-unknown-linux-gnu -lg7221codec-x86_64-unknown-linux-gnu -lyuv-x86_64-unknown-linux-gnu -lwebrtc-x86_64-unknown-linux-gnu  -lpj-x86_64-unknown-linux-gnu -lssl -lcrypto -luuid -lm -lrt -lpthread  -lasound -lSDL2   

# gcc -c -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1 -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -I/home/vsedyshev/Work/1111/pjproject/pjlib/include -I/home/vsedyshev/Work/1111/pjproject/pjlib-util/include -I/home/vsedyshev/Work/1111/pjproject/pjnath/include -I/home/vsedyshev/Work/1111/pjproject/pjmedia/include -I/home/vsedyshev/Work/1111/pjproject/pjsip/include  \
# 	-o output/sample-x86_64-unknown-linux-gnu/resampleplay.o \
# 	../src/samples/resampleplay.c 
# gcc -o ../bin/samples/x86_64-unknown-linux-gnu/resampleplay \
#      output/sample-x86_64-unknown-linux-gnu/resampleplay.o -L/home/vsedyshev/Work/1111/pjproject/pjlib/lib -L/home/vsedyshev/Work/1111/pjproject/pjlib-util/lib -L/home/vsedyshev/Work/1111/pjproject/pjnath/lib -L/home/vsedyshev/Work/1111/pjproject/pjmedia/lib -L/home/vsedyshev/Work/1111/pjproject/pjsip/lib -L/home/vsedyshev/Work/1111/pjproject/third_party/lib -lSDL2     -lSDL2      -lpjsua-x86_64-unknown-linux-gnu -lpjsip-ua-x86_64-unknown-linux-gnu -lpjsip-simple-x86_64-unknown-linux-gnu -lpjsip-x86_64-unknown-linux-gnu -lpjmedia-codec-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjmedia-videodev-x86_64-unknown-linux-gnu -lpjmedia-audiodev-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjnath-x86_64-unknown-linux-gnu -lpjlib-util-x86_64-unknown-linux-gnu  -lsrtp-x86_64-unknown-linux-gnu -lresample-x86_64-unknown-linux-gnu -lgsmcodec-x86_64-unknown-linux-gnu -lspeex-x86_64-unknown-linux-gnu -lilbccodec-x86_64-unknown-linux-gnu -lg7221codec-x86_64-unknown-linux-gnu -lyuv-x86_64-unknown-linux-gnu -lwebrtc-x86_64-unknown-linux-gnu  -lpj-x86_64-unknown-linux-gnu -lssl -lcrypto -luuid -lm -lrt -lpthread  -lasound -lSDL2   

# gcc -c -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1 -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -I/home/vsedyshev/Work/1111/pjproject/pjlib/include -I/home/vsedyshev/Work/1111/pjproject/pjlib-util/include -I/home/vsedyshev/Work/1111/pjproject/pjnath/include -I/home/vsedyshev/Work/1111/pjproject/pjmedia/include -I/home/vsedyshev/Work/1111/pjproject/pjsip/include  \
# 	-o output/sample-x86_64-unknown-linux-gnu/simpleua.o \
# 	../src/samples/simpleua.c 
# gcc -o ../bin/samples/x86_64-unknown-linux-gnu/simpleua \
#      output/sample-x86_64-unknown-linux-gnu/simpleua.o -L/home/vsedyshev/Work/1111/pjproject/pjlib/lib -L/home/vsedyshev/Work/1111/pjproject/pjlib-util/lib -L/home/vsedyshev/Work/1111/pjproject/pjnath/lib -L/home/vsedyshev/Work/1111/pjproject/pjmedia/lib -L/home/vsedyshev/Work/1111/pjproject/pjsip/lib -L/home/vsedyshev/Work/1111/pjproject/third_party/lib -lSDL2     -lSDL2      -lpjsua-x86_64-unknown-linux-gnu -lpjsip-ua-x86_64-unknown-linux-gnu -lpjsip-simple-x86_64-unknown-linux-gnu -lpjsip-x86_64-unknown-linux-gnu -lpjmedia-codec-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjmedia-videodev-x86_64-unknown-linux-gnu -lpjmedia-audiodev-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjnath-x86_64-unknown-linux-gnu -lpjlib-util-x86_64-unknown-linux-gnu  -lsrtp-x86_64-unknown-linux-gnu -lresample-x86_64-unknown-linux-gnu -lgsmcodec-x86_64-unknown-linux-gnu -lspeex-x86_64-unknown-linux-gnu -lilbccodec-x86_64-unknown-linux-gnu -lg7221codec-x86_64-unknown-linux-gnu -lyuv-x86_64-unknown-linux-gnu -lwebrtc-x86_64-unknown-linux-gnu  -lpj-x86_64-unknown-linux-gnu -lssl -lcrypto -luuid -lm -lrt -lpthread  -lasound -lSDL2   

# gcc -c -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1 -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -I/home/vsedyshev/Work/1111/pjproject/pjlib/include -I/home/vsedyshev/Work/1111/pjproject/pjlib-util/include -I/home/vsedyshev/Work/1111/pjproject/pjnath/include -I/home/vsedyshev/Work/1111/pjproject/pjmedia/include -I/home/vsedyshev/Work/1111/pjproject/pjsip/include  \
# 	-o output/sample-x86_64-unknown-linux-gnu/simple_pjsua.o \
# 	../src/samples/simple_pjsua.c 
# gcc -o ../bin/samples/x86_64-unknown-linux-gnu/simple_pjsua \
#      output/sample-x86_64-unknown-linux-gnu/simple_pjsua.o -L/home/vsedyshev/Work/1111/pjproject/pjlib/lib -L/home/vsedyshev/Work/1111/pjproject/pjlib-util/lib -L/home/vsedyshev/Work/1111/pjproject/pjnath/lib -L/home/vsedyshev/Work/1111/pjproject/pjmedia/lib -L/home/vsedyshev/Work/1111/pjproject/pjsip/lib -L/home/vsedyshev/Work/1111/pjproject/third_party/lib -lSDL2     -lSDL2      -lpjsua-x86_64-unknown-linux-gnu -lpjsip-ua-x86_64-unknown-linux-gnu -lpjsip-simple-x86_64-unknown-linux-gnu -lpjsip-x86_64-unknown-linux-gnu -lpjmedia-codec-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjmedia-videodev-x86_64-unknown-linux-gnu -lpjmedia-audiodev-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjnath-x86_64-unknown-linux-gnu -lpjlib-util-x86_64-unknown-linux-gnu  -lsrtp-x86_64-unknown-linux-gnu -lresample-x86_64-unknown-linux-gnu -lgsmcodec-x86_64-unknown-linux-gnu -lspeex-x86_64-unknown-linux-gnu -lilbccodec-x86_64-unknown-linux-gnu -lg7221codec-x86_64-unknown-linux-gnu -lyuv-x86_64-unknown-linux-gnu -lwebrtc-x86_64-unknown-linux-gnu  -lpj-x86_64-unknown-linux-gnu -lssl -lcrypto -luuid -lm -lrt -lpthread  -lasound -lSDL2   

# gcc -c -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1 -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -I/home/vsedyshev/Work/1111/pjproject/pjlib/include -I/home/vsedyshev/Work/1111/pjproject/pjlib-util/include -I/home/vsedyshev/Work/1111/pjproject/pjnath/include -I/home/vsedyshev/Work/1111/pjproject/pjmedia/include -I/home/vsedyshev/Work/1111/pjproject/pjsip/include  \
# 	-o output/sample-x86_64-unknown-linux-gnu/sipecho.o \
# 	../src/samples/sipecho.c 
# gcc -o ../bin/samples/x86_64-unknown-linux-gnu/sipecho \
#      output/sample-x86_64-unknown-linux-gnu/sipecho.o -L/home/vsedyshev/Work/1111/pjproject/pjlib/lib -L/home/vsedyshev/Work/1111/pjproject/pjlib-util/lib -L/home/vsedyshev/Work/1111/pjproject/pjnath/lib -L/home/vsedyshev/Work/1111/pjproject/pjmedia/lib -L/home/vsedyshev/Work/1111/pjproject/pjsip/lib -L/home/vsedyshev/Work/1111/pjproject/third_party/lib -lSDL2     -lSDL2      -lpjsua-x86_64-unknown-linux-gnu -lpjsip-ua-x86_64-unknown-linux-gnu -lpjsip-simple-x86_64-unknown-linux-gnu -lpjsip-x86_64-unknown-linux-gnu -lpjmedia-codec-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjmedia-videodev-x86_64-unknown-linux-gnu -lpjmedia-audiodev-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjnath-x86_64-unknown-linux-gnu -lpjlib-util-x86_64-unknown-linux-gnu  -lsrtp-x86_64-unknown-linux-gnu -lresample-x86_64-unknown-linux-gnu -lgsmcodec-x86_64-unknown-linux-gnu -lspeex-x86_64-unknown-linux-gnu -lilbccodec-x86_64-unknown-linux-gnu -lg7221codec-x86_64-unknown-linux-gnu -lyuv-x86_64-unknown-linux-gnu -lwebrtc-x86_64-unknown-linux-gnu  -lpj-x86_64-unknown-linux-gnu -lssl -lcrypto -luuid -lm -lrt -lpthread  -lasound -lSDL2   

# gcc -c -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1 -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -I/home/vsedyshev/Work/1111/pjproject/pjlib/include -I/home/vsedyshev/Work/1111/pjproject/pjlib-util/include -I/home/vsedyshev/Work/1111/pjproject/pjnath/include -I/home/vsedyshev/Work/1111/pjproject/pjmedia/include -I/home/vsedyshev/Work/1111/pjproject/pjsip/include  \
# 	-o output/sample-x86_64-unknown-linux-gnu/siprtp.o \
# 	../src/samples/siprtp.c 
# gcc -o ../bin/samples/x86_64-unknown-linux-gnu/siprtp \
#      output/sample-x86_64-unknown-linux-gnu/siprtp.o -L/home/vsedyshev/Work/1111/pjproject/pjlib/lib -L/home/vsedyshev/Work/1111/pjproject/pjlib-util/lib -L/home/vsedyshev/Work/1111/pjproject/pjnath/lib -L/home/vsedyshev/Work/1111/pjproject/pjmedia/lib -L/home/vsedyshev/Work/1111/pjproject/pjsip/lib -L/home/vsedyshev/Work/1111/pjproject/third_party/lib -lSDL2     -lSDL2      -lpjsua-x86_64-unknown-linux-gnu -lpjsip-ua-x86_64-unknown-linux-gnu -lpjsip-simple-x86_64-unknown-linux-gnu -lpjsip-x86_64-unknown-linux-gnu -lpjmedia-codec-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjmedia-videodev-x86_64-unknown-linux-gnu -lpjmedia-audiodev-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjnath-x86_64-unknown-linux-gnu -lpjlib-util-x86_64-unknown-linux-gnu  -lsrtp-x86_64-unknown-linux-gnu -lresample-x86_64-unknown-linux-gnu -lgsmcodec-x86_64-unknown-linux-gnu -lspeex-x86_64-unknown-linux-gnu -lilbccodec-x86_64-unknown-linux-gnu -lg7221codec-x86_64-unknown-linux-gnu -lyuv-x86_64-unknown-linux-gnu -lwebrtc-x86_64-unknown-linux-gnu  -lpj-x86_64-unknown-linux-gnu -lssl -lcrypto -luuid -lm -lrt -lpthread  -lasound -lSDL2   

# gcc -c -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1 -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -I/home/vsedyshev/Work/1111/pjproject/pjlib/include -I/home/vsedyshev/Work/1111/pjproject/pjlib-util/include -I/home/vsedyshev/Work/1111/pjproject/pjnath/include -I/home/vsedyshev/Work/1111/pjproject/pjmedia/include -I/home/vsedyshev/Work/1111/pjproject/pjsip/include  \
# 	-o output/sample-x86_64-unknown-linux-gnu/sipstateless.o \
# 	../src/samples/sipstateless.c 
# gcc -o ../bin/samples/x86_64-unknown-linux-gnu/sipstateless \
#      output/sample-x86_64-unknown-linux-gnu/sipstateless.o -L/home/vsedyshev/Work/1111/pjproject/pjlib/lib -L/home/vsedyshev/Work/1111/pjproject/pjlib-util/lib -L/home/vsedyshev/Work/1111/pjproject/pjnath/lib -L/home/vsedyshev/Work/1111/pjproject/pjmedia/lib -L/home/vsedyshev/Work/1111/pjproject/pjsip/lib -L/home/vsedyshev/Work/1111/pjproject/third_party/lib -lSDL2     -lSDL2      -lpjsua-x86_64-unknown-linux-gnu -lpjsip-ua-x86_64-unknown-linux-gnu -lpjsip-simple-x86_64-unknown-linux-gnu -lpjsip-x86_64-unknown-linux-gnu -lpjmedia-codec-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjmedia-videodev-x86_64-unknown-linux-gnu -lpjmedia-audiodev-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjnath-x86_64-unknown-linux-gnu -lpjlib-util-x86_64-unknown-linux-gnu  -lsrtp-x86_64-unknown-linux-gnu -lresample-x86_64-unknown-linux-gnu -lgsmcodec-x86_64-unknown-linux-gnu -lspeex-x86_64-unknown-linux-gnu -lilbccodec-x86_64-unknown-linux-gnu -lg7221codec-x86_64-unknown-linux-gnu -lyuv-x86_64-unknown-linux-gnu -lwebrtc-x86_64-unknown-linux-gnu  -lpj-x86_64-unknown-linux-gnu -lssl -lcrypto -luuid -lm -lrt -lpthread  -lasound -lSDL2   

# gcc -c -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1 -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -I/home/vsedyshev/Work/1111/pjproject/pjlib/include -I/home/vsedyshev/Work/1111/pjproject/pjlib-util/include -I/home/vsedyshev/Work/1111/pjproject/pjnath/include -I/home/vsedyshev/Work/1111/pjproject/pjmedia/include -I/home/vsedyshev/Work/1111/pjproject/pjsip/include  \
# 	-o output/sample-x86_64-unknown-linux-gnu/stateful_proxy.o \
# 	../src/samples/stateful_proxy.c 
# gcc -o ../bin/samples/x86_64-unknown-linux-gnu/stateful_proxy \
#      output/sample-x86_64-unknown-linux-gnu/stateful_proxy.o -L/home/vsedyshev/Work/1111/pjproject/pjlib/lib -L/home/vsedyshev/Work/1111/pjproject/pjlib-util/lib -L/home/vsedyshev/Work/1111/pjproject/pjnath/lib -L/home/vsedyshev/Work/1111/pjproject/pjmedia/lib -L/home/vsedyshev/Work/1111/pjproject/pjsip/lib -L/home/vsedyshev/Work/1111/pjproject/third_party/lib -lSDL2     -lSDL2      -lpjsua-x86_64-unknown-linux-gnu -lpjsip-ua-x86_64-unknown-linux-gnu -lpjsip-simple-x86_64-unknown-linux-gnu -lpjsip-x86_64-unknown-linux-gnu -lpjmedia-codec-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjmedia-videodev-x86_64-unknown-linux-gnu -lpjmedia-audiodev-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjnath-x86_64-unknown-linux-gnu -lpjlib-util-x86_64-unknown-linux-gnu  -lsrtp-x86_64-unknown-linux-gnu -lresample-x86_64-unknown-linux-gnu -lgsmcodec-x86_64-unknown-linux-gnu -lspeex-x86_64-unknown-linux-gnu -lilbccodec-x86_64-unknown-linux-gnu -lg7221codec-x86_64-unknown-linux-gnu -lyuv-x86_64-unknown-linux-gnu -lwebrtc-x86_64-unknown-linux-gnu  -lpj-x86_64-unknown-linux-gnu -lssl -lcrypto -luuid -lm -lrt -lpthread  -lasound -lSDL2   

# gcc -c -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1 -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -I/home/vsedyshev/Work/1111/pjproject/pjlib/include -I/home/vsedyshev/Work/1111/pjproject/pjlib-util/include -I/home/vsedyshev/Work/1111/pjproject/pjnath/include -I/home/vsedyshev/Work/1111/pjproject/pjmedia/include -I/home/vsedyshev/Work/1111/pjproject/pjsip/include  \
# 	-o output/sample-x86_64-unknown-linux-gnu/stateless_proxy.o \
# 	../src/samples/stateless_proxy.c 
# gcc -o ../bin/samples/x86_64-unknown-linux-gnu/stateless_proxy \
#      output/sample-x86_64-unknown-linux-gnu/stateless_proxy.o -L/home/vsedyshev/Work/1111/pjproject/pjlib/lib -L/home/vsedyshev/Work/1111/pjproject/pjlib-util/lib -L/home/vsedyshev/Work/1111/pjproject/pjnath/lib -L/home/vsedyshev/Work/1111/pjproject/pjmedia/lib -L/home/vsedyshev/Work/1111/pjproject/pjsip/lib -L/home/vsedyshev/Work/1111/pjproject/third_party/lib -lSDL2     -lSDL2      -lpjsua-x86_64-unknown-linux-gnu -lpjsip-ua-x86_64-unknown-linux-gnu -lpjsip-simple-x86_64-unknown-linux-gnu -lpjsip-x86_64-unknown-linux-gnu -lpjmedia-codec-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjmedia-videodev-x86_64-unknown-linux-gnu -lpjmedia-audiodev-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjnath-x86_64-unknown-linux-gnu -lpjlib-util-x86_64-unknown-linux-gnu  -lsrtp-x86_64-unknown-linux-gnu -lresample-x86_64-unknown-linux-gnu -lgsmcodec-x86_64-unknown-linux-gnu -lspeex-x86_64-unknown-linux-gnu -lilbccodec-x86_64-unknown-linux-gnu -lg7221codec-x86_64-unknown-linux-gnu -lyuv-x86_64-unknown-linux-gnu -lwebrtc-x86_64-unknown-linux-gnu  -lpj-x86_64-unknown-linux-gnu -lssl -lcrypto -luuid -lm -lrt -lpthread  -lasound -lSDL2   

# gcc -c -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1 -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -I/home/vsedyshev/Work/1111/pjproject/pjlib/include -I/home/vsedyshev/Work/1111/pjproject/pjlib-util/include -I/home/vsedyshev/Work/1111/pjproject/pjnath/include -I/home/vsedyshev/Work/1111/pjproject/pjmedia/include -I/home/vsedyshev/Work/1111/pjproject/pjsip/include  \
# 	-o output/sample-x86_64-unknown-linux-gnu/stereotest.o \
# 	../src/samples/stereotest.c 
# gcc -o ../bin/samples/x86_64-unknown-linux-gnu/stereotest \
#      output/sample-x86_64-unknown-linux-gnu/stereotest.o -L/home/vsedyshev/Work/1111/pjproject/pjlib/lib -L/home/vsedyshev/Work/1111/pjproject/pjlib-util/lib -L/home/vsedyshev/Work/1111/pjproject/pjnath/lib -L/home/vsedyshev/Work/1111/pjproject/pjmedia/lib -L/home/vsedyshev/Work/1111/pjproject/pjsip/lib -L/home/vsedyshev/Work/1111/pjproject/third_party/lib -lSDL2     -lSDL2      -lpjsua-x86_64-unknown-linux-gnu -lpjsip-ua-x86_64-unknown-linux-gnu -lpjsip-simple-x86_64-unknown-linux-gnu -lpjsip-x86_64-unknown-linux-gnu -lpjmedia-codec-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjmedia-videodev-x86_64-unknown-linux-gnu -lpjmedia-audiodev-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjnath-x86_64-unknown-linux-gnu -lpjlib-util-x86_64-unknown-linux-gnu  -lsrtp-x86_64-unknown-linux-gnu -lresample-x86_64-unknown-linux-gnu -lgsmcodec-x86_64-unknown-linux-gnu -lspeex-x86_64-unknown-linux-gnu -lilbccodec-x86_64-unknown-linux-gnu -lg7221codec-x86_64-unknown-linux-gnu -lyuv-x86_64-unknown-linux-gnu -lwebrtc-x86_64-unknown-linux-gnu  -lpj-x86_64-unknown-linux-gnu -lssl -lcrypto -luuid -lm -lrt -lpthread  -lasound -lSDL2   

# gcc -c -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1 -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -I/home/vsedyshev/Work/1111/pjproject/pjlib/include -I/home/vsedyshev/Work/1111/pjproject/pjlib-util/include -I/home/vsedyshev/Work/1111/pjproject/pjnath/include -I/home/vsedyshev/Work/1111/pjproject/pjmedia/include -I/home/vsedyshev/Work/1111/pjproject/pjsip/include  \
# 	-o output/sample-x86_64-unknown-linux-gnu/streamutil.o \
# 	../src/samples/streamutil.c 
# gcc -o ../bin/samples/x86_64-unknown-linux-gnu/streamutil \
#      output/sample-x86_64-unknown-linux-gnu/streamutil.o -L/home/vsedyshev/Work/1111/pjproject/pjlib/lib -L/home/vsedyshev/Work/1111/pjproject/pjlib-util/lib -L/home/vsedyshev/Work/1111/pjproject/pjnath/lib -L/home/vsedyshev/Work/1111/pjproject/pjmedia/lib -L/home/vsedyshev/Work/1111/pjproject/pjsip/lib -L/home/vsedyshev/Work/1111/pjproject/third_party/lib -lSDL2     -lSDL2      -lpjsua-x86_64-unknown-linux-gnu -lpjsip-ua-x86_64-unknown-linux-gnu -lpjsip-simple-x86_64-unknown-linux-gnu -lpjsip-x86_64-unknown-linux-gnu -lpjmedia-codec-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjmedia-videodev-x86_64-unknown-linux-gnu -lpjmedia-audiodev-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjnath-x86_64-unknown-linux-gnu -lpjlib-util-x86_64-unknown-linux-gnu  -lsrtp-x86_64-unknown-linux-gnu -lresample-x86_64-unknown-linux-gnu -lgsmcodec-x86_64-unknown-linux-gnu -lspeex-x86_64-unknown-linux-gnu -lilbccodec-x86_64-unknown-linux-gnu -lg7221codec-x86_64-unknown-linux-gnu -lyuv-x86_64-unknown-linux-gnu -lwebrtc-x86_64-unknown-linux-gnu  -lpj-x86_64-unknown-linux-gnu -lssl -lcrypto -luuid -lm -lrt -lpthread  -lasound -lSDL2   

# gcc -c -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1 -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -I/home/vsedyshev/Work/1111/pjproject/pjlib/include -I/home/vsedyshev/Work/1111/pjproject/pjlib-util/include -I/home/vsedyshev/Work/1111/pjproject/pjnath/include -I/home/vsedyshev/Work/1111/pjproject/pjmedia/include -I/home/vsedyshev/Work/1111/pjproject/pjsip/include  \
# 	-o output/sample-x86_64-unknown-linux-gnu/strerror.o \
# 	../src/samples/strerror.c 
# gcc -o ../bin/samples/x86_64-unknown-linux-gnu/strerror \
#      output/sample-x86_64-unknown-linux-gnu/strerror.o -L/home/vsedyshev/Work/1111/pjproject/pjlib/lib -L/home/vsedyshev/Work/1111/pjproject/pjlib-util/lib -L/home/vsedyshev/Work/1111/pjproject/pjnath/lib -L/home/vsedyshev/Work/1111/pjproject/pjmedia/lib -L/home/vsedyshev/Work/1111/pjproject/pjsip/lib -L/home/vsedyshev/Work/1111/pjproject/third_party/lib -lSDL2     -lSDL2      -lpjsua-x86_64-unknown-linux-gnu -lpjsip-ua-x86_64-unknown-linux-gnu -lpjsip-simple-x86_64-unknown-linux-gnu -lpjsip-x86_64-unknown-linux-gnu -lpjmedia-codec-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjmedia-videodev-x86_64-unknown-linux-gnu -lpjmedia-audiodev-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjnath-x86_64-unknown-linux-gnu -lpjlib-util-x86_64-unknown-linux-gnu  -lsrtp-x86_64-unknown-linux-gnu -lresample-x86_64-unknown-linux-gnu -lgsmcodec-x86_64-unknown-linux-gnu -lspeex-x86_64-unknown-linux-gnu -lilbccodec-x86_64-unknown-linux-gnu -lg7221codec-x86_64-unknown-linux-gnu -lyuv-x86_64-unknown-linux-gnu -lwebrtc-x86_64-unknown-linux-gnu  -lpj-x86_64-unknown-linux-gnu -lssl -lcrypto -luuid -lm -lrt -lpthread  -lasound -lSDL2   

# gcc -c -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1 -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -I/home/vsedyshev/Work/1111/pjproject/pjlib/include -I/home/vsedyshev/Work/1111/pjproject/pjlib-util/include -I/home/vsedyshev/Work/1111/pjproject/pjnath/include -I/home/vsedyshev/Work/1111/pjproject/pjmedia/include -I/home/vsedyshev/Work/1111/pjproject/pjsip/include  \
# 	-o output/sample-x86_64-unknown-linux-gnu/tonegen.o \
# 	../src/samples/tonegen.c 
# gcc -o ../bin/samples/x86_64-unknown-linux-gnu/tonegen \
#      output/sample-x86_64-unknown-linux-gnu/tonegen.o -L/home/vsedyshev/Work/1111/pjproject/pjlib/lib -L/home/vsedyshev/Work/1111/pjproject/pjlib-util/lib -L/home/vsedyshev/Work/1111/pjproject/pjnath/lib -L/home/vsedyshev/Work/1111/pjproject/pjmedia/lib -L/home/vsedyshev/Work/1111/pjproject/pjsip/lib -L/home/vsedyshev/Work/1111/pjproject/third_party/lib -lSDL2     -lSDL2      -lpjsua-x86_64-unknown-linux-gnu -lpjsip-ua-x86_64-unknown-linux-gnu -lpjsip-simple-x86_64-unknown-linux-gnu -lpjsip-x86_64-unknown-linux-gnu -lpjmedia-codec-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjmedia-videodev-x86_64-unknown-linux-gnu -lpjmedia-audiodev-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjnath-x86_64-unknown-linux-gnu -lpjlib-util-x86_64-unknown-linux-gnu  -lsrtp-x86_64-unknown-linux-gnu -lresample-x86_64-unknown-linux-gnu -lgsmcodec-x86_64-unknown-linux-gnu -lspeex-x86_64-unknown-linux-gnu -lilbccodec-x86_64-unknown-linux-gnu -lg7221codec-x86_64-unknown-linux-gnu -lyuv-x86_64-unknown-linux-gnu -lwebrtc-x86_64-unknown-linux-gnu  -lpj-x86_64-unknown-linux-gnu -lssl -lcrypto -luuid -lm -lrt -lpthread  -lasound -lSDL2   

# gcc -c -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1 -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -I/home/vsedyshev/Work/1111/pjproject/pjlib/include -I/home/vsedyshev/Work/1111/pjproject/pjlib-util/include -I/home/vsedyshev/Work/1111/pjproject/pjnath/include -I/home/vsedyshev/Work/1111/pjproject/pjmedia/include -I/home/vsedyshev/Work/1111/pjproject/pjsip/include  \
# 	-o output/sample-x86_64-unknown-linux-gnu/vid_codec_test.o \
# 	../src/samples/vid_codec_test.c 
# gcc -o ../bin/samples/x86_64-unknown-linux-gnu/vid_codec_test \
#      output/sample-x86_64-unknown-linux-gnu/vid_codec_test.o -L/home/vsedyshev/Work/1111/pjproject/pjlib/lib -L/home/vsedyshev/Work/1111/pjproject/pjlib-util/lib -L/home/vsedyshev/Work/1111/pjproject/pjnath/lib -L/home/vsedyshev/Work/1111/pjproject/pjmedia/lib -L/home/vsedyshev/Work/1111/pjproject/pjsip/lib -L/home/vsedyshev/Work/1111/pjproject/third_party/lib -lSDL2     -lSDL2      -lpjsua-x86_64-unknown-linux-gnu -lpjsip-ua-x86_64-unknown-linux-gnu -lpjsip-simple-x86_64-unknown-linux-gnu -lpjsip-x86_64-unknown-linux-gnu -lpjmedia-codec-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjmedia-videodev-x86_64-unknown-linux-gnu -lpjmedia-audiodev-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjnath-x86_64-unknown-linux-gnu -lpjlib-util-x86_64-unknown-linux-gnu  -lsrtp-x86_64-unknown-linux-gnu -lresample-x86_64-unknown-linux-gnu -lgsmcodec-x86_64-unknown-linux-gnu -lspeex-x86_64-unknown-linux-gnu -lilbccodec-x86_64-unknown-linux-gnu -lg7221codec-x86_64-unknown-linux-gnu -lyuv-x86_64-unknown-linux-gnu -lwebrtc-x86_64-unknown-linux-gnu  -lpj-x86_64-unknown-linux-gnu -lssl -lcrypto -luuid -lm -lrt -lpthread  -lasound -lSDL2   

# gcc -c -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1 -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -I/home/vsedyshev/Work/1111/pjproject/pjlib/include -I/home/vsedyshev/Work/1111/pjproject/pjlib-util/include -I/home/vsedyshev/Work/1111/pjproject/pjnath/include -I/home/vsedyshev/Work/1111/pjproject/pjmedia/include -I/home/vsedyshev/Work/1111/pjproject/pjsip/include  \
# 	-o output/sample-x86_64-unknown-linux-gnu/vid_streamutil.o \
# 	../src/samples/vid_streamutil.c 
# gcc -o ../bin/samples/x86_64-unknown-linux-gnu/vid_streamutil \
#      output/sample-x86_64-unknown-linux-gnu/vid_streamutil.o -L/home/vsedyshev/Work/1111/pjproject/pjlib/lib -L/home/vsedyshev/Work/1111/pjproject/pjlib-util/lib -L/home/vsedyshev/Work/1111/pjproject/pjnath/lib -L/home/vsedyshev/Work/1111/pjproject/pjmedia/lib -L/home/vsedyshev/Work/1111/pjproject/pjsip/lib -L/home/vsedyshev/Work/1111/pjproject/third_party/lib -lSDL2     -lSDL2      -lpjsua-x86_64-unknown-linux-gnu -lpjsip-ua-x86_64-unknown-linux-gnu -lpjsip-simple-x86_64-unknown-linux-gnu -lpjsip-x86_64-unknown-linux-gnu -lpjmedia-codec-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjmedia-videodev-x86_64-unknown-linux-gnu -lpjmedia-audiodev-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjnath-x86_64-unknown-linux-gnu -lpjlib-util-x86_64-unknown-linux-gnu  -lsrtp-x86_64-unknown-linux-gnu -lresample-x86_64-unknown-linux-gnu -lgsmcodec-x86_64-unknown-linux-gnu -lspeex-x86_64-unknown-linux-gnu -lilbccodec-x86_64-unknown-linux-gnu -lg7221codec-x86_64-unknown-linux-gnu -lyuv-x86_64-unknown-linux-gnu -lwebrtc-x86_64-unknown-linux-gnu  -lpj-x86_64-unknown-linux-gnu -lssl -lcrypto -luuid -lm -lrt -lpthread  -lasound -lSDL2   

# g++ -c -g -O2 -DPJ_AUTOCONF=1 -O2 -DPJ_IS_BIG_ENDIAN=0 -DPJ_IS_LITTLE_ENDIAN=1 -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -DPJMEDIA_VIDEO_DEV_HAS_SDL=1 -I/usr/include/SDL2 -D_REENTRANT -DPJMEDIA_USE_OLD_FFMPEG=1       -I/home/vsedyshev/Work/1111/pjproject/pjlib/include -I/home/vsedyshev/Work/1111/pjproject/pjlib-util/include -I/home/vsedyshev/Work/1111/pjproject/pjnath/include -I/home/vsedyshev/Work/1111/pjproject/pjmedia/include -I/home/vsedyshev/Work/1111/pjproject/pjsip/include  \
# 	-o output/pjsua2_sample-x86_64-unknown-linux-gnu/pjsua2_demo.o \
# 	../src/samples/pjsua2_demo.cpp
# gcc -o ../bin/samples/x86_64-unknown-linux-gnu/pjsua2_demo \
#      output/pjsua2_sample-x86_64-unknown-linux-gnu/pjsua2_demo.o -L/home/vsedyshev/Work/1111/pjproject/pjlib/lib -L/home/vsedyshev/Work/1111/pjproject/pjlib-util/lib -L/home/vsedyshev/Work/1111/pjproject/pjnath/lib -L/home/vsedyshev/Work/1111/pjproject/pjmedia/lib -L/home/vsedyshev/Work/1111/pjproject/pjsip/lib -L/home/vsedyshev/Work/1111/pjproject/third_party/lib -lSDL2     -lSDL2      -lpjsua2-x86_64-unknown-linux-gnu -lstdc++ -lpjsua-x86_64-unknown-linux-gnu -lpjsip-ua-x86_64-unknown-linux-gnu -lpjsip-simple-x86_64-unknown-linux-gnu -lpjsip-x86_64-unknown-linux-gnu -lpjmedia-codec-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjmedia-videodev-x86_64-unknown-linux-gnu -lpjmedia-audiodev-x86_64-unknown-linux-gnu -lpjmedia-x86_64-unknown-linux-gnu -lpjnath-x86_64-unknown-linux-gnu -lpjlib-util-x86_64-unknown-linux-gnu  -lsrtp-x86_64-unknown-linux-gnu -lresample-x86_64-unknown-linux-gnu -lgsmcodec-x86_64-unknown-linux-gnu -lspeex-x86_64-unknown-linux-gnu -lilbccodec-x86_64-unknown-linux-gnu -lg7221codec-x86_64-unknown-linux-gnu -lyuv-x86_64-unknown-linux-gnu -lwebrtc-x86_64-unknown-linux-gnu  -lpj-x86_64-unknown-linux-gnu -lssl -lcrypto -luuid -lm -lrt -lpthread  -lasound -lSDL2   
