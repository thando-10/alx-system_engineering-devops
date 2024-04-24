#!/usr/bin/env bash
#USING Puppet

file { '/etc/ssh/ssh_config':
}

file_line { 'Turn off passwd auth':
 path	=> '/etc/ssh/ssh_config',
 line	=> 'IdentityFile ~/.ssh/school',
 match	=> '^#IdentityFile',
}
