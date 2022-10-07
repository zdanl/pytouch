from setuptools import setup

# __________         ___________                     .__
# \______   \ ___.__.\__    ___/____   __ __   ____  |  |__
# |     ___/<   |  |  |    |  /  _ \ |  |  \_/ ___\ |  |  \
# |    |     \___  |  |    | (  <_> )|  |  /\  \___ |   Y  \
# |____|     / ____|  |____|  \____/ |____/  \___  >|___|  /
#       .    \/ Twitter @dzethoxy, Github: @zdanl\/ v0.1 \/
#

setup(
    name="pytouch",
    version="0.1",
    packages=["pytouch", "pytouch.engine", "pytouch.ascii"],
    install_requires=["nuitka"],
    url="https://mescalin.co/staff/zulla",
    license="MIT",
    author="zdanl",
    author_email="dan@mescalin.co",
    description="pytouch"
)


