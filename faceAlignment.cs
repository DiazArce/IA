private Mat FaceAlignment(CascadeClassifier cascadEye, Mat src)
        {

            int index = 0;
            int direction;
            double angle;
            double radians;
            Rect eye1 = new Rect(0, 0, 0, 0);
            Rect eye2 = new Rect(0, 0, 0, 0);
            Rect eye_left;
            Rect eye_right;
            var result = new Mat();
            using (var gray = new Mat())
            {
                //result = src.Clone();
                Cv2.CvtColor(src, gray, ColorConversionCodes.BGR2GRAY);

                // Detect faces
                Rect[] eyes = cascadEye.DetectMultiScale(gray);


                
                foreach (Rect eye in eyes)
                {

                    if (index == 0)
                    {
                        eye1.X = eye.X;
                        eye1.Y = eye.Y;
                        eye1.Width = eye.Width;
                        eye1.Height = eye.Height;

                        index = 1;
                        Console.WriteLine("eye X is {0}", eye.X);
                    }
                    else
                    {
                        eye2.X = eye.X;
                        eye2.Y = eye.Y;
                        eye2.Width = eye.Width;
                        eye2.Height = eye.Height;
                    }

                }
                Console.WriteLine("eye 1 x is {0}", eye1.X);
                if (eye1.X < eye2.X)
                {
                    Console.WriteLine("eye 1 x is {0}", eye1.X);
                    Console.WriteLine("eye 2 x is {0}", eye2.X);
                    eye_left = eye1;
                    eye_right = eye2;
                }
                else
                {
                    eye_left = eye2;
                    eye_right = eye1;
                }
                Console.WriteLine("eye left X is {0}", eye_left.X);
                Console.WriteLine("eye left width is {0}", eye_left.Width);
                double eyeL_center_x = eye_left.X + (eye_left.Width / 2);
                double eyeL_center_y = eye_left.Y + (eye_left.Height / 2);
                double eyeR_center_x = eye_right.X + (eye_right.Width / 2);
                double eyeR_center_y = eye_right.Y + (eye_right.Height / 2);
                Console.WriteLine("eye Left center X is {0}", eyeL_center_x);
                Console.WriteLine("eye Right center Y is {0}", eyeR_center_y);

                //calcul point 3rd to apply euclidean distance theorm
                if (eyeL_center_y < eyeR_center_y)
                {

                    Console.WriteLine("eye Left center Y is {0}", eyeL_center_y);
                    //int point_3rd_x = eyeL_center_x;
                    //int point_3rd_y = eyeR_center_y;
                    //int direction = 1;
                    //int a = EuclideanDistance(point_3rd_x, point_3rd_y, eyeL_center_x, eyeL_center_y);
                    //int b = EuclideanDistance(point_3rd_x, point_3rd_y, eyeR_center_x, eyeR_center_y);
                    //double result = a / b;
                    //radians = Math.Atan(result);
                    //angle = radians * (180 / Math.PI);
                    //radians = Math.Atan2(y, x); arctg of the angle formedby the x_axis and a point (x,y)
                    radians = Math.Atan2(eyeL_center_y, eyeL_center_x);
                    angle = radians * (180 / Math.PI);
                    direction = 1;
                }
                else
                {

                    //int point_3rd_x = eyeR_center_x;
                    //int point_3rd_y = eyeL_center_y;
                    //int direction = -1;

                    //int a = EuclideanDistance(point_3rd_x, point_3rd_y, eyeR_center_x, eyeR_center_y);
                    //int b = EuclideanDistance(point_3rd_x, point_3rd_y, eyeL_center_x, eyeL_center_y);
                    radians = Math.Atan2(eyeR_center_y, eyeR_center_x);
                    angle = radians * (180 / Math.PI);
                    direction = -1;
                }
                double rotate = angle * direction;
                int scale = 1;
                Console.WriteLine("rotate is {0}",rotate);
                var imageCenter = new Point2f(src.Cols / 2f, src.Rows / 2f);
                var rotationMat = Cv2.GetRotationMatrix2D(imageCenter, rotate, scale);
                Cv2.WarpAffine(src, result, rotationMat, src.Size());
                Cv2.ImShow("face correct", result);
                Cv2.WaitKey(1);
                return result;
            }
        }
