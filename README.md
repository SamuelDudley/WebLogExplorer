# Hawkview
An online tool to share and analyse [Ardupilot](http://ardupilot.org/) telemetry (.tlog) and flash (.bin) logs.
This project aims to replicate the functionality of [MAVExplorer](https://github.com/ArduPilot/MAVProxy/blob/master/MAVProxy/tools/MAVExplorer.py) with a web based front end.

Currently in Alpha, this is a proof of concept which needs a bit more refinement to be truly useful to the community.

Much of the web front end & plotting back end code is taken directly from [PX4 - Flight Review](https://github.com/PX4/flight_review/) and data is plotted with the [bokeh](http://bokeh.pydata.org/en/latest/) library.



### Original license from [PX4 - Flight Review](https://github.com/PX4/flight_review/blob/master/LICENSE.md)

Copyright (c) 2016, PX4 Pro Drone Autopilot
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

* Redistributions of source code must retain the above copyright notice, this
  list of conditions and the following disclaimer.

* Redistributions in binary form must reproduce the above copyright notice,
  this list of conditions and the following disclaimer in the documentation
  and/or other materials provided with the distribution.

* Neither the name of GpsDrivers nor the names of its
  contributors may be used to endorse or promote products derived from
  this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
