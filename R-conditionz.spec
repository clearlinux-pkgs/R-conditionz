#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-conditionz
Version  : 0.1.0
Release  : 12
URL      : https://cran.r-project.org/src/contrib/conditionz_0.1.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/conditionz_0.1.0.tar.gz
Summary  : Control How Many Times Conditions are Thrown
Group    : Development/Tools
License  : MIT
Requires: R-R6
Requires: R-uuid
BuildRequires : R-R6
BuildRequires : R-uuid
BuildRequires : buildreq-R

%description
calls conditions are thrown (shown to the user). Includes control of
    warnings and messages.

%prep
%setup -q -c -n conditionz
cd %{_builddir}/conditionz

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1640991961

%install
export SOURCE_DATE_EPOCH=1640991961
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library conditionz
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library conditionz
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library conditionz
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc conditionz || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/conditionz/DESCRIPTION
/usr/lib64/R/library/conditionz/INDEX
/usr/lib64/R/library/conditionz/LICENSE
/usr/lib64/R/library/conditionz/Meta/Rd.rds
/usr/lib64/R/library/conditionz/Meta/features.rds
/usr/lib64/R/library/conditionz/Meta/hsearch.rds
/usr/lib64/R/library/conditionz/Meta/links.rds
/usr/lib64/R/library/conditionz/Meta/nsInfo.rds
/usr/lib64/R/library/conditionz/Meta/package.rds
/usr/lib64/R/library/conditionz/NAMESPACE
/usr/lib64/R/library/conditionz/NEWS.md
/usr/lib64/R/library/conditionz/R/conditionz
/usr/lib64/R/library/conditionz/R/conditionz.rdb
/usr/lib64/R/library/conditionz/R/conditionz.rdx
/usr/lib64/R/library/conditionz/help/AnIndex
/usr/lib64/R/library/conditionz/help/aliases.rds
/usr/lib64/R/library/conditionz/help/conditionz.rdb
/usr/lib64/R/library/conditionz/help/conditionz.rdx
/usr/lib64/R/library/conditionz/help/paths.rds
/usr/lib64/R/library/conditionz/html/00Index.html
/usr/lib64/R/library/conditionz/html/R.css
/usr/lib64/R/library/conditionz/tests/test-all.R
/usr/lib64/R/library/conditionz/tests/testthat/test-ConditionKeeper.R
/usr/lib64/R/library/conditionz/tests/testthat/test-capture_message.R
/usr/lib64/R/library/conditionz/tests/testthat/test-capture_warning.R
/usr/lib64/R/library/conditionz/tests/testthat/test-handle_conditions.R
