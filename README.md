# REQUIREMENTS

 * A build instance.  A Docker image, VirtualBox VM, or even a chroot are all
   examples of build instances you can use.
 * A build environment inside the instance.  This can
   usually be summarised as:
  1. `sudo dnf install rpm-build redhat-rpm-config rpmdevtools`
  2. `sudo dnf groupinstall "Development Tools"`

# USAGE

## Existing Packages ##

 * `cd SPECS`.
 * Find and/or edit the *<package name>.spec* file for the package you
 are interested in.
 * Check the *<package name>.README.md* file (if it exists) for the
 package you are interested in for any build or other notes.
 * Dependancies that need to be installed to build the package are
 listed in the *<package name>.deps* file.
  * Quickly install the deps with `xargs -a <package name>.deps sudo
    yum -y install`.
 * Build the package with `rpmbuild -ba <package name>.spec`.

## New Packages ##

 * Create a new **.spec** file under `SPECS` for the package.
  * `rpmdev-newspec <package name>.spec`
 * List the build dependancies in a `<package name>.deps` file (also
   under the `SPECS` directory).
 * List any notes and special build instructions in a `<package
   name>.README.md` file (also under the `SPECS` directory).
 * Install the dependancies and build the package:
  * `xargs -a <package name>.deps sudo
    yum -y install && rpmbuild -ba <package name>.spec`.
   