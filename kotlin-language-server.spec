
BuildArch:      noarch
Summary:        Kotlin language server
Name:           kotlin-language-server
Version:        1.3.3
Release:        1%{?dist}

License:        MIT
URL:            https://github.com/fwcd/kotlin-language-server
Source0:        https://github.com/fwcd/kotlin-language-server/releases/download/%{version}/server.zip

BuildRequires:  bash
Requires:       (java-headless >= 1:1.11.0 or java >= 1.11.0)

%description
A language server that provides smart code completion, diagnostics, hover, document symbols, definition lookup, method signature help and more for Kotlin.

%prep
unzip %{SOURCE0}

%install
mkdir -p -m0755 %{buildroot}/opt/kotlin-lsp/bin
cp %{_builddir}/server/bin/kotlin-language-server %{buildroot}/opt/kotlin-lsp/bin/kotlin-language-server
cp -r %{_builddir}/server/lib %{buildroot}/opt/kotlin-lsp

mkdir -p -m0755 %{buildroot}%{_bindir}
ln -sr /opt/kotlin-lsp/bin/kotlin-language-server %{buildroot}%{_bindir}/kotlin-language-server

%files
/opt/kotlin-lsp
%{_bindir}/kotlin-language-server

%changelog
