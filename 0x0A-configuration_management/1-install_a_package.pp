# Install puppet-lint version 1.1.0
package { 'puppet-lint':
  source   => 'https://rubygems.org'
  ensure   => '2.5.0',
  provider => 'gem',
}
