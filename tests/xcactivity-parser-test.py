import subprocess
import six

script_path = './src/xcactivity-parser.py'

# helpers

def string_from_std(std):
    if six.PY2:
        return std
    return str(std, encoding='utf8')


def run_subprocess(params):
    sp = subprocess.Popen(params, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = sp.communicate()
    return string_from_std(out), string_from_std(err)


# tests

def test_script_run():
    out, err = run_subprocess([script_path])
    assert len(err) != 0


def test_usage_message_on_no_params():
    out, err = run_subprocess([script_path])
    assert "Usage:" in err


def test_usage_message_on_only_file_parameter():
    out, err = run_subprocess([script_path, "-x", "/"])
    assert "Usage:" in err


def test_usage_message_on_only_directory_parameter():
    out, err = run_subprocess([script_path, "-f", "/"])
    assert "Usage:" in err


def test_usage_message_on_only_arch_parameter():
    out, err = run_subprocess([script_path, "-a", "i386"])
    assert "Usage:" in err


def test_searching_message_on_two_parameters():
    out, err = run_subprocess([script_path, "-f", "/", "-x", "/"])
    assert "Usage:" in err


def test_searching_message_on_all_parameters():
    out, err = run_subprocess([script_path, "-f", "/", "-x", "/", "-a", "i386"])
    assert not "Usage:" in err


def test_full_path_for_file():
    out, err = run_subprocess([script_path, "-f", "asd", "-x", "/"])
    assert "full path" in err


def test_directory_existance():
    out, err = run_subprocess([script_path, "-f", "/", "-x", "asfsd"])
    assert "directory" in err
    assert "exist" in err

# Working with real files :)

fixtures_path = './tests/fixtures/one-file'


def test_arguments_on_existed_file():
    existingfile = "/Volumes/data/Projects/dyci-main/Dynamic\ Code\ Injection/dyci/Classes/Notifications/SFInjectionsNotificationsCenter.m"
    compilationString = "/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/clang -x objective-c -arch i386 -fmessage-length=0 -fdiagnostics-show-note-include-stack -fmacro-backtrace-limit=0 -std=gnu99 -fobjc-arc -fmodules -fmodules-cache-path=/Users/ptaykalo/Library/Developer/Xcode/DerivedData/ModuleCache -fmodules-prune-interval=86400 -fmodules-prune-after=345600 -Wnon-modular-include-in-framework-module -Werror=non-modular-include-in-framework-module -Wno-trigraphs -fpascal-strings -Os -Wno-missing-field-initializers -Wno-missing-prototypes -Werror=return-type -Wunreachable-code -Wno-implicit-atomic-properties -Werror=deprecated-objc-isa-usage -Werror=objc-root-class -Wno-receiver-is-weak -Wno-arc-repeated-use-of-weak -Wduplicate-method-match -Wno-missing-braces -Wparentheses -Wswitch -Wunused-function -Wno-unused-label -Wno-unused-parameter -Wunused-variable -Wunused-value -Wempty-body -Wconditional-uninitialized -Wno-unknown-pragmas -Wno-shadow -Wno-four-char-constants -Wno-conversion -Wconstant-conversion -Wint-conversion -Wbool-conversion -Wenum-conversion -Wshorten-64-to-32 -Wpointer-sign -Wno-newline-eof -Wno-selector -Wno-strict-selector-match -Wundeclared-selector -Wno-deprecated-implementations -DNS_BLOCK_ASSERTIONS=1 -DOBJC_OLD_DISPATCH_PROTOTYPES=0 -isysroot /Applications/Xcode.app/Contents/Developer/Platforms/iPhoneSimulator.platform/Developer/SDKs/iPhoneSimulator8.1.sdk -fexceptions -fasm-blocks -fstrict-aliasing -Wprotocol -Wdeprecated-declarations -g -Wno-sign-conversion -fobjc-abi-version=2 -fobjc-legacy-dispatch -mios-simulator-version-min=8.1 -iquote /Users/ptaykalo/Library/Developer/Xcode/DerivedData/DYCI-hfgqlcmijbqsjtcnjyhbxgpcckwj/Build/Intermediates/dyci-framework.build/Release-iphonesimulator/dyci.build/dyci-generated-files.hmap -I/Users/ptaykalo/Library/Developer/Xcode/DerivedData/DYCI-hfgqlcmijbqsjtcnjyhbxgpcckwj/Build/Intermediates/dyci-framework.build/Release-iphonesimulator/dyci.build/dyci-own-target-headers.hmap -I/Users/ptaykalo/Library/Developer/Xcode/DerivedData/DYCI-hfgqlcmijbqsjtcnjyhbxgpcckwj/Build/Intermediates/dyci-framework.build/Release-iphonesimulator/dyci.build/dyci-all-target-headers.hmap -iquote /Users/ptaykalo/Library/Developer/Xcode/DerivedData/DYCI-hfgqlcmijbqsjtcnjyhbxgpcckwj/Build/Intermediates/dyci-framework.build/Release-iphonesimulator/dyci.build/dyci-project-headers.hmap -I/Users/ptaykalo/Library/Developer/Xcode/DerivedData/DYCI-hfgqlcmijbqsjtcnjyhbxgpcckwj/Build/Products/Release-iphonesimulator/include -I/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/include -I/Users/ptaykalo/Library/Developer/Xcode/DerivedData/DYCI-hfgqlcmijbqsjtcnjyhbxgpcckwj/Build/Intermediates/dyci-framework.build/Release-iphonesimulator/dyci.build/DerivedSources/i386 -I/Users/ptaykalo/Library/Developer/Xcode/DerivedData/DYCI-hfgqlcmijbqsjtcnjyhbxgpcckwj/Build/Intermediates/dyci-framework.build/Release-iphonesimulator/dyci.build/DerivedSources -F/Users/ptaykalo/Library/Developer/Xcode/DerivedData/DYCI-hfgqlcmijbqsjtcnjyhbxgpcckwj/Build/Products/Release-iphonesimulator -MMD -MT dependencies -MF /Users/ptaykalo/Library/Developer/Xcode/DerivedData/DYCI-hfgqlcmijbqsjtcnjyhbxgpcckwj/Build/Intermediates/dyci-framework.build/Release-iphonesimulator/dyci.build/Objects-normal/i386/SFInjectionsNotificationsCenter.d --serialize-diagnostics /Users/ptaykalo/Library/Developer/Xcode/DerivedData/DYCI-hfgqlcmijbqsjtcnjyhbxgpcckwj/Build/Intermediates/dyci-framework.build/Release-iphonesimulator/dyci.build/Objects-normal/i386/SFInjectionsNotificationsCenter.dia -c /Volumes/data/Projects/dyci-main/Dynamic\ Code\ Injection/dyci/Classes/Notifications/SFInjectionsNotificationsCenter.m -o /Users/ptaykalo/Library/Developer/Xcode/DerivedData/DYCI-hfgqlcmijbqsjtcnjyhbxgpcckwj/Build/Intermediates/dyci-framework.build/Release-iphonesimulator/dyci.build/Objects-normal/i386/SFInjectionsNotificationsCenter.o"
    out, err = run_subprocess([script_path, "-f", existingfile, "-x", fixtures_path, "-a", "i386"])
    assert not "Usage:" in err
    # print out
    # print err
    assert compilationString == out.strip()


def test_arguments_on_existed_file_with_different_architecture():
    existingfile = "/Volumes/data/Projects/dyci-main/Dynamic\ Code\ Injection/dyci/Classes/Notifications/SFInjectionsNotificationsCenter.m"
    compilationString = "/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/clang -x objective-c -arch x86_64 -fmessage-length=0 -fdiagnostics-show-note-include-stack -fmacro-backtrace-limit=0 -std=gnu99 -fobjc-arc -fmodules -fmodules-cache-path=/Users/ptaykalo/Library/Developer/Xcode/DerivedData/ModuleCache -fmodules-prune-interval=86400 -fmodules-prune-after=345600 -Wnon-modular-include-in-framework-module -Werror=non-modular-include-in-framework-module -Wno-trigraphs -fpascal-strings -Os -Wno-missing-field-initializers -Wno-missing-prototypes -Werror=return-type -Wunreachable-code -Wno-implicit-atomic-properties -Werror=deprecated-objc-isa-usage -Werror=objc-root-class -Wno-receiver-is-weak -Wno-arc-repeated-use-of-weak -Wduplicate-method-match -Wno-missing-braces -Wparentheses -Wswitch -Wunused-function -Wno-unused-label -Wno-unused-parameter -Wunused-variable -Wunused-value -Wempty-body -Wconditional-uninitialized -Wno-unknown-pragmas -Wno-shadow -Wno-four-char-constants -Wno-conversion -Wconstant-conversion -Wint-conversion -Wbool-conversion -Wenum-conversion -Wshorten-64-to-32 -Wpointer-sign -Wno-newline-eof -Wno-selector -Wno-strict-selector-match -Wundeclared-selector -Wno-deprecated-implementations -DNS_BLOCK_ASSERTIONS=1 -DOBJC_OLD_DISPATCH_PROTOTYPES=0 -isysroot /Applications/Xcode.app/Contents/Developer/Platforms/iPhoneSimulator.platform/Developer/SDKs/iPhoneSimulator8.1.sdk -fexceptions -fasm-blocks -fstrict-aliasing -Wprotocol -Wdeprecated-declarations -g -Wno-sign-conversion -fobjc-abi-version=2 -fobjc-legacy-dispatch -mios-simulator-version-min=8.1 -iquote /Users/ptaykalo/Library/Developer/Xcode/DerivedData/DYCI-hfgqlcmijbqsjtcnjyhbxgpcckwj/Build/Intermediates/dyci-framework.build/Release-iphonesimulator/dyci.build/dyci-generated-files.hmap -I/Users/ptaykalo/Library/Developer/Xcode/DerivedData/DYCI-hfgqlcmijbqsjtcnjyhbxgpcckwj/Build/Intermediates/dyci-framework.build/Release-iphonesimulator/dyci.build/dyci-own-target-headers.hmap -I/Users/ptaykalo/Library/Developer/Xcode/DerivedData/DYCI-hfgqlcmijbqsjtcnjyhbxgpcckwj/Build/Intermediates/dyci-framework.build/Release-iphonesimulator/dyci.build/dyci-all-target-headers.hmap -iquote /Users/ptaykalo/Library/Developer/Xcode/DerivedData/DYCI-hfgqlcmijbqsjtcnjyhbxgpcckwj/Build/Intermediates/dyci-framework.build/Release-iphonesimulator/dyci.build/dyci-project-headers.hmap -I/Users/ptaykalo/Library/Developer/Xcode/DerivedData/DYCI-hfgqlcmijbqsjtcnjyhbxgpcckwj/Build/Products/Release-iphonesimulator/include -I/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/include -I/Users/ptaykalo/Library/Developer/Xcode/DerivedData/DYCI-hfgqlcmijbqsjtcnjyhbxgpcckwj/Build/Intermediates/dyci-framework.build/Release-iphonesimulator/dyci.build/DerivedSources/x86_64 -I/Users/ptaykalo/Library/Developer/Xcode/DerivedData/DYCI-hfgqlcmijbqsjtcnjyhbxgpcckwj/Build/Intermediates/dyci-framework.build/Release-iphonesimulator/dyci.build/DerivedSources -F/Users/ptaykalo/Library/Developer/Xcode/DerivedData/DYCI-hfgqlcmijbqsjtcnjyhbxgpcckwj/Build/Products/Release-iphonesimulator -MMD -MT dependencies -MF /Users/ptaykalo/Library/Developer/Xcode/DerivedData/DYCI-hfgqlcmijbqsjtcnjyhbxgpcckwj/Build/Intermediates/dyci-framework.build/Release-iphonesimulator/dyci.build/Objects-normal/x86_64/SFInjectionsNotificationsCenter.d --serialize-diagnostics /Users/ptaykalo/Library/Developer/Xcode/DerivedData/DYCI-hfgqlcmijbqsjtcnjyhbxgpcckwj/Build/Intermediates/dyci-framework.build/Release-iphonesimulator/dyci.build/Objects-normal/x86_64/SFInjectionsNotificationsCenter.dia -c /Volumes/data/Projects/dyci-main/Dynamic\ Code\ Injection/dyci/Classes/Notifications/SFInjectionsNotificationsCenter.m -o /Users/ptaykalo/Library/Developer/Xcode/DerivedData/DYCI-hfgqlcmijbqsjtcnjyhbxgpcckwj/Build/Intermediates/dyci-framework.build/Release-iphonesimulator/dyci.build/Objects-normal/x86_64/SFInjectionsNotificationsCenter.o"
    out, err = run_subprocess([script_path, "-f", existingfile, "-x", fixtures_path, "-a", "x86_64"])
    assert not "Usage:" in err
    # print out
    # print err
    assert compilationString == out.strip()


def test_arguments_on_existed_file_with_non_existed_architecture():
    existingfile = "/Volumes/data/Projects/dyci-main/Dynamic\ Code\ Injection/dyci/Classes/Notifications/SFInjectionsNotificationsCenter.m"
    compilationString = "/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/clang -x objective-c -arch i386 -fmessage-length=0 -fdiagnostics-show-note-include-stack -fmacro-backtrace-limit=0 -std=gnu99 -fobjc-arc -fmodules -fmodules-cache-path=/Users/ptaykalo/Library/Developer/Xcode/DerivedData/ModuleCache -fmodules-prune-interval=86400 -fmodules-prune-after=345600 -Wnon-modular-include-in-framework-module -Werror=non-modular-include-in-framework-module -Wno-trigraphs -fpascal-strings -Os -Wno-missing-field-initializers -Wno-missing-prototypes -Werror=return-type -Wunreachable-code -Wno-implicit-atomic-properties -Werror=deprecated-objc-isa-usage -Werror=objc-root-class -Wno-receiver-is-weak -Wno-arc-repeated-use-of-weak -Wduplicate-method-match -Wno-missing-braces -Wparentheses -Wswitch -Wunused-function -Wno-unused-label -Wno-unused-parameter -Wunused-variable -Wunused-value -Wempty-body -Wconditional-uninitialized -Wno-unknown-pragmas -Wno-shadow -Wno-four-char-constants -Wno-conversion -Wconstant-conversion -Wint-conversion -Wbool-conversion -Wenum-conversion -Wshorten-64-to-32 -Wpointer-sign -Wno-newline-eof -Wno-selector -Wno-strict-selector-match -Wundeclared-selector -Wno-deprecated-implementations -DNS_BLOCK_ASSERTIONS=1 -DOBJC_OLD_DISPATCH_PROTOTYPES=0 -isysroot /Applications/Xcode.app/Contents/Developer/Platforms/iPhoneSimulator.platform/Developer/SDKs/iPhoneSimulator8.1.sdk -fexceptions -fasm-blocks -fstrict-aliasing -Wprotocol -Wdeprecated-declarations -g -Wno-sign-conversion -fobjc-abi-version=2 -fobjc-legacy-dispatch -mios-simulator-version-min=8.1 -iquote /Users/ptaykalo/Library/Developer/Xcode/DerivedData/DYCI-hfgqlcmijbqsjtcnjyhbxgpcckwj/Build/Intermediates/dyci-framework.build/Release-iphonesimulator/dyci.build/dyci-generated-files.hmap -I/Users/ptaykalo/Library/Developer/Xcode/DerivedData/DYCI-hfgqlcmijbqsjtcnjyhbxgpcckwj/Build/Intermediates/dyci-framework.build/Release-iphonesimulator/dyci.build/dyci-own-target-headers.hmap -I/Users/ptaykalo/Library/Developer/Xcode/DerivedData/DYCI-hfgqlcmijbqsjtcnjyhbxgpcckwj/Build/Intermediates/dyci-framework.build/Release-iphonesimulator/dyci.build/dyci-all-target-headers.hmap -iquote /Users/ptaykalo/Library/Developer/Xcode/DerivedData/DYCI-hfgqlcmijbqsjtcnjyhbxgpcckwj/Build/Intermediates/dyci-framework.build/Release-iphonesimulator/dyci.build/dyci-project-headers.hmap -I/Users/ptaykalo/Library/Developer/Xcode/DerivedData/DYCI-hfgqlcmijbqsjtcnjyhbxgpcckwj/Build/Products/Release-iphonesimulator/include -I/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/include -I/Users/ptaykalo/Library/Developer/Xcode/DerivedData/DYCI-hfgqlcmijbqsjtcnjyhbxgpcckwj/Build/Intermediates/dyci-framework.build/Release-iphonesimulator/dyci.build/DerivedSources/i386 -I/Users/ptaykalo/Library/Developer/Xcode/DerivedData/DYCI-hfgqlcmijbqsjtcnjyhbxgpcckwj/Build/Intermediates/dyci-framework.build/Release-iphonesimulator/dyci.build/DerivedSources -F/Users/ptaykalo/Library/Developer/Xcode/DerivedData/DYCI-hfgqlcmijbqsjtcnjyhbxgpcckwj/Build/Products/Release-iphonesimulator -MMD -MT dependencies -MF /Users/ptaykalo/Library/Developer/Xcode/DerivedData/DYCI-hfgqlcmijbqsjtcnjyhbxgpcckwj/Build/Intermediates/dyci-framework.build/Release-iphonesimulator/dyci.build/Objects-normal/i386/SFInjectionsNotificationsCenter.d --serialize-diagnostics /Users/ptaykalo/Library/Developer/Xcode/DerivedData/DYCI-hfgqlcmijbqsjtcnjyhbxgpcckwj/Build/Intermediates/dyci-framework.build/Release-iphonesimulator/dyci.build/Objects-normal/i386/SFInjectionsNotificationsCenter.dia -c /Volumes/data/Projects/dyci-main/Dynamic\ Code\ Injection/dyci/Classes/Notifications/SFInjectionsNotificationsCenter.m -o /Users/ptaykalo/Library/Developer/Xcode/DerivedData/DYCI-hfgqlcmijbqsjtcnjyhbxgpcckwj/Build/Intermediates/dyci-framework.build/Release-iphonesimulator/dyci.build/Objects-normal/i386/SFInjectionsNotificationsCenter.o"
    out, err = run_subprocess([script_path, "-f", existingfile, "-x", fixtures_path, "-a", "x86_64"])
    assert not "Usage:" in err
    # print out
    # print err
    assert compilationString != out.strip()


def test_for_filesearch_with_spaces():
    existingfile = "/Volumes/data/Projects/dyci-main/Support/Xcode/Source/Classes/Directory\ With\ Spaces/SomeGeneralDyciFile.m"
    compilationString = "/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/clang -x objective-c -arch x86_64 -fmessage-length=0 -fdiagnostics-show-note-include-stack -fmacro-backtrace-limit=0 -std=c99 -fobjc-arc -Wno-trigraphs -fpascal-strings -O0 -Wno-missing-field-initializers -Wno-missing-prototypes -Wno-implicit-atomic-properties -Wno-receiver-is-weak -Wno-arc-repeated-use-of-weak -Wno-missing-braces -Wparentheses -Wswitch -Wno-unused-function -Wno-unused-label -Wno-unused-parameter -Wunused-variable -Wunused-value -Wno-empty-body -Wno-uninitialized -Wno-unknown-pragmas -Wno-shadow -Wno-four-char-constants -Wno-conversion -Wno-constant-conversion -Wno-int-conversion -Wno-bool-conversion -Wno-enum-conversion -Wno-shorten-64-to-32 -Wpointer-sign -Wno-newline-eof -Wno-selector -Wno-strict-selector-match -Wno-undeclared-selector -Wno-deprecated-implementations -isysroot /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.10.sdk -fasm-blocks -fstrict-aliasing -Wprotocol -Wdeprecated-declarations -mmacosx-version-min=10.7 -g -Wno-sign-conversion -iquote /Users/ptaykalo/Library/Developer/Xcode/DerivedData/SFDYCIPlugin-fazyfnchxursjxbrqdmlnerzwutq/Build/Intermediates/SFDYCIPlugin.build/Debug/SFDYCIPlugin.build/SFDYCIPlugin-generated-files.hmap -I/Users/ptaykalo/Library/Developer/Xcode/DerivedData/SFDYCIPlugin-fazyfnchxursjxbrqdmlnerzwutq/Build/Intermediates/SFDYCIPlugin.build/Debug/SFDYCIPlugin.build/SFDYCIPlugin-own-target-headers.hmap -I/Users/ptaykalo/Library/Developer/Xcode/DerivedData/SFDYCIPlugin-fazyfnchxursjxbrqdmlnerzwutq/Build/Intermediates/SFDYCIPlugin.build/Debug/SFDYCIPlugin.build/SFDYCIPlugin-all-target-headers.hmap -iquote /Users/ptaykalo/Library/Developer/Xcode/DerivedData/SFDYCIPlugin-fazyfnchxursjxbrqdmlnerzwutq/Build/Intermediates/SFDYCIPlugin.build/Debug/SFDYCIPlugin.build/SFDYCIPlugin-project-headers.hmap -I/Users/ptaykalo/Library/Developer/Xcode/DerivedData/SFDYCIPlugin-fazyfnchxursjxbrqdmlnerzwutq/Build/Products/Debug/include -I/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/include -I/Users/ptaykalo/Library/Developer/Xcode/DerivedData/SFDYCIPlugin-fazyfnchxursjxbrqdmlnerzwutq/Build/Intermediates/SFDYCIPlugin.build/Debug/SFDYCIPlugin.build/DerivedSources/x86_64 -I/Users/ptaykalo/Library/Developer/Xcode/DerivedData/SFDYCIPlugin-fazyfnchxursjxbrqdmlnerzwutq/Build/Intermediates/SFDYCIPlugin.build/Debug/SFDYCIPlugin.build/DerivedSources -F/Users/ptaykalo/Library/Developer/Xcode/DerivedData/SFDYCIPlugin-fazyfnchxursjxbrqdmlnerzwutq/Build/Products/Debug -MMD -MT dependencies -MF /Users/ptaykalo/Library/Developer/Xcode/DerivedData/SFDYCIPlugin-fazyfnchxursjxbrqdmlnerzwutq/Build/Intermediates/SFDYCIPlugin.build/Debug/SFDYCIPlugin.build/Objects-normal/x86_64/SomeGeneralDyciFile.d --serialize-diagnostics /Users/ptaykalo/Library/Developer/Xcode/DerivedData/SFDYCIPlugin-fazyfnchxursjxbrqdmlnerzwutq/Build/Intermediates/SFDYCIPlugin.build/Debug/SFDYCIPlugin.build/Objects-normal/x86_64/SomeGeneralDyciFile.dia -c /Volumes/data/Projects/dyci-main/Support/Xcode/Source/Classes/Directory\ With\ Spaces/SomeGeneralDyciFile.m -o /Users/ptaykalo/Library/Developer/Xcode/DerivedData/SFDYCIPlugin-fazyfnchxursjxbrqdmlnerzwutq/Build/Intermediates/SFDYCIPlugin.build/Debug/SFDYCIPlugin.build/Objects-normal/x86_64/SomeGeneralDyciFile.o"
    out, err = run_subprocess(
        [script_path, "-f", existingfile, "-x", './tests/fixtures/file-with-spaces', "-a", "x86_64"])
    assert not "Usage:" in err
    # print out
    # print err
    assert compilationString == out.strip()
