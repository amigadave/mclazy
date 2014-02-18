#!/usr/bin/python
# Licensed under the GNU General Public License Version 2
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

# Copyright (C) 2014
#    Richard Hughes <richard@hughsie.com>

class Package:

    def __init__(self):
        self.name = None
        self.version = None
        self.release = None

    def get_url(self):
        uri = 'http://kojipkgs.fedoraproject.org/packages/'
        uri += "%s/%s/%s/src/" % (self.name, self.version, self.release)
        uri += "%s-%s-%s.src.rpm" % (self.name, self.version, self.release)
        return uri

    def get_nvr(self):
        return "%s-%s-%s" % (self.name, self.version, self.release)
