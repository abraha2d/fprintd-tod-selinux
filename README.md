
# SELinux Policy for fprint-tod

We the standard policy the fingerprint reader is not going to work. See [this sample ausearch output](./sample.log) for more details. Using that output the file [fprintd_policy.te](./fprintd_policy.te) was created. The other files were created using the tool `sepolicy generate --init /usr/libexec/fprintd` and the files [fprintd_policy.if](./fprintd_policy.if), [fprintd_policy.fc](./fprintd_policy.fc), and  [fprintd_policy.te](./fprintd_policy.te) were overridden with their originals from the [fedora-selinux/selinux-policy](https://github.com/fedora-selinux/selinux-policy) repository see resource [3-5].

## Resources

- [1] https://fedoraproject.org/wiki/SELinux/IndependentPolicy
- [2] https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/7/html/selinux_users_and_administrators_guide/security-enhanced_linux-prioritizing_selinux_modules#Security-Enhanced_Linux-prioritizing_selinux_modules
- [3] https://github.com/fedora-selinux/selinux-policy/blob/rawhide/policy/modules/contrib/fprintd.fc
- [4] https://github.com/fedora-selinux/selinux-policy/blob/rawhide/policy/modules/contrib/fprintd.te
- [5] https://github.com/fedora-selinux/selinux-policy/blob/rawhide/policy/modules/contrib/fprintd.if