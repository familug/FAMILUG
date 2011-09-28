    import java.security.MessageDigest;
    import java.security.NoSuchAlgorithmException;
    public class MD5HashTest {
        private static String getMD5Digest(String str) {
            try {
                byte[] buffer = str.getBytes();
                byte[] result = null;
                StringBuffer buf = null;
                MessageDigest md5 = MessageDigest.getInstance("MD5");
                //allocate room for the hash    result = new byte[md5.getDigestLength()];
                //calculate hash    md5.reset();
                md5.update(buffer);
                result = md5.digest();
                System.out.println(result);
                //create hex string from the 16-byte hash    buf = new StringBuffer(result.length * 2);
                for (int i = 0; i < result.length; i++) {
                    int intVal = result[i] & 0xff;
                    if (intVal < 0x10) {
                        buf.append("0");
                       
                    }
                    buf.append(Integer.toHexString(intVal).toUpperCase());
                   
                }
                return buf.toString();
               
            }
            catch (NoSuchAlgorithmException e) {
                System.err.println("Exception caught: " + e);
                e.printStackTrace();
               
            }
            return null;
           
        }
        public static void main(String[] args) {
            String result = getMD5Digest("This is a text to hash");
            System.out.println("result=" + result);
           
        }
       
    }

