<script>
  // @ts-nocheck

  import { backendAddress } from "../../stores";

  import Form from "../entries/form.svelte";
  import Input from "../entries/input.svelte";

  let email = "";
  let api = `${backendAddress}reset`;

  const navigateUser = "/home";
  const warnMessage =
    "If you can't see your Email, try checking out Spam Messages!";

  const handleReset = (e) => {
    email = e.detail;
  };
</script>

<Form {email} {api} {warnMessage} {navigateUser} on:resetInput={handleReset}>
  <Input
    inputName={"Email"}
    inputType={"email"}
    inputAutocomplete={"on"}
    inputValue={email}
    on:input={(e) => (email = e.target.value)}
  />
  <button>Reset Password</button>
</Form>
