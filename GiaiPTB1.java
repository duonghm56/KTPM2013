
public class GiaiPTB1 {

	public static double giai(double a, double b) throws Exception{
		if(a!=0){
			return -b/a;
		}else{
			if(b==0){
				throw new Exception("VSN");
			}else{
				throw new Exception("VN");
			}
		}
	}
	
}  
