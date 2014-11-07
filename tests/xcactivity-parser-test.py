import subprocess

script_path='./src/xcactivity-parser.py'
fixtures_path='./tests/fixtures/'

def test_script_run():
	sp = subprocess.Popen([script_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	out, err = sp.communicate()
	assert len(err) != 0


def test_usage_message_on_no_params():
	sp = subprocess.Popen([script_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	out, err = sp.communicate()
	assert "Usage:" in err

def test_usage_message_on_only_file_parameter():
	sp = subprocess.Popen([script_path, "-x", "/"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	out, err = sp.communicate()
	assert "Usage:" in err

def test_usage_message_on_only_directory_parameter():
	sp = subprocess.Popen([script_path, "-f", "/"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	out, err = sp.communicate()
	assert "Usage:" in err

def test_searching_message_on_both_parameters():
	sp = subprocess.Popen([script_path, "-f", "/", "-x", "/"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	out, err = sp.communicate()
	assert not "Usage:" in err

def test_full_path_for_file():
	sp = subprocess.Popen([script_path, "-f", "asd", "-x", "/"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	out, err = sp.communicate()
	assert "full path" in err

def test_directory_existance():
	sp = subprocess.Popen([script_path, "-f", "/", "-x", "asfsd"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	out, err = sp.communicate()
	assert "directory" in err
	assert "exist" in err

