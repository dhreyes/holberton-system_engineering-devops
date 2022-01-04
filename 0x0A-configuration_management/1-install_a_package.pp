# Install puppet-lint version 1.1.0
package { 'puppet-lint':
  ensure   => '2.5.0',
  provider => 'gem',
  source   => 'https://rubygems.org'
}
  provider => 'gem',
