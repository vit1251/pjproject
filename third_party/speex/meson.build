project('speex', 'c', version: '1.3.5')

# compilers

c_compiler = meson.get_compiler('c')

# includes

speex_inc = include_directories('include')

# configure

conf_data = configuration_data()

short_size = c_compiler.sizeof('short')
int_size = c_compiler.sizeof('int')
long_size = c_compiler.sizeof('long')

if short_size == 2
    conf_data.set('SIZE16', 'short')
elif int_size == 2
    conf_data.set('SIZE16', 'int')
else
#error
endif

if int_size == 4
    conf_data.set('SIZE32', 'int')
elif long_size == 4
    conf_data.set('SIZE32', 'long')
else
#error
endif

configure_file(input : 'include/speex/speex_config_types.h.in',
               output : 'speex_config_types.h',
               configuration : conf_data)

#

conf_data_1 = configuration_data()
configure_file(input : 'config.h.in',
               output : 'config.h',
               configuration : conf_data_1)

#

speex_sources = [
    'libspeex/bits.c',
    'libspeex/cb_search.c',
    'libspeex/exc_10_16_table.c',
    'libspeex/exc_10_32_table.c',
    'libspeex/exc_20_32_table.c',
    'libspeex/exc_5_256_table.c',
    'libspeex/exc_5_64_table.c',
    'libspeex/exc_8_128_table.c',
    'libspeex/fftwrap.c',
    'libspeex/filterbank.c',
    'libspeex/filters.c',
    'libspeex/gain_table.c',
    'libspeex/gain_table_lbr.c',
    'libspeex/hexc_10_32_table.c',
    'libspeex/hexc_table.c',
    'libspeex/high_lsp_tables.c',
    'libspeex/kiss_fft.c',
    'libspeex/kiss_fftr.c',
    'libspeex/lpc.c',
    'libspeex/lsp.c',
    'libspeex/lsp_tables_nb.c',
    'libspeex/ltp.c',
    'libspeex/mdf.c',
    'libspeex/modes.c',
    'libspeex/modes_wb.c',
    'libspeex/nb_celp.c',
    'libspeex/preprocess.c',
    'libspeex/quant_lsp.c',
    'libspeex/resample.c',
    'libspeex/sb_celp.c',
    'libspeex/smallft.c',
    'libspeex/speex.c',
    'libspeex/speex_callbacks.c',
    'libspeex/speex_header.c',
    'libspeex/scal.c',
    'libspeex/stereo.c',
    'libspeex/vbr.c',
    'libspeex/vq.c',
    'libspeex/window.c',
]

speex = static_library('speex', speex_sources,
        include_directories: [speex_inc],
        c_args: [
             '-DHAVE_CONFIG_H',
             '-Wall', '-DPJ_LINUX=1', '-O2', '-DPJ_IS_BIG_ENDIAN=0', '-DPJ_IS_LITTLE_ENDIAN=1',
        ]
    )
speex_dep = declare_dependency(
        include_directories: [speex_inc],
        link_with: speex
    )
