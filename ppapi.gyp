# Copyright (c) 2010 The Chromium Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.


{
  'variables': {
    'chromium_code': 1,  # Use higher warning level.
  },
  'target_defaults': {
    'conditions': [
      # Linux shared libraries should always be built -fPIC.
      #
      # TODO(ajwong): For internal pepper plugins, which are statically linked
      # into chrome, do we want to build w/o -fPIC?  If so, how can we express
      # that in the build system?
      ['OS=="linux" or OS=="openbsd" or OS=="freebsd" or OS=="solaris"', {
        'cflags': ['-fPIC', '-fvisibility=hidden'],

        # This is needed to make the Linux shlib build happy. Without this,
        # -fvisibility=hidden gets stripped by the exclusion in common.gypi
        # that is triggered when a shared library build is specified.
        'cflags/': [['include', '^-fvisibility=hidden$']],
      }],
    ],
  },
  'targets': [
    {
      'target_name': 'ppapi_c',
      'type': 'none',
      'all_dependent_settings': {
        'include_dirs': [
           '..',
        ],
      },
      'sources': [
        'c/pp_completion_callback.h',
        'c/pp_errors.h',
        'c/pp_event.h',
        'c/pp_instance.h',
        'c/pp_module.h',
        'c/pp_point.h',
        'c/pp_rect.h',
        'c/pp_resource.h',
        'c/pp_size.h',
        'c/pp_stdint.h',
        'c/pp_var.h',
        'c/ppb.h',
        'c/ppb_core.h',
        'c/ppb_image_data.h',
        'c/ppb_instance.h',
        'c/ppb_var.h',
        'c/ppp.h',
        'c/ppp_class.h',
        'c/ppp_instance.h',

        # Dev interfaces.
        'c/dev/pp_cursor_type_dev.h',
        'c/dev/pp_file_info_dev.h',
        'c/dev/pp_video_dev.h',
        'c/dev/ppb_audio_config_dev.h',
        'c/dev/ppb_audio_dev.h',
        'c/dev/ppb_audio_trusted_dev.h',
        'c/dev/ppb_buffer_dev.h',
        'c/dev/ppb_char_set_dev.h',
        'c/dev/ppb_cursor_control_dev.h',
        'c/dev/ppb_directory_reader_dev.h',
        'c/dev/ppb_file_chooser_dev.h',
        'c/dev/ppb_file_io_dev.h',
        'c/dev/ppb_file_io_trusted_dev.h',
        'c/dev/ppb_file_ref_dev.h',
        'c/dev/ppb_file_system_dev.h',
        'c/dev/ppb_find_dev.h',
        'c/dev/ppb_font_dev.h',
        'c/dev/ppb_graphics_2d_dev.h',
        'c/dev/ppb_graphics_3d_dev.h',
        'c/dev/ppb_opengles_dev.h',
        'c/dev/ppb_scrollbar_dev.h',
        'c/dev/ppb_testing_dev.h',
        'c/dev/ppb_url_loader_dev.h',
        'c/dev/ppb_url_request_info_dev.h',
        'c/dev/ppb_url_response_info_dev.h',
        'c/dev/ppb_url_util_dev.h',
        'c/dev/ppb_video_decoder_dev.h',
        'c/dev/ppp_cursor_control_dev.h',
        'c/dev/ppp_find_dev.h',
        'c/dev/ppp_graphics_3d_dev.h',
        'c/dev/ppp_printing_dev.h',
        'c/dev/ppp_widget_dev.h',
        'c/dev/ppp_zoom_dev.h',
      ],
    },
    {
      'target_name': 'ppapi_cpp_objects',
      'type': 'static_library',
      'dependencies': [
        'ppapi_c'
      ],
      'include_dirs': [
        '..',
      ],
      'sources': [
        'cpp/completion_callback.h',
        'cpp/core.cc',
        'cpp/core.h',
        'cpp/graphics_2d.cc',
        'cpp/graphics_2d.h',
        'cpp/image_data.cc',
        'cpp/image_data.h',
        'cpp/instance.cc',
        'cpp/instance.h',
        'cpp/module.cc',
        'cpp/module.h',
        'cpp/module_impl.h',
        'cpp/paint_aggregator.cc',
        'cpp/paint_aggregator.h',
        'cpp/paint_manager.cc',
        'cpp/paint_manager.h',
        'cpp/point.h',
        'cpp/rect.cc',
        'cpp/rect.h',
        'cpp/resource.cc',
        'cpp/resource.h',
        'cpp/scriptable_object.cc',
        'cpp/scriptable_object.h',
        'cpp/size.h',
        'cpp/var.cc',
        'cpp/var.h',

        # Dev interfaces.
        'cpp/dev/audio_config_dev.cc',
        'cpp/dev/audio_config_dev.h',
        'cpp/dev/audio_dev.cc',
        'cpp/dev/audio_dev.h',
        'cpp/dev/buffer_dev.cc',
        'cpp/dev/buffer_dev.h',
        'cpp/dev/directory_entry_dev.cc',
        'cpp/dev/directory_entry_dev.h',
        'cpp/dev/directory_reader_dev.cc',
        'cpp/dev/directory_reader_dev.h',
        'cpp/dev/file_chooser_dev.cc',
        'cpp/dev/file_chooser_dev.h',
        'cpp/dev/file_io_dev.cc',
        'cpp/dev/file_io_dev.h',
        'cpp/dev/file_ref_dev.cc',
        'cpp/dev/file_ref_dev.h',
        'cpp/dev/file_system_dev.cc',
        'cpp/dev/file_system_dev.h',
        'cpp/dev/font_dev.cc',
        'cpp/dev/font_dev.h',
        'cpp/dev/graphics_3d_dev.cc',
        'cpp/dev/graphics_3d_dev.h',
        'cpp/dev/scrollbar_dev.cc',
        'cpp/dev/scrollbar_dev.h',
        'cpp/dev/url_loader_dev.cc',
        'cpp/dev/url_loader_dev.h',
        'cpp/dev/url_request_info_dev.cc',
        'cpp/dev/url_request_info_dev.h',
        'cpp/dev/url_response_info_dev.cc',
        'cpp/dev/url_response_info_dev.h',
        'cpp/dev/url_util_dev.cc',
        'cpp/dev/url_util_dev.h',
        'cpp/dev/video_decoder_dev.cc',
        'cpp/dev/video_decoder_dev.h',
        'cpp/dev/widget_dev.cc',
        'cpp/dev/widget_dev.h',
      ],
      'conditions': [
        ['OS=="win"', {
          'msvs_guid': 'AD371A1D-3459-4E2D-8E8A-881F4B83B908',
          'msvs_settings': {
            'VCCLCompilerTool': {
              'AdditionalOptions': ['/we4244'],  # implicit conversion, possible loss of data
            },
          },
        }],
        ['OS=="linux"', {
          'cflags': ['-Wextra', '-pedantic'],
        }],
        ['OS=="mac"', {
          'xcode_settings': {
            'WARNING_CFLAGS': ['-Wextra', '-pedantic'], 
           },
        }]
      ],
    },
    {
      'target_name': 'ppapi_cpp',
      'type': 'static_library',
      'dependencies': [
        'ppapi_c',
        'ppapi_cpp_objects',
      ],
      'include_dirs': [
        '..',
      ],
      'sources': [
        'cpp/module_embedder.h',
        'cpp/ppp_entrypoints.cc',
      ],
      'conditions': [
        ['OS=="win"', {
          'msvs_guid': '057E7FA0-83C0-11DF-8395-0800200C9A66',
        }],
        ['OS=="linux"', {
          'cflags': ['-Wextra', '-pedantic'],
        }],
        ['OS=="mac"', {
          'xcode_settings': {
            'WARNING_CFLAGS': ['-Wextra', '-pedantic'],
           },
        }]
      ],
    },
    {
      'target_name': 'ppapi_example',
      'dependencies': [
        'ppapi_cpp'
      ],
      'xcode_settings': {
        'INFOPLIST_FILE': 'example/Info.plist',
      },
      'sources': [
        'example/example.cc',
      ],
      'conditions': [
        ['OS=="win"', {
          'product_name': 'ppapi_example',
          'type': 'shared_library',
          'msvs_guid': 'EE00E36E-9E8C-4DFB-925E-FBE32CEDB91B',
          'sources': [
            'example/example.rc',
          ],
          'run_as': {
            'action': [
              '<(PRODUCT_DIR)/<(EXECUTABLE_PREFIX)chrome<(EXECUTABLE_SUFFIX)',
              '--register-pepper-plugins=$(TargetPath);application/x-ppapi-example',
              'file://$(ProjectDir)/example/example.html',
            ],
          },
        }],
        ['OS=="linux" or OS=="freebsd" or OS=="openbsd" or OS=="solaris"', {
          'product_name': 'ppapi_example',
          'type': 'shared_library',
          'cflags': ['-fvisibility=hidden'],
          # -gstabs, used in the official builds, causes an ICE. Simply remove
          # it.
          'cflags!': ['-gstabs'],
        }],
        ['OS=="mac"', {
          'type': 'loadable_module',
          'mac_bundle': 1,
          'product_name': 'PPAPIExample',
          'product_extension': 'plugin',
          'sources+': [
            'example/Info.plist'
          ],
        }],
      ],
      # See README for instructions on how to run and debug on the Mac.
      #'conditions' : [
      #  ['OS=="mac"', {
      #    'target_name' : 'Chromium',
      #    'type' : 'executable',
      #    'xcode_settings' : {
      #      'ARGUMENTS' : '--renderer-startup-dialog --internal-pepper --no-sandbox file://${SRCROOT}/test_page.html'
      #    },
      #  }],
      #],
    },
    {
      'target_name': 'ppapi_tests',
      'type': 'loadable_module',
      'sources': [
        # Common test files.
        'tests/test_case.cc',
        'tests/test_case.h',
        'tests/test_instance.cc',
        'tests/test_instance.h',

        # Test cases.
        'tests/test_buffer.cc',
        'tests/test_buffer.h',
        'tests/test_char_set.cc',
        'tests/test_char_set.h',
        'tests/test_file_ref.cc',
        'tests/test_file_ref.h',
        'tests/test_graphics_2d.cc',
        'tests/test_graphics_2d.h',
        'tests/test_image_data.cc',
        'tests/test_image_data.h',
        'tests/test_paint_aggregator.cc',
        'tests/test_paint_aggregator.h',
        'tests/test_scrollbar.cc',
        'tests/test_scrollbar.h',
        'tests/test_url_loader.cc',
        'tests/test_url_loader.h',
        'tests/test_url_util.cc',
        'tests/test_url_util.h',
        'tests/test_var.cc',
        'tests/test_var.h',
      ],
      'dependencies': [
        'ppapi_cpp'
      ],
      'conditions': [
        ['OS=="win"', {
          'defines': [
            '_CRT_SECURE_NO_DEPRECATE',
            '_CRT_NONSTDC_NO_WARNINGS',
            '_CRT_NONSTDC_NO_DEPRECATE',
            '_SCL_SECURE_NO_DEPRECATE',
          ],
        }],
        ['OS=="mac"', {
          'mac_bundle': 1,
          'product_name': 'ppapi_tests',
          'product_extension': 'plugin',
        }],
      ],
    },
  ],
}
