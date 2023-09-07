<script>
  // @ts-nocheck

  import Form from "./entries/form.svelte";
  import Input from "./entries/input.svelte";

  let email = "";
  let password = "";
  let cnfrmPassword = "";
  let api = "http://127.0.0.1:5000/resetpassword";

  const handleReset = (e) => {
    email = e.detail;
  };
</script>

<Form {email} {password} {cnfrmPassword} {api} on:resetInput={handleReset}>
  <Input
    inputName={"Email"}
    inputType={"email"}
    inputAutocomplete={"on"}
    inputValue={email}
    on:input={(e) => (email = e.target.value)}
  />
  <button>Reset Password</button>
</Form>
